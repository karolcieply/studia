import pandas as pd
import seaborn as sns
import numpy as np
antropo = pd.read_csv("antropo.csv")
inbody = pd.read_csv("inbody.csv")
#print(antropo.describe())
#print(antropo.head())
antropo[antropo==0] = np.nan
antropo[antropo==""] = np.nan
#print(antropo.head())
#print(antropo.describe())
antropo["Wysokosc"][antropo["Wysokosc"]==17.2] = 172
antropo["WysokoscSiedzeniowa"][antropo["WysokoscSiedzeniowa"]==175.5] = 75.5
print(antropo.describe())
(8,9,10,12,13,14,15,17,19,20,21)