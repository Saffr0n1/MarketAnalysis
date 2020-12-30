import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
from statsmodels.tsa.stattools import grangercausalitytests


intel = yf.Ticker("INTC")
amd = yf.Ticker("AMD")
nvidia = yf.Ticker("NVDA")
btc = yf.Ticker("BTC-USD")

dataA = pd.DataFrame(amd.history(period="2y"))
dataN = pd.DataFrame(nvidia.history(period="2y"))
dataB = pd.DataFrame(btc.history(period="2y"))

dataA.rename(columns={"Close": "AMD-C"}, inplace=True)
dataN.rename(columns={"Close": "NVIDIA-C"}, inplace=True)
dataB.rename(columns={"Close": "BTC-C"}, inplace=True)

allData = pd.concat([dataA["AMD-C"], dataN["NVIDIA-C"], dataB["BTC-C"]], axis=1)
allData = allData.loc['20181230':'20201230']
allData = allData.fillna(method='pad')
allData = allData.dropna()

dataTransform = allData.diff().dropna()

print(allData)
print(dataTransform)
print(dataTransform.describe())

maxlag = 12
test = 'ssr-chi2test'

def grangers_causality_matrix(data, variables, test = 'ssr_chi2test', verbose=False):

    dataset = pd.DataFrame(np.zeros((len(variables), len(variables))), columns=variables, index=variables)

    for c in dataset.columns:
        for r in dataset.index:
            test_result = grangercausalitytests(data[[r,c]], maxlag=maxlag, verbose=False)
            p_values = [round(test_result[i+1][0][test][1],4) for i in range(maxlag)]
            if verbose: print(f'Y = {r}, X = {c}, P Values = {p_values}')

            min_p_value = np.min(p_values)
            dataset.loc[r,c] = min_p_value

    dataset.columns = [var + '_x' for var in variables]
    dataset.index = [var + '_y' for var in variables]

    return dataset

print(grangers_causality_matrix(allData, variables = allData.columns))
print(grangers_causality_matrix(dataTransform, variables = dataTransform.columns))
