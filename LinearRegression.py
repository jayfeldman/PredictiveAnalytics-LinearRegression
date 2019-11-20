#!/usr/bin/env python
# coding: utf-8

# # Linear Regression: Number of Lights vs Yield.
# BACKGROUND:  Considering expansion from 8 lights to 30+ lights.
# 

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

datafile = "LightsYield.csv"
data = pd.read_csv(datafile)

slope, intercept, r_value, p_value, std_err = stats.linregress(data["Lights"], data["Yield"])    

plt.scatter(data["Lights"], data["Yield"], alpha=0.5)
plt.title('Yield by Number of Lights')
plt.xlabel('Number of Lights')
plt.ylabel('Yield (oz)')
plt.plot(data["Lights"], slope*np.array(data["Lights"]) + intercept, 'r')
plt.show()
 
print("Best Fit: Slope = {:.2f} Intercept = {:.2f}. R Value = {:.2f}".format(slope, intercept, r_value**2))
