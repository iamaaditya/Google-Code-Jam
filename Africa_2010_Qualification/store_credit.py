from itertools import combinations
from sys import argv

def solve(C, I, P):
    """ solves equal sum for the given list l """
    for i, p in enumerate(P):
        if C-p in P[i+1:]:
            return P.index(p)+1, P[i+1:].index(C-p) + i + 2
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
            C = int( f.readline() )
            I = int( f.readline() )
            P = map(int, f.readline().split(" ") )

            a,b = solve(C, I, P)
            print "Case #" + str(case_count) + ": " + str(a) + " " + str(b)
    
main()
