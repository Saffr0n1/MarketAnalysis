#Key Dates CPU: Comet Lake (4/2020) Zen2 (8/2019) Zen3 (8/2020) (11/2020)
#Key Dates GPU: RX5000 (12/2019) RX6000 (11/2020) RTX3000 (9/2020)

import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
# The repo for this package shows you how to use it!

intel = yf.Ticker("INTC")
amd = yf.Ticker("AMD")
nvidia = yf.Ticker("NVDA")

dataI = intel.history(period="2y")
dataA = amd.history(period="2y")
dataN = nvidia.history(period="2y")

print(dataI)

# These dataframes have columns ['Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits']

keyDatesCPU = [dt.datetime(2020,4,30), dt.datetime(2019,8,7), dt.datetime(2020,8,1) ,dt.datetime(2020,11,3)]
keyDatesGPU = [dt.datetime(2019,12,12), dt.datetime(2020,11,18), dt.datetime(2020,9,17)]

fig = plt.figure()
plt.plot(dataI.index, dataI['Close'], label="Intel",c='b')
plt.plot(dataA.index, dataA['Close'], label="AMD",c='r')
for item in keyDatesCPU:
    plt.axvline(x=item, c='k')
plt.legend(loc="upper left")
plt.show()

fig2 = plt.figure()
plt.plot(dataA.index, dataA['Close'], label="AMD",c='r')
plt.plot(dataN.index, dataN['Close'], label="NVIDIA",c='g')
for item in keyDatesGPU:
    plt.axvline(x=item, c='k')
plt.legend(loc="upper left")
plt.show()