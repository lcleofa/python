# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:51:43 2019

@author: 862903
"""

import random
y = [random.random()*100.0 for i in range(10)]
print("Print y")
print(y)

print("Sorted List")
for i in range(len(y)):
     print("%.2f" % y[i])

def avg(x):
     return sum(x) / len(x)

print("Avg: " + str(avg(y)))
print("Max: " + str(max(y)))
print("Min: " + str(min(y)))
z = sum(1 if i<50.0 else 0 for i in y)
print("Number Below 50: " + str(z))

 # another method with NumPy
import numpy as np
print(np.mean(y))
print(np.average(y))
print(np.std(y))
print(np.median(y))