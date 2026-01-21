from xtick.code.Config import Config
from xtick.code.util import XTickUtil

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
'''


def getQunatData(type: int, field: str, token: str, method: str = "get") -> str:
    """
     * 量化指标-实时接口，行情数据全推
     * 获取沪深京股票交易日盘中实时指标数据，包括涨速、换手率、市盈率、市净率等。
    """
    url = Config.SERVER_URL + "/doc/quant/data"
    params = {"type": type, "field": field, "token": token}
    return XTickUtil.request(url, method, params)

def getQunatTime(type: int, field: str, token: str, method: str = "get") -> str:
    """
        * 量化指标-实时接口 ，行情数据全推
        * 获取沪深京股票交易日盘中实时指标数据，包括涨速、换手率、市盈率、市净率等。
    """
    url = Config.SERVER_URL + "/doc/quant/time"
    params = {"type": type, "field": field, "token": token}
    return XTickUtil.request(url, method, params)
