# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:38:28 2017

@author: vsG
"""

import numpy as np
import matplotlib.pyplot as plt

def calcDistance(p1, p2):
    pass
    
a = np.loadtxt(".\\testSet.txt")
plt.scatter(a[:,:1], a[:,1:2])
plt.show()