# -*- coding: utf-8 -*-
import numpy as np
 


a=np.arange(15).reshape(3,5) #3 satır beş sutun haline getir 2 boyutlu matrix
print(a)
print(type(a))
print("Dimension count=",str(a.ndim))

b=np.arange(10)
print(b.shape)
print(b.ndim) #Bunu çizği olarak düşün yani tek boyutlu.

#c=np.arange(10).reshape(2,3)
#print(c)             böyle hata alıyorusun