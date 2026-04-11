<p align=center>
<br>
  <a href="http://www.xtick.top/">
    <img src="http://www.xtick.top/assets/nav.png" alt="实时行情报价数据接口" style="width:260px;height:120px">
  </a>
</p>

<p align=center>
   <a href="http://www.xtick.top/">XTick提供实时行情报价数据接入解决方案。</a>
</p>

## 项目介绍

XTick行情API提供了全面、准确、稳定的行情数据，帮助开发者和研究者构建创新的交易和分析工具，满足金融行业的需求，进行深入的市场分析和模型验证。
<br>您的支持，是我们继续维护好XTick项目的动力。
<br>XTick官网：http://www.xtick.top<br>


## 金融数据指标API接口文档
### 1、AD指标
AD指标（Accumulation/Distribution）是一种用于量化分析股票、期货或其他金融资产的技术指标。它主要用于判断资金流向以及市场买卖压力的变化，进而辅助投资者做出买卖决策。
#### 接口地址：/doc/ad
#### 请求示例：http://api.xtick.top/doc/ad?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 2、ADOSC指标
ADOSC指标是一种技术分析指标，全称为累积/派发指标（Accumulation/Distribution Oscillator）。它用于衡量市场买卖压力的强度和方向。
#### 接口地址：/doc/adosc
#### 请求示例：http://api.xtick.top/doc/adosc?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInFastPeriod=3&optInSlowPeriod=10
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInFastPeriod：快速移动平均线周期。参考值：3。
- optInSlowPeriod：慢速移动平均线周期。参考值：10。
#### 输出参数
- output:指标计算值。

### 3、OBV指标
OBV指标（On-Balance Volume）是一种量能指标，用于衡量成交量的变化趋势和预测价格趋势的强弱。OBV指标通过统计成交量的正负值来判断市场的买卖力量，从而预测价格的上涨或下跌趋势。
#### 接口地址：/doc/obv
#### 请求示例：http://api.xtick.top/doc/obv?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 4、AVGPRICE指标
称为平均价格，Average Price (AVGPRICE) 。指标计算公式：AVGPRICE = (开盘价 + 最高价 + 最低价 + 收盘价) / 4 。它可以帮助分析师确定资产价格的趋势和波动性。
#### 接口地址：/doc/avgprice
#### 请求示例：http://api.xtick.top/doc/avgprice?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 5、MEDPRICE指标
称为中位数价格指标，Median Price Indicator。指标计算公式：MEDPRICE = (最高价 + 最低价) / 2。
#### 接口地址：/doc/medprice
#### 请求示例：http://api.xtick.top/doc/medprice?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 6、TYPPRICE指标
TYPPRICE是一种计算股票或其他金融资产的典型价格的方法。指标计算公式：Typical Price = (High + Low + Close) / 3。
#### 接口地址：/doc/typprice
#### 请求示例：http://api.xtick.top/doc/typprice?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 7、WCLPRICE指标
WCLPRICE指标称为加权收盘价，英文名称为Weighted Close Price。指标计算公式：WCLPRICE = (最高价 + 最低价 + 2 * 收盘价) / 4 。
#### 接口地址：/doc/wclprice
#### 请求示例：http://api.xtick.top/doc/wclprice?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 8、ADX指标
ADX指标（Average Directional Movement Index）是一种技术分析指标，用于衡量市场趋势的强弱程度。它由J. Welles Wilder于1978年提出，并广泛应用于股票、期货和外汇市场等。
#### 接口地址：/doc/adx
#### 请求示例：http://api.xtick.top/doc/adx?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInTimePeriod=14
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInTimePeriod：移动平均线周期。参考值：14。
#### 输出参数
- output:指标计算值。

### 9、ADXR指标
ADXR指标（Average Directional Movement Index Rating）是根据ADX指标（Average Directional Index）计算得出的一个指标，用于衡量市场趋势的强度。它是J. Welles Wilder开发的技术分析工具之一。
#### 接口地址：/doc/adxr
#### 请求示例：http://api.xtick.top/doc/adxr?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInTimePeriod=14
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInTimePeriod：移动平均线周期。参考值：14。
#### 输出参数
- output:指标计算值。

### 10、APO指标
APO（Absolute Price Oscillator）指标是一种技术分析指标，用于衡量股票价格的变动幅度。它计算了两个不同时间周期的移动平均线之间的差异，从而提供了价格变动的绝对数值。
#### 接口地址：/doc/apo
#### 请求示例：http://api.xtick.top/doc/apo?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInFastPeriod=12&optInSlowPeriod=26&optInMAType=1
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInFastPeriod：快速移动平均线周期。参考值：12。
- optInSlowPeriod：慢速移动平均线周期。参考值：26。
- optInMAType：移动平均线类型。取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线。参考值：1。
#### 输出参数
- output:指标计算值。

### 11、AROON指标
AROON指标的中文名称是“阿隆指标”，该指标是一种技术分析指标，用于衡量价格趋势的强度和趋势的方向。阿隆指标由两条线组成：上升线（Aroon Up）和下降线（Aroon Down）。
#### 接口地址：/doc/aroon
#### 请求示例：http://api.xtick.top/doc/aroon?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInTimePeriod=14
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInTimePeriod：移动平均线周期。参考值：14。
#### 输出参数
- down:指标计算值。
- up:指标计算值。

### 12、AROONOSC指标
AroonOsc指标的名称是Aroon Oscillator（阿隆振荡器），它是Aroon指标的衍生指标。
#### 接口地址：/doc/aroonosc
#### 请求示例：http://api.xtick.top/doc/aroonosc?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInTimePeriod=14
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInTimePeriod：移动平均线周期。参考值：14。
#### 输出参数
- output:指标计算值。

### 13、BOP指标
BOP指标的名称是Balance of Power，也称为能量平衡指标。
#### 接口地址：/doc/bop
#### 请求示例：http://api.xtick.top/doc/bop?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 14、CCI指标
CCI指标的全称是“商品通道指数”（Commodity Channel Index），它是一种技术分析指标，用于评估商品（或其他金融资产）的价格波动情况和超买超卖状态。
#### 接口地址：/doc/cci
#### 请求示例：http://api.xtick.top/doc/cci?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInTimePeriod=14
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInTimePeriod：移动平均线周期。参考值：14。
#### 输出参数
- output:指标计算值。

### 15、CMO指标
CMO指标的名称：Chande Momentum Oscillator（CMO，钱德动量振荡器）。
#### 接口地址：/doc/cmo
#### 请求示例：http://api.xtick.top/doc/cmo?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=14
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：14。
#### 输出参数
- output:指标计算值。

### 16、DX指标
动向指标(DMI)，英文名称是Directional Movement Index。动向指标（Dx）是一种技术分析指标，用于衡量市场趋势的强度和方向。它由综合指标（+DI和-DI）计算得出，可以帮助交易者判断市场是上涨趋势、下跌趋势还是盘整。
#### 接口地址：/doc/dx
#### 请求示例：http://api.xtick.top/doc/dx?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 17、MACD指标
MACD指标的中文名称为移动平均线收敛/发散指标，英文名称为Moving Average Convergence Divergence。
#### 接口地址：/doc/macd
#### 请求示例：http://api.xtick.top/doc/macd?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInFastPeriod=26&optInSlowPeriod=12&optInSignalPeriod=9
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInFastPeriod：快速移动平均线周期。参考值：26。
- optInSlowPeriod：慢速移动平均线周期。参考值：12。
- optInSignalPeriod：信号移动平均线周期。参考值：9。
#### 输出参数
- diff:指标计算值。
- dea:指标计算值。
- hist:指标计算值。

### 18、MACDEXT指标
MACDEXT指标的中文名称是MACD扩展，英文名称是MACD Extended。MACD扩展是基于移动平均线收敛背离（MACD）指标的一种变种指标。
#### 接口地址：/doc/macdext
#### 请求示例：http://api.xtick.top/doc/macdext?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInFastPeriod=26&optInFastMAType=1&optInSlowPeriod=12&optInSlowMAType=1&optInSignalPeriod=9&optInSignalMAType=1
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInFastPeriod：快速移动平均线周期。参考值：26。
- optInFastMAType：快速移动平均线类型。取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线。参考值：1。
- optInSlowPeriod：慢速移动平均线周期。参考值：12。
- optInSlowMAType：慢速移动平均线类型。取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线。参考值：1。
- optInSignalPeriod：信号移动平均线周期。参考值：9。
- optInSignalMAType：信号移动平均线类型。取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线。参考值：1。
#### 输出参数
- diff:指标计算值。
- dea:指标计算值。
- hist:指标计算值。

### 19、MACDFIX指标
MACDFIX指标的中文名称为移动平均收敛/背离指标，英文名称为Moving Average Convergence Divergence Fix。
#### 接口地址：/doc/macdfix
#### 请求示例：http://api.xtick.top/doc/macdfix?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInSignalPeriod=9
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInSignalPeriod：信号移动平均线周期。参考值：9。
#### 输出参数
- diff:指标计算值。
- dea:指标计算值。
- hist:指标计算值。

### 20、MFI指标
MFI指标的中文名称是资金流量指标，英文名称是Money Flow Index。MFI指标是一种衡量资金流入和流出的指标。它通过计算一定时期内的典型价格和成交量的买卖压力来衡量市场的超买和超卖情况。
#### 接口地址：/doc/mfi
#### 请求示例：http://api.xtick.top/doc/mfi?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInTimePeriod=14
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInTimePeriod：移动平均线周期。参考值：14。
#### 输出参数
- output:指标计算值。

### 21、MINUSDI指标
MINUSDI指标中文名称为负向动向指标，英文名称为Negative Directional Indicator。它是技术分析中的一个指标，用于衡量市场下跌趋势的强度。
#### 接口地址：/doc/minusdi
#### 请求示例：http://api.xtick.top/doc/minusdi?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInTimePeriod=14
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInTimePeriod：移动平均线周期。参考值：14。
#### 输出参数
- output:指标计算值。

### 22、MINUSDM指标
MINUSDM指标的中文名称为负方向运动指标，英文名称为Minus Directional Movement Indicator。该指标用于衡量股价下跌的动力和趋势强度。
#### 接口地址：/doc/minusdm
#### 请求示例：http://api.xtick.top/doc/minusdm?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInTimePeriod=14
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInTimePeriod：移动平均线周期。参考值：14。
#### 输出参数
- output:指标计算值。

### 23、MOM指标
MOM金融指标的中文名称为动量指标，英文名称为Momentum Indicator。该指标是通过比较当前价格与一定期间前的价格变动情况来衡量市场的趋势力量。
#### 接口地址：/doc/mom
#### 请求示例：http://api.xtick.top/doc/mom?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=10
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：10。
#### 输出参数
- output:指标计算值。

### 24、PLUSDI指标
正向移动方向指标，英文名称是Positive Directional Indicator。
#### 接口地址：/doc/plusdi
#### 请求示例：http://api.xtick.top/doc/plusdi?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInTimePeriod=14
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInTimePeriod：移动平均线周期。参考值：14。
#### 输出参数
- output:指标计算值。

### 25、PLUSDM指标
正向动向变动指标，英文名称是Positive Directional Movement。
#### 接口地址：/doc/plusdm
#### 请求示例：http://api.xtick.top/doc/plusdm?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInTimePeriod=14
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInTimePeriod：移动平均线周期。参考值：14。
#### 输出参数
- output:指标计算值。

### 26、PPO指标
价格振荡百分比指标，英文名称为Percentage Price Oscillator。
#### 接口地址：/doc/ppo
#### 请求示例：http://api.xtick.top/doc/ppo?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInFastPeriod=12&optInSlowPeriod=26&optInMAType=1
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInFastPeriod：快速移动平均线周期。参考值：12。
- optInSlowPeriod：慢速移动平均线周期。参考值：26。
- optInMAType：移动平均线类型。取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线。参考值：1。
#### 输出参数
- output:指标计算值。

### 27、ROC指标
ROC金融指标的中文名称是变动率，英文名称是Rate of Change，ROC指标是一种衡量价格变动速度的技。
#### 接口地址：/doc/roc
#### 请求示例：http://api.xtick.top/doc/roc?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=12
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：12。
#### 输出参数
- output:指标计算值。

### 28、ROCP指标
ROCP指标的中文名称为变化率指标，英文名称为Rate of Change Percentage。
#### 接口地址：/doc/rocp
#### 请求示例：http://api.xtick.top/doc/rocp?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=12
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：12。
#### 输出参数
- output:指标计算值。

### 29、ROCR指标
ROCR金融指标是指Rate of Change Ratio，其中文名称是变动率比率，英文名称是Rate of Change Ratio。该指标用于衡量价格的变动率，并通过计算价格的百分比变化来表示。
#### 接口地址：/doc/rocr
#### 请求示例：http://api.xtick.top/doc/rocr?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=12
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：12。
#### 输出参数
- output:指标计算值。

### 30、ROCR100指标
ROCR100金融指标的中文名称为价格变动率，英文名称为Rate of Change Ratio 100，指标介绍为衡量价格在一定时间内的变动幅度，以百分比表示。
#### 接口地址：/doc/rocr100
#### 请求示例：http://api.xtick.top/doc/rocr100?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=12
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：12。
#### 输出参数
- output:指标计算值。

### 31、RSI指标
RSI指标是相对强弱指标，全称为Relative Strength Index。它是一种用于衡量市场超买超卖状态的技术指标，由J. Welles Wilder于1978年提出。RSI指标的计算基于一定时期内的价格变动幅度，通过将一定时期内的上涨幅度和下跌幅度进行比较，以确定市场的强弱程度。
#### 接口地址：/doc/rsi
#### 请求示例：http://api.xtick.top/doc/rsi?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=12
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：12。
#### 输出参数
- output:指标计算值。

### 32、STOCH指标
STOCH是随机指标（KDJ指标），英文名称是Stochastic Oscillator。该指标是一种用来测量价格相对于其价格范围的位置的技术指标。
#### 接口地址：/doc/stoch
#### 请求示例：http://api.xtick.top/doc/stoch?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInFastK_Period=9&optInSlowK_Period=5&optInSlowK_MAType=2&optInSlowD_Period=5&optInSlowD_MAType=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInFastK_Period：快速移动平均线K周期。参考值：9。
- optInSlowK_Period：慢速移动平均线K周期。参考值：5。
- optInSlowK_MAType：慢速移动平均线K类型。取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线。参考值：2。
- optInSlowD_Period：慢速移动平均线D周期。参考值：5。
- optInSlowD_MAType：慢速移动平均线D类型。取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线。参考值：2。
#### 输出参数
- k:指标计算值。
- d:指标计算值。

### 33、STOCHF指标
STOCHF是随机振荡指标（Stochastic Fast）。
#### 接口地址：/doc/stochf
#### 请求示例：http://api.xtick.top/doc/stochf?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInFastK_Period=5&optInFastD_Period=3&optInFastD_MAType=1
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInFastK_Period：快速移动平均线K周期。参考值：5。
- optInFastD_Period：慢速移动平均线D周期。参考值：3。
- optInFastD_MAType：慢速移动平均线D类型。取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线。参考值：1。
#### 输出参数
- k:指标计算值。
- d:指标计算值。

### 34、STOCHRSI指标
随机相对强弱指标，Stochastic Relative Strength Index (STOCHRSI)。
#### 接口地址：/doc/stochrsi
#### 请求示例：http://api.xtick.top/doc/stochrsi?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=14&optInFastK_Period=5&optInFastD_Period=3&optInFastD_MAType=1
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：14。
- optInFastK_Period：快速移动平均线K周期。参考值：5。
- optInFastD_Period：慢速移动平均线D周期。参考值：3。
- optInFastD_MAType：慢速移动平均线D类型。取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线。参考值：1。
#### 输出参数
- k:指标计算值。
- d:指标计算值。

### 35、TRIX指标
TRIX金融指标的中文名称是三重指数平滑平均线，英文名称是Triple Exponential Moving Average (TRIX)。TRIX是一种技术分析指标，用于衡量资产价格的趋势强度。
#### 接口地址：/doc/trix
#### 请求示例：http://api.xtick.top/doc/trix?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 36、ULTOSC指标
ULTOSC称为综合摆动指标，英文名称：Ultimate Oscillator (ULTOSC)。综合摆动指标是一种多周期的技术指标，用于衡量市场买卖力量的强弱。它通过将短期、中期和长期的价格波动进行加权平均，以提供更全面的市场信号。
#### 接口地址：/doc/ultosc
#### 请求示例：http://api.xtick.top/doc/ultosc?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInTimePeriod1=7&optInTimePeriod2=14&optInTimePeriod3=28
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInTimePeriod1：移动平均线周期1。参考值：7。
- optInTimePeriod2：移动平均线周期2。参考值：14。
- optInTimePeriod3：移动平均线周期3。参考值：28。
#### 输出参数
- output:指标计算值。

### 37、WILLR指标
WILLR指标的中文名称为威廉指标(WR)，英文名称为Williams' %R(W%R)。该指标通过测量价格在给定时间周期内的相对变动程度，来判断市场的超买和超卖情况。
#### 接口地址：/doc/willr
#### 请求示例：http://api.xtick.top/doc/willr?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInTimePeriod=10
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInTimePeriod：移动平均线周期。参考值：10。
#### 输出参数
- output:指标计算值。

### 38、HTDCPERIOD指标
Dominant Cycle Period 希尔伯特变换-主导周期。
#### 接口地址：/doc/htdcperiod
#### 请求示例：http://api.xtick.top/doc/htdcperiod?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 39、HTDCPHASE指标
Dominant Cycle Phase 希尔伯特变换-主导循环阶段。
#### 接口地址：/doc/htdcphase
#### 请求示例：http://api.xtick.top/doc/htdcphase?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 40、HTPHASOR指标
Phasor Components 希尔伯特变换-希尔伯特变换相量分量。
#### 接口地址：/doc/htphasor
#### 请求示例：http://api.xtick.top/doc/htphasor?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- inphase:指标计算值。
- quadrature:指标计算值。

### 41、HTSINE指标
SineWave 希尔伯特变换-正弦波。
#### 接口地址：/doc/htsine
#### 请求示例：http://api.xtick.top/doc/htsine?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- sine:指标计算值。
- leadsine:指标计算值。

### 42、HTTRENDMODE指标
Trend vs Cycle Mode 希尔伯特变换-趋势与周期模式。
#### 接口地址：/doc/httrendmode
#### 请求示例：http://api.xtick.top/doc/httrendmode?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 43、DEMA指标
DEMA指标是一种双指数移动平均线，全称为Double Exponential Moving Average。DEMA指标用于平滑价格数据，以便更好地识别价格趋势。
#### 接口地址：/doc/dema
#### 请求示例：http://api.xtick.top/doc/dema?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 44、EMA指标
EMA指标是指数移动平均线，全称为Exponential Moving Average。它是一种常用的技术分析工具，用于平滑价格数据并识别趋势。
#### 接口地址：/doc/ema
#### 请求示例：http://api.xtick.top/doc/ema?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 45、KAMA指标
KAMA是考夫曼自适应移动平均线，全称为Kaufman Adaptive Moving Average。是由Perry J. Kaufman开发的一种技术分析工具，用于平滑股价走势并提供趋势信号。
#### 接口地址：/doc/kama
#### 请求示例：http://api.xtick.top/doc/kama?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 46、MAMA指标
MAMA是MESA自适应移动平均线，全称为MESA Adaptive Moving Average。它是根据价格的移动平均线和自适应移动平均线来计算的，它的设计初衷是能够更好地适应不同市场的变化。
#### 接口地址：/doc/mama
#### 请求示例：http://api.xtick.top/doc/mama?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInFastLimit=0&optInSlowLimit=0
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInFastLimit：输入参数。参考值：0。
- optInSlowLimit：输入参数。参考值：0。
#### 输出参数
- mama:指标计算值。
- fama:指标计算值。

### 47、SMA指标
SMA指标是简单移动平均线，全称为Simple Moving Average。它是一种常用的技术分析指标，用于平滑价格数据并显示价格趋势。
#### 接口地址：/doc/sma
#### 请求示例：http://api.xtick.top/doc/sma?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 48、T3指标
T3是三重移动平均线，全称是Triple Exponential Moving Average。它是指数移动平均线（EMA）的一种改进版本。T3指标通过使用三次平滑来减少EMA的滞后性，并提供更快的响应速度。
#### 接口地址：/doc/t3
#### 请求示例：http://api.xtick.top/doc/t3?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20&optInVFactor=1
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
- optInVFactor：va系数。参考值：1。
#### 输出参数
- output:指标计算值。

### 49、TEMA指标
TEMA是三重指数移动平均线，全程为Triple Exponential Moving Average。它是一种技术分析指标，用于平滑价格数据并识别趋势的变化。TEMA通过多次平滑价格数据来减少价格波动的影响，从而更准确地识别趋势的变化。
#### 接口地址：/doc/tema
#### 请求示例：http://api.xtick.top/doc/tema?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 50、TRIMA指标
TRIMA是三重指数平均线，全称为Triangular Moving Average。它是一种平滑的移动平均线，通过将价格数据进行多次平均处理来消除噪音和波动。
#### 接口地址：/doc/trima
#### 请求示例：http://api.xtick.top/doc/trima?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 51、WMA指标
WMA指标是一种移动平均线指标，全称为Weighted Moving Average。它是一种加权平均线指标，与简单移动平均线（SMA）不同，WMA在计算平均值时给予较近期的数据更高的权重。
#### 接口地址：/doc/wma
#### 请求示例：http://api.xtick.top/doc/wma?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 52、CDL2CROWS指标
形态识别-Cdl2Crows指标。Two Crows 两只乌鸦，三日K线模式，第一天长阳，第二天高开收阴，第三天再次高开继续收阴，收盘比前一日收盘价低，预示股价下跌。
#### 接口地址：/doc/cdl2crows
#### 请求示例：http://api.xtick.top/doc/cdl2crows?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 53、CDL3BLACKCROWS指标
形态识别-Cdl3BlackCrows指标。Three Black Crows 三只乌鸦，三日K线模式，连续三根阴线，每日收盘价都下跌且接近最低价，每日开盘价都在上根K线实体内，预示股价下跌。
#### 接口地址：/doc/cdl3blackcrows
#### 请求示例：http://api.xtick.top/doc/cdl3blackcrows?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 54、CDL3INSIDE指标
形态识别-Cdl3Inside指标。Three Inside Up/Down 三内部上涨和下跌，三日K线模式，母子信号+长K线，以三内部上涨为例，K线为阴阳阳，第三天收盘价高于第一天开盘价，第二天K线在第一天K线内部，预示着股价上涨。
#### 接口地址：/doc/cdl3inside
#### 请求示例：http://api.xtick.top/doc/cdl3inside?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 55、CDL3LINESTRIKE指标
形态识别-Cdl3LineStrike指标。Three-Line Strike 三线打击，四日K线模式，前三根阳线，每日收盘价都比前一日高，开盘价在前一日实体内，第四日市场高开，收盘价低于第一日开盘价，预示股价下跌。
#### 接口地址：/doc/cdl3linestrike
#### 请求示例：http://api.xtick.top/doc/cdl3linestrike?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 56、CDL3OUTSIDE指标
形态识别-Cdl3Outside指标。Three Outside Up/Down 三外部上涨和下跌,三日K线模式，与三内部上涨和下跌类似，K线为阴阳阳，但第一日与第二日的K线形态相反，以三外部上涨为例，第一日K线在第二日K线内部，预示着股价上涨。
#### 接口地址：/doc/cdl3outside
#### 请求示例：http://api.xtick.top/doc/cdl3outside?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 57、CDL3STARSINSOUTH指标
形态识别-Cdl3StarsInSouth指标。Three Stars In The South 南方三星，三日K线模式，与大敌当前相反，三日K线皆阴，第一日有长下影线，第二日与第一日类似，K线整体小于第一日，第三日无下影线实体信号，成交价格都在第一日振幅之内，预示下跌趋势反转，股价上升。
#### 接口地址：/doc/cdl3starsinsouth
#### 请求示例：http://api.xtick.top/doc/cdl3starsinsouth?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 58、CDL3WHITESOLDIERS指标
形态识别-Cdl3WhiteSoldiers指标。Three Advancing White Soldiers 三个白兵，三日K线模式，三日K线皆阳，每日收盘价变高且接近最高价，开盘价在前一日实体上半部，预示股价上升。
#### 接口地址：/doc/cdl3whitesoldiers
#### 请求示例：http://api.xtick.top/doc/cdl3whitesoldiers?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 59、CDLABANDONEDBABY指标
形态识别-CdlAbandonedBaby指标。Abandoned Baby 弃婴，三日K线模式，第二日价格跳空且收十字星（开盘价与收盘价接近，最高价最低价相差不大），预示趋势反转，发生在顶部下跌，底部上涨。
#### 接口地址：/doc/cdlabandonedbaby
#### 请求示例：http://api.xtick.top/doc/cdlabandonedbaby?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInPenetration=0.3
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInPenetration：穿透率。参考值：0.3。
#### 输出参数
- output:指标计算值。

### 60、CDLADVANCEBLOCK指标
形态识别-CdlAdvanceBlock指标。Advance Block 大敌当前，三日K线模式，三日都收阳，每日收盘价都比前一日高，开盘价都在前一日实体以内，实体变短，上影线变长。
#### 接口地址：/doc/cdladvanceblock
#### 请求示例：http://api.xtick.top/doc/cdladvanceblock?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 61、CDLBELTHOLD指标
形态识别-CdlBeltHold指标。Belt-hold CDLBELTHOLD 捉腰带线，两日K线模式，下跌趋势中，第一日阴线，第二日开盘价为最低价，阳线，收盘价接近最高价，预示价格上涨。
#### 接口地址：/doc/cdlbelthold
#### 请求示例：http://api.xtick.top/doc/cdlbelthold?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 62、CDLBREAKAWAY指标
形态识别-CdlBreakaway。指标Breakaway 脱离，五日K线模式，以看涨脱离为例，下跌趋势中，第一日长阴线，第二日跳空阴线，延续趋势开始震荡，第五日长阳线，收盘价在第一天收盘价与第二天开盘价之间，预示价格上涨。
#### 接口地址：/doc/cdlbreakaway
#### 请求示例：http://api.xtick.top/doc/cdlbreakaway?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 63、CDLCLOSINGMARUBOZU指标
形态识别-CdlClosingMarubozu指标。Closing Marubozu 收盘缺影线，一日K线模式，以阳线为例，最低价低于开盘价，收盘价等于最高价，预示着趋势持续。
#### 接口地址：/doc/cdlclosingmarubozu
#### 请求示例：http://api.xtick.top/doc/cdlclosingmarubozu?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 64、CDLCONCEALBABYSWALL指标
形态识别-CdlConcealBabysWall指标。Concealing Baby Swallow 藏婴吞没，四日K线模式，下跌趋势中，前两日阴线无影线，第二日开盘、收盘价皆低于第二日，第三日倒锤头，第四日开盘价高于前一日最高价，收盘价低于前一日最低价，预示着底部反转。
#### 接口地址：/doc/cdlconcealbabyswall
#### 请求示例：http://api.xtick.top/doc/cdlconcealbabyswall?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 65、CDLCOUNTERATTACK指标
形态识别-CdlCounterAttack指标。Counterattack 反击线，二日K线模式，与分离线类似。
#### 接口地址：/doc/cdlcounterattack
#### 请求示例：http://api.xtick.top/doc/cdlcounterattack?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 66、CDLDARKCLOUDCOVER指标
形态识别-CdlDarkCloudCover指标。Dark Cloud Cover 乌云盖顶，二日K线模式，第一日长阳，第二日开盘价高于前一日最高价，收盘价处于前一日实体中部以下，预示着股价下跌。
#### 接口地址：/doc/cdldarkcloudcover
#### 请求示例：http://api.xtick.top/doc/cdldarkcloudcover?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInPenetration=0.5
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInPenetration：穿透率。参考值：0.5。
#### 输出参数
- output:指标计算值。

### 67、CDLDOJI指标
形态识别-CdlDoji指标。Doji 十字，一日K线模式，开盘价与收盘价基本相同。
#### 接口地址：/doc/cdldoji
#### 请求示例：http://api.xtick.top/doc/cdldoji?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 68、CDLDOJISTAR指标
形态识别-CdlDojiStar指标。Doji Star 十字星，一日K线模式，开盘价与收盘价基本相同，上下影线不会很长，预示着当前趋势反转。
#### 接口地址：/doc/cdldojistar
#### 请求示例：http://api.xtick.top/doc/cdldojistar?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 69、CDLDRAGONFLYDOJI指标
形态识别-CdlDragonflyDoji指标。Dragonfly Doji 蜻蜓十字/T形十字，一日K线模式，开盘后价格一路走低，之后收复，收盘价与开盘价相同，预示趋势反转。
#### 接口地址：/doc/cdldragonflydoji
#### 请求示例：http://api.xtick.top/doc/cdldragonflydoji?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 70、CDLENGULFING指标
形态识别-CdlEngulfing指标。Dragonfly 蜻蜓十字/T形十字指标，一日K线模式，开盘后价格一路走低，之后收复，收盘价与开盘价相同，预示趋势反转。
#### 接口地址：/doc/cdlengulfing
#### 请求示例：http://api.xtick.top/doc/cdlengulfing?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 71、CDLEVENINGDOJISTAR指标
形态识别-CdlEveningDojiStar指标。Evening Doji Star 十字暮星指标，三日K线模式，基本模式为暮星，第二日收盘价和开盘价相同，预示顶部反转。
#### 接口地址：/doc/cdleveningdojistar
#### 请求示例：http://api.xtick.top/doc/cdleveningdojistar?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInPenetration=0.3
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInPenetration：穿透率。参考值：0.3。
#### 输出参数
- output:指标计算值。

### 72、CDLEVENINGSTAR指标
形态识别-CdlEveningStar指标。Evening Star 暮星指标，三日K线模式，与晨星相反，上升趋势中,第一日阳线，第二日价格振幅较小，第三日阴线，预示顶部反转。
#### 接口地址：/doc/cdleveningstar
#### 请求示例：http://api.xtick.top/doc/cdleveningstar?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInPenetration=0.3
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInPenetration：穿透率。参考值：0.3。
#### 输出参数
- output:指标计算值。

### 73、CDLGAPSIDESIDEWHITE指标
形态识别-CdlGapSideSideWhite指标。Up/Down-gap side-by-side white lines 向上/下跳空并列阳线指标，二日K线模式，上升趋势向上跳空，下跌趋势向下跳空,第一日与第二日有相同开盘价，实体长度差不多，则趋势持续。
#### 接口地址：/doc/cdlgapsidesidewhite
#### 请求示例：http://api.xtick.top/doc/cdlgapsidesidewhite?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 74、CDLGRAVESTONEDOJI指标
形态识别-CdlGravestoneDoji指标。Gravestone Doji 墓碑十字/倒T十字指标。一日K线模式，开盘价与收盘价相同，上影线长，无下影线，预示底部反转。
#### 接口地址：/doc/cdlgravestonedoji
#### 请求示例：http://api.xtick.top/doc/cdlgravestonedoji?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 75、CDLHAMMER指标
形态识别-CdlHammer指标。Hammer 锤头指标。一日K线模式，实体较短，无上影线，下影线大于实体长度两倍，处于下跌趋势底部，预示反转。
#### 接口地址：/doc/cdlhammer
#### 请求示例：http://api.xtick.top/doc/cdlhammer?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 76、CDLHANGINGMAN指标
形态识别-CdlHangingMan指标。Hanging Man 上吊线指标。一日K线模式，形状与锤子类似，处于上升趋势的顶部，预示着趋势反转。
#### 接口地址：/doc/cdlhangingman
#### 请求示例：http://api.xtick.top/doc/cdlhangingman?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 77、CDLHARAMI指标
形态识别-CdlHarami指标。Harami Pattern 母子线指标。二日K线模式，分多头母子与空头母子，两者相反，以多头母子为例，在下跌趋势中，第一日K线长阴，第二日开盘价收盘价在第一日价格振幅之内，为阳线，预示趋势反转，股价上升。
#### 接口地址：/doc/cdlharami
#### 请求示例：http://api.xtick.top/doc/cdlharami?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 78、CDLHARAMICROSS指标
形态识别-CdlHaramiCross指标。Harami Cross Pattern 十字孕线指标。二日K线模式，与母子县类似，若第二日K线是十字线，便称为十字孕线，预示着趋势反转。
#### 接口地址：/doc/cdlharamicross
#### 请求示例：http://api.xtick.top/doc/cdlharamicross?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 79、CDLHIGNWAVE指标
形态识别-CdlHignWave指标。
#### 接口地址：/doc/cdlhignwave
#### 请求示例：http://api.xtick.top/doc/cdlhignwave?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 80、CDLHIKKAKE指标
形态识别-CdlHikkake指标。Hikkake Pattern 陷阱，三日K线模式，与母子类似，第二日价格在前一日实体范围内,第三日收盘价高于前两日，反转失败，趋势继续。
#### 接口地址：/doc/cdlhikkake
#### 请求示例：http://api.xtick.top/doc/cdlhikkake?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 81、CDLHIKKAKEMOD指标
形态识别-CdlHikkakeMod指标。Modified Hikkake Pattern 修正陷阱，三日K线模式，与陷阱类似，上升趋势中，第三日跳空高开；下跌趋势中，第三日跳空低开，反转失败，趋势继续。
#### 接口地址：/doc/cdlhikkakemod
#### 请求示例：http://api.xtick.top/doc/cdlhikkakemod?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 82、CDLHOMINGPIGEON指标
形态识别-CdlHomingPigeon指标。Homing Pigeon 家鸽，二日K线模式，与母子线类似，不同的的是二日K线颜色相同，第二日最高价、最低价都在第一日实体之内，预示着趋势反转。
#### 接口地址：/doc/cdlhomingpigeon
#### 请求示例：http://api.xtick.top/doc/cdlhomingpigeon?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 83、CDLIDENTICAL3CROWS指标
形态识别-CdlIdentical3Crows指标。Identical Three Crows 三胞胎乌鸦，三日K线模式，上涨趋势中，三日都为阴线，长度大致相等，每日开盘价等于前一日收盘价，收盘价接近当日最低价，预示价格下跌。
#### 接口地址：/doc/cdlidentical3crows
#### 请求示例：http://api.xtick.top/doc/cdlidentical3crows?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 84、CDLINNECK指标
形态识别-CdlInNeck指标。In-Neck Pattern 颈内线，二日K线模式，下跌趋势中，第一日长阴线，第二日开盘价较低，收盘价略高于第一日收盘价，阳线，实体较短，预示着下跌继续。
#### 接口地址：/doc/cdlinneck
#### 请求示例：http://api.xtick.top/doc/cdlinneck?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 85、CDLINVERTEDHAMMER指标
形态识别-CdlInvertedHammer指标。Inverted Hammer 倒锤头，一日K线模式，上影线较长，长度为实体2倍以上，无下影线，在下跌趋势底部，预示着趋势反转。
#### 接口地址：/doc/cdlinvertedhammer
#### 请求示例：http://api.xtick.top/doc/cdlinvertedhammer?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 86、CDLKICKING指标
形态识别-CdlKicking指标。Kicking 反冲形态，二日K线模式，与分离线类似，两日K线为秃线，颜色相反，存在跳空缺口。
#### 接口地址：/doc/cdlkicking
#### 请求示例：http://api.xtick.top/doc/cdlkicking?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 87、CDLKICKINGBYLENGTH指标
形态识别-CdlKickingByLength指标。Kicking - bull/bear determined by the longer marubozu 由较长缺影线决定的反冲形态，二日K线模式，与反冲形态类似，较长缺影线决定价格的涨跌。
#### 接口地址：/doc/cdlkickingbylength
#### 请求示例：http://api.xtick.top/doc/cdlkickingbylength?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 88、CDLLADDERBOTTOM指标
形态识别-CdlLadderBottom指标。Ladder Bottom 梯底，五日K线模式，下跌趋势中，前三日阴线，开盘价与收盘价皆低于前一日开盘、收盘价，第四日倒锤头，第五日开盘价高于前一日开盘价，阳线，收盘价高于前几日价格振幅，预示着底部反转。
#### 接口地址：/doc/cdlladderbottom
#### 请求示例：http://api.xtick.top/doc/cdlladderbottom?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 89、CDLLONGLEGGEDDOJI指标
形态识别-CdlLongLeggedDoji指标。Long Legged Doji 长脚十字，一日K线模式，开盘价与收盘价相同居当日价格中部，上下影线长，表达市场不确定性。
#### 接口地址：/doc/cdllongleggeddoji
#### 请求示例：http://api.xtick.top/doc/cdllongleggeddoji?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 90、CDLLONGLINE指标
形态识别-CdlLongLine指标。Long Line Candle 长蜡烛，一日K线模式，K线实体长，无上下影线。
#### 接口地址：/doc/cdllongline
#### 请求示例：http://api.xtick.top/doc/cdllongline?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 91、CDLMARUBOZU指标
形态识别-CdlMarubozu指标。Marubozu 光头光脚/缺影线，一日K线模式，上下两头都没有影线的实体，阴线预示着熊市持续或者牛市反转，阳线相反。
#### 接口地址：/doc/cdlmarubozu
#### 请求示例：http://api.xtick.top/doc/cdlmarubozu?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 92、CDLMATHOLD指标
形态识别-CdlMatHold指标。Mat Hold 铺垫，五日K线模式，上涨趋势中，第一日阳线，第二日跳空高开影线，第三、四日短实体影线，第五日阳线，收盘价高于前四日，预示趋势持续。
#### 接口地址：/doc/cdlmathold
#### 请求示例：http://api.xtick.top/doc/cdlmathold?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInPenetration=0.5
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInPenetration：穿透率。参考值：0.5。
#### 输出参数
- output:指标计算值。

### 93、CDLMATCHINGLOW指标
形态识别-CdlMatchingLow指标。Matching Low 相同低价，二日K线模式，下跌趋势中，第一日长阴线，第二日阴线，收盘价与前一日相同，预示底部确认，该价格为支撑位。
#### 接口地址：/doc/cdlmatchinglow
#### 请求示例：http://api.xtick.top/doc/cdlmatchinglow?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 94、CDLMORNINGDOJISTAR指标
形态识别-CdlMorningDojiStar指标。Morning Doji Star 十字晨星,三日K线模式，基本模式为晨星，第二日K线为十字星，预示底部反转。
#### 接口地址：/doc/cdlmorningdojistar
#### 请求示例：http://api.xtick.top/doc/cdlmorningdojistar?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInPenetration=0.3
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInPenetration：穿透率。参考值：0.3。
#### 输出参数
- output:指标计算值。

### 95、CDLMORNINGSTAR指标
形态识别-CdlMorningStar指标。Morning Star 晨星，三日K线模式，下跌趋势，第一日阴线，第二日价格振幅较小，第三天阳线，预示底部反转。
#### 接口地址：/doc/cdlmorningstar
#### 请求示例：http://api.xtick.top/doc/cdlmorningstar?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInPenetration=0.3
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInPenetration：穿透率。参考值：0.3。
#### 输出参数
- output:指标计算值。

### 96、CDLONNECK指标
形态识别-CdlOnNeck指标。On-Neck Pattern 颈上线,二日K线模式，下跌趋势中，第一日长阴线，第二日开盘价较低，收盘价与前一日最低价相同，阳线，实体较短，预示着延续下跌趋势。
#### 接口地址：/doc/cdlonneck
#### 请求示例：http://api.xtick.top/doc/cdlonneck?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 97、CDLPIERCING指标
形态识别-CdlPiercing指标。Piercing Pattern 刺透形态，两日K线模式，下跌趋势中，第一日阴线，第二日收盘价低于前一日最低价，收盘价处在第一日实体上部，预示着底部反转。
#### 接口地址：/doc/cdlpiercing
#### 请求示例：http://api.xtick.top/doc/cdlpiercing?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 98、CDLRICKSHAWMAN指标
形态识别-CdlRickshawMan指标。Rickshaw Man 黄包车夫,一日K线模式，与长腿十字线类似，若实体正好处于价格振幅中点，称为黄包车夫。
#### 接口地址：/doc/cdlrickshawman
#### 请求示例：http://api.xtick.top/doc/cdlrickshawman?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 99、CDLRISEFALL3METHODS指标
形态识别-CdlRiseFall3Methods指标。Rising/Falling Three Methods 上升/下降三法，五日K线模式，以上升三法为例，上涨趋势中，第一日长阳线，中间三日价格在第一日范围内小幅震荡，第五日长阳线，收盘价高于第一日收盘价，预示股价上升。
#### 接口地址：/doc/cdlrisefall3methods
#### 请求示例：http://api.xtick.top/doc/cdlrisefall3methods?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 100、CDLSEPERATINGLINES指标
形态识别-CdlSeperatingLines指标。
#### 接口地址：/doc/cdlseperatinglines
#### 请求示例：http://api.xtick.top/doc/cdlseperatinglines?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 101、CDLSHOOTINGSTAR指标
形态识别-CdlShootingStar指标。Shooting Star 射击之星，一日K线模式，上影线至少为实体长度两倍，没有下影线，预示着股价下跌。
#### 接口地址：/doc/cdlshootingstar
#### 请求示例：http://api.xtick.top/doc/cdlshootingstar?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 102、CDLSHORTLINE指标
形态识别-CdlShortLine指标。Short Line Candle 短蜡烛，一日K线模式，实体短，无上下影线。
#### 接口地址：/doc/cdlshortline
#### 请求示例：http://api.xtick.top/doc/cdlshortline?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 103、CDLSPINNINGTOP指标
形态识别-CdlSpinningTop指标。Spinning Top 纺锤，一日K线，实体小。
#### 接口地址：/doc/cdlspinningtop
#### 请求示例：http://api.xtick.top/doc/cdlspinningtop?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 104、CDLSTALLEDPATTERN指标
形态识别-CdlStalledPattern指标。Stalled Pattern 停顿形态，三日K线模式，上涨趋势中，第二日长阳线，第三日开盘于前一日收盘价附近，短阳线，预示着上涨结束。
#### 接口地址：/doc/cdlstalledpattern
#### 请求示例：http://api.xtick.top/doc/cdlstalledpattern?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 105、CDLSTICKSANDWHICH指标
形态识别-CdlStickSandwhich指标。
#### 接口地址：/doc/cdlsticksandwhich
#### 请求示例：http://api.xtick.top/doc/cdlsticksandwhich?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 106、CDLTAKURI指标
形态识别-CdlTakuri指标。Takuri (Dragonfly Doji with very long lower shadow) 探水竿，一日K线模式，大致与蜻蜓十字相同，下影线长度长。
#### 接口地址：/doc/cdltakuri
#### 请求示例：http://api.xtick.top/doc/cdltakuri?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 107、CDLTASUKIGAP指标
形态识别-CdlTasukiGap指标。Tasuki Gap 跳空并列阴阳线，三日K线模式，分上涨和下跌，以上升为例，前两日阳线，第二日跳空，第三日阴线，收盘价于缺口中，上升趋势持续。
#### 接口地址：/doc/cdltasukigap
#### 请求示例：http://api.xtick.top/doc/cdltasukigap?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 108、CDLTHRUSTING指标
形态识别-CdlThrusting指标。Thrusting Pattern 插入，二日K线模式，与颈上线类似，下跌趋势中，第一日长阴线，第二日开盘价跳空，收盘价略低于前一日实体中部，与颈上线相比实体较长，预示着趋势持续。
#### 接口地址：/doc/cdlthrusting
#### 请求示例：http://api.xtick.top/doc/cdlthrusting?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 109、CDLTRISTAR指标
形态识别-CdlTristar指标。Tristar Pattern 三星，三日K线模式，由三个十字组成，第二日十字必须高于或者低于第一日和第三日，预示着反转。
#### 接口地址：/doc/cdltristar
#### 请求示例：http://api.xtick.top/doc/cdltristar?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 110、CDLUNIQUE3RIVER指标
形态识别-CdlUnique3River指标。Unique 3 River 奇特三河床，三日K线模式，下跌趋势中，第一日长阴线，第二日为锤头，最低价创新低，第三日开盘价低于第二日收盘价，收阳线，收盘价不高于第二日收盘价，预示着反转，第二日下影线越长可能性越大。
#### 接口地址：/doc/cdlunique3river
#### 请求示例：http://api.xtick.top/doc/cdlunique3river?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 111、CDLUPSIDEGAP2CROWS指标
形态识别-CdlUpsideGap2Crows指标。Upside Gap Two Crows 向上跳空的两只乌鸦，三日K线模式，第一日阳线，第二日跳空以高于第一日最高价开盘，收阴线，第三日开盘价高于第二日，收阴线，与第一日比仍有缺口。
#### 接口地址：/doc/cdlupsidegap2crows
#### 请求示例：http://api.xtick.top/doc/cdlupsidegap2crows?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 112、CDLXSIDEGAP3METHODS指标
形态识别-CdlXSideGap3Methods指标。Upside/Downside Gap Three Methods 上升/下降跳空三法，五日K线模式，以上升跳空三法为例，上涨趋势中，第一日长阳线，第二日短阳线，第三日跳空阳线，第四日阴线，开盘价与收盘价于前两日实体内，第五日长阳线，收盘价高于第一日收盘价，预示股价上升。
#### 接口地址：/doc/cdlxsidegap3methods
#### 请求示例：http://api.xtick.top/doc/cdlxsidegap3methods?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 113、ACOS指标
反余弦函数。
#### 接口地址：/doc/acos
#### 请求示例：http://api.xtick.top/doc/acos?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 114、ASIN指标
反正弦函数。
#### 接口地址：/doc/asin
#### 请求示例：http://api.xtick.top/doc/asin?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 115、ATAN指标
反正切函数。
#### 接口地址：/doc/atan
#### 请求示例：http://api.xtick.top/doc/atan?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 116、CEIL指标
向上取整数。
#### 接口地址：/doc/ceil
#### 请求示例：http://api.xtick.top/doc/ceil?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 117、COS指标
余弦函数。
#### 接口地址：/doc/cos
#### 请求示例：http://api.xtick.top/doc/cos?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 118、COSH指标
双曲正弦函数。
#### 接口地址：/doc/cosh
#### 请求示例：http://api.xtick.top/doc/cosh?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 119、EXP指标
指数曲线。
#### 接口地址：/doc/exp
#### 请求示例：http://api.xtick.top/doc/exp?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 120、FLOOR指标
向下取整数。
#### 接口地址：/doc/floor
#### 请求示例：http://api.xtick.top/doc/floor?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 121、LN指标
自然对数。
#### 接口地址：/doc/ln
#### 请求示例：http://api.xtick.top/doc/ln?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 122、LOG10指标
对数函数。
#### 接口地址：/doc/log10
#### 请求示例：http://api.xtick.top/doc/log10?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 123、SIN指标
正弦函数。
#### 接口地址：/doc/sin
#### 请求示例：http://api.xtick.top/doc/sin?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 124、SINH指标
双曲正弦函数。
#### 接口地址：/doc/sinh
#### 请求示例：http://api.xtick.top/doc/sinh?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 125、SQRT指标
非负实数的平方根。
#### 接口地址：/doc/sqrt
#### 请求示例：http://api.xtick.top/doc/sqrt?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 126、TAN指标
正切函数。
#### 接口地址：/doc/tan
#### 请求示例：http://api.xtick.top/doc/tan?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 127、TANH指标
双曲正切函数。
#### 接口地址：/doc/tanh
#### 请求示例：http://api.xtick.top/doc/tanh?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 128、ADD指标
向量加法运算。
#### 接口地址：/doc/add
#### 请求示例：http://api.xtick.top/doc/add?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal0=1&inReal1=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal0：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：1。
- inReal1：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 129、DIV指标
向量减法运算。
#### 接口地址：/doc/div
#### 请求示例：http://api.xtick.top/doc/div?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal0=1&inReal1=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal0：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：1。
- inReal1：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 130、MAX指标
周期内最大值。
#### 接口地址：/doc/max
#### 请求示例：http://api.xtick.top/doc/max?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 131、MAXINDEX指标
周期内最大值的索引。
#### 接口地址：/doc/maxindex
#### 请求示例：http://api.xtick.top/doc/maxindex?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 132、MIN指标
周期内最小值。
#### 接口地址：/doc/min
#### 请求示例：http://api.xtick.top/doc/min?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 133、MININDEX指标
周期内最小值的索引。
#### 接口地址：/doc/minindex
#### 请求示例：http://api.xtick.top/doc/minindex?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 134、MINMAX指标
周期内最小值和最大值。
#### 接口地址：/doc/minmax
#### 请求示例：http://api.xtick.top/doc/minmax?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- min:指标计算值。
- max:指标计算值。

### 135、MINMAXINDEX指标
周期内最小值和最大值索引。
#### 接口地址：/doc/minmaxindex
#### 请求示例：http://api.xtick.top/doc/minmaxindex?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- minidx:指标计算值。
- maxidx:指标计算值。

### 136、MULT指标
向量乘法运算。
#### 接口地址：/doc/mult
#### 请求示例：http://api.xtick.top/doc/mult?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal0=1&inReal1=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal0：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：1。
- inReal1：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 137、SUB指标
向量除法运算。
#### 接口地址：/doc/sub
#### 请求示例：http://api.xtick.top/doc/sub?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal0=1&inReal1=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal0：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：1。
- inReal1：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 138、SUM指标
周期内求和。
#### 接口地址：/doc/sum
#### 请求示例：http://api.xtick.top/doc/sum?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 139、ATR指标
ATR称为真实波动幅度指标，英文名称为Average True Range。ATR指标是一种衡量市场波动性的技术指标，它通过计算一定时间内的价格波动幅度，来评估市场的波动性程度。
#### 接口地址：/doc/atr
#### 请求示例：http://api.xtick.top/doc/atr?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInTimePeriod=14
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInTimePeriod：移动平均线周期。参考值：14。
#### 输出参数
- output:指标计算值。

### 140、NATR指标
NATR称为归一化真实波动幅度，英文名称为Normalized Average True Range。该指标用于衡量市场的波动性。
#### 接口地址：/doc/natr
#### 请求示例：http://api.xtick.top/doc/natr?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInTimePeriod=14
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInTimePeriod：移动平均线周期。参考值：14。
#### 输出参数
- output:指标计算值。

### 141、TRUERANGE指标
称为真实波幅，英文名称为True Range。它是一种衡量价格波动性的指标。
#### 接口地址：/doc/truerange
#### 请求示例：http://api.xtick.top/doc/truerange?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
#### 输出参数
- output:指标计算值。

### 142、BETA指标
Beta指标。
#### 接口地址：/doc/beta
#### 请求示例：http://api.xtick.top/doc/beta?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal0=2&inReal1=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal0：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- inReal1：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 143、CORREL指标
Correl指标。
#### 接口地址：/doc/correl
#### 请求示例：http://api.xtick.top/doc/correl?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal0=2&inReal1=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal0：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- inReal1：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 144、LINEARREG指标
LinearReg指标。
#### 接口地址：/doc/linearreg
#### 请求示例：http://api.xtick.top/doc/linearreg?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 145、LINEARREGANGLE指标
LinearRegAngle指标。
#### 接口地址：/doc/linearregangle
#### 请求示例：http://api.xtick.top/doc/linearregangle?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 146、LINEARREGINTERCEPT指标
LinearRegIntercept指标。
#### 接口地址：/doc/linearregintercept
#### 请求示例：http://api.xtick.top/doc/linearregintercept?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 147、LINEARREGSLOPE指标
LinearRegSlope指标。
#### 接口地址：/doc/linearregslope
#### 请求示例：http://api.xtick.top/doc/linearregslope?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 148、STDDEV指标
StdDev指标。
#### 接口地址：/doc/stddev
#### 请求示例：http://api.xtick.top/doc/stddev?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=5&optInNbDev=1
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：5。
- optInNbDev：标准差倍数。参考值：1。
#### 输出参数
- output:指标计算值。

### 149、TSF指标
Tsf指标。
#### 接口地址：/doc/tsf
#### 请求示例：http://api.xtick.top/doc/tsf?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
#### 输出参数
- output:指标计算值。

### 150、VARIANCE指标
方差。
#### 接口地址：/doc/variance
#### 请求示例：http://api.xtick.top/doc/variance?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=5&optInNbDev=1
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：5。
- optInNbDev：标准差倍数。参考值：1。
#### 输出参数
- output:指标计算值。

### 151、BBANDS指标
BBANDS称为布林带，英文名称为Bollinger Bands。布林带是一种基于统计学原理的技术分析指标，由约翰·布林格（John Bollinger）于20世纪80年代提出。它通过计算价格的标准差来确定价格的高低波动区间，并以此构建出上下两条通道线，从而帮助判断价格的超买和超卖情况。
#### 接口地址：/doc/bbands
#### 请求示例：http://api.xtick.top/doc/bbands?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=20&optInNbDevUp=2&optInNbDevDn=2&optInMAType=1
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：20。
- optInNbDevUp：上轨道线的标准偏差倍数。参考值：2。
- optInNbDevDn：下轨道线的标准偏差倍数。参考值：2。
- optInMAType：移动平均线类型。取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线。参考值：1。
#### 输出参数
- up:指标计算值。
- mid:指标计算值。
- low:指标计算值。

### 152、HTTRENDLINE指标
HTTRENDLINE称为趋势线，英文名称为HTTRENDLINE。该指标是一种基于趋势线的技术分析工具。
#### 接口地址：/doc/httrendline
#### 请求示例：http://api.xtick.top/doc/httrendline?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
#### 输出参数
- output:指标计算值。

### 153、MIDPOINT指标
MIDPOINT是一种基于价格的技术指标，用于衡量价格趋势的中点。
#### 接口地址：/doc/midpoint
#### 请求示例：http://api.xtick.top/doc/midpoint?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=14
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：14。
#### 输出参数
- output:指标计算值。

### 154、MIDPRICE指标
MIDPRICE指标是一种技术分析工具，用于计算一段时间内的市场中间价。
#### 接口地址：/doc/midprice
#### 请求示例：http://api.xtick.top/doc/midprice?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInTimePeriod=14
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInTimePeriod：移动平均线周期。参考值：14。
#### 输出参数
- output:指标计算值。

### 155、MOVINGAVERAGE指标
MOVINGAVERAGE金融指标的中文名称为移动平均线，英文名称为Moving Average。该指标通过计算一段时间内收盘价的平均值来观察价格变动的趋势。
#### 接口地址：/doc/movingaverage
#### 请求示例：http://api.xtick.top/doc/movingaverage?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&inReal=2&optInTimePeriod=14&optInMAType=1
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- inReal：数据标签。取值范围：1|open-开盘价；2|close-收盘价；3|high-最高价；4|low-最低价；5|volume-成交量；6|amount-成交额。参考值：2。
- optInTimePeriod：移动平均线周期。参考值：14。
- optInMAType：移动平均线类型。取值范围：1|SMA-简单移动平均线；2|EMA-指数移动平均线；3|WMA-加权移动平均线；4|DEMA-双指数移动平均线；5|TEMA-三重指数移动平均线；6|TRIMA-三重移动平均线；7|KAMA-考夫曼自适应移动平均线；8|MAMA-自适应移动平均线；9|T3-三重移动平均线。参考值：1。
#### 输出参数
- output:指标计算值。

### 156、SAR指标
SAR称为抛物线指标，英文名称为Parabolic SAR (Stop and Reverse)。
#### 接口地址：/doc/sar
#### 请求示例：http://api.xtick.top/doc/sar?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInAcceleration=0.02&optInMaximum=0.2
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInAcceleration：加速因子。参考值：0.02。
- optInMaximum：最大值。参考值：0.2。
#### 输出参数
- output:指标计算值。

### 157、SAREXT指标
SAREXT称为拓展停损点指标，英文名称为SAREXT (Extended Stop and Reverse Indicator)。
#### 接口地址：/doc/sarext
#### 请求示例：http://api.xtick.top/doc/sarext?type=1&code=000001&period=1d&fq=front&startDate=2025-01-01&endDate=2026-01-01&token=123456789&optInStartValue=0&optInOffsetOnReverse=0&optInAccelerationInitLong=0.02&optInAccelerationLong=0.02&optInAccelerationMaxLong=0.02&optInAccelerationInitShort=0.02&optInAccelerationShort=0.02&optInAccelerationMaxShort=0.02
#### 输入参数
- type：股票类别。
- code：股票代码。
- period：k线周期。
- fq：除权方式。
- startDate：起始时间。
- endDate：结束时间。
- token：令牌。
- optInStartValue：起始值。参考值：0。
- optInOffsetOnReverse：反转偏移量。参考值：0。
- optInAccelerationInitLong：多头初始加速因子。参考值：0.02。
- optInAccelerationLong：多头加速因子。参考值：0.02。
- optInAccelerationMaxLong：多头最大加速因子。参考值：0.02。
- optInAccelerationInitShort：空头初始加速因子。参考值：0.02。
- optInAccelerationShort：空头加速因子。参考值：0.02。
- optInAccelerationMaxShort：空头最大加速因子。参考值：0.02。
#### 输出参数
- output:指标计算值。
