import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt 
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
import collections
from scipy.signal import argrelextrema
from matplotlib.figure import Figure
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
Ka = 50
Kf = 0.01
If = 2
Rf = 1
Ra = 3

def findr(P,W):
	Ea=Kf*Ka*If*W
	return (Ea*Ea - 2*P*Ra)/2*P
	
	
def Pow(r,w):
	Ea=Kf*Ka*If*w
	V=Ea*r/(Ra+r)
	I=Ea/(Ra+r)
	P=V*I
	
	return(np.float(P))
	
def pando(r,w):
	P1 = Pow(r,w)
	
	while(1):
		if(Pow(r+0.001,w)>P1):
			r=r+0.001
			P1=Pow(r,w)
		elif(Pow(r-0.001,w)>P1):
			r=r-0.001
			P1=Pow(r,w)
		else:	
			break
	return np.float(P1)			
	

P =list() #power
L =list() #Load
V =list() #Voltage
I =list() #Current 

with open('windspeed_20.txt') as w:
	k = np.asarray(w.readlines(),np.float)

with open('pressure.txt') as p:
	pr = np.asarray(p.readlines(),np.float)

with open('temp.txt') as t:
	te = np.asarray(t.readlines(),np.float)

with open('loaddata.txt') as load:
	ld = np.asarray(load.readlines(),np.float)

#FOR PLOTTING THE GRAPH AT W RPM
'''
for rl in range (0,5000):
	p = np.power((Ka*Kf*If*w[i]/(Ra+(rl/100))),2) * (rl/100)
	k.append(p)
	l.append(rl/100)
	
for rl in range (0,5000):
	v = Ka*Kf*If*w[i]/(Ra+(rl/100)) * (rl/100)
	i = Ka*Kf*If*w[i]/(Ra+(rl/100))
	V.append(v)
	I.append(i)
	
plt.figure(1)
plt.subplot(311)
plt.title("MPPT at Windspeed "+ str(w))
plt.ylabel("Power")
plt.xlabel("Load")
plt.plot(l,k)
plt.subplot(313)
plt.title("Voltage VS Current at "+ str(w))
plt.ylabel("Voltage")
plt.xlabel("Load")
plt.plot(I,V)
plt.show()
'''
#machine learning part 
#DATA WILL BE TRAINED CONTINUOUSLY TAKING THE DATA SET OF EVERY 2 HOUR DATA
#data containing the present trainset from 1st 125 minutes = 2 hour dataset



traindata =[[ 412.632],
 [ 334.656],
 [ 394.596],
 [ 465.552],
 [ 410.904],
 [ 412.452],
 [ 502.776],
 [ 527.292],
 [ 423.324],
 [ 547.596],
 [ 637.416],
 [ 625.752],
 [ 638.604],
 [ 675.972],
 [ 656.064],
 [ 763.308],
 [ 786.852],
 [ 662.112],
 [ 455.076],
 [ 575.388],
 [ 459.468],
 [ 683.784],
 [ 442.872],
 [ 582.444],
 [ 644.760]]



loaddata =[[ 14188.763],
 [  9332.886],
 [ 12975.500],
 [ 18061.555],
 [ 14070.174],
 [ 14176.387],
 [ 21065.308],
 [ 23169.737],
 [ 14933.600],
 [ 24988.448],
 [ 33858.263],
 [ 32630.463],
 [ 33984.589],
 [ 38078.178],
 [ 35868.331],
 [ 48553.258],
 [ 51594.672],
 [ 36532.691],
 [ 17257.847],
 [ 27589.279],
 [ 17592.570],
 [ 38963.379],
 [ 16344.634],
 [ 28270.084],
 [ 34642.954]]	


regr_1 = DecisionTreeRegressor(max_depth=2)
regr_1.fit(traindata, loaddata)
temp = regr_1.predict([770])

print temp
