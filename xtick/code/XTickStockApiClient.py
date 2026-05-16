import sys
import os
# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import json
from datetime import datetime, timedelta

import pandas as pd

from xtick.code.Config import Config
from xtick.code.api.XTickMarketApi import getStockInfo, getCalendar, getHolderNum, getCoreIndicator, getTopHolder, getTopFlowHolder, getKlineMinute, getKlineMarket
from xtick.code.api.XTickWatchApi import getLonghubangHistory, getDayKlineRealtime, getMinuteKlineRealtime, getFiveLevelRealtime, getFiveLevelHistory, getAmountStat, getMarketFactor
from xtick.code.api.XTickCoreApi import getCoreBidTime, getCoreTime, getCoreChuQuan, getCoreTingpai, getCoreST, getCoreHistoryPrice, getCoreFenbi, getCoreFenjia
from xtick.code.api.XTickHotApi import getLianbanTianti, getMarketEmotion, getMoneyFlow, getBidHistory, getBidDetail, getNews, getTimeKline, getConceptStocks, getStockConcepts, getDayUpdate
from xtick.code.api.XTickQuantApi import getQuantDataRealtime, getQuantDataHistory
from xtick.code.api.XTickIndicatorApi import macd
from xtick.code.api.XTickWebSocketApi import querysubscribe, unsubscribe

'''
# GitHub: https://github.com/xticktop/xtick
# Token Application: http://www.xtick.top/
# Api Document: https://ccn9lag3l54q.feishu.cn/wiki/ABenwEvDOiShYrkaLAJcFY5gnZf
# XTick股票数据API客户端 - 完整的接口调用示例
'''


class XTickStockApiClient(object):
    """XTick股票数据API客户端，提供所有接口的调用示例"""

    def __init__(self):
        self.token = Config.TOKEN

    def demoForMarketApi(self):
        """行情数据接口测试（XTickMarketApi）"""
        print("\n" + "="*80)
        print("【行情数据接口测试 - XTickMarketApi】")
        print("="*80)
        
        type_val = 1  # 沪深京A股
        code = "000001"
        last_month = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        today = datetime.now().strftime("%Y-%m-%d")

        # 1. 股票列表
        print("\n[1] 股票列表 - 获取指数列表:")
        result = getStockInfo(symbol="index", token=self.token)
        df = pd.DataFrame(json.loads(result))
        print(f"返回数据条数: {len(df)}")
        if len(df) > 0:
            print(df.head())

        # 2. 交易日历
        print("\n[2] 交易日历 - 获取个股交易日历:")
        result = getCalendar(code=code, startDate=last_month, endDate=today, token=self.token)
        df = pd.DataFrame(json.loads(result))
        print(f"返回数据条数: {len(df)}")
        if len(df) > 0:
            print(df.head())

        # 3. 股东数
        print("\n[3] 股东数 - 获取平安银行股东数:")
        result = getHolderNum(code=code, startDate="2023-01-01", endDate="2024-12-31", token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            print(df.head())

        # 4. 财务指标
        print("\n[4] 财务指标 - 获取平安银行财务指标:")
        result = getCoreIndicator(code=code, startDate="2023-01-01", endDate="2024-12-31", token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            print(df.head())

        # 5. 十大股东
        print("\n[5] 十大股东 - 获取平安银行十大股东:")
        result = getTopHolder(code=code, startDate="2023-01-01", endDate="2024-12-31", token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            print(df.head())

        # 6. 十大流通股东
        print("\n[6] 十大流通股东 - 获取平安银行十大流通股东:")
        result = getTopFlowHolder(code=code, startDate="2023-01-01", endDate="2024-12-31", token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            print(df.head())

        # 7. 分钟数据-实时
        print("\n[7] 分钟数据-实时 - 获取平安银行实时分钟数据:")
        result = getKlineMinute(type=type_val, code=code, fq=1, token=self.token)
        df = pd.DataFrame(json.loads(result))
        print(f"返回数据条数: {len(df)}")
        if len(df) > 0:
            print(df.tail())

        # 8. 行情数据-通用（日线）
        print("\n[8] 行情数据-通用 - 获取平安银行最近30天日线:")
        result = getKlineMarket(type=type_val, code=code, fq=1, period="1d", 
                               startDate=last_month, endDate=today, token=self.token)
        df = pd.DataFrame(json.loads(result))
        print(f"返回数据条数: {len(df)}")
        if len(df) > 0:
            print(df.head())

    def demoForWatchApi(self):
        """盯盘数据接口测试（XTickWatchApi）"""
        print("\n" + "="*80)
        print("【盯盘数据接口测试 - XTickWatchApi】")
        print("="*80)
        
        type_val = 1
        code = "000001"
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        # 1. 龙虎榜-历史
        print("\n[1] 龙虎榜-历史 - 获取昨日龙虎榜数据:")
        result = getLonghubangHistory(tradeDate=yesterday, token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df.head())

        # 2. 日K线-实时
        print("\n[2] 日K线-实时 - 获取平安银行实时日K线:")
        result = getDayKlineRealtime(type=type_val, code=code, token=self.token)
        df = pd.DataFrame(json.loads(result))
        print(f"返回数据条数: {len(df)}")
        if len(df) > 0:
            print(df)

        # 3. 分钟K线-实时
        print("\n[3] 分钟K线-实时 - 获取平安银行实时分钟K线:")
        result = getMinuteKlineRealtime(type=type_val, code=code, token=self.token)
        df = pd.DataFrame(json.loads(result))
        print(f"返回数据条数: {len(df)}")
        if len(df) > 0:
            print(df.tail())

        # 4. 买卖五档-实时
        print("\n[4] 买卖五档-实时 - 获取平安银行实时五档:")
        result = getFiveLevelRealtime(type=type_val, code=code, token=self.token)
        df = pd.DataFrame(json.loads(result))
        print(f"返回数据条数: {len(df)}")
        if len(df) > 0:
            print(df)

        # 5. 买卖五档-历史
        print("\n[5] 买卖五档-历史 - 获取平安银行昨日五档历史:")
        result = getFiveLevelHistory(type=type_val, code=code, tradeDate=yesterday, token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df.head())

        # 6. 成交统计
        print("\n[6] 成交统计 - 获取昨日全市场成交统计:")
        result = getAmountStat(tradeDate=yesterday, token=self.token)
        data = json.loads(result)
        print(f"成交统计数据: {data}")

    def demoForCoreApi(self):
        """核心数据接口测试（XTickCoreApi）"""
        print("\n" + "="*80)
        print("【核心数据接口测试 - XTickCoreApi】")
        print("="*80)
        
        type_val = 1
        code = "000001"
        last_month = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        today = datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        # 1. 竞价数据-实时
        print("\n[1] 竞价数据-实时 - 获取平安银行实时竞价:")
        result = getCoreBidTime(type=type_val, code=code, token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df)

        # 2. 核心指标-实时
        print("\n[2] 核心指标-实时 - 获取平安银行核心指标:")
        result = getCoreTime(type=type_val, code=code, field="x001,x002,x003,x004,x005", token=self.token)
        data = json.loads(result)
        print(f"核心指标数据: {data}")

        # 3. 除权变更
        print("\n[3] 除权变更 - 获取平安银行除权记录:")
        result = getCoreChuQuan(type=type_val, code=code, startDate="2020-01-01", endDate=today, token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df)

        # 4. 停牌数据
        print("\n[4] 停牌数据 - 获取平安银行停牌记录:")
        result = getCoreTingpai(type=type_val, code=code, startDate="2020-01-01", endDate=today, token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df)

        # 5. ST数据
        print("\n[5] ST数据 - 获取ST股票记录:")
        result = getCoreST(type=type_val, code="000004", startDate="2023-01-01", endDate=today, token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df)

        # 6. 涨跌停价格
        print("\n[6] 涨跌停价格 - 获取平安银行涨跌停记录:")
        result = getCoreHistoryPrice(type=type_val, code=code, fq=1, startDate=last_month, endDate=today, token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df.head())

        # 7. 分笔数据
        print("\n[7] 分笔数据 - 获取平安银行昨日分笔:")
        result = getCoreFenbi(type=type_val, code=code, tradeDate=yesterday, token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df.head())

        # 8. 分价数据
        print("\n[8] 分价数据 - 获取平安银行昨日分价:")
        result = getCoreFenjia(type=type_val, code=code, tradeDate=yesterday, token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df.head())

    def demoForHotApi(self):
        """短线热点接口测试（XTickHotApi）"""
        print("\n" + "="*80)
        print("【短线热点接口测试 - XTickHotApi】")
        print("="*80)
        
        type_val = 1
        code = "000001"
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        last_month = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        today = datetime.now().strftime("%Y-%m-%d")

        # 1. 连板天梯
        print("\n[1] 连板天梯 - 获取昨日连板数据:")
        result = getLianbanTianti(type=type_val, flag=1, tradeDate=yesterday, token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df.head())

        # 2. 市场情绪
        print("\n[2] 市场情绪 - 获取昨日市场情绪:")
        result = getMarketEmotion(type=type_val, tradeDate=yesterday, token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df)

        # 3. 资金流向
        print("\n[3] 资金流向 - 获取平安银行资金流向:")
        result = getMoneyFlow(type=type_val, code=code, startDate=last_month, endDate=today, token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df.head())

        # 4. 竞价历史
        print("\n[4] 竞价历史 - 获取平安银行竞价历史:")
        result = getBidHistory(type=type_val, code=code, seq=0, startDate=last_month, endDate=today, token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df.head())

        # 5. 竞价详情
        print("\n[5] 竞价详情 - 获取平安银行昨日竞价详情:")
        result = getBidDetail(type=type_val, code=code, tradeDate=yesterday, token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df.head())

        # 6. 新闻资讯
        print("\n[6] 新闻资讯 - 获取最近10分钟新闻:")
        result = getNews(minutes=10, tradeDate=today, token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df.head())

        # 7. 日内分时
        print("\n[7] 日内分时 - 获取平安银行日内分时:")
        result = getTimeKline(type=type_val, code=code, token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df.head())

        # 8. 概念板块
        print("\n[8] 概念板块 - 获取农业板块股票:")
        result = getConceptStocks(symbol="agn", token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df.head())

        # 9. 股票概念
        print("\n[9] 股票概念 - 获取平安银行所属概念:")
        result = getStockConcepts(code=code, token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df)

        # 10. 增量更新
        print("\n[10] 增量更新 - 获取昨日竞价增量数据:")
        data = getDayUpdate(dataType="bid", symbol="bj", tradeDate=yesterday, token=self.token)
        if data:
            print(f"增量更新数据类型: {type(data)}")
            if isinstance(data, list) and len(data) > 0:
                df = pd.DataFrame(data)
                print(f"返回数据条数: {len(df)}")
                print(df.head())

    def demoForQuantApi(self):
        """量化因子接口测试（XTickQuantApi）"""
        print("\n" + "="*80)
        print("【量化因子接口测试 - XTickQuantApi】")
        print("="*80)
        
        type_val = 1
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        # 1. 量化因子-实时
        print("\n[1] 量化因子-实时 - 获取全市场量化因子:")
        result = getQuantDataRealtime(type=type_val, field="all", token=self.token)
        data = json.loads(result)
        if 'data' in data:
            df = pd.DataFrame(data['data'])
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df.head())

        # 2. 量化因子-历史
        print("\n[2] 量化因子-历史 - 获取昨日量化因子历史:")
        result = getQuantDataHistory(tradeDate=yesterday, token=self.token)
        data = json.loads(result)
        if 'data' in data:
            df = pd.DataFrame(data['data'])
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df.head())

    def demoForIndicatorApi(self):
        """金融指标接口测试（XTickIndicatorApi）"""
        print("\n" + "="*80)
        print("【金融指标接口测试 - XTickIndicatorApi】")
        print("="*80)
        
        type_val = 1
        code = "000001"
        last_year = (datetime.now() - timedelta(days=360)).strftime("%Y-%m-%d")
        today = datetime.now().strftime("%Y-%m-%d")

        # MACD指标示例
        print("\n[MACD指标] - 计算平安银行MACD指标:")
        result = macd(type=type_val, code=code, period="1d", fq="front", 
                     startDate=last_year, endDate=today,
                     inReal=2, optInFastPeriod="12", optInSlowPeriod="26", 
                     optInSignalPeriod="9", token=self.token)
        data = json.loads(result)
        if data:
            df = pd.DataFrame(data)
            print(f"返回数据条数: {len(df)}")
            if len(df) > 0:
                print(df.head())

    def demoForWebSocketApi(self):
        """WebSocket接口测试（XTickWebSocketApi）"""
        print("\n" + "="*80)
        print("【WebSocket接口测试 - XTickWebSocketApi】")
        print("="*80)

        # 1. 查询订阅
        print("\n[1] WebSocket查询订阅:")
        result = querysubscribe(token=self.token)
        data = json.loads(result)
        print(f"订阅信息: {data}")

        # 2. 取消订阅
        print("\n[2] WebSocket取消订阅:")
        result = unsubscribe(token=self.token)
        data = json.loads(result)
        print(f"取消订阅结果: {data}")

    def allDemo(self):
        """
        所有API接口的完整Demo示例
        注意：会调用所有接口，因此调用API接口次数多，请按需调用
        """
        print("\n" + "#"*80)
        print("# XTick API 完整测试示例")
        print("#"*80)
        
        self.demoForMarketApi()       # 行情数据接口
        self.demoForWatchApi()        # 盯盘数据接口
        self.demoForCoreApi()         # 核心数据接口
        self.demoForHotApi()          # 短线热点接口
        self.demoForQuantApi()        # 量化因子接口
        self.demoForIndicatorApi()    # 金融指标接口
        self.demoForWebSocketApi()    # WebSocket接口
        
        print("\n" + "#"*80)
        print("# 所有API接口测试完成！")
        print("#"*80)


if __name__ == "__main__":
    # 创建客户端实例
    client = XTickStockApiClient()
    
    # 运行单个接口测试示例（按需选择）
    # client.demoForMarketApi()
    # client.demoForWatchApi()
    # client.demoForCoreApi()
    # client.demoForHotApi()
    # client.demoForQuantApi()
    # client.demoForIndicatorApi()
    # client.demoForWebSocketApi()
    
    # 运行所有接口测试（注意：会调用大量API，耗时较长）
    client.allDemo()
