# -*- coding: utf-8 -*-

import numpy as np

a=np.array([1,2,3,4,5,6])
a=a.reshape(2,3)
print(a)
print(a.dtype)
print(a.ndim)


b=np.array([[2,3],[4,5],[9,8]])
print(b)
print(b.dtype)
print(b.ndim)