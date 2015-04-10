# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 19:15:02 2014

@author: aaditya prakash


"""

import numpy as np
import scipy as sc


def parseInput(strI):
    """ parses given input and returns the matrix """
    lin = strI.split('\n')
    numTests = int(lin[0])
    arr = np.zeros(shape=(numTests*2, 4,4))    
    choosenVal = []
    
    j=1 # j indicates the line number of the record
    for i in range(2*numTests):
        
        choosenVal.append(int(lin[j]))
        j += 1
        
        for k in range(4):
            arr[i][k] = lin[j].split(' ')
            j += 1
    return choosenVal, arr

def Magic(choosenVal, arr):
    strOutput = []
    
    for i in range(len(arr)/2):
        fVal = choosenVal[i*2]-1
        sVal = choosenVal[i*2 + 1] -1
        fMat = arr[i*2]
        sMat = arr[i*2+1]
        
        fRows = set(fMat[fVal])
        sRows = set(sMat[sVal])
        
        interRows =  fRows.intersection(sRows)

        lint = len(interRows)
        
        if(lint==0):
            strOutput.append("Case #" + str(i+1) + ": Volunteer cheated!")
        elif(lint==1):
            strOutput.append("Case #" + str(i+1) + ": " + str(int(list(interRows)[0])))
        else:
            strOutput.append("Case #" + str(i+1) + ": Bad magician!")
            
    fileOut = file("Magic_Out_small.txt", "w")
    for item in strOutput:
        print>>fileOut, item
    fileOut.close()
    

fInput = file("A-small.in", "r")
strInput = fInput.read()
choosenVal, arr = parseInput(strInput)

strOutput = Magic(choosenVal, arr)


        
    
        
       
    



