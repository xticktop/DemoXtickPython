from xtick.scripts.Config import Config
from xtick.scripts.util import XTickUtil
import json

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
# 盯盘数据接口 - 深度行情、日K线、分钟K线、成交统计、日K线复权等
'''


def getDayKlineRealtime(type: int, code: str, token: str = "", method: str = "get") -> str:
    """
    日K线-实时数据
    获取盘中实时日K线数据。支持批量参数，支持ALL参数。
    
    :param type: 标的类型
        - 1-沪深京A股, 2-沪深指数, 3-港股, 4-ETF基金, 5-沪深可转债
    :param code: 股票代码。支持单个、批量(最多50个)、all全市场
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/order/day"
    params = {"type": type, "code": code, "token": token}
    return XTickUtil.request(url, method, params)


def getMinuteKlineRealtime(type: int, code: str, token: str = "", method: str = "get") -> str:
    """
    分钟K线-实时数据
    获取盘中分钟K线实时数据。支持批量参数，支持ALL参数。
    
    :param type: 标的类型
        - 1-沪深京A股, 2-沪深指数, 3-港股, 4-ETF基金, 5-沪深可转债
    :param code: 股票代码。支持单个、批量(最多50个)、all全市场
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/order/minute"
    params = {"type": type, "code": code, "token": token}
    return XTickUtil.request(url, method, params)


def getDeepRealtime(type: int, code: str, token: str = "", method: str = "get") -> str:
    """
    深度行情-实时数据
    获取盘中深度行情实时数据。支持批量参数，不支持ALL参数。
    
    :param type: 标的类型
        - 1-沪深京A股, 2-沪深指数, 3-港股, 4-ETF基金, 5-沪深可转债
    :param code: 股票代码。支持单个、批量(最多50个)。注意：不支持all参数
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/order/deep"
    params = {"type": type, "code": code, "token": token}
    return XTickUtil.request(url, method, params)


def getDeepHistory(type: int, code: str, tradeDate: str, token: str = "", method: str = "get") -> str:
    """
    深度行情-历史数据
    获取盘中深度行情历史数据，盘后更新数据。
    该接口为历史数据接口，盘中交易时间段不能调用接口下载历史数据，其它时间段无限制。建议中午11:30-13:00时间段下载。
    
    :param type: 标的类型
        - 1-沪深京A股, 2-沪深指数, 3-港股, 4-ETF基金, 5-沪深可转债
    :param code: 股票代码，仅支持单个股票获取
    :param tradeDate: 交易日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/order/history"
    params = {"type": type, "code": code, "tradeDate": tradeDate, "token": token}
    return XTickUtil.request(url, method, params)


def getAmountStat(tradeDate: str, token: str = "", method: str = "get") -> str:
    """
    成交统计-实时接口
    按交易日，获取全市场成交额统计，包括科创板、创业板、北证、沪深两市等成交额统计。
    
    :param tradeDate: 交易日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/order/amount"
    params = {"tradeDate": tradeDate, "token": token}
    return XTickUtil.request(url, method, params)


def getFqKlineUpdate(type: int, fq: str, tradeDate: str, token: str = "", method: str = "get") -> str:
    """
    日K线复权-更新接口
    盘后获取当天全市场股票日线数据，包括前复权、不复权、后复权三种方式。
    仅支持近一周内的增量数据调用，主要是方便更新日K线。
    
    :param type: 标的类型
        - 1-沪深京A股, 2-沪深指数, 3-港股, 4-ETF基金, 5-沪深可转债
    :param fq: 复权类型
        - 1-不复权, 2-前复权, 3-后复权
    :param tradeDate: 交易日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/order/fqkline"
    params = {"type": type, "fq": fq, "tradeDate": tradeDate, "token": token}
    return XTickUtil.request(url, method, params)
