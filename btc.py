import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv("BTC_USD.csv")
data1=data.info()
data1=data.describe()
print(data1)
plt.figure("Dilara Kabar")
dt=plt.plot(data["Date"],data["Volume"],color="red")
x=plt.xlabel("Date",size=10)
y=plt.ylabel("Volume",size=10)
plt.legend("Volume for BTC")
plt.title("BTC volume in 2021-2022" ,size=12)
plt.grid(True,color='k')
plt.show()

