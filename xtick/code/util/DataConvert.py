import json

import pandas as pd

staticmethod


def toFile(file: str, data: str):
    """
    将请求返回的字符串数据写到文件中，包括Csv、Json、Txt文件
    :param file: 文件路径
    :param data: 字符串
    """
    with open(file, "w", encoding='utf-8') as file:
        file.write(data)


staticmethod


def toDataFrame(data: str) -> pd.DataFrame:
    """
    将请求返回的Json格式数据转换为DataFrame格式
    :param data: Json格式数据
    """
    return pd.DataFrame(json.loads(data))

if __name__ == '__main__':
    print("StockApiDemo")
