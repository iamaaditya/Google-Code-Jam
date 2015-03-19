from __future__ import division
from itertools import combinations
from sys import argv

def solve(l):
    """ solves equal sum for the given list l """

    return False 
    

def main():
    filename = 'input.in'
    if len(argv) > 1:
        filename = argv[1]

    with open(filename) as f:
        N = int( f.readline() )
        case_count = 0
        for i in xrange(N):
            case_count += 1
            l = f.readline().rstrip()
            ans = solve(l)
            print "Case #" + str(case_count) + ": " + str(ans)
    
main()


