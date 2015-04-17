from __future__ import division
from math import ceil
from math import floor
from itertools import product
from copy import copy
from sys import argv

def solve_first_attempt_errors(l):
    l.sort(reverse=True)
    if max(l) <= 3:
        return max(l)

    if len(l) <= 1:
        return 1 + solve([int(ceil(l[0]/2)), int(floor(l[0]/2))])
    
    remaining_time = solve(l[1:])
    # decide if special minute or no special minute
    # time_without = remaining_time + max(0, l[0] - remaining_time)
    time_without = l[0]
    new_list = []
    new_list.extend(l[1:])
    new_list.append(int(ceil(l[0]/2)))
    new_list.append(int(floor(l[0]/2)))
    new_list.sort(reverse=True)
    time_with = 1 + solve(new_list)

    return min(time_with, time_without) 

def solution_second_attempt(l):
    sol = max(l)
    for i in xrange(1, max(l)+1):
        time_count = i + sum([int(ceil(diner/i)) -1 for diner in l if diner > i])
        print i, time_count, time_count - i , sol
        sol = min(sol, time_count)
    return sol

def main():
    filename = 'Binput.in'
    if len(argv) > 1:
        filename = argv[1]

    with open(filename) as f:
        T = int( f.readline() )
        case_count = 0
        for i in xrange(T):
            case_count += 1
            d = f.readline().rstrip('\n')
            l = f.readline().rstrip('\n')
            lin = map(int, l.split(' '))
            ans = solution_second_attempt(lin)
            print "Case #" + str(case_count) + ": " + str(ans)
    
main()
