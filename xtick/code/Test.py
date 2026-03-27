# 定时器实时预警

# 定时器实时预警

import datetime

import sys

import time

sys.path.append('H:\\app\\tdx\\PYPlugins\\user')

from tqcenter import tq

tq.initialize('定时器实时预警Handlebar效果.py')

# 获取A股全部股票（测试时限制数量）



def get_real_time_data(stock_code):
    """

    获取股票的实时行情数据

    根据通达信TQ接口文档，这里需要调用相应的数据获取函数

    """

    try:

        # 获取最近两天的数据，用于获取前一日收盘价

        market_data = tq.get_market_data(

            field_list="",

            stock_list=[stock_code],

            count=2,  # 获取2天数据，用于获取前一日收盘价

            period='1d',

            dividend_type='none',

            fill_data=True

        )

        print(market_data)

    except Exception as e:

        print(f"获取{stock_code}实时数据失败: {e}")

    return '0.00', '0.00', '0'


if __name__ == "__main__":
    print("开始执行定时器实时预警")
    all_stocks = tq.get_stock_list(market='103')
    print(all_stocks)
    for stock in all_stocks[:10]:
        get_real_time_data(stock)
