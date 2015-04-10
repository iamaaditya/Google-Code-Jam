# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 15:42:54 2014

@author: aaditya prakash
"""

import math
import time
import numpy as np
import scipy as sc
from itertools import permutations
from itertools import combinations


def fun__(strIn):
    strOutput = []
    strList = strIn.split("\n")
    numT = int(strList[0])
    
    for i in range(numT):
        llIn = strList[i+1]
        res = Strategy(llIn)
        strOutput.append("Case #" + str(i+1) + ": " + str(res))
    
    fileOut = file("A-small-OUT.txt", "w")
    for item in strOutput:
        print>>fileOut, item
    fileOut.close()
    

inS = 'ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvzq'
outS = 'ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupqz'

#alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)]

dicConv = {}  
i=0
for c in inS:
    dicConv[c] = outS[i]
    i+=1
    
def Strategy(llIn):
    strO = ''
    for c in llIn:
        if c == ' ' : 
            strO += c
            continue
        else:
            strO += dicConv[c]
    return strO
    

fInput = file("A-small-practice.in", "r")
strIn = fInput.read()
timeStart = time.clock()

fun__(strIn)

print('Time (sec):' + str(time.clock() - timeStart))

