from xtick.code.Config import Config
from xtick.code.util import XTickUtil

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
'''

def getHotMoney(type: int, code: str, startDate: str, endDate: str, token: str, method: str = "get") -> str:
    """
    获取沪深京股票交易日盘中资金流数据。盘中实时更新。
    资金区分标准如下：
    特大单：成交金额大于或等于100万元或成交量大于或等于5000手
    大单：成交金额大于或等于20万元或成交量大于或等于1000手
    中单：成交金额大于或等于4万元或成交量大于或等于200手
    小单：其它为小单
    """
    url = Config.SERVER_URL + "/doc/hot/money"
    params = {"type": type, "code": code, "startDate": startDate, "endDate": endDate, "token": token}
    return XTickUtil.request(url, method, params)


def getHotBoard(type: int, flag: int, tradeDate: str, token: str, method: str = "get") -> str:
    """
     * 获取沪深京股票交易日盘中盘中涨停、跌停、炸板数据。盘中实时更新。
     * flag ，枚举取值如下：
     * - 1 - 涨停
     * - 2 - 跌停
     * - 3 - 炸板
    """
    url = Config.SERVER_URL + "/doc/hot/board"
    params = {"type": type, "flag": flag, "tradeDate": tradeDate, "token": token}
    return XTickUtil.request(url, method, params)


def getHotNews(minutes: int, tradeDate: str, token: str, method: str = "get") -> str:
    """
     * 获取财联社、同花顺、东方财富等主流金融平台资讯信息，跟随市场热点、核心。盘中实时更新。
     * 参数1：minutes 最新消息时间范围，表示获取几分钟内的最新消息。
     * 注意：
     * minutes取值大于0，按按照minutes参数，获取minutes时间内的最新消息。
     * minutes取值为0，按按照tradeDate参数，获取历史数据。
     * 参数2：tradeDate 时间范围，若需要获取历史数据，则需要将minutes设置为0。
    """
    url = Config.SERVER_URL + "/doc/hot/news"
    params = {"minutes": minutes, "tradeDate": tradeDate,  "token": token}
    return XTickUtil.request(url, method, params)


def getHotTimekline(type: int, code: str, token: str,
                    method: str = "get") -> str:
    """
     * 获取股票盘中日内分时数据，保留了价格在每个时间点的变化细节，股价全天的波动轨迹。盘中实时更新。
     """
    url = Config.SERVER_URL + "/doc/hot/timekline"
    params = {"type": type, "code": code, "token": token}
    return XTickUtil.request(url, method, params)


def getHotBk(symbol: str, token: str, method: str = "get") -> str:
    """
    * 获取概念板块、地域板块、行业板块数据，以及概念板块下对应的成分股数据。
     * symbol 用于表示要获取的概念板块的分类，枚举取值如下：
     * - sw1 - 申万一级行业划分
     * - sw2 - 申万二级行业划分
     * - sw3 - 申万三级行业划分
     * - zjh1 -  证监会一级行业划分
     * - zjh2 -  证监会二级行业划分
     * - ahy - A平台行业划分
     * - afg - A平台风格划分
     * - agn - A平台概念划分
     * - bgn - B平台概念划分
     * - bdy1 - B平台一级地域划分
     * - bdy1 - B平台二级地域划分
     * - cgn -  C平台概念划分
     """
    url = Config.SERVER_URL + "/doc/hot/bk"
    params = {"symbol": symbol, "token": token}
    return XTickUtil.request(url, method, params)


def getHotGainian(code: str, token: str, method: str = "get") -> str:
    """
     * 获取个股关联的概念板块、地域板块、行业板块数据。
     """
    url = Config.SERVER_URL + "/doc/hot/gainian"
    params = {"code": code, "token": token}
    return XTickUtil.request(url, method, params)
