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


    # KeysInHandCopy = copy(KeysInHand)
    # cdictCopy = copy(cdict)
    # return findKey(KeysInHandCopy, cdictCopy)
    # run this part of the loop for every number 
    print "*"*100, len(cdict)
    total_sol = []
    for chest_i in cdict:
        KeysInHandCopy = copy(KeysInHand)
        cdictCopy = copy(cdict)
        chest_i_key = cdictCopy[chest_i][0] 
        if chest_i_key not in KeysInHandCopy:
            continue
        KeysInHandCopy.remove(chest_i_key)
        _, new_keys = cdictCopy.pop(chest_i)
        KeysInHandCopy.extend(new_keys)
        for chest_j in cdictCopy:
            if chest_j == chest_i : continue
            chest_j_key = cdictCopy[chest_j][0] 
            if chest_j_key not in KeysInHandCopy:
                continue
            KeysInHandCopy.remove(chest_j_key)
            _, new_keys = cdictCopy.pop(chest_j)
            KeysInHandCopy.extend(new_keys)
            sols = findKey(copy(KeysInHandCopy),copy(cdictCopy))
            # if chest_i == 9: print chest_i, chest_j , KeysInHandCopy, sols
            # print chest_i, chest_j , len(sols)
            if not sols: break
            total_sol.append(chest_j)
        # print "*"*100
    
    # print total_sol
    if not sols: return im
    return sols

# sols = []    
def findKey(KeysInHand, cdict):
    # global sols
    # base case of the recursion
    if len(KeysInHand) == 1 and len(cdict) == 1 and KeysInHand[0] in [chest_keys for chest_keys, _ in cdict.values()]:
        return [cdict.keys()[0]]
    
    # there is another base case, where we get stuck in the wrong solution that is KeysInHand do not open any of the existing chest
    if not set(KeysInHand) & set([chest_keys for chest_keys, _ in  cdict.values()]): 
        return []

    # now the recursive step only way to make the loop run for every key in hand for every possible combination of the chest it opens is to have double loop
    for key in KeysInHand:
        chest = cdict.keys()
        for chest_i in chest:
            if chest_i in cdict and cdict[chest_i][0] != key: continue
            if key not in KeysInHand: continue
            if chest_i not in cdict: continue
            KeysInHandCopy = copy(KeysInHand)
            cdictCopy = copy(cdict)
            KeysInHandCopy.remove(key)
            new_keys = cdictCopy.pop(chest_i)[1]
            KeysInHandCopy.extend(new_keys)
            # before you proceed check if we are going to be stuck in the next chest , and if yes then avoid that chest and continue with other chest
            if not set(KeysInHandCopy) & set([chest_keys for chest_keys, _ in  cdictCopy.values()]): 
                continue
            KeysInHand.remove(key)
            new_keys = cdict.pop(chest_i)[1]
            KeysInHand.extend(new_keys)
            return [chest_i] + findKey(KeysInHand,cdict) 
    return []

def main():
    filename = 'input.in'
    if len(argv) > 1:
        filename = argv[1]

    with open(filename) as f:
        T = int( f.readline() )
        case_count = 0
        for i in xrange(T):
            # K N
            K, N = map(int, f.readline().rstrip('\n').split(' '))
            # K integers (type of keys you start with 
            Keys = map(int,  f.readline().rstrip('\n').split(' '))
            # N lines (each one chest)
            Chests = []
            for i in xrange(0,N):
                Chests.append(map(int,  f.readline().rstrip('\n').split(' ')))
                # Ti Ki (Ti = key needed to open the chest) (Ki = number of keys inside the chest) ....Ki integers... (type of keys contained)
            case_count += 1
            if case_count != 18: continue
            print K, N, Keys, Chests, "*"*30
            ans = solve(K,N,Keys, Chests)
            if ans != "IMPOSSIBLE":
                ans = ' '.join(map(str, ans))

            print "Case #" + str(case_count) + ": " + str(ans)
            # break
    
main()
