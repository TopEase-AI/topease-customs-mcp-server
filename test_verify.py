import asyncio
import json
from topease_mcp.customs import CustomsDataService, CustomsQueryParams

async def test():
    svc = CustomsDataService()

    params = CustomsQueryParams(page_index=1, page_size=5)
    result = await svc.search(params)
    print('search() total=%d, records=%d' % (result.total, len(result.records)))

    # Also test mock directly
    mock_result = svc._search_mock(params)
    print('_search_mock() total=%d, records=%d' % (mock_result.total, len(mock_result.records)))

    for r in mock_result.records[:3]:
        d = r.to_dict()
        keys = list(d.keys())
        print('  Keys:', keys)

    d = mock_result.records[0].to_dict()
    keys = list(d.keys())
    assert '进口商代码' not in keys, 'importer_tcode should not be in output'
    assert '出口商代码' not in keys, 'exporter_tcode should not be in output'
    print('PASS: No tcode fields in output dict')

    body = params.to_api_body()
    assert 'TCode' not in body, 'TCode should not be in API body'
    print('PASS: No TCode in API body')
    print('API body:', json.dumps(body, indent=2, ensure_ascii=False))

asyncio.run(test())




# @mcp.tool(name="显示 headers 信息", description="获取并显示请求的 headers信息")
# async def echo_headers(ctx: Context) -> str:
#     """获取请求的 header 信息"""
#     # 检查是否存在 request 对象并进行类型校验
#     if ctx.request_context.request and isinstance(ctx.request_context.request, Request):
#         headers = dict(ctx.request_context.request.headers)
#         return str(headers)
    
#     return "No headers available"