import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import collections
from matplotlib.figure import Figure
import xlrd 


book = xlrd.open_workbook("bitsdata_cbkm_2015.xls")
'''
tsr = (rotor_speed * radius) / velocity_wind
lmbda = np.power(((1/,-1)
beta = 20  """degree""" 
'''
k =list()
l =list()
p = 0

for lmbda in range (1,15):
	beta = 20 
	p = np.power((1/(lmbda+0.089) - 0.035/(np.power(beta,3)+1)) ,-1)
	cp = np.power(2.71828,-16.5 / (p)) * (98/(p) - 0.4 * beta) / 2 
	k.append(cp)
	l.append(lmbda)
	

plt.plot(l,k)
plt.show()



