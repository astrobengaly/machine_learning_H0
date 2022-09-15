#!/usr/bin/env python
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
import sys as sys

import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

# ML algorithm to be deployed
alg=sys.argv[1]

# sighz/hz value
sig=float(sys.argv[2])

# gcv value (true or false, if GridSearchValue() was deployed or not)
gcv=sys.argv[3]

zmin=float(sys.argv[4])
zmax=float(sys.argv[5])

# Creating functions that calculates mean, standard deviation and bias-variance tradeoff (BVT) of the H0 results
def calc_mean(x):
    return np.mean(x)

def calc_std(x):
    return np.std(x)

# BVT definition: (x-mu)**2 + sig**2.
def calc_mse(x,mu,sig):
    return (x-mu)**2 + sig**2.

# creating array that will receive stat results
meanres_arr = []

# number of Nz values to be analysed
nz_values = [20,30,50,80]

# Fiducial H0 value
h_ref = 67.36

# looping through nz
for nz in nz_values:

    if sig < 0.01:

        filename = 'results_sklearn_sigh0p00'+str(int(sig*1000))+'_'+str(nz)+'pts_h0p'+str(int(h0*100))+'_'+alg+'_zmin'+str(int(zmin*100))+'_zmax'+str(int(zmax*100))+'_GCV'

    if sig >= 0.01:
        
        filename = 'results_sklearn_sigh0p0'+str(int(sig*100))+'_'+str(nz)+'pts_h0p'+str(int(h0*100))+'_'+alg+'_zmin'+str(int(zmin*100))+'_zmax'+str(int(zmax*100))+'_GCV'

    # loading results
    (h,sctrain,sctest) = np.loadtxt(filename+'.dat',unpack='true')
    
    # printing stats results (mean, std deviation and BVT) of the H0 measurements from simulations - can also be done for sctrain and sctest
    print(alg, gcv, nz, zmin, zmax, "%.5f" % sig, "%.5f" % calc_mean(h), "%.5f" % calc_std(h), "%.5f" calc_bvt(calc_mean(h),h_ref,calc_std(h)))

    # appending results
    meanres_arr.append([nz, calc_mean(h), calc_std(h), calc_bvt(calc_mean(h),h_ref,calc_std(h))])

# creating a numpy array with the appended results
meanres_arr = np.array(meanres_arr)

# saving results in a text file
if sig < 0.01:  
    np.savetxt('mean_results_sigh0p00'+str(int(sig*1000))+'_'+str(alg)+'_GCV'+gcv+'_zmin'+str(int(zmin*100))+'_zmax'+str(int(zmax*100))+'.dat', meanres_arr)
else:
    np.savetxt('mean_results_sigh0p0'+str(int(sig*100))+'_'+str(alg)+'_GCV'+gcv+'_zmin'+str(int(zmin*100))+'_zmax'+str(int(zmax*100))+'.dat', meanres_arr)
