# -*- coding: utf-8 -*-
import numpy as np

a=np.arange(10)

b=a  # burada sadece b ye anın bulunduğu adres verildi b ne değişrse a dada değişir
print(b)
print(b[2])
print(a[2])


b[0]=121
print(a)
print(b)
print("\n\n")
c=a.copy()
c[0]=51
print(c)
print(a)
print(b)
print("*****************************************")
d=a.view()
print(a)
print(d)
d[0]=80
print(a)
print(d)
print("*********************************************")
d.shape=2,5
print(a)
print(d)
a[0]=123
print(a)
print(d)