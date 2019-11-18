#!/usr/bin/env python
# coding: utf-8

# # Linear Regression: Number of Lights vs Yield.
# BACKGROUND:  Considering expansion from 8 lights to 30+ lights.
# 

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

lights = []
yields = []
row = []

f = open('LightsYield.csv', 'r')
f1 = f.readlines()

for x in f1:
    row = np.array(x.split(',') )
    lights.append(float(row[0].strip('\n')))
    yields.append(float(row[1].strip('\n')))
    
slope, intercept, r_value, p_value, std_err = stats.linregress(lights,yields)    

plt.scatter(lights, yields, alpha=0.5)
plt.title('Yield by Number of Lights')
plt.xlabel('Number of Lights')
plt.ylabel('Yield (oz)')
plt.plot(lights, slope*np.array(lights) + intercept, 'r')
plt.show()
 
print("Best Fit: Slope = {:.2f} Intercept = {:.2f}. R Value = {:.2f}".format(slope, intercept, r_value**2))
