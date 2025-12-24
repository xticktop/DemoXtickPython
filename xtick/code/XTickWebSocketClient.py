import json
import urllib

import websocket  # pip install websocket-client

from xtick.code.util import XTickUtil

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
'''


class XTickWebSocketClient(object):

    def __init__(self, url):
        self.url = url  # Enter your websocket URL here
        self.ws = None

    def on_open(self, ws):
        """
        Callback object which is called at opening websocket.
        1 argument:
        @ ws: the WebSocketApp object
        """
        print('A new WebSocketApp is opened and subscribed!')

    def on_data(self, ws, string, type, continue_flag):
        """
        4 arguments.
        The 1st argument is this class object.
        The 2nd argument is utf-8 string which we get from the server.
        The 3rd argument is data type. ABNF.OPCODE_TEXT or ABNF.OPCODE_BINARY will be came.
        The 4th argument is continue flag. If 0, the data continue
        """
        if type == websocket.ABNF.OPCODE_BINARY:
            packet = XTickUtil.process_data(string)
            print(f"Received data: {packet}")
        elif type == websocket.ABNF.OPCODE_TEXT:
            # 处理文本数据
            print(f"Received data: {string}")


    def on_error(self, ws, error):
        """
        Callback object which is called when got an error.
        2 arguments:
        @ ws: the WebSocketApp object
        @ error: exception object
        """
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        """
        Callback object which is called when the connection is closed.
        2 arguments:
        @ ws: the WebSocketApp object
        @ close_status_code
        @ close_msg
        """
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()

    # authCodes参数解释
    # 订阅类别 period.market.type  tick.SH.1
    # period代表周期，可取枚举值如下：tick time   代表tick数据和K线数据
    # market代表市场，可取枚举值如下：SZ SH BJ HK 代表深交所、上交所、北交所、港交所
    # type代表数据类型，可取枚举值如下：1 3 10 20  代表沪深京A股type=1，港股type=3，沪深指数type=10，沪深ETF type=20;
    #
    # 最后，总结，大家关注以下枚举值即可
    # 订阅tick数据可取枚举值如下：
    # - 000001.SZ - 订阅股票tick数据，按个数订阅。
    # - bid.1 - 订阅沪深京A股集合竞价期间竞价数据。
    # - quant.1 - 订阅沪深京A股量化因子数据，数据字段参考《3.7 量化指标接口》。
    # - tick.SZ.1 - 订阅深交所A股的tick数据。
    # - tick.SZ.10 - 订阅深交所指数的tick数据。
    # - tick.SZ.20 - 订阅深交所ETF的tick数据。
    # - tick.SH.1 - 订阅上交所A股的tick数据。
    # - tick.SH.10 - 订阅上交所指数的tick数据。
    # - tick.SH.20 - 订阅上交所ETF的tick数据。
    # - tick.BJ.1 - 订阅北交所ETF的tick数据。
    # - tick.HK.3 - 订阅港交所ETF的tick数据。
    # - minute.SZ.1 - 订阅深交所A股的1分钟k线数据，推送频率为实时。
    # - minute.SZ.10 - 订阅深交所指数的1分钟k线数据，推送频率为实时。
    # - minute.SZ.20 - 订阅深交所ETF的1分钟k线数据，推送频率为实时。
    # - minute.SH.1 - 订阅上交所A股的1分钟k线数据，推送频率为实时。
    # - minute.SH.10 - 订阅上交所指数的1分钟k线数据，推送频率为实时。
    # - minute.SH.20 - 订阅上交所ETF的1分钟k线数据，推送频率为实时。
    # - minute.BJ.1 - 订阅北交所A股的1分钟k线数据，推送频率为实时。
    # - minute.HK.3 - 订阅港交所港股的1分钟k线数据，推送频率为实时。
    # - time.SZ.1 - 订阅深交所A股的1分钟k线数据，推送频率为一分钟。
    # - time.SH.1 - 订阅上交所A股的1分钟k线数据，推送频率为一分钟。
    # - time.BJ.1 - 订阅北交所A股的1分钟k线数据，推送频率为一分钟。
    # - time.HK.3 - 订阅港交所港股的1分钟k线数据，推送频率为一分钟。
if __name__ == "__main__":
    #auth_codes = ["000001.SZ", "600000.SH", "00001.HK", "920001.BJ", "000001.SH","510300.SH"]
    #auth_codes = ["bid.1","tick.SZ.1", "tick.SZ.10", "tick.SZ.20", "time.SZ.1", "tick.SH.1","tick.SH.10", "tick.SH.20", "time.SH.1", "tick.BJ.1", "time.BJ.1","tick.HK.3", "time.HK.3"]
    auth_codes = ["tick.SZ.1", "minute.SZ.1", "time.SZ.1", "tick.HK.3"]  # 新用户，可以订阅北交所的tick行情数据

    user_info = json.dumps({
        "token": "8db5dff854625724840c9b02ca48d601",  # 登录XTick官网，获取token
        "authCodes": auth_codes
    })
    user_encoded = urllib.parse.quote(user_info)
    endpoint_uri = f"ws://ws.xtick.top/ws/{user_encoded}"
    xTickClient = XTickWebSocketClient(endpoint_uri)
    xTickClient.start()
