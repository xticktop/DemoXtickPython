# XTick 金融行情数据平台

<p align="center">
  <a href="http://www.xtick.top/">
    <img src="./doc/images/xticklogo.png" alt="XTick Logo" style="width:260px;height:120px">
  </a>
</p>

<p align="center">
  <strong>专业金融行情数据API服务平台</strong>
</p>

<p align="center">
  <a href="https://github.com/xticktop/xtick">
    <img src="https://img.shields.io/badge/GitHub-XTick-blue.svg" alt="GitHub">
  </a>
  <a href="http://www.xtick.top/">
    <img src="https://img.shields.io/badge/Website-XTick-green.svg" alt="Website">
  </a>
  <a href="https://img.shields.io/badge/Python-3.8+-blue.svg">
    <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  </a>
  <a href="https://img.shields.io/badge/License-MIT-yellow.svg">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  </a>
</p>

---

## 📖 项目介绍

XTick是一个专业的金融行情数据API服务平台，为量化交易、投资分析、金融研究提供强大的数据支撑。平台提供沪深京A股、港股、指数、ETF、可转债等全市场的实时和历史行情数据。

### ✨ 核心特性

- 🚀 **实时行情**：盘中实时推送分钟级、Tick级行情数据
- 📊 **历史数据**：覆盖多年的K线、财务、股东等历史数据
- 🔢 **量化因子**：提供丰富的量化因子和技术指标计算
- 📈 **短线热点**：连板天梯、市场情绪、资金流向等短线交易数据
- 🌐 **多语言支持**：提供Java、Python等多语言SDK
- ⚡ **高性能**：支持批量查询和全市场数据推送
- 🔒 **安全可靠**：Token认证机制，保障数据安全

---

## 📊 数据覆盖范围

## 已接入数据预览

<p><strong>接入数据预览</strong></p>
<table style="width:89%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;">数据类别</td>
<td style="text-align: left;">数据细分</td>
<td style="text-align: left;">更新方式</td>
<td style="text-align: left;">数据全推</td>
<td style="text-align: left;">获取方式</td>
<td style="text-align: left;">历史数据范围</td>
</tr>
<tr>
<td rowspan="2" style="text-align: center;">tick数据</td>
<td style="text-align: left;">tick实时数据</td>
<td style="text-align: left;">实时更新</td>
<td style="text-align: left;">数据全推</td>
<td style="text-align: left;">api调用</td>
<td rowspan="2" style="text-align: left;"><p>指数和北证：2025年10月-至今</p>
<p>A股、ETF：2025年2月-至今</p></td>
</tr>
<tr>
<td style="text-align: left;">tick历史数据</td>
<td style="text-align: left;">盘后更新</td>
<td style="text-align: left;">按个股获取</td>
<td style="text-align: left;">api调用</td>
</tr>
<tr>
<td rowspan="3" style="text-align: center;">竞价数据</td>
<td style="text-align: left;">竞价实时数据</td>
<td style="text-align: left;">实时更新</td>
<td style="text-align: left;">数据全推</td>
<td style="text-align: left;">api调用</td>
<td rowspan="3" style="text-align: left;"><p>竞价历史：2025年7月-至今</p>
<p>竞价历史详情：2025年2月-至今</p></td>
</tr>
<tr>
<td style="text-align: left;">竞价历史数据</td>
<td style="text-align: left;">9:25分更新</td>
<td style="text-align: left;">数据全推</td>
<td style="text-align: left;">api调用</td>
</tr>
<tr>
<td style="text-align: left;">竞价历史详情数据</td>
<td style="text-align: left;">9:25分更新</td>
<td style="text-align: left;">按个股获取</td>
<td style="text-align: left;">api调用</td>
</tr>
<tr>
<td rowspan="3" style="text-align: center;">分钟数据</td>
<td style="text-align: left;">1分钟实时数据</td>
<td style="text-align: left;">实时更新</td>
<td style="text-align: left;">数据全推</td>
<td style="text-align: left;">api调用</td>
<td rowspan="3" style="text-align: left;"><p>分钟级别数据：2024年4月-至今</p>
<p>所有分钟周期数据，均支持复权</p></td>
</tr>
<tr>
<td style="text-align: left;">1分钟K线数据</td>
<td style="text-align: left;">按1分钟频率实时更新</td>
<td style="text-align: left;">数据全推</td>
<td style="text-align: left;">api调用</td>
</tr>
<tr>
<td style="text-align: left;">其它分钟K线数据</td>
<td style="text-align: left;">按1分钟频率实时更新</td>
<td style="text-align: left;">按个股获取</td>
<td style="text-align: left;">api调用</td>
</tr>
<tr>
<td rowspan="2" style="text-align: center;">日线数据</td>
<td style="text-align: left;">日线实时数据</td>
<td style="text-align: left;">实时更新</td>
<td style="text-align: left;">数据全推</td>
<td style="text-align: left;">api调用</td>
<td rowspan="2" style="text-align: left;"><p>日线级别数据：公司上市-至今</p>
<p>日线数据支持复权</p></td>
</tr>
<tr>
<td style="text-align: left;">日线历史数据</td>
<td style="text-align: left;">3:35分更新</td>
<td style="text-align: left;">数据全推</td>
<td style="text-align: left;">api调用</td>
</tr>
<tr>
<td rowspan="2" style="text-align: center;">量化数据</td>
<td style="text-align: left;">量化因子实时数据</td>
<td style="text-align: left;">实时更新</td>
<td style="text-align: left;">数据全推</td>
<td style="text-align: left;">api调用</td>
<td rowspan="2" style="text-align: left;">2008年1月-至今</td>
</tr>
<tr>
<td style="text-align: left;">量化因子历史数据</td>
<td style="text-align: left;">3:35分更新</td>
<td style="text-align: left;">数据全推</td>
<td style="text-align: left;">api调用</td>
</tr>
<tr>
<td style="text-align: center;">核心指标</td>
<td style="text-align: left;">核心指标实时数据</td>
<td style="text-align: left;">实时更新</td>
<td style="text-align: left;">按个股获取</td>
<td style="text-align: left;">api调用</td>
<td style="text-align: left;">参考量化数据</td>
</tr>
<tr>
<td rowspan="2" style="text-align: center;">金融指标</td>
<td style="text-align: left;">金融指标实时数据</td>
<td style="text-align: left;">实时更新</td>
<td style="text-align: left;">按个股获取</td>
<td style="text-align: left;">api调用</td>
<td rowspan="2" style="text-align: left;"><p>分钟级别指标：2024年4月-至今</p>
<p>日线级别指标：公司上市-至今</p></td>
</tr>
<tr>
<td style="text-align: left;">金融指标历史数据</td>
<td style="text-align: left;">3:35分更新</td>
<td style="text-align: left;">按个股获取</td>
<td style="text-align: left;">api调用</td>
</tr>
<tr>
<td style="text-align: center;">财务数据</td>
<td style="text-align: left;">盘后更新</td>
<td style="text-align: left;">盘后更新</td>
<td style="text-align: left;">按个股获取</td>
<td style="text-align: left;">api调用</td>
<td style="text-align: left;">2008年1月-至今</td>
</tr>
<tr>
<td rowspan="3" style="text-align: center;">其它数据</td>
<td style="text-align: left;">交易日历</td>
<td style="text-align: left;">3:35分更新</td>
<td style="text-align: left;">按个股获取</td>
<td style="text-align: left;">api调用</td>
<td style="text-align: left;">公司上市-至今</td>
</tr>
<tr>
<td style="text-align: left;">股票列表</td>
<td style="text-align: left;">盘后更新</td>
<td style="text-align: left;">按个股获取</td>
<td style="text-align: left;">api调用</td>
<td style="text-align: left;">每日更新</td>
</tr>
<tr>
<td style="text-align: left;">复权变更数据</td>
<td style="text-align: left;">盘后更新</td>
<td style="text-align: left;">按个股获取</td>
<td style="text-align: left;">api调用</td>
<td style="text-align: left;">公司上市-至今</td>
</tr>
</tbody>
</table>

---

## 📡 API接口文档

XTick平台提供**六大类API接口**，共计**86+个接口**。

### 接口分类总览

| 接口分类 | 接口数量 | 主要功能 |
|---------|---------|----------|
| 行情数据接口 | 8个 | 股票列表、交易日历、K线数据、财务数据等 |
| 盯盘数据接口 | 7个 | 龙虎榜、日K线、分钟K线、买卖五档、成交统计等 |
| 核心数据接口 | 8个 | 竞价数据、核心指标、除权、停牌、ST、分笔分价等 |
| 短线热点接口 | 10个 | 连板天梯、市场情绪、资金流向、新闻、概念板块等 |
| 量化因子接口 | 2个 | 实时和历史量化因子数据 |
| 金融指标接口 | 51+个 | MACD、RSI、KDJ等技术指标计算 |

### 通用说明

- **请求方式**：所有HTTP API均支持GET和POST方法
- **认证方式**：所有接口都需要Token认证
- **返回格式**：JSON格式
- **日期格式**：`YYYY-MM-DD`，如 `2024-01-01`
- **标的类型(type)**：
  - `1` - 沪深京A股
  - `2` - 沪深指数
  - `3` - 港股
  - `4` - ETF基金
  - `5` - 沪深可转债
- **复权类型(fq)**：
  - `1` - 不复权
  - `2` - 前复权
  - `3` - 后复权
  - `4` - 等比前复权
  - `5` - 等比后复权

---



### 1️⃣ 行情数据接口 (Market Data APIs)

#### 1.1 股票列表

**接口地址**：`/doc/stockinfo`

**功能描述**：获取股票列表，包括沪深京A股、港股、指数、ETF、可转债等。

**请求示例**：
```bash
GET http://api.xtick.top/doc/stockinfo?symbol=all&token=YOUR_TOKEN
```

**请求参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| symbol | String | 是 | all-全部, sz-深交所, sh-上交所, bj-北交所, hk-港交所, index-指数, bond-可转债, cyb-创业板, kcb-科创板, etf-ETF, st-ST股票, ts-退市股票 |
| token | String | 是 | API Token |

**返回字段**：type(标的类别), code(股票代码), name(股票名称)

#### 1.2 交易日历

**接口地址**：`/doc/calendar`

**功能描述**：获取A股交易日历，包含交易所和个股交易日历（2020年至今）。

**请求参数**：code(股票代码/all/ssb), startDate, endDate, token

**返回字段**：code, time(交易日期), status(1-正常交易, 2-休市), preTime(上一交易日)

#### 1.3 分钟数据-实时接口

**接口地址**：`/doc/kline/minute`

**功能描述**：获取日内一分钟实时数据。

**请求参数**：type, code(单个股票), fq, token

**返回字段**：type, code, time, open, close, high, low, volume, amount, preClose

#### 1.4 行情数据-通用接口

**接口地址**：`/doc/kline/market`

**功能描述**：获取多周期K线数据（1m/5m/15m/30m/1h/1d/1w/1mon/1q/1y），支持复权。

**请求参数**：type, code(单个股票), fq, period, startDate, endDate, token

**注意事项**：
- 分钟数据单次请求时间跨度不超过31天
- 支持code=all获取全市场数据（仅最近一个月）

#### 1.5 股东数

**接口地址**：`/doc/holdernum`

**功能描述**：获取股东户数数据（2001年至今）。

**请求参数**：code(单个股票), startDate, endDate, token

#### 1.6 财务指标

**接口地址**：`/doc/gaap`

**功能描述**：获取财务指标数据（2007年至今）。

**返回字段**：ocfps(每股经营现金流), bps(每股净资产), eps(每股收益), roe(净资产收益率)等22个字段

#### 1.7 十大股东

**接口地址**：`/doc/topholder`

**功能描述**：获取十大股东数据（公司上市至今）。

#### 1.8 十大流通股东

**接口地址**：`/doc/topflowholder`

**功能描述**：获取十大流通股东数据（2004年至今）。

---

### 2️⃣ 盯盘数据接口 (Watch Data APIs)

#### 2.1 日K线-实时数据

**接口地址**：`/doc/order/day`

**功能描述**：获取盘中实时日K线数据，支持批量和全推。

**请求参数**：type, code(支持单个/批量最多50个/all), token

#### 2.2 分钟K线-实时数据

**接口地址**：`/doc/order/minute`

**功能描述**：获取盘中分钟K线实时数据，支持批量和全推。

#### 2.3 深度行情-实时数据

**接口地址**：`/doc/order/deep`

**功能描述**：获取盘中买卖五档盘口实时数据（Tick数据）。

**返回字段**：lastPrice, open, high, low, bp1-bp5(买一至买五价), bv1-bv5(买量), sp1-sp5(卖价), sv1-sv5(卖量)等

#### 2.4 深度行情-历史数据

**接口地址**：`/doc/order/history`

**功能描述**：获取盘中买卖五档历史数据，盘后更新。

**请求参数**：type, code(单个股票), tradeDate, token

#### 2.5 成交统计

**接口地址**：`/doc/order/amount`

**功能描述**：按交易日获取全市场成交额统计。

---

### 3️⃣ 核心数据接口 (Core Data APIs)

#### 3.1 竞价数据-实时接口

**接口地址**：`/doc/core/bidtime`

**功能描述**：获取交易日盘中实时竞价数据（9:15-9:25）。

**请求参数**：type, code(支持单个/批量/all), token

#### 3.2 核心指标-实时接口

**接口地址**：`/doc/core/time`

**功能描述**：获取盘中实时指标数据（涨速、换手率、市盈率、市净率等）。

**请求参数**：type, code(单个股票), field(多个字段用逗号分隔，最多10个), token

#### 3.3 除权变更数据

**接口地址**：`/doc/core/chuquan`

**功能描述**：获取股票除权除息历史数据，盘后更新。

**请求参数**：type, code(单个/all), startDate, endDate, token

#### 3.4 停牌数据

**接口地址**：`/doc/core/tingpai`

**功能描述**：获取停牌股票历史数据，盘后更新。

#### 3.5 ST数据

**接口地址**：`/doc/core/st`

**功能描述**：获取ST股票历史数据（2022年3月至今），盘后更新。

#### 3.6 涨跌停价格

**接口地址**：`/doc/core/price`

**功能描述**：获取股票涨跌停历史数据，盘后更新。

**请求参数**：type, code, fq(复权类型), startDate, endDate, token

#### 3.7 分笔数据

**接口地址**：`/doc/core/fenbi`

**功能描述**：获取股票分时成交数据。

**请求参数**：type, code(单个股票), tradeDate, token

#### 3.8 分价数据

**接口地址**：`/doc/core/fenjia`

**功能描述**：获取股票分价成交数据，盘后更新。

---

### 4️⃣ 短线热点接口 (Hot Spot APIs)

#### 4.1 连板天梯-实时接口

**接口地址**：`/doc/hot/board`

**功能描述**：获取涨停板、跌停板、炸板数据。

**请求参数**：type, flag(1-涨停, 2-跌停, 3-炸板), tradeDate, token

#### 4.2 市场情绪-实时接口

**接口地址**：`/doc/hot/emotion`

**功能描述**：获取市场情绪数据，短线选手复盘必备工具。

#### 4.3 资金流向-实时接口

**接口地址**：`/doc/hot/timemoney`

**功能描述**：获取资金流数据，盘中实时更新。

**请求参数**：type, code(单个/all), startDate, endDate, token

#### 4.4 竞价数据-历史接口

**接口地址**：`/doc/hot/bidhistory`

**功能描述**：获取竞价历史数据，仅保留集合竞价最后一条数据和开盘数据。

**请求参数**：type, code, seq(0-9:25数据, 1-倒数第二条), startDate, endDate, token

#### 4.5 竞价详情-实时接口

**接口地址**：`/doc/hot/biddetail`

**功能描述**：获取开盘集合竞价阶段个股的所有竞价信息，9:25更新。

#### 4.6 新闻资讯-实时接口

**接口地址**：`/doc/hot/news`

**功能描述**：获取财联社、新浪财经、格隆汇、华尔街见闻等主流金融平台资讯。

**请求参数**：minutes(>0获取最近分钟数, =0按tradeDate获取历史), tradeDate, token

#### 4.7 日内分时-实时接口

**接口地址**：`/doc/hot/timekline`

**功能描述**：获取股票盘中日内分时数据。

#### 4.8 概念板块成分股数据

**接口地址**：`/doc/hot/bk`

**功能描述**：获取概念板块、地域板块、行业板块及成分股数据。

**请求参数**：symbol(sw1/sw2/sw3申万行业, zjh1/zjh2证监会行业, bdy1/bdy2地域, ahy行业, afg风格, agn/bgn/cgn概念), token

#### 4.9 股票关联概念板块数据

**接口地址**：`/doc/hot/gainian`

**功能描述**：获取个股关联的概念板块、地域板块、行业板块数据。

#### 4.10 增量更新

**接口地址**：`/doc/hot/dayupdate`

**功能描述**：提供交易日当天全市场增量数据（收盘后历史数据）。

**请求参数**：dataType(bid-竞价详情, 1m-1分钟数据), symbol(index/etf/cyb/kcb/bj/szm/shm), tradeDate, token

**注意**：该接口数据量大，严格限流，请勿频繁调用。

---

### 5️⃣ 量化因子接口 (Quant Factor APIs)

#### 5.1 量化因子-实时接口

**接口地址**：`/doc/quant/data`

**功能描述**：获取盘中实时因子指标数据，支持全推。

**请求参数**：type, field(all或指定字段，最多10个), token

**常用字段**：
- x001-x005: 昨收价、最新价、开盘价、最高价、最低价
- x006-x007: 成交量、成交额
- x015: 涨速, x016-x020: 1-5分钟涨速
- x021-x023: 静态/动态/TTM市盈率
- x024-x025: 总市值、流通市值
- x026-x028: 市净率、换手率、实际换手率
- x033-x038: 5/10/20/30/60/120日均线
- x039-x041: MACD-DIF/DEA/MACD
- x042-x044: KDJ-K/D/J
- x045-x047: RSI、WR、CCI

#### 5.2 量化因子-历史接口

**接口地址**：`/doc/quant/history`

**功能描述**：获取盘中因子指标历史数据，盘后更新。

**请求参数**：tradeDate, token

---

### 6️⃣ 金融指标接口 (Indicator APIs)

提供51+技术指标计算，每个指标对应独立API端点。

**主要指标**：
- **趋势指标**：AD(累积/分布线), MACD(平滑异同移动平均线), SMA(简单移动平均), EMA(指数移动平均)
- **震荡指标**：RSI(相对强弱指数), KDJ(随机指标), WR(威廉指标), CCI(顺势指标)
- **成交量指标**：OBV(能量潮), MFI(资金流量指标)
- **波动指标**：ATR(真实波幅), BOLL(布林带)
- **其他指标**：WMA(加权移动平均), SAR(抛物线转向)等

**通用参数**：type, code, period, fq, startDate, endDate, inReal, optInFastPeriod, optInSlowPeriod, optInSignalPeriod, token

**详细文档**：[http://www.xtick.top/indicator](http://www.xtick.top/indicator)

---

## 🚀 Python SDK使用指南

本项目提供了完整的Python API调用示例，位于 `xtick/scripts/api/` 目录。

### 项目结构

```
xtick/scripts/
├── api/
│   ├── XTickBaseApi.py        # 基础数据接口（8个接口）
│   ├── XTickMarketApi.py      # 行情数据接口（8个接口）
│   ├── XTickWatchApi.py       # 盯盘数据接口（7个接口）
│   ├── XTickCoreApi.py        # 核心数据接口（8个接口）
│   ├── XTickHotApi.py         # 短线热点接口（10个接口）
│   ├── XTickQuantApi.py       # 量化因子接口（2个接口）
│   ├── XTickIndicatorApi.py   # 金融指标接口（51+个指标）
├── XTickStockApiClient.py     # 完整测试客户端
├── Config.py                  # 配置文件
└── util/
    ├── XTickUtil.py           # 工具类
    └── DataConvert.py         # 数据转换
```

### 快速开始

#### 1. 安装依赖

```bash
pip install -r requirements.txt
```

#### 2. 配置Token

编辑 `xtick/scripts/Config.py`：

```python
TOKEN = "your_token_here"  # 从 http://www.xtick.top/ 获取
SERVER_URL = "http://api.xtick.top"
```

#### 3. 调用API示例

```python
from xtick.scripts.api.XTickMarketApi import getKlineMarket
from xtick.scripts.Config import Config
import json

# 获取平安银行日K线数据
result = getKlineMarket(
    type=1,              # 沪深京A股
    code="000001",       # 股票代码
    fq=1,                # 不复权
    period="1d",         # 日线
    startDate="2024-01-01",
    endDate="2024-12-31",
    token=Config.TOKEN
)

data = json.loads(result)
print(f"获取到 {len(data)} 条K线数据")
```

#### 4. 运行完整测试

```bash
# 运行所有接口测试
python xtick/scripts/XTickStockApiClient.py

# 或单独测试某个模块
python -c "from xtick.scripts.XTickStockApiClient import XTickStockApiClient; \
           client = XTickStockApiClient(); \
           client.demoForMarketApi()"
```

### 完整测试客户端

`XTickStockApiClient.py` 提供了所有接口的完整测试用例：

```python
from xtick.scripts.XTickStockApiClient import XTickStockApiClient

client = XTickStockApiClient()

# 按需选择要测试的接口
client.demoForMarketApi()       # 行情数据接口（8个）
client.demoForWatchApi()        # 盯盘数据接口（7个）
client.demoForCoreApi()         # 核心数据接口（8个）
client.demoForHotApi()          # 短线热点接口（10个）
client.demoForQuantApi()        # 量化因子接口（2个）
client.demoForIndicatorApi()    # 金融指标接口（示例）

# 或运行所有测试（注意：会调用大量API）
client.allDemo()
```

---

## 📝 使用示例

### HTTP请求示例

```bash
# 获取股票列表
curl "http://api.xtick.top/doc/stockinfo?symbol=index&token=YOUR_TOKEN"

# 获取K线数据
curl "http://api.xtick.top/doc/kline/market?type=1&code=000001&fq=1&period=1d&startDate=2024-01-01&endDate=2024-12-31&token=YOUR_TOKEN"

# 获取实时买卖五档
curl "http://api.xtick.top/doc/order/five?type=1&code=000001&token=YOUR_TOKEN"
```

### Python调用示例

```python
import requests
import json
import pandas as pd

TOKEN = "YOUR_TOKEN"
BASE_URL = "http://api.xtick.top"

def get_kline_data(code, period="1d", start_date="2024-01-01", end_date="2024-12-31"):
    """获取K线数据"""
    url = f"{BASE_URL}/doc/kline/market"
    params = {
        "type": 1,
        "code": code,
        "fq": 1,
        "period": period,
        "startDate": start_date,
        "endDate": end_date,
        "token": TOKEN
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    return pd.DataFrame(data)

# 使用示例
df = get_kline_data("000001")
print(df.head())
print(f"数据条数: {len(df)}")
```

更多示例请参考 `xtick/scripts/XTickStockApiClient.py`

---

## ⚠️ 注意事项

### API调用限制

1. **频率限制**：请合理控制API调用频率，避免频繁请求
2. **批量限制**：批量查询时单次最多50个股票代码
3. **时间跨度**：分钟数据单次请求时间跨度不超过31天
4. **全推数据**：使用`code=all`参数时请注意数据量较大
5. **增量更新接口**：严格限流，请勿频繁调用

### 数据准确性

1. 实时数据可能存在秒级延迟
2. 财务数据以公司公告为准
3. 复权数据仅供参考，实际交易请以券商数据为准

### Token安全

1. 请勿将Token泄露给他人
2. 建议定期更换Token
3. 不要在公开代码中硬编码Token

---

## 🔗 相关链接

- **官方网站**：[http://www.xtick.top/](http://www.xtick.top/)
- **API文档**：[飞书文档](https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf)
- **金融指标API**：[http://www.xtick.top/indicator](http://www.xtick.top/indicator)
- **GitHub**：[https://github.com/xticktop/xtick](https://github.com/xticktop/xtick)
- **Gitee**：[https://gitee.com/xtick/xtick](https://gitee.com/xtick/xtick)
- **Skills项目**：[https://github.com/xticktop/skills](https://github.com/xticktop/skills)

---

## 👥 交流与支持

### QQ交流群

欢迎加入QQ群进行交流（加群备注：**XTick**）

<img src="./doc/images/qqGroup.png" alt="QQ群" width="300">

### 联系方式

- **邮箱**：xticktop@163.com
- **问题反馈**：通过GitHub Issues提交

---

## 📄 许可证

本项目采用 MIT 许可证 - 查看 LICENSE 文件了解详情

---

## 🙏 致谢

感谢所有为本项目做出贡献的开发者和用户！

您的支持是我们继续维护项目的动力，欢迎Star和Fork！

---

**免责声明**：本项目仅供学习和研究使用，请勿用于商业用途。平台提供的数据仅供参考，不构成投资建议。投资有风险，入市需谨慎。
