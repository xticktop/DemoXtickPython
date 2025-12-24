from xtick.code.Config import Config
from xtick.code.util import XTickUtil

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
'''
def getCalendar(code: str, startDate: str, endDate: str, token: str, method: str = "get") -> str:
    """
     * 获取A股历史交易，包含交易所交易日历和个股交易日历。
     * 交易所是指上交所、深交所、北交所的交易日历。
    """
    url = Config.SERVER_URL + "/doc/calendar"
    params = {"code": code, "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getStockInfo(symbol: str, token: str, method: str = "get") -> str:
    """
     * 获取市场所有股票代码
     * 获取市场所有股票代码
     * symbol 用于表示要获取的股票分类，枚举取值如下：
     * - all - 全部股票
     * - sz - 深交所股票
     * - sh - 上交所股票
     * - bj -  北交所股票
     * - hk - 港交所股票
     * - index- 指数
     * - cyb - 创业板股票
     * - kcb - 科创板股票
     * - etf - 全部ETF
     * - st- st股票
    """
    url = Config.SERVER_URL + "/doc/stockinfo"
    params = {"symbol": symbol, "token": token}
    return XTickUtil.request(url, method, params)
