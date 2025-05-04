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


if __name__ == "__main__":
    auth_codes = ["tick.SZ", "tick.SH", "tick.BJ", "tick.HK"]
    user_info = json.dumps({
        "token": "",#登录XTick官网，获取token
        "authCodes": auth_codes
    })
    user_encoded = urllib.parse.quote(user_info)
    endpoint_uri = f"ws://ws.xtick.top/ws/{user_encoded}"
    xTickClient = XTickWebSocketClient(endpoint_uri)
    xTickClient.start()
