import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Stockdataset\Google.csv')

plt.plot(df["Date"], df["Open"], 'ro--')

plt.show()