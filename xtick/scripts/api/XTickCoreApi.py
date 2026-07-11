from xtick.scripts.Config import Config
from xtick.scripts.util import XTickUtil

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
# 核心数据接口 - 竞价、核心指标、除权、停牌、ST等
'''


def getCoreBidTime(type: int, code: str, token: str = "", method: str = "get") -> str:
    """
    竞价数据-实时接口
    获取沪深京股票交易日盘中实时竞价数据，竞价时间段：9:15-9:25。
    
    :param type: 标的类型，1-沪深京A股
    :param code: 股票代码。支持单个、批量(最多50个)、all全市场
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/core/bidtime"
    params = {"type": type, "code": code, "token": token}
    return XTickUtil.request(url, method, params)


def getCoreTime(type: int, code: str, field: str, token: str = "", method: str = "get") -> str:
    """
    核心指标-实时接口
    获取沪深京股票交易日盘中实时指标数据，包括涨速、换手率、市盈率、市净率等。
    
    :param type: 标的类型，1-沪深京A股
    :param code: 股票代码，仅支持单个股票获取
    :param field: 需要返回字段。多个字段之间用英文逗号分割，单次请求不超过10个字段
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/core/time"
    params = {"type": type, "code": code, "field": field, "token": token}
    return XTickUtil.request(url, method, params)


def getCoreChuQuan(type: int, code: str, startDate: str, endDate: str, token: str = "", method: str = "get") -> str:
    """
    除权变更数据
    股票除权除息历史数据，盘后更新。可以按单个股票获取个股除权除息历史记录，也可以使用all参数。
    
    :param type: 标的类型 - 1-沪深京A股, 4-ETF基金
    :param code: 股票代码。支持单个或all(需日期相同)
    :param startDate: 开始日期，格式：2026-05-15
    :param endDate: 结束日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/core/chuquan"
    params = {"type": type, "code": code, "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getCoreTingpai(type: int, code: str, startDate: str, endDate: str, token: str = "", method: str = "get") -> str:
    """
    停牌数据
    停牌股票历史数据，盘后更新。可以按单个股票获取个股停牌历史记录，也可以使用all参数。
    
    :param type: 标的类型 - 1-沪深京A股, 4-ETF基金
    :param code: 股票代码。支持单个或all(需日期相同)
    :param startDate: 开始日期，格式：2026-05-15
    :param endDate: 结束日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/core/tingpai"
    params = {"type": type, "code": code, "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getCoreST(type: int, code: str, startDate: str, endDate: str, token: str = "", method: str = "get") -> str:
    """
    ST数据
    ST股票历史数据，数据从2022年3月开始，盘后更新。可以按单个股票获取个股ST历史记录，也可以使用all参数。
    
    :param type: 标的类型 - 1-沪深京A股, 4-ETF基金
    :param code: 股票代码。支持单个或all(需日期相同)
    :param startDate: 开始日期，格式：2026-05-15
    :param endDate: 结束日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/core/st"
    params = {"type": type, "code": code, "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getCoreHistoryPrice(type: int, code: str, fq: int, startDate: str, endDate: str, token: str = "", method: str = "get") -> str:
    """
    涨停停价格
    股票涨跌停历史数据，盘后更新。可以按单个股票获取个股涨跌停历史记录，也可以使用all参数。
    
    :param type: 标的类型 - 1-沪深京A股, 4-ETF基金
    :param code: 股票代码。支持单个或all(需日期相同)
    :param fq: 复权类型 - 1-不复权, 2-前复权, 3-后复权
    :param startDate: 开始日期，格式：2026-05-15
    :param endDate: 结束日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/core/price"
    params = {"type": type, "code": code, "fq": fq, "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getCoreFenbi(type: int, code: str, tradeDate: str, token: str = "", method: str = "get") -> str:
    """
    分笔数据
    股票分时成交数据接口
    
    :param type: 标的类型，1-沪深京A股
    :param code: 股票代码，仅支持单个股票获取
    :param tradeDate: 交易日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/core/fenbi"
    params = {"type": type, "tradeDate": tradeDate, "code": code, "token": token}
    return XTickUtil.request(url, method, params)


def getCoreFenjia(type: int, code: str, tradeDate: str, token: str = "", method: str = "get") -> str:
    """
    分价数据
    股票分价成交数据接口，盘后更新
    
    :param type: 标的类型，1-沪深京A股
    :param code: 股票代码，仅支持单个股票获取
    :param tradeDate: 交易日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/core/fenjia"
    params = {"type": type, "tradeDate": tradeDate, "code": code, "token": token}
    return XTickUtil.request(url, method, params)
