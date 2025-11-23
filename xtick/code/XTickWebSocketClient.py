import io
import json
import urllib
import zipfile

import websocket  # pip install websocket-client

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
        print('A new WebSocketApp is opened!')

        print("depth quote are subscribed!")

    def on_data(self, ws, string, type, continue_flag):
        """
        4 arguments.
        The 1st argument is this class object.
        The 2nd argument is utf-8 string which we get from the server.
        The 3rd argument is data type. ABNF.OPCODE_TEXT or ABNF.OPCODE_BINARY will be came.
        The 4th argument is continue flag. If 0, the data continue
        """

    def on_message(self, ws, message):
        """
        Callback object which is called when received data.
        2 arguments:
        @ ws: the WebSocketApp object
        @ message: utf-8 data received from the server
        """
        packet = self.create_packet(message)
        print(f"Received message: {packet}")

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

    def create_packet(self, data):
        try:
            with zipfile.ZipFile(io.BytesIO(data), 'r') as zip_ref:
                for entry in zip_ref.namelist():
                    if entry == "data.json":
                        with zip_ref.open(entry) as file:
                            content = file.read().decode('utf-8')
                            packet = json.loads(content)
                            return packet
        except Exception as e:
            print(f"Failed to parse data: {e}")
        return None

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
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
     # 深交所：tick.SZ.1  tick.SZ.10  tick.SZ.20
     # 上交所：tick.SH.1  tick.SH.10  tick.SH.20
     # 北交所：tick.BJ.1
     # 港交所：tick.HK.3
     #
     # 订阅time数据可取枚举值如下：
     # 深交所：time.SZ.1  time.SZ.10  time.SZ.20
     # 上交所：time.SH.1  time.SH.10  time.SH.20
     # 北交所：time.BJ.1
     # 港交所：time.HK.3
     # - bid.1 - 订阅沪深京集合竞价数据。
     # - tick.SZ.1 - 订阅深交所A股的tick数据。
     # - tick.SZ.10 - 订阅深交所指数的tick数据。
     # - tick.SZ.20 - 订阅深交所ETF的tick数据。
     # - tick.SH.1 - 订阅上交所A股的tick数据。
     # - tick.SH.10 - 订阅上交所指数的tick数据。
     # - tick.SH.20 - 订阅上交所ETF的tick数据。
     # - tick.BJ.1 - 订阅北交所ETF的tick数据。
     # - tick.HK.3 - 订阅港交所ETF的tick数据。
     # - time.SZ.1 - 订阅深交所A股的k线数据，包括1m。
     # - time.SH.1 - 订阅上交所A股的k线数据，包括1m。
     # - time.BJ.1 - 订阅北交所A股的k线数据，包括1m。
     # - time.HK.3 - 订阅港交所港股的k线数据，包括1m。
if __name__ == "__main__":
    #auth_codes = ["000001.SZ", "600000.SH", "00001.HK", "920001.BJ", "000001.SH","510300.SH"]
    #auth_codes = ["bid.1","tick.SZ.1", "tick.SZ.10", "tick.SZ.20", "time.SZ.1", "tick.SH.1","tick.SH.10", "tick.SH.20", "time.SH.1", "tick.BJ.1", "time.BJ.1","tick.HK.3", "time.HK.3"]
    auth_codes = ["tick.BJ.1"] #新用户，可以订阅北交所的tick行情数据

    user_info = json.dumps({
        "token": "",#登录XTick官网，获取token
        "authCodes": auth_codes
    })
    user_encoded = urllib.parse.quote(user_info)
    endpoint_uri = f"ws://ws.xtick.top/ws/{user_encoded}"
    xTickClient = XTickWebSocketClient(endpoint_uri)
    xTickClient.start()
