# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:33:39 2019

@author: Deepti Ravishyam
"""



l=[5, 1, 3, 2, 4 ]

def wave(list):
       # Bubble sort
       for i in range(len(list)):
              for j in range(len(list)-i-1):
                     if list[j+1]<list[j]:
                            list[j],list[j+1]=list[j+1],list[j]
                            
       # Or just use A.sort()
                     
       print (list)
       
       for j in range(0,len(list)-1,2):
              list[j],list[j+1]=list[j+1],list[j]
       
       print (list)


wave(l)