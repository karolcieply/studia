from ntpath import join
import pandas as pd
import seaborn as sns
dfInb = pd.read_csv("dane_inbody.csv")
dfAnt = pd.read_csv("dane_antropo_13.csv")
#dfMerged = pd.concat([dfInb, dfAnt], keys="id", axis=1).set_index("Id").drop("id", axis=1)
#dfMerged = pd.merge(dfInb,dfAnt,"outer").set_index("Id")#.drop("id", axis=1)
dfMerged = dfInb.join(dfAnt, how="outer", lsuffix="idl").set_index("Id").drop("ididl", axis=1)
print(dfMerged.corr())