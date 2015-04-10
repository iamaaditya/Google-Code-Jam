from __future__ import division
from itertools import combinations
from math import *
from sys import argv
from pickle import *

def IsPalindrome(n):
    s = str(n)
    return s==s[::-1]

def generate_list(l):
    """ solves equal sum for the given list l """
    sol = []
    for i in xrange(1, int(ceil(sqrt(10**14)))):
        if IsPalindrome(i) and IsPalindrome(i*i): sol.append(i*i)
    dump(sol, open('sol_large', 'wb'))
    return False 

def solve(A,B):
    """ returns the number of fair and square numbers in the range A to B, both inclusive """
    sol = load(open('sol_large','rb'))
    return len([i for i in sol if i >= A and i <= B])

def main():
    filename = 'input.in'
    if len(argv) > 1:
        filename = argv[1]

    with open(filename) as f:
        T = int( f.readline() )
        case_count = 0
        for i in xrange(T):
            case_count += 1
            A,B = map(int, f.readline().rstrip('\n').split(' '))
            ans = solve(A,B)
            print "Case #" + str(case_count) + ": " + str(ans)
    
main()
# generate_list(2)



