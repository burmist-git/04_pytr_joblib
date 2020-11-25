#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Date        : Sun Nov 22 13:38:47 CET 2020
Autor       : Leonid Burmistrov
Description : Simple reminder-training example joblib.
'''

import numpy as np
import time
from joblib import Parallel, delayed

def main():
    np_arr = np.array([])
    #fill_np_arr_in_one_shot(np_arr)
    #fill_np_arr_for(np_arr)
    #fill_np_arr_append(np_arr)
    fill_np_arr_for_Parallel(np_arr)
    
def fill_np_arr_for_Parallel(np_arr):
    tic = time.time()
    np_arr = Parallel(n_jobs=njobs)(delayed(fill_np_arr_random)(np_arr) for _ in range(0,njobs))
    toc = time.time()
    print(type(np_arr))
    print(type(np_arr[0]))
    print(len(np_arr[0]))
    print(np_arr[0])
    print('{} {:.2f} s'.format(len(np_arr),toc - tic))
    time.sleep(3)

def fill_np_arr_for(np_arr):
    tic = time.time()
    for _ in range(0,njobs):
        np_arr = fill_np_arr_random(np_arr=np_arr)
    toc = time.time()
    print('{} {:.2f} s'.format(len(np_arr),toc - tic))
    time.sleep(3)

def fill_np_arr_random(np_arr):
    return np.append(np_arr, np.random.random(size=(n_per_job,)))

def fill_np_arr_append(np_arr):
    tic = time.time()
    np_arr=np.append([],
              [np.random.random(size=(n_per_job,)),
               np.random.random(size=(n_per_job,)),
               np.random.random(size=(n_per_job,)),
               np.random.random(size=(n_per_job,)),
               np.random.random(size=(n_per_job,)),
               np.random.random(size=(n_per_job,))])
    toc = time.time()
    print('{} {:.2f} s'.format(len(np_arr),toc - tic))
    time.sleep(3)

def fill_np_arr_in_one_shot(np_arr):
    tic = time.time()
    np_arr=np.random.random(size=(n_per_job*njobs,))
    toc = time.time()
    print('{} {:.2f} s'.format(len(np_arr),toc - tic))
    time.sleep(3)
    
def slow_mean(data, sl):
    return data[sl].mean()
    
def printDf(data,sl):
    print(sl)
    print(len(data[sl]))
    print(data[sl])

njobs=8
#n_per_job=int(6.4e7)
n_per_job=int(1e5)
    
if __name__ == "__main__":
    main()
