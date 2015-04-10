from __future__ import division
from itertools import combinations
from sys import argv

def solve(base_combinations, opposing_bases, sequence):

    sol = []
    for base in sequence:
        sol.append(base)
        # first priority base combination
        if len(sol) <= 1 : continue
        for i,j in [(-1,-2), (-2,-1)]:
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
    

def main():
    filename = 'input.in'
    if len(argv) > 1:
        filename = argv[1]

    with open(filename) as f:
        T = int( f.readline() )
        case_count = 0
        for i in xrange(T):
            case_count += 1
            l = f.readline().rstrip('\n')
            ans = solve(l)
            print "Case #" + str(case_count) + ": " + str(ans)

def demo():
    base_combinations = {}
    opposing_bases = []

    base_combinations[('Q', 'F')] = 'T'
    opposing_bases.append(set(['Q', 'F']))

    sequence = ['F','A','Q','F','D','F','Q']

    print solve(base_combinations, opposing_bases, sequence)

# main()
demo()


