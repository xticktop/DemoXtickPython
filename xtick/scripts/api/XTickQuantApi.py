from xtick.scripts.Config import Config
from xtick.scripts.util import XTickUtil

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
# 量化因子接口 - 实时和历史量化因子数据
'''


def getQuantDataRealtime(type: int, field: str, token: str = "", method: str = "get") -> str:
    """
    量化因子-实时接口
    获取沪深京股票交易日盘中因子指标数据，实时推送，包括涨速、换手率、市盈率、市净率等。支持数据全推。
    
    :param type: 标的类型，1-沪深京A股
    :param field: 需要返回字段。返回全部字段填写all；多个字段之间用英文逗号分割，单次请求不超过10个字段。
                  常用字段：x001(昨收价), x002(最新价), x003(开盘价), x004(最高价), x005(最低价),
                  x006(成交量), x007(成交额), x008(涨跌), x009(振幅), x010(均价), x011(现均差),
                  x012(涨停价), x013(跌停价), x014(涨停板), x015(涨速), x016-x020(1-5分钟涨速),
                  x021(静态市盈率), x022(动态市盈率), x023(TTM市盈率), x024(总市值), x025(流通市值),
                  x026(市净率), x027(换手率), x028(实际换手率), x029(涨幅), x030-x032(5/10/20日涨幅),
                  x033-x038(5/10/20/30/60/120日均线), x039-x041(MACD-DIF/DEA/MACD),
                  x042-x044(KDJ-K/D/J), x045(RSI), x046(WR), x047(CCI)等
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/quant/data"
    params = {"type": type, "field": field, "token": token}
    return XTickUtil.request(url, method, params)


def getQuantDataHistory(tradeDate: str, token: str = "", method: str = "get") -> str:
    """
    量化因子-历史接口
    获取沪深京股票交易日盘中因子指标历史数据，盘后更新。
    
    :param tradeDate: 交易日期，格式：2026-05-15
    :param token: 登录网站获取token
    :param method: 请求方法，默认get
    :return: JSON字符串
    """
    if not token:
        token = Config.TOKEN
    url = Config.SERVER_URL + "/doc/quant/history"
    params = {"tradeDate": tradeDate, "token": token}
    return XTickUtil.request(url, method, params)
