# -*- coding: utf-8 -*-
import numpy as np

a=np.array([20,30,40,50])

b=np.arange(4)

c=a-b
d=b**3
e=10*np.sin(a)
print(e<7)
print(a*b)  #bu elementer çarpım yani xx yy çarpımı
print(a@b) #bu bize matrix çarpımını verir
print(a.dot(b)) #matrix çarpımın başka hali


f=np.ones((3,4))
z=np.zeros((3,4))
h=np.random.random((2,4))

l=np.sum(b)
g=np.min(a)
p=np.max(a)
print(b.max())
r=np.sqrt(25)
w=np.sqrt(a)
