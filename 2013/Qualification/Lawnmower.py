from __future__ import division
from itertools import combinations
from sys import argv

def solve(lawn):
    """ solves equal sum for the given list l """
    y = 'YES'
    n = 'NO'

    for row in lawn:
        largest = max(row)
        indexes_smaller_than_largest = [i for i in xrange(len(row)) if row[i] < largest]
        for i in indexes_smaller_than_largest:
            colm = [row1[i] for row1 in lawn]
            if row[i] < max(colm): return n
    return y 
    

def main():
    filename = 'input.in'
    if len(argv) > 1:
        filename = argv[1]

    with open(filename) as f:
        N = int( f.readline() )
        case_count = 0
        for i in xrange(N):
            case_count += 1
            n, m = f.readline().rstrip('\n').split()
            lawn = []
            for i in xrange(int(n)):
                lawn.append(map(int, f.readline().rstrip('\n').split(' ')))
            ans = solve(lawn)
            print "Case #" + str(case_count) + ": " + str(ans)
    
main()
