from __future__ import division
from itertools import combinations
from sys import argv

def solve(arg):
    base_combinations, opposing_bases, sequence = arg
    sol = []
    for base in sequence:
        sol.append(base)
        # first priority base combination
        for i,j in [(-1,-2), (-2,-1)]:
            if len(sol) <= 1 : continue
            if (sol[i], sol[j]) in base_combinations:
                new_base = base_combinations[(sol[i], sol[j])]
                del sol[-1] # remove the last element
                del sol[-1] # remove the second last element
                sol.append(new_base)

        # second priority opposing bases
        sol_set = set(sol)
        for opposing_base_set in opposing_bases:
            if not opposing_base_set - sol_set : sol = []
    return sol 

def get_data(ln):
    base_combinations = {}
    opposing_bases = []

    it =  iter(ln.split(' '))
    C = int( it.next() )
    for j in xrange(C):
        A, B, C= it.next()
        base_combinations[(A, B)] = C

    D = int( it.next() )
    for k in xrange(D):
        opposing_bases.append(set(it.next()))
    
    N = int( it.next() )
    sequence = list(it.next())
    
    return base_combinations, opposing_bases, sequence

def main():
    filename = 'input.in'
    if len(argv) > 1:
        filename = argv[1]

    with open(filename) as f:
        T = int( f.readline() )
        case_count = 0
        for i in xrange(T):
            case_count += 1
            ln = f.readline().rstrip('\n')
            ans = solve(get_data(ln))
            # print ans
            print "Case #" + str(case_count) + ": [" + str(', '.join(ans)) + "]"

def demo():
    base_combinations = {}
    opposing_bases = []

    base_combinations[('Q', 'F')] = 'T'
    opposing_bases.append(set(['Q', 'F']))

    sequence = ['F','A','Q','F','D','F','Q']

    print solve(base_combinations, opposing_bases, sequence)

main()
# get_data('2 EEZ AAB 2 QE ZY 7 QEEEERA')
# demo()


