from xtick.code.api import XTickStockApi

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
'''


class XTickWebSocketClient(object):
    def demoForMarketData(self):
        type: int = 1  # 沪深京A股Type=1,港股Type=3,ETF Type=20
        code: str = "000001"
        startDate: str = "2025-04-25"
        endDate: str = "2025-05-25"
        token: str = ""  # 登录XTick官网，获取token
        historyKlinePeriods = ["1m", "5m", "15m", "30m", "1h", "2h", "1d", "1w", "1mon", "1q", "1hy", "1y"]  # K线周期
        dividends = ["1", "2", "3", "4", "5"]  # 复权类型
        for period in historyKlinePeriods:
            for fq in dividends:
                result = XTickStockApi.getMarketData(type, code, period, fq, startDate, endDate, token, "get")
                print(f"code={code},period={period},fq={fq},date={startDate}~{endDate},history data size={result}")

    def demoForFinancialData(self):
        type: int = 1  # 沪深京A股Type=1,港股Type=3,ETF Type=20
        code: str = "000001"
        startDate: str = "2024-04-25"
        endDate: str = "2025-05-25"
        token: str = ""  # 登录XTick官网，获取token

        reports = ["Pershareindex", "Balance", "CashFlow", "Capital", "Holdernum", "Top10holder",
                   "Top10flowholder"]  # 财务报表类型

        for report in reports:
            result = XTickStockApi.getFinancialData(type, code, report, startDate, endDate, token, "get")
            print(f"code={code},period={report},date={startDate}~{endDate}, data={result}")


if __name__ == "__main__":
    # stockApi = XTickStockApi()
    xTickClient = XTickWebSocketClient()
    # token: str = "8db5dff854625724840c9b02ca48d601"  # 登录XTick官网，获取token
    # result = stockApi.getMarketData(1, "000001", "1m", "1", "2025-12-11", "2025-12-11", token, "get")
    # print(f"Received data: {result}")
    xTickClient.demoForFinancialData()
    xTickClient.demoForMarketData()
