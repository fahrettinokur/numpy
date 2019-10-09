# -*- coding: utf-8 -*-

import numpy as np

sayilar =[0,5,10,15,20,25,30]
print(sayilar[::-1]) # buda tersten diz demek sadece tek boyutluda kullanılır
print(sayilar[6])
print(sayilar[0:5])
print("\n\n\n")
sayilar2=np.array([[0,2,10],[58,45,69]])
print(sayilar2)
print(sayilar2[0,2])
print(sayilar2[:,2])
print(sayilar2[:,1],"\n\n\n")
print(sayilar2[:,0:2])
print(sayilar2[-1,:])#son satıdaki tüm sütünlar