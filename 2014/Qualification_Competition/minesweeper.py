# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 02:00:02 2014

@author: aaditya prakash
"""
from heapq import merge
from itertools import count

def Minesweeper(strInput):
    strList = strInput.split("\n")
    strOutput = []
    
    numT = int(strList[0])
    
    # for i in range(1,numT+1):
    #     R, C, M = map(int, strList[i].split(' '))
    #     print(R,C,M)
    #     if(M > (R*C)-4):
    #         strOutput[i] = "Impossible"
    #         continue
    #     MineSearch(R,C,M)
        
        

def MineSearch(R, C, M):
    print(R,C,M)    
    mine = np.zeros(shape=(R,C))
    i=1    
    for ll in printMatrixSpiral(R,C):
        lR, lC = ll
        mine[lR][lC]=i
        i +=1
    print(mine)


def printMatrixSpiral(width,height):
  """
  width: width of the matrix
  height: height of the matrix
  """
  result = []
  #special case
  if width is 0  or height is 0 : return result
  #calculate outer loop limit
  if height<width: minS = height
  else: minS=width
  if minS & 1 is 1: limit = minS/2
  else: limit = minS/2+1
  #calculate length 
  xlen=width-1
  ylen=height-1
  
  #outer loop
  for index in range(limit+1):
    i,j = index,index # init to coordinate of diagonal entry
    
    if xlen<0 or ylen<0: return result 
    if xlen == 0 and minS&1==1: 
      for jj in range(ylen+1):
        result.append((i,j+jj))
      return result
    if ylen ==0 and minS&1==1:
      for ii in range(xlen+1):
        result.append((i+ii,j))
      return result
      
    #turn right
    while(i<index+xlen):
      result.append((i,j))
      i+=1
    
    #turn down
    while j< index+ylen:
      result.append((i,j))
      j+=1
    
    #turn left
    while i>index:
      result.append((i,j))
      i-=1
 
    #turn up
    while j>index:
      result.append((i,j))
      j-=1
 
    #next spiral square 
    xlen-=2
    ylen-=2
  return result   
        
fInput = file("mine.txt", "r")
strInput = fInput.read()
Minesweeper(strInput)



