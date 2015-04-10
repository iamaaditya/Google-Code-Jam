# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 20:45:13 2014

@author: aaditya prakash
"""

import math
import time



def CookieGame(strInput):
    
    strList = strInput.split("\n")
    
    strOutput = []
    
    numT = int(strList[0])
    
    for i in range(numT):
        llIn = strList[i+1].split(' ')
        res = Strategy(llIn)
        strOutput.append("Case #" + str(i+1) + ": " + str(res))
    
    fileOut = file("cookie_Out1.txt", "w")
    for item in strOutput:
        print>>fileOut, item
    fileOut.close()
    
    
def Strategy(llIn):
    """ Returns the best strategy for given values of C F X in a list """
    C = float(llIn[0])
    F = float(llIn[1])
    X = float(llIn[2])
    
    #print(C,F,X)
            
    totalTime = 0
    cRate = 2
    prevBestTime = X/cRate
    
    if(X <= C/cRate): return prevBestTime
    
    
    while True:
        time = C/cRate
        totalTime += time
        cRate += F
        withThisRate = X/cRate
        bestTime = totalTime + withThisRate
        if(bestTime >= prevBestTime): return prevBestTime
        prevBestTime = bestTime
        
    
fInput = file("B-small-attempt0.in", "r")
strInput = fInput.read()
CookieGame(strInput)



