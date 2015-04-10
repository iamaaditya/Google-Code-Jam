# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 00:22:59 2014

@author: aaditya prakash
"""


def WarGame(strInput):
    
    strList = strInput.split("\n")
    
    strOutput = []
    
    numT = int(strList[0])
    
    for i in range(numT):
        t = float(strList[3*i+1])    
        llNao = strList[3*i+2].split(' ')
        llKen = strList[3*i+3].split(' ')
        
        llNao1 = map(float, llNao)
        llKen1 = map(float, llKen)
        llNao2 = map(float, llNao)
        llKen2 = map(float, llKen)
        
        resWar = WarStrategy(llNao1, llKen1)
        resDeceit = DeceitfulWarStrategy(llNao2, llKen2)
        
        strOutput.append("Case #" + str(i+1) + ": " + str(resDeceit) + " " + str(resWar))
        
    fileOut = file("war_Out_large.txt", "w")
    for item in strOutput:
        print>>fileOut, item
    fileOut.close()
        
def StrategyKen(llKen, Nao):
    """ given his own weights and naomi's current weights returns Ken's o/p"""
    mx = max(llKen)
    mn = min(llKen)
    
    if Nao > mx: 
        return mn
    play=1
    for l in llKen:
        if(l > Nao): play = min(play, l)
    return play
    
def StrategyNaoWar(llNao):
    """ return Naomi's fair play strategy """
    return max(llNao)
    
def WarStrategy(llNao, llKen):
    scoreNao = 0
    
    while len(llNao) > 0:
        naoPlay = StrategyNaoWar(llNao)
        llNao.remove(naoPlay)
        
        kenPlay = StrategyKen(llKen, naoPlay)
        llKen.remove(kenPlay)
        
        if(naoPlay > kenPlay): scoreNao += 1
    return scoreNao

def StrategyNaoDeceit(llNao, llKen):
    mxNao = max(llNao)
    mnNao = min(llNao)
    
    mxKen = max(llKen)
    mnKen = min(llKen)
    
    say = mxNao
    
    if(mxNao > mxKen):
        play=1
        for l in llNao:
            if(l > mnKen): play = min(play, l)
    else:
        play = mnNao
    return say, play
        
def DeceitfulWarStrategy(llNao, llKen):
    scoreNao = 0
    scoreKen = 0
    while len(llNao) > 0:
        naoSay, naoPlay = StrategyNaoDeceit(llNao, llKen)
        llNao.remove(naoPlay)
        
        kenPlay = StrategyKen(llKen, naoSay)
        llKen.remove(kenPlay)
        
        if(naoPlay > kenPlay): scoreNao += 1
    return scoreNao

fInput = file("D-large.in", "r")
strInput = fInput.read()
WarGame(strInput)
