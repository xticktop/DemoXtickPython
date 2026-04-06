from xtick.code.Config import Config
from xtick.code.util import XTickUtil

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
'''


def getCoreTime(type: int, code: str, field: str, token: str, method: str = "get") -> str:
    """
     * 核心指标-实时接口
     * 获取沪深京股票交易日盘中实时指标数据，包括涨速、换手率、市盈率、市净率等。
    """
    url = Config.SERVER_URL + "/doc/core/time"
    params = {"type": type, "code": code, "field": field, "token": token}
    return XTickUtil.request(url, method, params)


def getCoreChuQuan(type: int, code: str, startDate: str, endDate: str, token: str, method: str = "get") -> str:
    """
     * 股票除权除息历史数据，盘后更新。
     * 可以按单个股票获取个股除权除息历史记录，也可以使用all参数，获取全市场的股票除权除息数据。
    """
    url = Config.SERVER_URL + "/doc/core/chuquan"
    params = {"type": type, "code": code, "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getCoreTingpai(type: int, code: str, startDate: str, endDate: str, token: str, method: str = "get") -> str:
    """
     * 停牌股票历史数据，盘后更新。
     * 可以按单个股票获取个股停牌历史记录，也可以使用all参数，获取全市场股票的停牌数据。
    """
    url = Config.SERVER_URL + "/doc/core/tingpai"
    params = {"type": type, "code": code, "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getCoreST(type: int, code: str, startDate: str, endDate: str, token: str, method: str = "get") -> str:
    """
     * ST股票历史数据，数据从2022年3月开始，盘后更新。
     * 可以按单个股票获取个股ST历史记录，也可以使用all参数，获取全市场的ST股票数据。
    """
    url = Config.SERVER_URL + "/doc/core/st"
    params = {"type": type, "code": code, "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getCoreHistoryPrice(type: int, code: str, fq: int, startDate: str, endDate: str, token: str,
                        method: str = "get") -> str:
    """
     * 股票涨跌停历史数据，盘后更新。
     * 可以按单个股票获取个股涨跌停历史记录，也可以使用all参数，获取全市场股票的涨跌停数据。
    """
    url = Config.SERVER_URL + "/doc/core/price"
    params = {"type": type, "code": code, "fq": fq, "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getCoreFenbi(type: int, code: str, tradeDate: str, token: str, method: str = "get") -> str:
    """
    股票分时成交数据接口
    """
    url = Config.SERVER_URL + "/doc/core/fenbi"
    params = {"type": type, "tradeDate": tradeDate, "code": code, "token": token}
    return XTickUtil.request(url, method, params)


def getCoreFenjia(type: int, code: str, tradeDate: str, token: str, method: str = "get") -> str:
    """
     * 股票分价成交数据接口，盘后更新
    """
    url = Config.SERVER_URL + "/doc/core/fenjia"
    params = {"type": type, "tradeDate": tradeDate, "code": code, "token": token}
    return XTickUtil.request(url, method, params)

def getBidDetail(type: int, code: str, tradeDate: str, token: str, method: str = "get") -> str:
    """
    * 开盘竞价阶段，个股的所有竞价信息。当天竞价完成后，9:25更新完数据。
    """
    url = Config.SERVER_URL + "/doc/core/biddetail"
    params = {"type": type, "code": code, "tradeDate": tradeDate, "token": token}
    return XTickUtil.request(url, method, params)


def getDayUpdate(dataType: str, symbol: str, tradeDate: str, token: str, method: str = "get") -> str:
    """
     * 提供交易日当天全市场增量数据的更新。这个接口单次获取数据量大，请不要频繁获取，该接口严格限流。
     * dataType 数据类别，枚举类型如下：
     * - bid - 全市场竞价详情数据。不需要携带symbol参数，即可获取全市场竞价详情数据。9:26分可获取。
     * - 1m - 全市场1分钟数据，需要携带symbol参数，按照股票分类获取分钟数据。
    """
    url = Config.SERVER_URL + "/doc/core/dayupdate"
    params = {"dataType": dataType, "tradeDate": tradeDate, "symbol": symbol, "token": token}
    return XTickUtil.request(url, method, params)
