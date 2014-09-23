# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 14:41:28 2014

@author: Samarth Bhargav
"""
import json, matplotlib
s = json.load( open("bmh_matplotlibrc.json") )
matplotlib.rcParams.update(s)

import matplotlib.pyplot as plt

import collections


def hypothesis(plotsize):    
    return 0.1 + plotsize * .0021;


data = collections.OrderedDict([(2000, 4.3), (2250, 4.8) ,(2500, 5.1),(2750, 5.7) ,(3000, 6.21), (3500, 8.1)])
plotsize = data.keys()
price = data.values()

plt.plot(range(1500, 3500), map(hypothesis, range(1500, 3500)), 'r', label="The Model we fit")
plt.plot(range(3500, 5000), map(hypothesis, range(3500, 5000)), 'r', ls="dashed", label="Predicted")
plt.plot(plotsize, price, 'bo', label="Data Points")
plt.xlim(1500, 5000)
plt.xlabel("Plot Size")
plt.ylim(0, 15)
plt.ylabel("Price (lakhs)")
plt.legend()
for pred in [3250, 4000, 4250]:
    plt.vlines(pred, 0, hypothesis(pred))
    plt.hlines(hypothesis(pred), 0, pred)
plt.show()

