from tokenize import PlainToken
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("income_.csv")
data=plt.bar(data["workclass"],data["age"])
data=plt.xlabel("Work Class",color="red",size=20)
data=plt.ylabel("Age",color="red",size=20)
plt.title("--Age And Work Class rate--",size=50)
print(data)
plt.show()


