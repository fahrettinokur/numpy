# -*- coding: utf-8 -*-

import numpy as np

a=np.floor(10*np.random.random((3,4))) # floor adı üzere zemine indir yani tam sayısını al sadece
print(a)
print(a.shape)
print(a.ravel()) #bu düz hale getir demek
a=a.ravel()
print(a)
print(a.shape)

a=a.reshape(4,3)
print(a)
print(a.T)
print(a.reshape(2,-1)) #baba sen iki satırlık birşey yap sütünü sen ayarlarsın veriye göre