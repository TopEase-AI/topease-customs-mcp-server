# 全球海关贸易数据 MCP

<a href="https://tradee.topease.net/" target="_blank">
  <img src="https://img.shields.io/badge/官网-tradee.topease.net-blue" alt="官网">
</a>
<a href="https://pypi.org/project/topease-mcp/" target="_blank">
  <img src="https://img.shields.io/pypi/v/topease-mcp" alt="PyPI">
</a>
<a href="https://pypi.org/project/topease-mcp/" target="_blank">
  <img src="https://img.shields.io/pypi/pyversions/topease-mcp" alt="Python">
</a>

全球海关贸易数据 MCP 服务 — 提供 238 个国家/地区的进出口贸易数据查询能力。

## 简介

`topease-customs-data` 是一个 MCP（Model Context Protocol）服务器，对接 [tradee.topease.net](https://tradee.topease.net/) 海关智能体贸易数据平台，支持按**进出口企业名称**、**产品关键字**、**HS编码**、**贸易时间**、**进出口类型**及**国家/市场/地区**进行多维度联合查询，帮助大模型快速获取真实的全球贸易情报数据。

> 使用前需在 [https://tradee.topease.net/](https://tradee.topease.net/) 注册并获取 API Key。

## 特性

- 🌍 **全球覆盖**：支持 238 个国家/地区的贸易数据查询
- 🔍 **多维度查询**：企业名称、产品关键字、HS 编码、贸易时间、进出口类型、国家联合筛选
- 🔐 **安全认证**：支持 API Key 认证，保护数据访问安全
- 🚀 **两种传输模式**：支持 stdio（桌面客户端）和 streamable-http（Web 应用）两种运行模式
- 📊 **丰富的返回字段**：包含企业信息、产品详情、贸易金额、数量、重量等完整数据

## 安装

### 使用 pip

```bash
pip install topease-mcp
```

### 使用 uv

```bash
uv add topease-mcp
```

### 使用 uvx（免安装，直接运行）

```bash
uvx topease-mcp
```

### 从源码安装

```bash
git clone https://github.com/topease020/topease-customs-mcp-server.git
cd topease-customs-mcp-server
uv pip install -e .
```

## 快速开始

### 方式一：stdio 模式（推荐用于 Claude Desktop、Trae 等桌面客户端）

在 Claude Desktop、Trae 等 MCP 客户端的配置文件中添加：

```json
{
  "mcpServers": {
    "topease-customs-data": {
      "command": "uvx",
      "args": ["topease-mcp"],
      "env": {
        "TOPEASE_MCP_API_KEY": "<YOUR_API_KEY>"
      }
    }
  }
}
```

或使用 pip 安装的版本：

```json
{
  "mcpServers": {
    "topease-customs-data": {
      "command": "python",
      "args": ["-m", "topease-mcp"],
      "env": {
        "TOPEASE_MCP_API_KEY": "<YOUR_API_KEY>"
      }
    }
  }
}
```

### 方式二：streamable-http 模式（推荐用于 Web 应用）

#### 公共服务地址

我们提供了公共的 streamable-http 服务，您可以直接使用以下配置：

| 配置项 | 值 |
|--------|------|
| **服务类型** | 可流式传输的 HTTP (streamableHttp) |
| **服务 URL** | `https://mcp.topease.net/mcp` |
| **请求头** | `Authorization=Bearer <your_api_key>` |

#### 在大模型客户端中配置

在 Claude Desktop、Trae 等支持 streamable-http 的客户端中添加配置：

```json
{
  "mcpServers": {
    "【PRO】TOPEASE 贸易数据查询 stream http": {
      "type": "streamableHttp",
      "url": "https://mcp.topease.net/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_API_KEY>"
      }
    }
  }
}
```

## API Key 配置说明

本服务支持两种 API Key 配置方式（按优先级排序）：

1. **环境变量**（推荐）：设置 `TOPEASE_MCP_API_KEY` 环境变量
2. **HTTP 请求头**（streamable-http 模式）：通过 `Authorization: Bearer <your_api_key>` 请求头传递

## 可用工具

### search_customs_data

查询海关贸易数据。支持多维度联合过滤。

| 参数 | 类型 | 必填 | 说明 | 默认值 |
|------|------|------|------|--------|
| `company_name` | string | 否 | 企业名称（模糊匹配进口商/出口商） | - |
| `product_keyword` | string | 否 | 产品描述关键字，如 "led"、"valve" | - |
| `hs_code` | string | 否 | HS 海关编码（前缀匹配），如 "8415" | - |
| `trade_type` | string | 否 | 贸易类型：`import`（进口）、`export`（出口）、`all`（全部） | `all` |
| `country` | string | 否 | 国家/地区名称（中文/英文/ISO编码均可），如 "China"、"美国"、"JP" | - |
| `date_from` | string | 否 | 起始日期，格式 YYYY-MM-DD | - |
| `date_to` | string | 否 | 结束日期，格式 YYYY-MM-DD | - |
| `page_index` | int | 否 | 页码 | `1` |
| `page_size` | int | 否 | 每页记录数（最大 20） | `20` |
| `sort_by` | string | 否 | 排序字段：`tradedate`、`quantity`、`weight`、`uusd` | `tradedate` |
| `sort_order` | string | 否 | 排序方向：`asc` / `desc` | `desc` |

> **注意**：
> 1. `company_name`、`product_keyword`、`hs_code`、`country` 至少填写一个
> 2. `page_size` 最大值为 20，超出会自动截断
> 3. `trade_type` 映射：`import`→1, `export`→0, `all`→2

## 返回字段说明

每条记录包含以下字段（中文键名，便于大模型理解）：

| 字段 | 说明 |
|------|------|
| `单据ID` | 单据编号 |
| `海关编码` | HS 海关编码 |
| `产品描述` | 产品描述 |
| `贸易类型` | 贸易类型（`进口` / `出口`） |
| `进口商` | 进口商名称 |
| `出口商` | 出口商名称 |
| `数量` | 数量 |
| `数量单位` | 数量单位 |
| `重量` | 重量 |
| `金额(USD)` | 金额（USD），保留 4 位小数 |
| `贸易日期` | 贸易日期 |
| `原产国` | 原产国 |
| `原产国ID` | 原产国 ID |

同时包含分页信息：

| 字段 | 说明 |
|------|------|
| `total` | 总记录数 |
| `page_index` | 当前页码 |
| `page_size` | 每页记录数 |
| `total_pages` | 总页数 |

## 使用示例

### 示例 1：按产品关键字查询

```
请帮我查一下 LED 产品 2025 年从美国的进口数据，前 5 条
```

大模型将自动调用：

```json
{
  "product_keyword": "led",
  "country": "美国",
  "trade_type": "import",
  "date_from": "2025-01-01",
  "date_to": "2025-12-31",
  "page_index": 1,
  "page_size": 5
}
```

### 示例 2：按企业名称查询

```
查询 IKEA SUPPLY AG 公司 2025 年从美国的出口记录
```

```json
{
  "company_name": "IKEA SUPPLY AG",
  "country": "美国",
  "trade_type": "export",
  "date_from": "2025-01-01",
  "date_to": "2025-12-31"
}
```

### 示例 3：按国家和 HS 编码查询

```
查询日本 8415 类目下的进口贸易数据
```

```json
{
  "country": "Japan",
  "hs_code": "8415",
  "trade_type": "import"
}
```

### 示例 4：使用 HTTP 请求头传递 API Key（streamable-http 模式）

```bash
curl -X POST https://mcp.topease.net/mcp \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_api_key" \
  -d '{
    "name": "search_customs_data",
    "parameters": {
      "product_keyword": "CABIN",
      "page_index": 1,
      "page_size": 10
    }
  }'
```

## 开发指南

### 项目结构

```
topease-mcp/
├── src/
│   └── topease_mcp/
│       ├── __init__.py      # 包初始化
│       ├── __main__.py      # 模块入口：python -m topease_mcp
│       ├── main.py          # MCP 服务入口，FastMCP 服务器定义
│       ├── customs.py       # 海关数据模型与 API 调用服务
│       ├── country.py       # 238 个国家/地区数据（含 ISO 编码）
│       ├── auth.py          # API Key 认证模块
│       └── setting.py       # 配置项（API 地址、端口）
├── pyproject.toml           # 项目配置与依赖
├── README.md                # 项目文档
└── .env.example             # 环境变量示例
```

### 核心模块说明

- **`main.py`**：定义 FastMCP 服务器，注册 `search_customs_data` 工具，处理 API Key 认证逻辑
- **`customs.py`**：定义数据模型（`CustomsRecord`、`CustomsQueryParams`），封装 API 请求和响应处理
- **`country.py`**：包含 238 个国家/地区数据，支持通过名称、英文名、ISO 编码查找国家 ID
- **`auth.py`**：API Key 验证模块，支持环境变量配置有效密钥列表
- **`setting.py`**：集中管理 API 基础地址和端口配置

### 本地开发

```bash
# 1. 克隆项目
git clone https://github.com/topease020/topease-customs-mcp-server.git
cd topease-customs-mcp-server

# 2. 安装依赖
uv sync

# 3. 运行测试（如果有）
uv run pytest

# 4. 本地运行
uv run python -m topease_mcp
```

## 常见问题

### Q: 支持哪些国家/地区？
A: 支持全球 238 个国家和地区，包括主要贸易经济体。可通过中文名、英文名、ISO 2/3 位编码查询。

### Q: 数据更新频率是多少？
A: 数据定期更新，具体请参考 [topease.net](https://tradee.topease.net/) 官网说明。

### Q: 如何获取 API Key？
A: 访问 [https://tradee.topease.net/](https://tradee.topease.net/) 注册账号即可获取。

### Q: 查询有什么限制？
A: API 有请求频率限制，具体限制请查看 API 文档。`page_size` 最大值为 20。

### Q: 为什么工具参数中没有 `api_key`？
A: 为了简化大模型调用，API Key 通过环境变量或 HTTP 请求头配置，不再需要在每次调用时传入参数。

### Q: 如何切换 stdio 和 streamable-http 模式？
A: 修改 `main.py` 中 `mcp.run()` 的 `transport` 参数即可：
- `transport="stdio"` — 桌面客户端模式
- `transport="streamable-http"` — Web 应用模式

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件。

## 贡献

欢迎提交 Issue 和 Pull Request！

## 联系方式

- 官网：[https://tradee.topease.net/](https://tradee.topease.net/)
- PyPI：[https://pypi.org/project/topease-mcp/](https://pypi.org/project/topease-mcp/)
- GitHub：[https://github.com/topease020/topease-customs-mcp-server.git](https://github.com/topease020/topease-customs-mcp-server.git)
