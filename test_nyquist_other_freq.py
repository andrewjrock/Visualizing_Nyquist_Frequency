# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 15:21:01 2021

@author: arock
"""

import numpy as np
import matplotlib.pyplot as plt
import os



cwd = os.getcwd().replace('//','/')+'/'

if not os.path.isdir(cwd+'Nyquist'):
    os.mkdir(cwd+'Nyquist')

#natrual frequency = 44.35
nf=44.35


#simulate 1 seconds
duration = 1

for hz in [44,45, 88,89, 100, 500, 1000, 10000]:
    
    truthpoints = 10000*duration+1
    truthtimes = np.linspace(0,duration,truthpoints)
    truthmeasurements = [np.sin(nf*2*np.pi*i) for i in truthtimes]
    points = duration*hz+1
    times = np.linspace(0,duration,points)
    measurements = [np.sin(nf*2*np.pi*i) for i in times]
    fig, ax = plt.subplots(figsize=(12,8))

    plt.plot(times,measurements,color='k',linestyle='dashed', marker='o',markersize=4)
    plt.plot(truthtimes, truthmeasurements, alpha = 0.3)
    plt.title("Natural Frequency sampled at {} Hz with Actual Frequency".format(hz))
    fig.savefig(cwd+"Nyquist/"+"Natural_Frequency_at_"+str(hz)+"_with_Frequency"+'.png',dpi=200)
    plt.close('all')


