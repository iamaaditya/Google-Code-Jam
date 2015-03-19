from __future__ import division
from itertools import combinations
from sys import argv
from string import ascii_lowercase

def map_letters():
    dic = {}
    dic['a'] = ('2',1)
    dic['b'] = ('2',2)
    dic['c'] = ('2',3)

    dic['d'] = ('3',1)
    dic['e'] = ('3',2)
    dic['f'] = ('3',3)

    dic['g'] = ('4',1)
    dic['h'] = ('4',2)
    dic['i'] = ('4',3)

    dic['j'] = ('5',1)
    dic['k'] = ('5',2)
    dic['l'] = ('5',3)

    dic['m'] = ('6',1)
    dic['n'] = ('6',2)
    dic['o'] = ('6',3)
    
    dic['p'] = ('7',1)
    dic['q'] = ('7',2)
    dic['r'] = ('7',3)
    dic['s'] = ('7',4)
    
    dic['t'] = ('8',1)
    dic['u'] = ('8',2)
    dic['v'] = ('8',3)

    dic['w'] = ('9',1)
    dic['x'] = ('9',2)
    dic['y'] = ('9',3)
    dic['z'] = ('9',4)

    dic[' '] = ('0',1)

    return dic
    
def solve(l,dic):
    """ solves equal sum for the given list l """
    
    ans = []
    prev_number = -1
    number_string = ''
    for c in l:
        number, times = dic[c]
        if prev_number == number:
            number_string += ' '
        number_string += number*times 
        prev_number = number
    return number_string.strip()
    

def main():
    filename = 'input.in'
    if len(argv) > 1:
        filename = argv[1]
    dic = map_letters()
    with open(filename) as f:
        N = int( f.readline() )
        case_count = 0
        for i in xrange(N):
            case_count += 1
            l = f.readline().rstrip('\n')
            ans = solve(l,dic)
            print "Case #" + str(case_count) + ": " + str(ans)
    
main()


