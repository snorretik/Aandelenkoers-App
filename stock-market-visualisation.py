import pandas as pd
import matplotlib.pyplot as plt
import tkinter

# source file is inside same folder and named "aex.csv"
df1_source = pd.read_csv(r"data/aex.csv")
df2_source = pd.read_csv(r"data/nasdaq.csv")

df1_close = df1_source[['Date', 'Close']]
df2_close = df2_source[['Date', 'Close']]

df1_close['Close'] = df1_close['Close'] * 7.50

df_total = pd.merge(df1_close, df2_close, how='outer', on='Date')
df_total.plot()
plt.show()