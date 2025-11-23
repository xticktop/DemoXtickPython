import io
import json
import requests
import zipfile

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
'''


class XTickWebSocketClient(object):
    def getFinancialData(self, type: int, code: str, report: str, startDate: str, endDate: str, token: str,
                         method: str = "post") -> str:
        url = "http://api.xtick.top/doc/financial"
        params = {"type": type, "code": code, "report": report, "startDate": startDate,
                  "endDate": endDate, "token": token}
        if method == 'post':
            response = requests.post(url, params=params)
            return self.create_packet(response.content)
        else:
            response = requests.get(url, params=params)
            return self.create_packet(response.content)

    def getMarketData(self, type: int, code: str, period: str, fq: str, startDate: str, endDate: str, token: str,
                      method: str = "post") -> str:
        url = "http://api.xtick.top/doc/market"
        params = {"type": type, "code": code, "period": period, "fq": fq, "startDate": startDate, "endDate": endDate,
                  "token": token}
        if method == 'post':
            response = requests.post(url, params=params)
            return self.create_packet(response.content)
        else:
            response = requests.get(url, params=params)
            return self.create_packet(response.content)

    def create_packet(self, data):
        try:
            with zipfile.ZipFile(io.BytesIO(data), 'r') as zip_ref:
                for entry in zip_ref.namelist():
                    if entry.endswith(".json"):
                        with zip_ref.open(entry) as file:
                            content = file.read().decode('utf-8')
                            packet = json.loads(content)
                            return packet
        except Exception as e:
            print(f"Failed to parse data: {e}")
        return None

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
                result = self.getMarketData(type, code, period, fq, startDate, endDate, token, "get")
                print(f"code={code},period={period},fq={fq},date={startDate}~{endDate},history data size={len(result)}")

    def demoForFinancialData(self):
        type: int = 1  # 沪深京A股Type=1,港股Type=3,ETF Type=20
        code: str = "000001"
        startDate: str = "2024-04-25"
        endDate: str = "2025-05-25"
        token: str = ""  # 登录XTick官网，获取token

        reports = ["Pershareindex", "Balance", "CashFlow", "Capital", "Holdernum", "Top10holder",
                   "Top10flowholder"]  # 财务报表类型

        for report in reports:
            result = self.getFinancialData(type, code, report, startDate, endDate, token, "get")
            print(f"code={code},period={report},date={startDate}~{endDate},history data size={len(result)}")


if __name__ == "__main__":
    xTickClient = XTickWebSocketClient()
    token: str = ""  # 登录XTick官网，获取token
    result = xTickClient.getMarketData(1, "000001", "1m", "1", "2025-04-25", "2025-05-25", token, "get")
    print(result)
    # xTickClient.demoForFinancialData()
    # xTickClient.demoForMarketData()
