# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 15:51:19 2014

@author: aaditya prakash
"""

import time


def fun__(strIn):
    strOutput = []
    strList = strIn.split("\n")
    numT = int(strList[0])
    
    for i in range(numT):
        llIn = strList[i+1]
        res = Strategy(llIn)
        strOutput.append("Case #" + str(i+1) + ": " + str(res))
    
    fileOut = file("C-large-OUT3.txt", "w")
    for item in strOutput:
        print>>fileOut, item
    fileOut.close()
    
def Strategy(llIn):
    A, B = map(int, llIn.split(' '))
    count =0
    for n in xrange(A, B):
        s = str(n)
        #print 'n ', s        
        nLl = map(int, [s[i:]+s[:i] for i in xrange(len(s))])
        #print nLl
        #if(count > 10): break
        setL = set()
        for i in range(1,len(nLl)):
            if nLl[i]<= B and nLl[i] > n: 
                setL.update([nLl[i]])
        count += len(setL)
                #print '*******', n, nLl[i], B
#        for m in xrange(n+1, B+1):
#            if m in nLl:
#                print "*******", n,m, B
#                count += 1
    
    return count
    

fInput = file("C-large-practice.in", "r")
strIn = fInput.read()
timeStart = time.clock()

fun__(strIn)

#print Strategy('1 9')
#print Strategy('10 40')
#print Strategy('100 500')
#print Strategy('1111 2222')

print('Time (sec):' + str(time.clock() - timeStart))




