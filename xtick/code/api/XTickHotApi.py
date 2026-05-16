from xtick.code.Config import Config
from xtick.code.util import XTickUtil

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
# 短线热点接口 - 连板、情绪、资金流向、新闻等
'''


def getLianbanTianti(type: int, flag: int, tradeDate: str, token: str = "", method: str = "get") -> str:
    """
    连板天梯-实时接口
    获取沪深京股票交易日盘中盘中涨停板、跌停板、炸板数据。梯队完整度是超短的重要指标。
    
    :param type: 标的类型 - 1-沪深京A股, 4-ETF基金
    :param flag: 上榜类型 - 1-涨停板, 2-跌停板, 3-炸板
    :param tradeDate: 交易日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/hot/board"
    params = {"type": type, "flag": flag, "tradeDate": tradeDate, "token": token}
    return XTickUtil.request(url, method, params)


def getMarketEmotion(type: int, tradeDate: str, token: str = "", method: str = "get") -> str:
    """
    市场情绪-实时接口
    市场情绪，短线选手复盘必备工具。
    
    :param type: 标的类型 - 1-沪深京A股, 4-ETF基金
    :param tradeDate: 交易日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/hot/emotion"
    params = {"type": type, "tradeDate": tradeDate, "token": token}
    return XTickUtil.request(url, method, params)


def getMoneyFlow(type: int, code: str, startDate: str, endDate: str, token: str = "", method: str = "get") -> str:
    """
    资金流向-实时接口
    获取沪深京股票交易日盘中资金流数据。盘中实时更新。
    
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
    url = Config.SERVER_URL + "/doc/hot/money"
    params = {"type": type, "code": code, "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getBidHistory(type: int, code: str, seq: int, startDate: str, endDate: str, token: str = "", method: str = "get") -> str:
    """
    竞价数据-历史接口
    竞价历史数据，该接口仅保留集合竞价期间的最后一条竞价数据和开盘数据。
    
    :param type: 标的类型，1-沪深京A股
    :param code: 股票代码。支持单个或all(需日期相同)
    :param seq: 序列号 - 0-集合竞价最后一条数据（9:25分）, 1-集合竞价倒数第二条数据
    :param startDate: 开始日期，格式：2026-05-15
    :param endDate: 结束日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/hot/bidhistory"
    params = {"type": type, "code": code, "seq": seq, "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getBidDetail(type: int, code: str, tradeDate: str, token: str = "", method: str = "get") -> str:
    """
    竞价详情-实时接口
    开盘集合竞价阶段，个股的所有竞价信息。当天竞价完成后，9:25更新完数据。
    
    :param type: 标的类型，1-沪深京A股
    :param code: 股票代码，仅支持单个股票获取
    :param tradeDate: 交易日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/hot/biddetail"
    params = {"type": type, "code": code, "tradeDate": tradeDate, "token": token}
    return XTickUtil.request(url, method, params)


def getNews(minutes: int, tradeDate: str, token: str = "", method: str = "get") -> str:
    """
    新闻资讯-实时接口
    获取财联社、新浪财经、格隆汇、华尔街见闻等主流金融平台资讯信息。
    
    :param minutes: 最新消息时间范围
        - minutes>0：获取minutes分钟内的最新消息
        - minutes=0：按tradeDate参数获取历史数据
    :param tradeDate: 交易日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/hot/news"
    params = {"minutes": minutes, "tradeDate": tradeDate, "token": token}
    return XTickUtil.request(url, method, params)


def getTimeKline(type: int, code: str, token: str = "", method: str = "get") -> str:
    """
    日内分时-实时接口
    获取股票盘中日内分时数据，保留了价格在每个时间点的变化细节，股价全天的波动轨迹。
    
    :param type: 标的类型
        - 1-沪深京A股, 2-沪深指数, 3-港股, 4-ETF基金, 5-沪深可转债
    :param code: 股票代码，仅支持单个股票获取
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/hot/timekline"
    params = {"type": type, "code": code, "token": token}
    return XTickUtil.request(url, method, params)


def getConceptStocks(symbol: str, token: str = "", method: str = "get") -> str:
    """
    概念板块成分股数据
    获取概念板块、地域板块、行业板块数据，以及概念板块下对应的成分股数据。
    
    :param symbol: 概念板块分类
        - sw1/sw2/sw3 - 申万一/二/三级行业划分
        - zjh1/zjh2 - 证监会一/二级行业划分
        - bdy1/bdy2 - 一/二级地域划分
        - ahy - 行业划分, afg - 风格划分
        - agn/bgn/cgn - A/B/C概念划分
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/hot/bk"
    params = {"symbol": symbol, "token": token}
    return XTickUtil.request(url, method, params)


def getStockConcepts(code: str, token: str = "", method: str = "get") -> str:
    """
    股票关联概念板块数据
    获取个股关联的概念板块、地域板块、行业板块数据。
    
    :param code: 股票代码，仅支持单个股票获取
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/hot/gainian"
    params = {"code": code, "token": token}
    return XTickUtil.request(url, method, params)


def getDayUpdate(dataType: str, symbol: str, tradeDate: str, token: str = "", method: str = "get") -> str:
    """
    增量更新
    提供交易日当天全市场增量数据的更新，是收盘后的历史数据。
    注意：这个接口单次获取数据量非常大，请不要频繁获取，该接口严格限流。
    
    :param dataType: 数据类别
        - bid - 全市场竞价详情数据（预计9:26分可获取）
        - 1m - 全市场1分钟数据（收盘后获取）
    :param symbol: 股票分类
        - index - 主要指数, etf - 场内基金
        - cyb - 深交所创业板股票, kcb - 上交所科创板股票
        - bj - 北交所股票
        - szm - 深交所主板股票, shm - 上交所主板股票
    :param tradeDate: 交易日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/hot/dayupdate"
    params = {"dataType": dataType, "symbol": symbol, "tradeDate": tradeDate, "token": token}
    return XTickUtil.request(url, method, params)
