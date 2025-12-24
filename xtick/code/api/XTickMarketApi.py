from xtick.code.Config import Config
from xtick.code.util import XTickUtil

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
'''

def getFinancialData(type: int, code: str, report: str, startDate: str, endDate: str, token: str,
                     method: str = "get") -> str:
    """
     *获取A股上市公司财务数据
     *Balance - 资产负债表
     *Income - 利润表
     *CashFlow - 现金流量表
     *Capital - 股本表
     *Holdernum - 股东数
     *Top10holder - 十大股东
     *Top10flowholder - 十大流通股东
     *Pershareindex - 每股指标
    """
    url = Config.SERVER_URL + "/doc/financial"
    params = {"type": type, "code": code, "report": report, "startDate": startDate, "endDate": endDate,
              "token": token}
    return XTickUtil.request(url, method, params)


def getKlineMarket(type: int, code: str, period: str, fq: str, startDate: str, endDate: str, token: str,
                       method: str = "get") -> str:
    """
    * 获取市场行情数据数据，包括历史数据和当日盘中实时数据
     * - 1m - 1分钟线
     * - 5m - 5分钟线
     * - 15m - 15分钟线
     * - 30m - 30分钟线
     * - 1h - 1小时线
     * - 1d - 日线
     * - 1w - 周线
     * - 1mon - 月线
     * - 1q - 季度线
     * - 1hy - 半年线
     * - 1y - 年线
     """
    url = Config.SERVER_URL + "/doc/kline/market"
    params = {"type": type, "code": code, "period": period, "fq": fq, "startDate": startDate, "endDate": endDate,
              "token": token}
    return XTickUtil.request(url, method, params)


def getKlineMinute(type: int, code: str, fq: str, token: str, method: str = "get") -> str:
    """
    * 提供日内一分钟实时数据，包括盘前9:15-25内竞价阶段数据。
    """
    url = Config.SERVER_URL + "/doc/kline/minute"
    params = {"type": type, "code": code, "fq": fq, "token": token}
    return XTickUtil.request(url, method, params)
