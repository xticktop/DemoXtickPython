from xtick.code.Config import Config
from xtick.code.util import XTickUtil

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
'''


def getTickTime(type: int, code: str, period: str, token: str, method: str = "get") -> str:
    """
    * 获取沪深京股票交易日盘中实时行情数据，包括tick数据、1分钟数据、日线数据。
    """
    url = Config.SERVER_URL + "/doc/tick/time"
    params = {"type": type, "code": code, "period": period, "token": token}
    return XTickUtil.request(url, method, params)


def getTickHistory(type: int, code: str, tradeDate: str, token: str, method: str = "get") -> str:
    """
    * 获取沪深京股票历史Tick数据
    """
    url = Config.SERVER_URL + "/doc/tick/history"
    params = {"type": type, "code": code, "tradeDate": tradeDate, "token": token}
    return XTickUtil.request(url, method, params)


def getBidDetail(type: int, code: str, tradeDate: str, token: str, method: str = "get") -> str:
    """
    * 开盘竞价阶段，个股的所有竞价信息。当天竞价完成后，9:25更新完数据。
    """
    url = Config.SERVER_URL + "/doc/bid/detail"
    params = {"type": type, "code": code, "tradeDate": tradeDate, "token": token}
    return XTickUtil.request(url, method, params)


def getBidHistory(type: int, code: str, startDate: str, endDate: str, token: str, method: str = "get") -> str:
    """
    * 获取沪深京股票的历史竞价数据
    """
    url = Config.SERVER_URL + "/doc/bid/history"
    params = {"type": type, "code": code, "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getBidTime(type: int, code: str, token: str, method: str = "get") -> str:
    """
    * 获取沪深京股票交易日盘中实时竞价数据，竞价时间段：9:15-9:25。每次调用接口返回最新竞价数据。
    """
    url = Config.SERVER_URL + "/doc/bid/time"
    params = {"type": type, "code": code, "token": token}
    return XTickUtil.request(url, method, params)


def getBidTimeWithOption(type: int, code: str, option: {}, token: str, method: str = "get") -> str:
    """
    * 获取沪深京股票交易日盘中实时竞价数据，竞价时间段：9:15-9:25。每次调用接口返回最新竞价数据。可以根据option参数过滤排序
    """
    url = Config.SERVER_URL + "/doc/bid/time"
    params = {"type": type, "code": code, "option": option, "token": token}
    return XTickUtil.request(url, method, params)
