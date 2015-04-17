from __future__ import division
# import pudb; pu.db
from itertools import combinations
from sys import argv
from pprint import pprint
from copy import deepcopy
from itertools import product

def solve_Brue(N, L, initial, final):
    # Brute Force

    ini_lists_ori = []
    for i in initial.split(' '):
        ini_lists_ori.append(map(int, list(i)))
    fin_lists = []
    for j in final.split(' '):
        fin_lists.append(map(int, list(j)))
    fin_lists = sorted(fin_lists)
    
    sols  = []
    for flips in product((0,1), repeat=L):
        ini_lists = deepcopy(ini_lists_ori)
        for switch_index in xrange(L):
            if flips[switch_index]:
                for device_index in xrange(N):
                    ini_lists[device_index][switch_index] = 0 if ini_lists[device_index][switch_index] else 1
        if sorted(ini_lists) == fin_lists: 
            sols.append(sum(flips))

    if sols : return min(sols)
    return 'NOT POSSIBLE'
 
 
def solve(N, L, initial, final):
    # Faster solution (generating the flip bits instead of permuting all combinations 

    ini_lists_ori = []
    for i in initial.split(' '):
        ini_lists_ori.append(map(int, list(i)))
    fin_lists = []
    for j in final.split(' '):
        fin_lists.append(map(int, list(j)))
    fin_lists = sorted(fin_lists)
    
    sols  = []
    for device in ini_lists_ori:
        flips = []
        for i in xrange(L):
            if device[i] == fin_lists[0][i]: flips.append(0)
            else: flips.append(1)

        ini_lists = deepcopy(ini_lists_ori)
        for switch_index in xrange(L):
            if flips[switch_index]:
                for device_index in xrange(N):
                    ini_lists[device_index][switch_index] = 0 if ini_lists[device_index][switch_index] else 1
        if sorted(ini_lists) == fin_lists: 
            sols.append(sum(flips))

    if sols : return min(sols)
    return 'NOT POSSIBLE'
    
def main():
    filename = 'input.in'
    if len(argv) > 1:
        filename = argv[1]
    with open(filename) as f:
        T = int( f.readline() )
        case_count = 0
        for i in xrange(T):
            case_count += 1
            N, L  = map(int, f.readline().rstrip('\n').split(' '))
            initial = f.readline().rstrip('\n')
            final = f.readline().rstrip('\n')
            # if case_count != 91: continue
            ans = solve(N, L, initial, final)
            # print N, L, 
            print "Case #" + str(case_count) + ": " + str(ans)
    
def demo():
    # print solve(3,2, '01 11 10', '11 00 10')
    # print  solve(2,2, '01 10', '10 01')
    # print solve(2,3, '101 111', '010 001')
    print solve(3, 3, '111 110 100', '100 101 111')

# demo()
main()


