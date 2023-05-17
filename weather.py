
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data=pd.read_csv("min_max.csv",delimiter=",")
min_=data["ANNUAL - MIN"]
max_=data["ANNUAL - MAX"]
year=data["YEAR"]
fig=plt.figure()
myaxes=fig.add_axes([18.5,19.5,20.5,21.5])
myaxes.plot(year,min_,"r",lw=20,label="min")
myaxes.plot(year,max_,"b",lw=20,label="max")
myaxes.set_xlabel("YEARS")
myaxes.set_ylabel("rainfall in ml")

