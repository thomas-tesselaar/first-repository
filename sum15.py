#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 22:00:27 2022

@author: thomastesselaar

This program prints out all 3x3 squares where the sum of all rows, cloumns, 
and diagonals are equal to 15.
"""

import numpy as np

arr = [[0, 0, 0], [0, 5, 0], [0, 0, 0]]



for i in range(2, 10, 2):
    arr[0][0] = i

    for j in range(1, 10, 2):
        if j == 5:
            continue
        arr[0][1] = j

        for k in range(2, 10, 2):
            if k in arr[0]:
                continue
            arr[0][2] = k
            
            if np.sum(arr[0]) != 15:
                continue
        
            for l in range(1, 10, 2):
                if (l in arr[0]):
                    continue
                arr[1][0] = l
    
                for n in range(1, 10, 2):
                    if (n in arr[0] or n in arr[1]):
                        continue
                    arr[1][2] = n
                    
                    if np.sum(arr[1]) != 15: 
                        continue
                    
                    for o in range(2, 10, 2):
                        if (o in arr[0] or o in arr[1]):
                            continue
                        arr[2][0] = o
                        
                        if (arr[0][0] + arr[1][0] + arr[2][0]) != 15: 
                            continue
            
                        for p in range(1, 10, 2):
                            if (p in arr[0] or p in arr[1] or p in arr[2]):
                                continue
                            arr[2][1] = p
                            
                            if (arr[0][1] + arr[1][1] + arr[2][1]) != 15: 
                                continue
                            
                            for q in range(2, 10, 2):
                                if (q in arr[0] or q in arr[1] or q in arr[2]) and q != arr[2][2]:
                                    continue
                                arr[2][2] = q
                                
                                if (arr[0][0] + arr[1][1] + arr[2][2]) != 15: 
                                    continue
                                
                                if (arr[0][2] + arr[1][1] + arr[2][0]) != 15: 
                                    continue
                    
                                print(str(arr[0][0]) + " " + str(arr[0][1]) + " " + str(arr[0][2]))
                                print(str(arr[1][0]) + " " + str(arr[1][1]) + " " + str(arr[1][2]))
                                print(str(arr[2][0]) + " " + str(arr[2][1]) + " " + str(arr[2][2]) + "\n")
                                
