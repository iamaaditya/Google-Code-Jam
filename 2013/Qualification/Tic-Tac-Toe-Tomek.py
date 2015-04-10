from __future__ import division
from itertools import combinations
from sys import argv

def solve(game):
    """ solves equal sum for the given list l """
    xw = 'X won'
    ow = 'O won'
    d = 'Draw'
    nc = 'Game has not completed'
    # check rows
    for line in game:
        if all([char in ['X','T'] for char in line]): return xw
        if all([char in ['O','T'] for char in line]): return ow
    # check column
    for i in xrange(0,4):
        colm =  [line[i] for line in game]
        if all([char in ['X','T'] for char in colm]): return xw
        if all([char in ['O','T'] for char in colm]): return ow

    # check left diagonal
    diagleft =  [ game[i][i] for i in xrange(0,4)]
    if all([char in ['X', 'T'] for char in diagleft]): return xw
    if all([char in ['O', 'T'] for char in diagleft]): return ow
    
    # check right diagonal
    diagright = [game[i][3-i] for i in xrange(0,4)]
    if all([char in ['X', 'T'] for char in diagright]): return xw
    if all([char in ['O', 'T'] for char in diagright]): return ow
        
    # check for uncomplete game
    if '.' in ''.join(game): return nc
    
    # else return draw
    return d 
    

def main():
    filename = 'input.in'
    if len(argv) > 1:
        filename = argv[1]

    with open(filename) as f:
        N = int( f.readline() )
        case_count = 0
        for i in xrange(N):
            case_count += 1
            game = []
            for i in xrange(0,4):
                game.append(f.readline().rstrip('\n'))
            f.readline() # this is the for empty line between the cases
            ans = solve(game)
            print "Case #" + str(case_count) + ": " + str(ans)
    
main()
