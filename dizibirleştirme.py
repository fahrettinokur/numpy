# -*- coding: utf-8 -*-

import numpy as np

a=np.floor(10*np.random.random((3,4)))
b=np.floor(10*np.random.random((3,4)))
print("a nın shape=",a.shape,"\n",a,"\n\n")
print("b nın shape=",b.shape,"\n",b,"\n\n")

c=np.vstack((a,b)) #üst üste alır yani dikey
print(c,"\n\n","c 'nin shape i=",c.shape)
print("\n\n")

d=np.hstack((a,b))#yan yana alır yani yatay
print(d,"\n\n","d nin shape i=",d.shape)