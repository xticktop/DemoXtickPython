import json
from datetime import datetime, timedelta

import pandas as pd

from xtick.code.Config import Config
from xtick.code.api import XTickMarketApi, XTickIndicatorApi, XTickBaseApi, XTickWebSocketApi, XTickWatchApi, \
    XTickQuantApi

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
'''


class XTickWebSocketClient(object):
    def demoForWebSocketApi(self):
        print("#####################################")
        token: str = Config.TOKEN  # 登录XTick官网，获取token
        print(f"[websocket.querysubscribe]:")
        result = XTickWebSocketApi.querysubscribe(token, "get")
        print(json.loads(result))

        print(f"[websocket.unsubscribe]:")
        result = XTickWebSocketApi.unsubscribe(token, "get")
        print(json.loads(result))

    def demoForBaseApi(self):
        print("#####################################")
        code: str = "000001"
        startDate: str = "2025-12-01"
        endDate: str = "2025-12-31"
        token: str = Config.TOKEN  # 登录XTick官网，获取token
        print(f"[base.calendar]code={code},startDate={startDate},endDate={endDate}:")
        result = XTickBaseApi.getCalendar(code, startDate, endDate, token, "get")
        df = pd.DataFrame(json.loads(result))
        print(df)

        print(f"[base.calendar]code=all,startDate={startDate},endDate={endDate}:")
        result = XTickBaseApi.getCalendar('all', "2025-12-23", "2025-12-23", token, "get")
        df = pd.DataFrame(json.loads(result))
        print(df)

        symbol: str = "cyb"  # 创业板
        print(f"[base.stockinfo]symbol={symbol}:")
        result = XTickBaseApi.getStockInfo(symbol, token, "get")
        df = pd.DataFrame(json.loads(result))
        print(df)

    def demoForWatchApi(self):
        print("#####################################")
        type: int = 1
        code: str = "000001"
        tradeDate: str = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        endDate: str = datetime.now().strftime("%Y-%m-%d")
        token: str = Config.TOKEN  # 登录XTick官网，获取token
        print(f"[watch.tick.time]type={type},code={code}:")
        result = XTickWatchApi.getTickTime(type, code, "tick", token, "get")
        print(result)

        print(f"[watch.tick.time]type={type},code=all:")
        result = XTickWatchApi.getTickTime(type, "all", "tick", token, "get")
        df = pd.DataFrame(json.loads(result))
        print(df)

        print(f"[watch.tick.history]type={type},code={code},tradeDate={tradeDate}:")
        result = XTickWatchApi.getTickHistory(type, code, tradeDate, token, "get")
        df = pd.DataFrame(result)
        print(df)

        print(f"[watch.bid.history]type={type},code={code},startDate={tradeDate},endDate={endDate}:")
        result = XTickWatchApi.getBidHistory(type, code, tradeDate, endDate, token, "get")
        df = pd.DataFrame(json.loads(result))
        print(df)

        print(f"[watch.bid.detail]type={type},code={code},tradeDate={tradeDate}:")
        result = XTickWatchApi.getBidDetail(type, code, tradeDate, token, "get")
        df = pd.DataFrame(json.loads(result))
        print(df)

        print(f"[watch.bid.time]type={type},code=all:")
        result = XTickWatchApi.getBidTime(type, "all", token, "get")
        df = pd.DataFrame(json.loads(result))
        print(df)

        print(f"[watch.bid.time.option]type={type},code={code}:")
        option = {"filter": "jjzf>5;jje>=10000000", "sort": "noe", "asc": 0, "limit": 100}
        result = XTickWatchApi.getBidTimeWithOption(type, "all", option, token, "get")
        df = pd.DataFrame(json.loads(result))
        print(df)

    def demoForQuantApi(self):
        print("#####################################")
        type: int = 1
        code: str = "000001"
        field: str = "x001,x002,x003,x004,x005"
        tradeDate: str = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        token: str = Config.TOKEN  # 登录XTick官网，获取token

        print(f"[core.time]type={type},code={code},field={field}:")
        result = XTickQuantApi.getCoreTime(type, code, field, token, "get")
        print(json.loads(result))

        print(f"[core.change]type={type},tradeDate={tradeDate}:")
        result = XTickQuantApi.getCoreChange(type, tradeDate, token, "get")
        df = pd.DataFrame(json.loads(result))
        print(df)

        print(f"[quant.data]type={type},field={field}:")
        result = XTickQuantApi.getQunatData(type, field, token, "get")
        df = pd.DataFrame(json.loads(result)['data'])
        print(df)

        print(f"[quant.data]type={type},field=all:")
        result = XTickQuantApi.getQunatData(type, "all", token, "get")
        df = pd.DataFrame(json.loads(result)['data'])
        print(df)

    def demoForMarketApi(self):
        print("#####################################")
        type: int = 1  # 沪深京A股Type=1,港股Type=3,ETF Type=20
        code: str = "000001"
        startDate: str = "2025-12-01"
        endDate: str = "2025-12-31"
        token: str = Config.TOKEN  # 登录XTick官网，获取token
        historyKlinePeriods = ["1m", "5m", "15m", "30m", "1h", "2h", "1d", "1w", "1mon", "1q", "1hy", "1y"]  # K线周期
        dividends = ["1", "2", "3", "4", "5"]  # 复权类型
        for period in historyKlinePeriods:
            for fq in dividends:
                print(
                    f"[kline.market]type={type},code={code},period={period},fq={fq},startDate={startDate},endDate={endDate}:")
                result = XTickMarketApi.getKlineMarket(type, code, period, fq, startDate, endDate, token, "get")
                df = pd.DataFrame(json.loads(result))
                print(df)

        for fq in dividends:
            print(f"[kline.minute]type={type},code={code},fq={fq}:")
            result = XTickMarketApi.getKlineMinute(type, code, fq, token, "get")
            df = pd.DataFrame(json.loads(result))
            print(df)

    def demoForFinancialApi(self):
        print("#####################################")
        type: int = 1  # 沪深京A股Type=1,港股Type=3,ETF Type=20
        code: str = "000001"
        startDate: str = "2024-04-25"
        endDate: str = "2025-05-25"
        token: str = Config.TOKEN  # 登录XTick官网，获取token

        reports = ["Pershareindex", "Balance", "CashFlow", "Capital", "Holdernum", "Top10holder",
                   "Top10flowholder"]  # 财务报表类型

        for report in reports:
            print(f"[Financial]type={type},code={code},report={report},startDate={startDate},endDate={endDate}:")
            result = XTickMarketApi.getFinancialData(type, code, report, startDate, endDate, token, "get")
            df = pd.DataFrame(json.loads(result))
            print(df)

    def demoForIndicatorApi(self):  # 金融指标Api数据,以macd指标作为demo
        print("#####################################")
        type: int = 1  # 沪深京A股Type=1,港股Type=3,ETF Type=20
        code: str = "000001"
        dividends = ["1", "2", "3"]  # 复权类型
        period: str = "1d"
        startDate: str = "2024-04-25"
        endDate: str = "2025-12-25"
        token: str = Config.TOKEN  # 登录XTick官网，获取token
        inReal: int = 2
        optInFastPeriod: str = 26
        ptInSlowPeriod: str = 12
        optInSignalPeriod: str = 9
        for dividend in dividends:
            print(f"[indicator.macd]type={type},code={code},period={period},startDate={startDate},endDate={endDate}:")
            result = XTickIndicatorApi.macd(type, code, period, dividend, startDate, endDate, token, inReal,
                                            optInFastPeriod, ptInSlowPeriod, optInSignalPeriod, "get")
            df = pd.DataFrame(json.loads(result))
            print(df)

    def allDemo(self):
        """
        所有API接口的Demo示例,会调用所有接口，因此调用API接口次数多，请按需调用
        """
        xTickClient.demoForQuantApi()  # 量化数据Api
        xTickClient.demoForWatchApi()  # 盯盘数据Api
        xTickClient.demoForWebSocketApi()  # WebSocket查询、取消操作Api
        xTickClient.demoForBaseApi()  # 基本数据Api
        xTickClient.demoForMarketApi()  # 市场行情数据Api
        xTickClient.demoForFinancialApi()  # 财务报表数据Api
        xTickClient.demoForIndicatorApi()  # 金融指标数据Api


if __name__ == "__main__":
    xTickClient = XTickWebSocketClient()
    token: str = Config.TOKEN  # 登录XTick官网，获取token
    result = XTickMarketApi.getKlineMarket(1, "000001", "1m", "1", "2025-12-11", "2025-12-11", token, "get")
    print(f"Received data: {result}")

    # xTickClient.allDemo() # 所有API接口的Demo示例,会调用所有接口，因此调用API接口次数多，请按需调用
