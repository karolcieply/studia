from math import floor, ceil, trunc
import numpy as np 
import pandas as pd
import os
x = 10
r = 15
wektor = [1,2,5,x,r]
wektor = wektor + [r]+list(range(3))
print(wektor)
print(len(wektor))
wnp = np.array(wektor)
print(wnp[wnp%3==0])
print(np.where(wnp>10, "duże", wnp))
print(list(range(2,8,3)))
print((a:="OK") + (b:="Google"))
print(a+"/"+b+"/"+b+"/"+a)
mat = np.arange(1,10)
mat.shape = (3,3)
print(mat)
print(mat[[0,1],:])
print(mat[:,[0,1]]%2==0)
print(mat.shape)
print(np.where(mat%2==0))
print(x:=[[1,3,5], mat, "test"])
print(x[1][1][:])
print(x[2][1:3])
print(y:= [mat[0,:], x])
print(df:= pd.DataFrame(y,columns=["a","aa","aaa"],index=["b","bb"]))
print(df["aa"]["bb"])
print(df.iloc[1][1])
xy = 1.234
print(round(xy))
print(floor(xy))
print(ceil(xy))
print(trunc(xy))
for i in (yx:=[1,3,4,6]):
    print(i, end=",")
print()
for i in range(len(yx)):
    print(i,end=",")
cukrzyca = np.array([1,1,1,0,0,0,1,0,1,0,0,0,0,1,1,1])
cukrzyca = cukrzyca==1
print(cukrzyca)
print(os.getcwd())