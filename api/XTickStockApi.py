import requests

from xtick.code.Config import Config
from xtick.code.util import XTickUtil

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
'''


def getFinancialData(type: int, code: str, report: str, startDate: str, endDate: str, token: str,
                     method: str = "post") -> str:
    url = Config.SERVER_URL + "/doc/financial"
    params = {"type": type, "code": code, "report": report, "startDate": startDate, "endDate": endDate,
              "token": token}
    if method == 'post':
        response = requests.post(url, params=params)
        return XTickUtil.process_data(response.content)
    else:
        response = requests.get(url, params=params)
        return XTickUtil.process_data(response.content)


def getMarketData(type: int, code: str, period: str, fq: str, startDate: str, endDate: str, token: str,
                  method: str = "post") -> str:
    url = Config.SERVER_URL + "/doc/market"
    params = {"type": type, "code": code, "period": period, "fq": fq, "startDate": startDate, "endDate": endDate,
              "token": token}
    if method == 'post':
        response = requests.post(url, params=params)
        return XTickUtil.process_data(response.content)
    else:
        response = requests.get(url, params=params)
        return XTickUtil.process_data(response.content)
