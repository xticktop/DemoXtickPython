from xtick.code.Config import Config
from xtick.code.util import XTickUtil
import json

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
# 盯盘数据接口 - 竞价、Tick、龙虎榜等
'''


def getLonghubangHistory(tradeDate: str, token: str = "", method: str = "get") -> str:
    """
    龙虎榜-历史数据
    龙虎榜详情历史数据，盘后更新数据。
    
    :param tradeDate: 交易日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/order/longhubang"
    params = {"tradeDate": tradeDate, "token": token}
    return XTickUtil.request(url, method, params)


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


def getFiveLevelRealtime(type: int, code: str, token: str = "", method: str = "get") -> str:
    """
    买卖五档-实时数据
    获取盘中买卖五档盘口实时数据，Tick实时数据。支持批量参数，支持ALL参数。
    
    :param type: 标的类型
        - 1-沪深京A股, 2-沪深指数, 3-港股, 4-ETF基金, 5-沪深可转债
    :param code: 股票代码。支持单个、批量(最多50个)、all全市场
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/order/five"
    params = {"type": type, "code": code, "token": token}
    return XTickUtil.request(url, method, params)


def getFiveLevelHistory(type: int, code: str, tradeDate: str, token: str = "", method: str = "get") -> str:
    """
    买卖五档-历史数据
    获取盘中买卖五档历史数据，盘后更新数据。
    
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


def getMarketFactor(type: int, code: str, token: str = "", method: str = "get") -> str:
    """
    实时行情指标
    沪深京A股实时行情指标，2分钟左右更新一次数据。
    
    :param type: 标的类型，1-沪深京A股
    :param code: 股票代码。支持单个、批量(最多50个)、all全市场
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/order/factor"
    params = {"type": type, "code": code, "token": token}
    return XTickUtil.request(url, method, params)
