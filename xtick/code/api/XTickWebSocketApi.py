from xtick.code.Config import Config
from xtick.code.util import XTickUtil

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
'''


def querysubscribe(token: str, method: str = "get") -> str:
    """
     * 查询已订阅服务
    """
    url = Config.SERVER_URL + "/doc/querysubscribe"
    params = {"token": token}
    return XTickUtil.request(url, method, params)


def unsubscribe(token: str, method: str = "get") -> str:
    """
     * 取消已订阅服务
    """
    url = Config.SERVER_URL + "/doc/unsubscribe"
    params = {"token": token}
    return XTickUtil.request(url, method, params)
