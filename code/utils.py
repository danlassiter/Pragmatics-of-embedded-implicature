#!/usr/bin/env python

import itertools
import numpy as np
import matplotlib

######################################################################

NULL = 'NULL'

COLORS = matplotlib.colors.cnames.values()

colors = ['#1B9E77', '#D95F02', '#7570B3', '#E7298A', '#66A61E', '#E6AB02', '#A6761D', '#666666']

PROB_LIMS = [0, 1.1]
LIKERT_LIMS = [0, 8]
PROB_AXIS_TICKS = np.arange(0.0, 1.1, 0.1)
LIKERT_AXIS_TICKS = np.arange(0.0, 8.0, 1.0)

def rownorm(mat):
    """Row normalization of a matrix"""
    return np.divide(mat.T, np.sum(mat, axis=1)).T
    
def colnorm(mat):
    """Column normalization of a matrix"""    
    return np.divide(mat, np.sum(mat, axis=0))

def safelog(vals):           
    with np.errstate(divide='ignore'):
        return np.log(vals)

def display_matrix(mat, display=True, rnames=None, cnames=None, title='', digits=4):
    """Utility function for displaying strategies to standard output.
    The display parameter saves a lot of conditionals in the important code"""
    if display:
        mat = np.round(mat, digits)
        rowlabelwidth = 2 + max([len(x) for x in rnames+cnames] + [digits+2])
        cwidth = 2 + max([len(x) for x in cnames] + [digits+2])
        # Divider bar of the appropriate width:
        print "-" * (cwidth * (max(len(cnames), len(rnames)) + 1))
        print title
        # Matrix with even-width columns wide enough for the data:
        print ''.rjust(rowlabelwidth) + "".join([str(s).rjust(cwidth) for s in cnames])        
        for i in range(mat.shape[0]):  
            print str(rnames[i]).rjust(rowlabelwidth) + "".join(str(x).rjust(cwidth) for x in mat[i, :])    

def powerset(x, minsize=0, maxsize=None):
    result = []
    if maxsize == None: maxsize = len(x)
    for i in range(minsize, maxsize+1):
        for val in itertools.combinations(x, i):
            result.append(list(val))
    return result

def mse(x, y):
    err = np.sqrt(np.sum((x-y)**2)/len(x))
    return err

