from __future__ import division
from itertools import combinations
from collections import OrderedDict
from copy import copy
from pprint import pprint 
from sys import argv

def solve(K, N, KeysInHand, Chests):
    """ solves Treasure chests for the given list l """
    im = "IMPOSSIBLE"
    cdict = OrderedDict()
    all_keys_inside = []
    key_to_chest = {}
    for i,c in enumerate( Chests ):
        # print i,c
        key_to_open = c[0]
        num_keys = c[1]
        keys_inside = []
        if num_keys:
            keys_inside = c[2:]
            all_keys_inside.extend(keys_inside)
        if key_to_open in key_to_chest:
            key_to_chest[key_to_open].append(i+1)
        else:
            key_to_chest[key_to_open] = [i+1]
        cdict[i+1] = (key_to_open, keys_inside)

    # if the number of keys inside and starting keys does not match the number of chests, solution impossible
    if len(KeysInHand) + len(all_keys_inside) < len(Chests): return im

    # another case of impossible is for every unique key there must be same number of chests that requires to open it and the total keys of that type
    total_keys = all_keys_inside + KeysInHand
    for u_key in key_to_chest.keys():
        # print ">u_key", u_key, total_keys.count(u_key), key_to_chest[u_key]
        if total_keys.count(u_key) < len(key_to_chest[u_key]): return im

    # order to open should be lexicographically small, so start with sorted list of the keys in hand
    # sol = []
    # for u_key in sorted(Keys):
    #     print u_key
    #     chests_to_open = key_to_chest[u_key]
    #     if len(chests_to_open) == 0: continue
    #     elif len(chests_to_open) <= Keys.count(u_key): 
    #         Keys.remove(u_key)
    #         sol.append(u_key)
    #         key_to_chest[u_key].remove(u_key)
    #     else:
    #         # this means a intelligent way has to be picked and not just brute force from top
    #         pass
    # print sol
    ## for key in KeysInHand:
        # chest = cdict.keys()
    # print findKey(KeysInHand, cdict)
    valid_sols = []
    KeysInHandCopy = copy(KeysInHand)
    cdictCopy = copy(cdict)
    for key in KeysInHandCopy:
        chest = cdictCopy.keys()
        for chest_i in chest:
            if cdictCopy[chest_i][0] != key:
                continue
            # print key
            # print KeysInHandCopy
            KeysInHandCopy.remove(key)
            new_keys = cdictCopy.pop(chest_i)[1]
            KeysInHandCopy.extend(new_keys)
            # print "KeysInHandCopy::", KeysInHandCopy
            sol = []
            sol.append(chest_i)
            # sol.extend(
            sol.extend(map(int, findKey(KeysInHandCopy, cdictCopy).split(' ')[:-1]))
            # sol = str(chest_i) + " " + str(findKey(KeysInHandCopy, cdictCopy))
            # print sol
            if len(set(sol)) == len(cdict): valid_sols.append(sol)
            KeysInHandCopy = copy(KeysInHand)
            cdictCopy = copy(cdict)
    return sorted(valid_sols)[0]
    
def findKey(KeysInHand, cdict):
    # print KeysInHand
    # print "*"*200
    # print cdict
    # print "*"*200
    # print cdict.keys()
    # print key_to_chest

    # base case of the recursion
    if len(KeysInHand) == 1 and len(cdict) == 1 and KeysInHand[0] in cdict:
        if KeysInHand:
            return str(KeysInHand)
    
    # there is another base case, where we get stuck in the wrong solution that is KeysInHand do not open any of the existing chest
    # if not all([key in cdict.values()[0] for key in KeysInHand]):
        # print "retruning from second base case", KeysInHand, cdict, "Keys:", cdict.keys()
        # return '' # return empty
        # perhaps this is not required

    # now the recursive step
    # only way to make the loop run for every key in hand for every possible combination of the chest it opens is to have double loop
    for key in KeysInHand:
        # print "entering loop"
        chest = cdict.keys()
        for chest_i in chest:
            if cdict[chest_i][0] != key:
                continue
            KeysInHand.remove(key)
            new_keys = cdict.pop(chest_i)[1]
            KeysInHand.extend(new_keys)
            # print "KeysInHand", KeysInHand
            return str(chest_i) + " " + str(findKey(KeysInHand, cdict))
    return ''

def main():
    filename = 'input.in'
    if len(argv) > 1:
        filename = argv[1]

    with open(filename) as f:
        T = int( f.readline() )
        case_count = 0
        for i in xrange(T):
            # K N
            # K integers (type of keys you start with 
            # N lines (each one chest)
                # Ti Ki (Ti = key needed to open the chest) (Ki = number of keys inside the chest) ....Ki integers... (type of keys contained)
            case_count += 1
            l = f.readline().rstrip('\n')
            ans = solve(l)
            print "Case #" + str(case_count) + ": " + str(ans)
    
# main()
def demo():
    K = 1 # number of keys you start with
    N = 4 # number of chest needed to be opened
    Keys = [1]
    # Chests = [[1,0], [1,2,1,3], [2,0], [3,1,2], [1,0]] # more chests than keys
    # Chests = [[1,0], [1,2,1,3], [2,0], [3,1,1]] # mismatch for the u-key 2, where the number of total keys is not the same as the number of chests required to open using that key
    Chests = [[1,0], [1,2,1,3], [2,0], [3,1,2]]
    print solve(K,N,Keys, Chests)

demo()



