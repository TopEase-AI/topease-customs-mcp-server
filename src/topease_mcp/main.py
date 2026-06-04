"""MCP server for customs trade data query.

Provides tools for querying customs trade data with mandatory
API key authentication. Third-party LLMs MUST provide a valid API_KEY
to access any tool on this server.

Real API: POST https://api.topease.net/api/search_trade

API Key Authentication:
    When using streamable-http protocol, API key should be passed in 
    Authorization header: Authorization=Bearer <your_api_key>

Usage:
    # Streamable HTTP mode (for Claude Desktop, Trae, etc.)
    python -m topease_mcp
    # or
    uvicorn server:app --host 0.0.0.0 --port 8001
"""

from __future__ import annotations

import json
import os
from typing import Any, Optional

from dotenv import load_dotenv
from fastmcp import FastMCP, Context
from starlette.requests import Request
from setting import PORT

load_dotenv()

TOPEASE_MCP_API_KEY = os.getenv("TOPEASE_MCP_API_KEY")

from auth import (
    validate_api_key,
)
from customs import (
    CustomsDataService,
    CustomsQueryParams,
    TradeType,
)

mcp = FastMCP(
    name="topease-customs-data",
    instructions=(
        "topease-customs-data MCP 提供全球海关贸易数据查询服务。"
    ),
)

_customs_service = CustomsDataService()


def _build_query_params(**kwargs: Any) -> CustomsQueryParams:
    """Build CustomsQueryParams from tool keyword arguments."""
    print(TradeType(kwargs.get("trade_type", "all")))
    return CustomsQueryParams(
        product_keyword=kwargs.get("product_keyword"),
        hs_code=kwargs.get("hs_code"),
        company_name=kwargs.get("company_name"),
        trade_type=TradeType(kwargs.get("trade_type", "all")),
        country=kwargs.get("country"),
        date_from=kwargs.get("date_from"),
        date_to=kwargs.get("date_to"),
        page_index=kwargs.get("page_index", 1),
        page_size=kwargs.get("page_size", 20),
        sort_by=kwargs.get("sort_by", "tradedate"),
        sort_order=kwargs.get("sort_order", "desc"),
    )

def _format_error(message: str) -> dict[str, Any]:
    return {"data": [], "message": message,"code":400}


# ──────────────────────────────────────────────
# MCP Tools
# ──────────────────────────────────────────────


def _get_api_key_from_headers(ctx: Context) -> Optional[str]:
    """Extract API key from Authorization header.
    
    Args:
        ctx: FastMCP Context object containing request information.
        
    Returns:
        The API key string if found and valid, None otherwise.
    """
    # 1. 检查上下文和请求对象是否存在
    if not ctx or not ctx.request_context or not ctx.request_context.request:
        return None
    
    # 2. 验证请求对象类型
    request = ctx.request_context.request
    if not isinstance(request, Request):
        return None
    
    # 3. 获取 headers（保留原始 Headers 对象，使用 get 方法避免 KeyError）
    headers = request.headers
    
    # 4. 检查 authorization 是否存在（大小写不敏感）
    auth_header = headers.get("Authorization") or headers.get("authorization")
    print("------------auth_header")
    print(auth_header)
    if not auth_header:
        return None  # authorization 不存在，返回 None
    
    # 5. 从 Bearer 格式中提取 API key
    if auth_header.startswith("Bearer "):
        api_key = auth_header[7:].strip()
        return api_key if api_key else None
    
    # 6. 支持 Token 格式
    if auth_header.startswith("Token "):
        api_key = auth_header[6:].strip()
        return api_key if api_key else None
    
    # 7. 其他格式或无效授权
    return None


@mcp.tool(
    name="search_customs_data",
    description=(
        "查询海关贸易数据。支持按企业名称(company_name)、"
        "产品关键字(product_keyword)、HS编码(hs_code)、"
        "贸易时间(date_from/date_to)、进出口类型(trade_type)及"
        "原产国(country)进行多维度联合查询。"
    ),
)
async def search_customs_data(
    company_name: str | None = None,
    product_keyword: str | None = None,
    hs_code: str | None = None,
    trade_type: str = "all",
    country: str | None = None,
    date_from: str | None = None,
    date_to: str | None = None,
    page_index: int = 1,
    page_size: int = 20,
    sort_by: str = "tradedate",
    sort_order: str = "desc",
    ctx: Context = Context  # 自动注入上下文
) -> dict:
    """Query customs trade data with multiple filter dimensions.

    Args:
        company_name: 企业名称（模糊匹配进口商/出口商名称），会做后置过滤。
        product_keyword: 产品描述关键字，例如 "CABIN"、"手机"。
        hs_code: HS海关编码（前缀匹配），例如 "8415"。
        trade_type: 贸易类型：import(进口)、export(出口)、all(全部，默认)。
        country: 数据源国（英文名），例如 "Japan"、"China"。
        date_from: 贸易起始日期，格式 YYYY-MM-DD。默认 2025-01-01。
        date_to: 贸易结束日期，格式 YYYY-MM-DD。默认当前时间。
        page_index: 页码，默认为1。
        page_size: 每页记录数，默认为20，最大100。
        sort_by: 排序字段，默认 tradedate。支持排序字段；tradedate,quantity,weight,uusd
        sort_order: 排序方向，asc/desc，默认 desc。

    Returns:
        JSON格式的查询结果，包含记录列表和分页信息。
    """
    # Try to get API key from headers first, then from parameter
    
    print("------------TOPEASE_MCP_API_KEY")
    print(TOPEASE_MCP_API_KEY)

    final_api_key = TOPEASE_MCP_API_KEY or _get_api_key_from_headers(ctx)
    
    if final_api_key == None:
        return _format_error(
            "API密钥缺失。请在请求头中传递 Authorization=Bearer <your_api_key> "
        )
    
    validate_api_key(final_api_key)
    _customs_service.set_api_key(final_api_key)

    if not any([company_name, product_keyword, hs_code, country]):
        return _format_error(
            "请至少提供一个查询条件："
            "企业名称(company_name)、产品关键字(product_keyword)、"
            "HS编码(hs_code) 或 原产国(country)"
        )

    params = _build_query_params(
        product_keyword=product_keyword,
        hs_code=hs_code,
        company_name=company_name,
        trade_type=trade_type,
        country=country,
        date_from=date_from,
        date_to=date_to,
        page_index=page_index,
        page_size=min(page_size, 20),
        sort_by=sort_by,
        sort_order=sort_order,
    )

    result = await _customs_service.search(params)
    return result


# ──────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────


def main() -> None:
    """Run the MCP server."""
    mcp.run(transport="stdio")
    # mcp.run(transport="streamable-http",port=PORT,host="0.0.0.0")


if __name__ == "__main__":
    main()
    