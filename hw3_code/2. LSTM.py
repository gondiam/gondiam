# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:48:35 2021

@author: gdiaz
"""
import tensorflow
import torch
import numpy as np
import math
"""
TODO NO FUNCA; ESA NO ES LA SOLUCION JODER!

"""


x1 = [0,0,1,1,1,0]
x2 = [1,1,0,1,1]

def sigmoid(x):
  return 1 / (1 + math.exp(-x))
    
def tanh(x):
    return math.tanh(x)

def calc_h(x):
    
    '''
        x and calculate it's h
    '''
    n = np.size(x)
    f = np.zeros(n)
    ii = np.zeros(n)
    o = np.zeros(n)
    c = np.zeros(n)
    h = np.zeros(n)
    for i in range(n):
        print(i)
        f[i] = sigmoid(-100)
        print(f[i])
        ii[i] = sigmoid(100*x[i]+100)
        print(ii[i])
        o[i] = sigmoid(100*x[i])
        print(o[i])
        tmp = tanh(-100*h[i-1]+50*x[i])
        print(tmp)
        c[i] = f[i]*c[i-1]+ii[i]*tmp
        print(c[i])
        h[i] = o[i]*tanh(c[i])
        
        #h[i] = round(h[i],2)
    return(h)     
coso1 = calc_h(x1)
print(coso1)

coso2 = calc_h(x2)
print(coso2)


