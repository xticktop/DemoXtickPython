# XTick

<p align=center>
  <a href="http://www.xtick.top/">
    <img src="./doc/images/xticklogo.png" alt="实时行情报价数据接口" style="width:260px;height:120px">
  </a>
</p>

<p align=center>
   XTick提供实时行情报价数据接入解决方案。
</p>

## 项目介绍

XTick行情API提供了全面、准确、稳定的行情数据，帮助开发者和研究者构建创新的交易和分析工具，满足金融行业的需求，进行深入的市场分析和模型验证。
<br>您的支持，是我们继续维护好XTick项目的动力。<br>
<p align=center>
  <a href="http://www.xtick.top/">
    <img src="./doc/images/xtick.png" alt="实时行情报价数据接口">
  </a>
</p>

## API接口文档
   API接口分为订阅数据、历史数据两大块。<br>
   除了订阅接口是Websocket API，其余接口为Http API接口且均支持GET和POST方法，下面以GET请求示例。 <br>

2.1 订阅数据接口
   在GitHub上，已实现Java版本和Python版本的订阅代码，请先下载代码直接调用。<br>
   订阅数据按照证券交易所订阅推送，包括上交所、深交所、北交所、港交所（只支持部分股票）。<br>
   数据为实时推送，发数据非常快，客户端接受到数据后，最好做异步处理，将接受数据和数据处理分开，避免接受数据阻塞。<br>
1. 订阅方法：<br>
   订阅数据：订阅为Websocket API，请在Github上下载开源项目，参考XTickWebSocketClient.java中已实现的订阅功能。<br>
   入参1：authCodes 枚举取值如下：
- tick.SZ - 订阅深交所A股的tick数据。
- tick.SH - 订阅上交所A股的tick数据。
- tick.BJ - 订阅北交所A股的tick数据。
- tick.HK - 订阅港交所港股的tick数据。
- time.SZ - 订阅深交所A股的k线数据，包括time、1m。
- time.SH - 订阅上交所A股的k线数据，包括time、1m。
- time.BJ - 订阅北交所A股的k线数据，包括time、1m。
- time.HK - 订阅港交所港股的k线数据，包括time、1m。<br>
  入参2：token 登录XTick网站，注册获取<br>

取消订阅：http://api.xtick.top/doc/unsubscribe?token=043fbdcba7f3f3ab332ffff123456789 <br>
入参：token 登录XTick网站，注册获取

2.2 行情数据接口
1. 请求方法：
   请求地址：http://api.xtick.top/doc/market?type=1&code=000001&period=tick&fq=none&startDate=2025-03-25&endDate=2025-03-25&token=043fbdcba7f3f3ab332ffff123456789
   备注：行情数据支持交易日内盘内实时更新。
   入参1：type 股票类别
   沪深京A股type=1，港股type=3，沪深ETF type=20;
   入参2：code 股票代码
   比如平安银行为000001
   入参3：period 用于表示要获取的周期，枚举取值如下：
- tick - 分笔数据
- 1m - 1分钟线
- 5m - 5分钟线
- 15m - 15分钟线
- 30m - 30分钟线
- 1h - 1小时线
- 1d - 日线
- 1w - 周线
- 1mon - 月线
- 1q - 季度线
- 1hy - 半年线
- 1y - 年线
  参数4：fq 除权方式，用于K线数据复权计算，对tick等其他周期数据无效，枚举取值如下：
- none 不复权
- front 前复权
- back 后复权
- front_ratio 等比前复权
- back_ratio 等比后复权
  参数5：时间范围，用于指定数据请求范围，表示的范围是[startDate , endDate]区间（包含前后边界）。
  特别说明：period为tick类型，则单次请求时间跨度最大为一天，即startDate和endDate日期需设置为同一天。
  period为分钟类型（包括1m、5m、15m、30m、1h），则单次请求时间跨度最大为一月，即endDate - startDate不超过30天。
- startDate - 起始时间，日期格式：2025-03-25
- endDate- 结束时间，日期格式：2025-03-25
  入参6：token 登录XTick网站，注册获取

2.3 财务数据接口
1. 请求方法：
   请求地址：http://api.xtick.top/doc/financial?type=1&code=000001&report=Pershareindex&startDate=2020-03-25&endDate=2025-03-25&token=043fbdcba7f3f3ab332ffff123456789
   入参1：type 股票类别
   沪深京A股type=1，港股type=3;
   入参2：code 股票代码
   比如平安银行为000001
   入参3：report 用于表示要获取的财务报表，枚举取值如下：
- Balance - 资产负债表
- Income - 利润表
- CashFlow - 现金流量表
- Capital - 股本表
- Holdernum - 股东数
- Top10holder - 十大股东
- Top10flowholder - 十大流通股东
- Pershareindex - 每股指标
  参数4：时间范围，用于指定数据请求范围，表示的范围是[startDate , endDate]区间（包含前后边界）。
- startDate - 起始时间，日期格式：2025-03-25
- endDate- 结束时间，日期格式：2025-03-25
  入参5：token 登录XTick网站，注册获取

## 项目地址

目前项目托管在 Gitee 和 Github 平台上中，欢迎大家 Star 和 Fork 支持~ <br>

### Java SDK :

Gitee地址：https://github.com/xticktop/xtick <br>
Github地址：https://github.com/xticktop/xtick <br>

## 关注&交流

为了方便小伙伴们沟通交流，创建了QQ群 (加群备注：XTick)
，目前项目还存在很多不足之处，欢迎各位大佬进群进行交流，为了防止广告进入，希望加群的时候能添加备注，谢谢~<br>
如遇问题联系作者，邮箱：xticktop@163.com <br>
[网站说明文档](https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf)<br>

| QQ群【推荐】                                                                                  |
|------------------------------------------------------------------------------------------|
| <img src="./doc/images/qqGroup.png" width="200"  height="200" /> |






