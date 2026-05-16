from xtick.code.Config import Config
from xtick.code.util import XTickUtil

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
# 行情数据接口 - K线、分钟数据等
'''


def getStockInfo(symbol: str = "all", token: str = "", method: str = "get") -> str:
    """
    股票列表接口
    按照股票池获取股票代码，包括沪深京A股、港股、沪深指数、ETF、可转债几类数据。

    :param symbol: 股票分类
        - all-全部股票, sz-深交所股票, sh-上交所股票, bj-北交所股票
        - hk-港交所股票, index-指数, bond-可转债
        - cyb-创业板股票, kcb-科创板股票, etf-全部ETF
        - st-st股票, ts-退市股票
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/stockinfo"
    params = {"symbol": symbol, "token": token}
    return XTickUtil.request(url, method, params)


def getCalendar(code: str, startDate: str, endDate: str, token: str = "", method: str = "get") -> str:
    """
    交易日历接口
    获取A股交易日历，包含交易所交易日历和个股交易日历。数据从2020年开始。

    :param code: 股票代码。code=ssb表示交易所交易日历；code=all且日期相同表示全市场
    :param startDate: 开始日期，格式：2026-05-15
    :param endDate: 结束日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/calendar"
    params = {"code": code, "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getHolderNum(code: str, startDate: str, endDate: str, token: str = "", method: str = "get") -> str:
    """
    股东数接口 - 数据范围：2001年-至今

    :param code: 股票代码，仅支持单个股票获取
    :param startDate: 开始日期，格式：2026-05-15
    :param endDate: 结束日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/holdernum"
    params = {"code": code, "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getCoreIndicator(code: str, startDate: str, endDate: str, token: str = "", method: str = "get") -> str:
    """
    财务指标接口 - 数据范围：2007年-至今

    :param code: 股票代码，仅支持单个股票获取
    :param startDate: 开始日期，格式：2026-05-15
    :param endDate: 结束日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/core"
    params = {"code": code, "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getTopHolder(code: str, startDate: str, endDate: str, token: str = "", method: str = "get") -> str:
    """
    十大股东接口 - 数据范围：公司上市-至今

    :param code: 股票代码，仅支持单个股票获取
    :param startDate: 开始日期，格式：2026-05-15
    :param endDate: 结束日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/topholder"
    params = {"code": code, "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getTopFlowHolder(code: str, startDate: str, endDate: str, token: str = "", method: str = "get") -> str:
    """
    十大流通股东接口 - 数据范围：2004年-至今

    :param code: 股票代码，仅支持单个股票获取
    :param startDate: 开始日期，格式：2026-05-15
    :param endDate: 结束日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/topflowholder"
    params = {"code": code, "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getKlineMarket(type: int, code: str, fq: int, period: str, startDate: str, endDate: str, 
                   token: str = "", method: str = "get") -> str:
    """
    行情数据-通用接口
    行情数据包括1分钟K线、5分钟K线、15分钟K线、30分钟K线、1小时K线、日K线、周K线、季度K线、年K线。
    支持复权数据获取，K线数据盘中实时更新。
    
    :param type: 标的类型
        - 1-沪深京A股, 2-沪深指数, 3-港股, 4-ETF基金, 5-沪深可转债
    :param code: 股票代码，仅支持单个股票获取
    :param fq: 复权类型
        - 1-不复权, 2-前复权, 3-后复权, 4-等比前复权, 5-等比后复权
    :param period: K线周期
        - 1m-1分钟线, 5m-5分钟线, 15m-15分钟线, 30m-30分钟线, 1h-1小时线
        - 1d-日线, 1w-周线, 1mon-月线, 1q-季度线, 1y-年线
    :param startDate: 开始日期，格式：2026-05-15
    :param endDate: 结束日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/kline/market"
    params = {"type": type, "code": code, "fq": fq, "period": period, 
              "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getKlineMinute(type: int, code: str, fq: int, token: str = "", method: str = "get") -> str:
    """
    分钟数据-实时接口
    提供日内一分钟实时数据，这个分钟接口调取数据会更快。
    
    :param type: 标的类型
        - 1-沪深京A股, 2-沪深指数, 3-港股, 4-ETF基金, 5-沪深可转债
    :param code: 股票代码，仅支持单个股票获取
    :param fq: 复权类型
        - 1-不复权, 2-前复权, 3-后复权, 4-等比前复权, 5-等比后复权
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/kline/minute"
    params = {"type": type, "code": code, "fq": fq, "token": token}
    return XTickUtil.request(url, method, params)
