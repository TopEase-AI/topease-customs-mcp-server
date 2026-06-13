# MCP 目录提交材料

本仓库用于提交到 MCP server registry / directory。

## 基础信息

| 字段 | 值 |
| --- | --- |
| Name | TOPEASE Customs MCP |
| Repository | `https://github.com/TopEase-AI/topease-customs-mcp-server` |
| Package | `topease-mcp` |
| PyPI | `https://pypi.org/project/topease-mcp/` |
| Website | `https://tradee.topease.net/` |
| Remote endpoint | `https://mcp.topease.net/mcp` |
| Transport | stdio, streamable HTTP |
| Auth | `Authorization: Bearer <TOPEASE_API_KEY>` |
| Tags | customs-data, trade-data, mcp, fastmcp, tradee, topease |

## 简短描述

```text
TOPEASE Customs MCP provides global customs import/export trade data search for agents, supporting company name, product keyword, HS code, country, trade direction, date range, paging, and sorting filters.
```

## 中文描述

```text
TOPEASE 海关数据 MCP 服务对接 Tradee 海关智能体贸易数据平台，支持按进出口企业名称、产品关键词、HS 编码、贸易时间、进出口类型、国家/市场/地区进行多维度联合查询，帮助 AI Agent 获取真实海关贸易记录并整理买家、供应商和市场样本线索。
```

## 安装配置

stdio：

```json
{
  "mcpServers": {
    "topease-customs-data": {
      "command": "uvx",
      "args": ["topease-mcp"],
      "env": {
        "TOPEASE_MCP_API_KEY": "<TOPEASE_API_KEY>"
      }
    }
  }
}
```

streamable HTTP：

```json
{
  "mcpServers": {
    "topease-customs-data": {
      "type": "streamableHttp",
      "url": "https://mcp.topease.net/mcp",
      "headers": {
        "Authorization": "Bearer <TOPEASE_API_KEY>"
      }
    }
  }
}
```

## Smithery 注意事项

Smithery URL 发布要求 Streamable HTTP；如果服务需要鉴权，则应支持 OAuth。当前远程服务使用 Tradee MCP API key 的 Bearer header 鉴权。若要正式发布到 Smithery，建议先补 OAuth 授权流，或改为 Smithery 支持的 MCPB/托管发布方式。

## 配套 Skill

Agent Skill / Claude Code Plugin 仓库：

```text
https://github.com/TopEase-AI/topease-customs-mcp-skill
```
