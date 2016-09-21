# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:06:44 2014

@author: Samarth Bhargav
"""

import json, matplotlib
s = json.load( open("bmh_matplotlibrc.json") )
matplotlib.rcParams.update(s)

import matplotlib.pyplot as plt
import random

random.seed(2332)




def frange(start, end=None, inc=None):
    """A range function, that does accept float increments..."""
    import math

    if end == None:
        end = start + 0.0
        start = 0.0
    else: start += 0.0 # force it to be a float

    if inc == None:
        inc = 1.0
    count = int(math.ceil((end - start) / inc))

    L = [None,] * count

    L[0] = start
    for i in xrange(1,count):
        L[i] = L[i-1] + inc
    return L

def get_class(samples, means, std_dev):
    assert len(means) == len(std_dev), "length of means and std_dev have to be equal"
    dimens = len(means)
    data = []
    for x in range(samples):
        row = []
        for i in range(dimens):
            row.append(random.gauss(means[i], std_dev[i]))
        data.append(row)
    return data

meansA = [ 1000, 2]
std_devA = [500,1]
meansB = [2000,5]
std_devB = [500,2]

samplers_per_class = 100
data = get_class(samplers_per_class, meansA, std_devA)
labels = ["A"] * samplers_per_class

data.extend(get_class(samplers_per_class, meansB, std_devB))

labels.extend([ "B"] * samplers_per_class)

for d,l in zip(data, labels):
    plt.plot(d[0], d[1], "ro" if l == "A" else "bo")
plt_data = zip(range(1,10), frange(0,10,0.1))

plt.show()
