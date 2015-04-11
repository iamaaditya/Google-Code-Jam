from __future__ import division
from itertools import combinations
from itertools import permutations
from itertools import product
from sys import argv
import sys
sys.setrecursionlimit(110000)

qt = {}
i = 'i'
j = 'j'
k = 'k'
a = '1'

qt[(a,a)] = (a, 1)
qt[(a,i)] = (i, 1)
qt[(a,j)] = (j, 1)
qt[(a,k)] = (k, 1)

qt[(i,a)] = (i, 1)
qt[(i,i)] = (a, -1)
qt[(i,j)] = (k, 1)
qt[(i,k)] = (j, -1)

qt[(j,a)] = (j, 1)
qt[(j,i)] = (k, -1)
qt[(j,j)] = (a, -1)
qt[(j,k)] = (i, 1)

qt[(k,a)] = (k, 1)
qt[(k,i)] = (j, 1)
qt[(k,j)] = (i, -1)
qt[(k,k)] = (a, -1)

red_sols = {}
def reduce(s):
    """ reduces the given string using the qt """
    # print len(s)
    global qt
    global red_sols
    if s in red_sols: return red_sols[s]
    if len(s) <= 1:
        return (s[0], 1)

    if len(s) <= 2:
        u, v = s[0], s[1]
        quv = qt[(u,v)]
        return quv[0], quv[1]

    base, sign = reduce(s[1:])
    # print base, sign
    red_sols[s[1:]] = (base,sign)
    result = qt[(s[0], base)]
    newbase = result[0]
    newsign = result[1]*sign

    return newbase, newsign

def simplify(w):
    for i in xrange(3):
        w = w.replace('ij', 'k')
        w = w.replace('ki', 'j')
        w = w.replace('jk', 'i')

        for pat in (['ikj', 'jik', 'kji']):
            w = w.replace(pat, '')
        # for pat in ['iiii', 'jjjj', 'kkkk']:
            # w = w.replace(pat,'')
        ls = ['ii', 'jj', 'kk']
        for pat in product(ls, ls):
            w = w.replace(''.join(pat), '')

    return w
# def solve(s):
    # print s
def solve(s):
    global red_sols
    global qt
    no = 'NO'
    yes = 'YES'
    sim_dic = {}
    i = 'i'
    j = 'j'
    k = 'k'
    a = '1'
    if len(s) < 3:
        return no
    if len(s) == 3:
        if s == 'ijk': return yes
        return no

    ct = (s[0], 1)
    all_i_indexes = []
    for i_index in xrange(1,len(s)-2):
        if ct[0] == i and ct[1] == 1:
            all_i_indexes.append(i_index-1)
        combine_c = qt[ct[0], s[i_index]]
        ct =(combine_c[0], ct[1]*combine_c[1])
    # print all_i_indexes

    print reduce('ji')
    et = (s[-1], 1)
    all_k_indexes = []
    for k_index in xrange(len(s)-2,1, -1):
        # print k_index, s[k_index], len(s)
        if et[0] == k and et[1] == 1:
            all_k_indexes.append(k_index+1)
        # combine_e = qt[et[0], s[k_index]]
        combine_e = qt[s[k_index],et[0]]
        # print s[k_index], k_index, et, combine_e[0], combine_e[1]*et[1]
        et =(combine_e[0], et[1]*combine_e[1])


    print all_i_indexes, all_k_indexes
    # ai = all_i_indexes[0]
    # ak = all_k_indexes[0]
    # print s[ai+1: ak-1]
    # print ai, ak

def solve_vs(s):
    global red_sols
    global qt
    no = 'NO'
    yes = 'YES'
    sim_dic = {}
    i = 'i'
    j = 'j'
    k = 'k'
    a = '1'
    if len(s) < 3:
        return no
    if len(s) == 3:
        if s == 'ijk': return yes
        return no

    ct = (0,0)
    dt = (0,0)
    et = (0,0)
    old_rem = 0
    rep_count = 0
    rep_list =set() 
    for i_index in xrange(len(s)-2):
        c = s[i_index]
        if i_index == 0:
            ct = (c, 1)
            # continue
        # if not (ct[0] == i and ct[1] == 1): 
            # combine = qt[ct[0], c]
            # ct =(combine[0], ct[1]*combine[1])
            # print ct
        if ct[0] == i and ct[1] == 1: 
            dt = (0,0)
            for j_index in xrange(i_index+1, len(s)- 1):
                # print i_index, j_index
                d = s[j_index]

                if j_index == i_index+1:
                    dt = (d,1)
                    # continue
                # if not (dt[0] == j and dt[1] == 1):
                #     combine = qt[dt[0], d]
                #     dt = (combine[0], dt[1]*combine[1])
                # else:
                # print ct, dt, i_index, j_index
                # print d, dt
                if dt[0] == j and dt[1] == 1:
                    # print s[:i_index+1], "*", s[i_index+1:j_index], "*", s[j_index:]
                    sim_str = s[j_index+1:]
                    # rem = ''
                    # if sim_str in sim_dic:
                        # rem =  sim_dic[sim_str]
                    # else:
                        # rem = simplify(sim_str)
                        # rem = sim_str
                        # sim_dic[sim_str] = rem
                    # if rem == 'kj' or rem =='jj' or rem == 'j' : continue
                    rem = sim_str
                    rep_list.add(simplify(rem))
                    if old_rem == len(rep_list): rep_count += 1
                    old_rem = len(rep_list)
                    # if rep_count > 90000: 
                        # print "HIT ***************************************"
                        # return no
                    rem = simplify(rem)
                    if rem:
                        et = reduce(rem)
                        # print rem, et
                        if et[0] == k and et[1] == 1:
                            return yes

                if j_index == i_index+1:
                    continue
                combine_d = qt[dt[0], d]
                dt = (combine_d[0], dt[1]*combine_d[1])
                # print "dt after", dt
        if i_index == 0: continue
        combine_c = qt[ct[0], c]
        ct =(combine_c[0], ct[1]*combine_c[1])
    return no


def s11olve_ols(s):
    global red_sols
    no = 'NO'
    yes = 'YES'

    i = 'i'
    j = 'j'
    k = 'k'
    a = '1'
    if len(s) < 3:
        return no
    if len(s) == 3:
        if s == 'ijk': return yes
        return no
    for m in xrange(1, len(s) -2 ):
        for n in xrange(m+1, len(s) ):
            
            x, y, z = s[:m],s[m:n], s[n:] 
            
            if len(x) == 1 and x[0] != i: continue
            if len(z) == 1 and z[0] != k: continue

            x = simplify(x)
            print x
            continue
            if len(x) == 1 and x[0] != i: continue
            
            # continue
            # print m, n , len(x), len(y), len(z)
            # print m, n
            # try:
            xr, yr , zr = 0,0,0
            if x in red_sols:
                xr = red_sols[x]
            else:
                red_sols[x] = xr
                xr = reduce(x)
            if xr != (i, 1) : continue 

            y = simplify(y)
            if len(y) == 1 and y[0] != j: continue
            if y in red_sols:
                yr = red_sols[y]
            else:
                yr = reduce(y)
                red_sols[y] = yr
            
            if yr != (j, 1) : continue

            z = simplify(z)
            if len(z) == 1 and z[0] != k: continue
            if z in red_sols:
                zr = red_sols[z]
            else:
                zr = reduce(z)
                red_sols[z] = zr
            if zr != (k, 1) : continue

            return yes
                # yr = reduce(y)
                # zr = reduce(z)
            # except:
                # print "returning form here"
                # return no
            # if xr == (i, 1) and yr == (j, 1) and zr == (k, 1): 
                # print xr, yr, zr
                # return yes

    return no 
    

def main():
    filename = 'input.in'
    if len(argv) > 1:
        filename = argv[1]

    with open(filename) as f:
        T = int( f.readline() )
        case_count = 0
        for i in xrange(T):
            case_count += 1
            L, X = f.readline().rstrip('\n').split(' ')
            st = f.readline().rstrip('\n')
            # print L, X, st[:5]
            if case_count == 5 : continue
            ans = solve(st*int(X))
            
            print "Case #" + str(case_count) + ": " + str(ans)
    
main()
# print solve('jijijijijiji')
# print solve('jkjjjkiijkjiiiikjkkiijkjjkijjkiiijijjijkjkiikjiiiikjkiikjjijijkijikkjijkkjjkjkkijijiiikiijkjijkjjkkjikjkkkkjjiikjkkkjijkjkiijkkjkjijikjkiiijkkkjkkjkkkikijkijkijijijjkkjkkkijjjkkiikiiiijkkkjkiikijkjkikjjjjkijjkkikkijjjkiiikijkjkjiijijjiiikjjkiijkkjikkkkkjiiiiikjkkkjiiikjikiikikkjkjiikiiiikiikjkkijjikiiijijjjjjjiikkiijikjjijiikjkijjkikjkjjjkijjijkjjjjjikjikikjikkjkjijkkjikjjijikijiikkjiikkkjiiiiikkikijijijjjijkjikkkjijjjjjkjijkikjiikkikikiikjkikijkkikjkkjijijjjjjjkjiijjiikjkkijkkjijkiijjiijjjjkkkikjjkjikikjijikjkjjjikijkjkkjkkjjijijjkkjkjikijjkjkijjjikkkikkikikijjkijijjkkkijjkikkjiijijijjiijkijijijikiijjkiijiiikijkjkkjkjijjijijikijiijijjkikjijiikiijkjkiikijkjikiijikkjkkikkjkikjkkkjjkiijkkkkjkjjijiikiijjiiijkkiijkkjkkkkjjijikikkjjkjjjjikjkkkkkkikkjkiiikikkjjjkkjjkjiijkjkkiikjjkjkijjiiijjkjkkjikijijjjkjijkkjijikjijkkijkkjikkkikjiikkkikjkiijikikikjkkjkjiiijkkkkijjikkijikjkikjjijijkkkjkjikjkjjkkjjkkijjikkkjiiikikikkkkikkjkkikkkkjjjkkkkjkijkkkjjiikkkkikijjjjiikjijkjjikkkjiikjijkijiikkkjkijjijiikjkijkjjiiiiiijiijkjjjjjjijkikkjkkkjikjkjjijkiiijijjkikiiijkkiiikkkikkkiijikjijjikikjiikkjijikkjjkijijkijkjkjiijiijkjkiiikkkjjjkjjkjkjjkjjikjijkkkkikjkjjjiiiikikjijjkjjjjkkkikkjkkikjijjkjkiiijjijkkiiikkjkiijjkjikjkkikkkjiiijkjjkkjjkkjjkikiiiikiiikikkkiiiiiiijijjkjkjjkkikkjjjjjiikjijiijkkkijijijkkjkijijiiikjkjkkjkjkijijkjijiikjjiikikikijijikjkjkjkjkiiiijiiikiikkijjkkjkijkkkkikikiiijijikkjjjjjiikkjiikkiijkiikkikjijjkkjiijiikjjijkkikikijkiikkijkkjjikjiijijjkjkiikjkkikiikkjiijkkkkiikikjkikjikiijkjikkkkjkjiijikikjkjikiijkiikiiikikjijjkiikikkkjjjkiijikijjjjikijkikjjkjijijijijiijkjikkiiikjkjkikikjjjkkkkkiiijjiiijkkkijikjkjjjkkjikjkjkijkijjkiikjijijjiiijikkikkjkikijjkjiiikiiijijijjikiikkijkjkkijiiijjjkikijkkikjikjijjkkjjjjjikjjkiikjjkjjkjjjiikiiikijkkikkkjiijiiijjjjkjjkijjkjjjikjiijkikjkiiikkjikikikjkkjkiiijkjjjjikjkiiijkikjkikjijjkikijkjikjiijjjikjjkikjjkjjkkkjkiijikkjjkjkiijijiijkkkikkjikkkjikikjijkikkkiiiikkkjjkiiikjkkijikijijjkkkijjikijikikjjkkjkkkkkijjiiikkijjiiikkkjjkikikjkkjjjkijkkkkkjiikkkjkkikjjjikjkiikikkjiikijjijkkikkkiijjjkkiikkjjkkjjiikkjijijkjikikjkijkiijjikkjkikijikikjjjkjikiijiikjkkiijijijkkkijkijijikjkkjkjjikkjkjkiiijkkkijkikkkiijjjjiijiiiikjjkjjiijjjkkjijjkikikkjjijijkikjjiikikiijkkijkjjikiiijkijiikkikiiijiijjjjijiikiikiikikkikiiiiijkjkijkijkikjkikijijkikjkkkikjkikjkiiiikkkkjkjjjikjkjijjijikijikiikjjkikjiikijkjkjjjkjiiiikijjjjjiijikjkijkkiikjjkkkkjkikijijjkijkikkiikijjikikkkiijjijjkkkikijiijkkjjkiijjikkjikjikiiikkkkiijiikikkkjjjkkkkiiiijiijjkiikjkkkjkkkiijjiikkijiiijkjjikkkkijiikkjkkjjjjkkijjijkjkkjjjijikjkkjjiijkjijkkikijkkkkikkikjjjjiiikijiikkjkjkkjkijkiijikikjijiikkiijkjjikjkiiikkjjkjjjjiijkikkkiijkjkikkijjkkkijkiiiijiijjiikkkkjjjkjjjjkikijjikkkkkjjikiikikkkkikiijiijikiijijkjjjikiikkikkkiijiikiiiikikkikijijjjjjjjkjkjkijikkikjkiijiiiikjkijjjkijjijkijjjiijkijkkkjjijijijkikikiikkkkijikjiijkijjkkkijkjkikkjkijjkjjikjjjikjjkkjkjjjijkkkijijijkjjiiijkkjkjkjijikiijkjjjjkjikjijkjkkjjkiiikjjkijkjkkjkjjkkkikjiikkkjkikikkikkkjkkiiiiikiikkkikijikkikikjkijjkkiikikkjiiikjijjiijijjjjkjjijkjjjijkkiiikkjkjkijijiikjijjjjjkjikkkjkjjkkikkijjikjkjjjikjjkikijiikjkkjjkjkkjjkijjiijjkjjiiiiikjkkjiikijjjjiikkiiiiijikjikijkiikkkkjjjijkjjkkiijjkiijjikiikjkjijkjkiikikjikjjkkijijikkiikkjjjiiijkiiijijjjikkikkiiikjjjijjikikjkkkiijkikjijiiiiijkkjijjkjiikkkjjkkjjjjkjkjiijkjijkjjjiiiijkkkiiiijjjkiijjiiiikkkjikijikjiikijjkkikkikijkkjjkkkiijjkjkjijijiikjkkikkikjijikkjikjkikkkikijjiijkkjkjjjjikkjkikkjijkjkjkjjkijikkkjkjkkkikikikjjjikkjikiikiikikikkjikjjjiijjkjikjijiiikjjkjijjiikjiiiijkjiikikkiijijikjkikijkjijkjkkkijjjikkjkikjijkkjjiiikijkijjijijjkikkkiikijjkikjjkikjkijijkjiikkjkikjiikkkkkjiijkikjiiijijijikkjjiiiiikiikjkkkijkijkjjjiijijjiijkjkkkkiiikjkjjkkkjijjijjkjkkkikiikjkkijijjiikkijjjjiikkkijkjjjijkjiiiiiikkijkiiikikiikjkjikjikjijijkkkjkijikikjijikkjijjkjjjkkijjjkkkjkjkijijjkikjiijkkkkkkiikkiikjikikjjkijkkiiijkkjkjjjjjjkkkjjiijkkikiikijkikjjkkjikiijiiiiiijjiiiijiikkkkkkiijikjjikjkjiiiikijjkkjikjiikiikjkkkkkjikiiijjjjkikkjjkjjiijkkjjkijkkjijkkiijjjjjjkkkkijjijjjjkkjkkjjkikkkjkkikkiijjjjjikkkjkkkkijjkkijijkjkijikjjikijiijjjikkkikkkjkiikjjkkkjkikjkjiiijjikkkkkkkjijjkkjijjjjiikjjjiiikkikikkjjjkijijiikkjkijiijijkijijikkkiikjijkkiiiijjiiiikkkkikjikjikjjiijijkkjjikijjiikjkijkkkikkijkijkikikiiiijjiikkjijkkkiikiikikkjkkjkkkiijkijkkjkjkjikiijjijkkiiiijijkiiiijijkjkjjjjkjkijkikkijjjkikiijikjkjiikjkijkkijiijjkijjjjjikkjkjiiijijjjkijjikjkkkjkkjjkkkkiijkijkkkjjijkjikkjiijjjjjkjjkkjijijikkjkijiijiiijkkjkkjiiijijkjjkkkjikjjkiiikijjiijkjiijiijjjkkjjiijjkjkkjjjkjkkjjjkikjjkikjiijjkikiijjiijjkkjkikikiiiijjkjjijjkiiijiijkkijkkkkiijjijijijkjjkkikijkkijijiiiijkjkijkkkiijjkijjkjjijiijjkikkijjjjjijijiiijijikkjkiijjkkjkjkjkkkikjikiiikjjiikiijikkjikikikijjjikikjjkkiikikkjiiiijkjiiijjjkjijkkijikiikikiikikjiiijjikkiijjijkjijijkkjiijiikkiiikjikkkijkkkjjijkjkjjikijjjikjjikikkikikjjjkkjkiikkiiikkkkjiijkjkiikjjikjijkkkijkkkiiikikijkkjjiikjjkkjjiijijiijjjjkkiikiiiijkiiikkijijjijkjkjkikjkkkjjijiijkijjjkiikkjkikjkkjjkjkjjjikkjijiijkjjiikkjjjkjikjiijjjikkkjijjkkjijiikkkkkkjkjiiikikikkiikjjijkijiiikkjikkkjjjijjjiiijikkiiijkjijjjijjikjjkikijjkiijkiikjkkjkkikkkkijkjiikjkkkjjkjjkiikikikjkjiijkjjiiikkkkjkjijiiiikjiikjkjijkjkikiijkkjiikikikiijiiikkkkjijijkjijikjjijijiijijiijjkkkiikijikjikjkjkiiijikijjijkjkkikikkjkkkikjkkkkjiiiiikikjkiiijkkiiijkjijkijiikkikijkikikikkjjjkiiikikkjijkjkjjjikjkjkjiijjikjjijkikiijkkjijiijjjikiijjkjiikijikjjkijikkkkjjjikjkjiijjkijkkkiijikjkikjijikikiijiijikkjjiikkiiijkjjkjijjikjijijkjjkkkkkkikijijikjikkjkjijjjijiiijiijiijijiijkjijkjkkjkkikijikjijiikiiiikkikkijjiijjjkkikkkikkjjijikkkkikjjjijkijkjkjiiiiiikikkijijjkijijjkkijjikjkjjkkjkjiikijjjikiiijkjjkjkijijijjjikijiijiiiijiiiikijjkjjkjkjjjjjjiijkijjikkikjijikkkijkkijijjjkijikkjkiiiikkikjkijikkijiijkijjjijkjjijijjkjkkjjjjikjikjjiijijjjkkjjijkjkikjjjjiikjikkjjjjjkjikkkijjijjjiiiikijjijjijiiiiikjjkijkijjjjkjkjkjkkkikiikkkjjijikijkjijikijiijkjijjjkkjiijiiikkkjikjjjkkkikiikiijjikjkikjijijkjkijijijkjjkjijjikikkjjiijkjikjikikiiikijkkjijkjjikkikjikjkjiikjijkkijikjjiiiijiijkijkjjkjijjjjkikjjkkjikjiikkiikikkiikijkikkjiiijijikijjijkjijkjijkjjjkikjikijjkjjjikkkijkkikijkkkjjkiiijikkjijjkkkjkkjiijjkikjjjkjijjjjikijjjjjjijjiiijkiijijkjkjkijjkjiikkiikikkkkjikjiijkkkjkijiijkjikjjikkjkjjkjkkiikikikkjkikijjiijjkkjjiikjkikkkjjkkiijkikjijjkikkjkijijjiikjikjijkkijkjiiikjkjkjjjkjkjjiijikiijikkjiikjijikkkkjjkjijjjjjijjijiijikkkkjikjkiikijjjkjjjkjkjijkkijkkjijikjiijijikkkjkkijkkikjkkjkkkkiiiikiijjjkkjikkjikkkkikijkkiikiijkijjiijikijkkijkiiikjikjkiiiikkikkkikjijijkijjikkkjjkkikkikikiijkkiijiiikiiiiiikkikjijkijjikkkjjkjiijjjjjkijkkkkkijjkjjijikjijijjikkkiiikkikkijkjkjjjkkkjjijikjkkikiiiijkiiikjkjjjijjkijjkjkiikjjikiikkkiijikijijkijjikkkjjkjkjkikjkkkkijkkkikijikkkjjkjjiiikkiijjiijkkkjjjjijkikiiikjiiiijkjkkjkjikkijjkikiiiikijkjijikjikijkkiikjkijkiijkkkkjjkkiikkjjkijkjikijiijjiijikkiiiijkjkijjkijjiiiikkjkjijkijiikikiijjikjkjiikjijkijjkjjjjiijkkijkjjijkijkiikkiiikkkiiijkkjjiijkjkkiikjkikjikijjiijijkkijkijjjikjjkijkjjkikiikkijkiijjijikkijjjjijkkkkiikiijjjjijkkjjkijkjijjjikjjiijjiiikkjkjijkikiikjijiikjjijkjijkjkikkikjikjiikkjjkiiiijkiikkjjiiikkjkkjkikjjikkjijjjjkjkkjkjiiiiijikkjjiiikiijjjkjjjjjiijikikjjjijiikiijikkjjiikiikjjjjkikjikjkiikkikkikiiiikikkjkijkkikikkijiiijjijikikkkjkikjiijjjijkiiijjkkikkkkiiiijikiijkjikkkiijijkjkkkjkkijkkkkkjikjjijkkkikjkjjjiiiijjkijkkikijkiijikikjkijjkjkiijkkijkikikiikjikjiikkjjikiiiiiijjkjjjikjkkjkjiikkkijijkkjjijjijkjkjjikijjiikjiikjiikkkikijiijkkikkkkiiijjkikijkijijikiijkjjikjkjikjkikjkjijkiikkikiiijjiiiijijijkkikjiiijikikijkkjjkkjkikjjikjkkiijjkjkjjkiikijjkkjkiiijjkjjjjjijijkjjjiikjijjijijiikjkjijiiiiijjjijjjikjkikkkkkiikjkiikjjjjijijijiijjjiijkikkkkjikjkjjjkkkkiikjiikijkijiijkjjkiijijijkjjjiijijkkkijjkkkiiijjjkjjjijjjkkkkiiijikkkjjijijkjkkkijikijjjkkiiijjikjijikiijkkijikkjiikijjjkijkijkjkkjijkkiikiijikjiijiikjjkjkjjikikikkiiiikkkkkkikkjjjiijjjikjjjkjijiikkijkikkkiijjkjkjjiikjjkiijkijijjjkjkkiikikjkjjiiiiijkjjkkkkjikjkiiijjiijjiijijkikkijkiijiikkiikkjiikjikjikjkjkikkjjikkjjjikkjkjiijkikjkijjkiiiikkkijkiijjkjijkkjjikjkjijjijjjkikiikjiiikjkjikjjjikkkikkikiijkjkkjkijjiiiijjkjjkkkiijiiikkjkijijkjjijkjjikkikkjkkjkkkiiiijjjikijikkjkkiiijjjjkjkjkijijkiiijjijkjkjjjjikjjiiijkkjkikikjjikjkjkjjjiijiijjjkjiikijjjijijkkiiikikjijikjkkkkjjkkjjjjjkkikkkijkkjkjijjkkkikikikikkiijjkjikjjikkkjijjijikijkkikkjiijkjkkjkkkkjiiijjijiikjjkiijkiikiikkikiijkjjkkijiiijkikjijkjiikkjjiijjkikjkkijiikikjjkkijjjjjjkjiijkjjjkjkkjjiiikiijjjikkiiijjiikikiiijkikikjjikkkkijjjjkijijjkiikijjkiijiijiiijkiikjkjijkiijijjjkkkikjkijikjiijikjijkkijikiiikiijijjjijkkikikkjijkjjjijikikkkiikikjikikkkikjikikijkikikjkjkkijkjiiijkijjkkkkjijikjikijkjkjiiijkiiikjkijjkikiikkkkkijijikiikikkjijkikikkjkiiiijjikijkjkkjijjikkiikkkjjkjjjkjijikiijjkjkjkjjijjjikkiikijijikjikjikiijjiikjjkikiikkikikiiikkjiijijjkikkikjjjkjiikjijkijiikjijjkikjijkijjjjiijijijjikiiiijjjikjjijiikjijijkkjkikijijjjikjkkjjijkiiikiiiikikkijkkjkikijkikkjjjikijkiijjkkjiikjjikijikjkkijjiiijjkkikkjiiiikjjkjkjiijkijjkkijiiijjikikkjiiijkjiiijikjkjikkijjkijkiijjijjjkjjjjkijikikjjkikkjjkikiijjkkjjkjiikikkjkikjjkjjkkjiiiikijjkikijjjiijiijikkijjiikikjkkiikjkkkjjkjijjikjjjikjjkikjjjkjjiiijijkjkiiikikikjkkkikjkijjijkiijjjijkkkikiikkijjiijkiijjikkjkijijkjiijkijijkkjkjjikiiiiikjkikkkkiikkiijkjkikkjkjjjiiijkjjkijkjjjkkkikjkkikiikjijjkjjjiikikijjkijkiikjkjkkikjiijkkkkkiiijiijjkijijijjjiijijkjijiikjjkiijjkkjkijjkiikikjjjijiijkjiijkkiikiijjjiikikkjijjjikkjjiikjikjikjjkkjiiiiikkkijkjiikiikiijijiiiiikkjikkkikijkjjiijjjkjkkkkkkijijkjjjkkikjkijjjkjkkiijiiiiijiijkikjkkkkjjijkjkkjijkjijiikkjkjjikkkiikiiijjkkjikjkiijiiiikjkkjjkiijkkjijiiikijjjikkjiiiikjiikijikijkjikkjkjkiiijiijiijkijkjkjijjijkijkjjkkiiiiijjjikkiiikkijkikjijikikjkiijijkjikkkjijjjjjiiiiijjjkjjkiikjjkjjkjiijiiiikiijkiijiikijkkjikikjikjkkjiikikkkiikjjjkiiikkkiijjkkikjjkjkjjkkkkkjkijiikjijiijjjiiijjiiiikjiijjkijkijjkkikjijkjikjijijkkjiiijjkkjijiikkijkiijkikkkijjjkkjkiijkjjikkkiikjijkijikikijjjjjiikkijijjjijkijkkkkiikjkikjjjikikiijjkjjijjiijkkjjiijkkkkkkkiijjikjkjkjkjjjjjjjkjiikiikijijijkjiijkikjijjiijikjjijikkikkjjjikjikkkkjjkjikjijjiikkkjjkjjijkjkkjjjjjikkijiikiiiiii')
# print solve('iijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijj')
# print simplify('iijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijjiijj')
# print simplify('jkjjjkiijkjiiiikjkkiijkjjkijjkiiijijjijkjkiikjiiiikjkiikjjijijkijikkjijkkjjkjkkijijiiikiijkjijkjjkkjikjkkkkjjiikjkkkjijkjkiijkkjkjijikjkiiijkkkjkkjkkkikijkijkijijijjkkjkkkijjjkkiikiiiijkkkjkiikijkjkikjjjjkijjkkikkijjjkiiikijkjkjiijijjiiikjjkiijkkjikkkkkjiiiiikjkkkjiiikjikiikikkjkjiikiiiikiikjkkijjikiiijijjjjjjiikkiijikjjijiikjkijjkikjkjjjkijjijkjjjjjikjikikjikkjkjijkkjikjjijikijiikkjiikkkjiiiiikkikijijijjjijkjikkkjijjjjjkjijkikjiikkikikiikjkikijkkikjkkjijijjjjjjkjiijjiikjkkijkkjijkiijjiijjjjkkkikjjkjikikjijikjkjjjikijkjkkjkkjjijijjkkjkjikijjkjkijjjikkkikkikikijjkijijjkkkijjkikkjiijijijjiijkijijijikiijjkiijiiikijkjkkjkjijjijijikijiijijjkikjijiikiijkjkiikijkjikiijikkjkkikkjkikjkkkjjkiijkkkkjkjjijiikiijjiiijkkiijkkjkkkkjjijikikkjjkjjjjikjkkkkkkikkjkiiikikkjjjkkjjkjiijkjkkiikjjkjkijjiiijjkjkkjikijijjjkjijkkjijikjijkkijkkjikkkikjiikkkikjkiijikikikjkkjkjiiijkkkkijjikkijikjkikjjijijkkkjkjikjkjjkkjjkkijjikkkjiiikikikkkkikkjkkikkkkjjjkkkkjkijkkkjjiikkkkikijjjjiikjijkjjikkkjiikjijkijiikkkjkijjijiikjkijkjjiiiiiijiijkjjjjjjijkikkjkkkjikjkjjijkiiijijjkikiiijkkiiikkkikkkiijikjijjikikjiikkjijikkjjkijijkijkjkjiijiijkjkiiikkkjjjkjjkjkjjkjjikjijkkkkikjkjjjiiiikikjijjkjjjjkkkikkjkkikjijjkjkiiijjijkkiiikkjkiijjkjikjkkikkkjiiijkjjkkjjkkjjkikiiiikiiikikkkiiiiiiijijjkjkjjkkikkjjjjjiikjijiijkkkijijijkkjkijijiiikjkjkkjkjkijijkjijiikjjiikikikijijikjkjkjkjkiiiijiiikiikkijjkkjkijkkkkikikiiijijikkjjjjjiikkjiikkiijkiikkikjijjkkjiijiikjjijkkikikijkiikkijkkjjikjiijijjkjkiikjkkikiikkjiijkkkkiikikjkikjikiijkjikkkkjkjiijikikjkjikiijkiikiiikikjijjkiikikkkjjjkiijikijjjjikijkikjjkjijijijijiijkjikkiiikjkjkikikjjjkkkkkiiijjiiijkkkijikjkjjjkkjikjkjkijkijjkiikjijijjiiijikkikkjkikijjkjiiikiiijijijjikiikkijkjkkijiiijjjkikijkkikjikjijjkkjjjjjikjjkiikjjkjjkjjjiikiiikijkkikkkjiijiiijjjjkjjkijjkjjjikjiijkikjkiiikkjikikikjkkjkiiijkjjjjikjkiiijkikjkikjijjkikijkjikjiijjjikjjkikjjkjjkkkjkiijikkjjkjkiijijiijkkkikkjikkkjikikjijkikkkiiiikkkjjkiiikjkkijikijijjkkkijjikijikikjjkkjkkkkkijjiiikkijjiiikkkjjkikikjkkjjjkijkkkkkjiikkkjkkikjjjikjkiikikkjiikijjijkkikkkiijjjkkiikkjjkkjjiikkjijijkjikikjkijkiijjikkjkikijikikjjjkjikiijiikjkkiijijijkkkijkijijikjkkjkjjikkjkjkiiijkkkijkikkkiijjjjiijiiiikjjkjjiijjjkkjijjkikikkjjijijkikjjiikikiijkkijkjjikiiijkijiikkikiiijiijjjjijiikiikiikikkikiiiiijkjkijkijkikjkikijijkikjkkkikjkikjkiiiikkkkjkjjjikjkjijjijikijikiikjjkikjiikijkjkjjjkjiiiikijjjjjiijikjkijkkiikjjkkkkjkikijijjkijkikkiikijjikikkkiijjijjkkkikijiijkkjjkiijjikkjikjikiiikkkkiijiikikkkjjjkkkkiiiijiijjkiikjkkkjkkkiijjiikkijiiijkjjikkkkijiikkjkkjjjjkkijjijkjkkjjjijikjkkjjiijkjijkkikijkkkkikkikjjjjiiikijiikkjkjkkjkijkiijikikjijiikkiijkjjikjkiiikkjjkjjjjiijkikkkiijkjkikkijjkkkijkiiiijiijjiikkkkjjjkjjjjkikijjikkkkkjjikiikikkkkikiijiijikiijijkjjjikiikkikkkiijiikiiiikikkikijijjjjjjjkjkjkijikkikjkiijiiiikjkijjjkijjijkijjjiijkijkkkjjijijijkikikiikkkkijikjiijkijjkkkijkjkikkjkijjkjjikjjjikjjkkjkjjjijkkkijijijkjjiiijkkjkjkjijikiijkjjjjkjikjijkjkkjjkiiikjjkijkjkkjkjjkkkikjiikkkjkikikkikkkjkkiiiiikiikkkikijikkikikjkijjkkiikikkjiiikjijjiijijjjjkjjijkjjjijkkiiikkjkjkijijiikjijjjjjkjikkkjkjjkkikkijjikjkjjjikjjkikijiikjkkjjkjkkjjkijjiijjkjjiiiiikjkkjiikijjjjiikkiiiiijikjikijkiikkkkjjjijkjjkkiijjkiijjikiikjkjijkjkiikikjikjjkkijijikkiikkjjjiiijkiiijijjjikkikkiiikjjjijjikikjkkkiijkikjijiiiiijkkjijjkjiikkkjjkkjjjjkjkjiijkjijkjjjiiiijkkkiiiijjjkiijjiiiikkkjikijikjiikijjkkikkikijkkjjkkkiijjkjkjijijiikjkkikkikjijikkjikjkikkkikijjiijkkjkjjjjikkjkikkjijkjkjkjjkijikkkjkjkkkikikikjjjikkjikiikiikikikkjikjjjiijjkjikjijiiikjjkjijjiikjiiiijkjiikikkiijijikjkikijkjijkjkkkijjjikkjkikjijkkjjiiikijkijjijijjkikkkiikijjkikjjkikjkijijkjiikkjkikjiikkkkkjiijkikjiiijijijikkjjiiiiikiikjkkkijkijkjjjiijijjiijkjkkkkiiikjkjjkkkjijjijjkjkkkikiikjkkijijjiikkijjjjiikkkijkjjjijkjiiiiiikkijkiiikikiikjkjikjikjijijkkkjkijikikjijikkjijjkjjjkkijjjkkkjkjkijijjkikjiijkkkkkkiikkiikjikikjjkijkkiiijkkjkjjjjjjkkkjjiijkkikiikijkikjjkkjikiijiiiiiijjiiiijiikkkkkkiijikjjikjkjiiiikijjkkjikjiikiikjkkkkkjikiiijjjjkikkjjkjjiijkkjjkijkkjijkkiijjjjjjkkkkijjijjjjkkjkkjjkikkkjkkikkiijjjjjikkkjkkkkijjkkijijkjkijikjjikijiijjjikkkikkkjkiikjjkkkjkikjkjiiijjikkkkkkkjijjkkjijjjjiikjjjiiikkikikkjjjkijijiikkjkijiijijkijijikkkiikjijkkiiiijjiiiikkkkikjikjikjjiijijkkjjikijjiikjkijkkkikkijkijkikikiiiijjiikkjijkkkiikiikikkjkkjkkkiijkijkkjkjkjikiijjijkkiiiijijkiiiijijkjkjjjjkjkijkikkijjjkikiijikjkjiikjkijkkijiijjkijjjjjikkjkjiiijijjjkijjikjkkkjkkjjkkkkiijkijkkkjjijkjikkjiijjjjjkjjkkjijijikkjkijiijiiijkkjkkjiiijijkjjkkkjikjjkiiikijjiijkjiijiijjjkkjjiijjkjkkjjjkjkkjjjkikjjkikjiijjkikiijjiijjkkjkikikiiiijjkjjijjkiiijiijkkijkkkkiijjijijijkjjkkikijkkijijiiiijkjkijkkkiijjkijjkjjijiijjkikkijjjjjijijiiijijikkjkiijjkkjkjkjkkkikjikiiikjjiikiijikkjikikikijjjikikjjkkiikikkjiiiijkjiiijjjkjijkkijikiikikiikikjiiijjikkiijjijkjijijkkjiijiikkiiikjikkkijkkkjjijkjkjjikijjjikjjikikkikikjjjkkjkiikkiiikkkkjiijkjkiikjjikjijkkkijkkkiiikikijkkjjiikjjkkjjiijijiijjjjkkiikiiiijkiiikkijijjijkjkjkikjkkkjjijiijkijjjkiikkjkikjkkjjkjkjjjikkjijiijkjjiikkjjjkjikjiijjjikkkjijjkkjijiikkkkkkjkjiiikikikkiikjjijkijiiikkjikkkjjjijjjiiijikkiiijkjijjjijjikjjkikijjkiijkiikjkkjkkikkkkijkjiikjkkkjjkjjkiikikikjkjiijkjjiiikkkkjkjijiiiikjiikjkjijkjkikiijkkjiikikikiijiiikkkkjijijkjijikjjijijiijijiijjkkkiikijikjikjkjkiiijikijjijkjkkikikkjkkkikjkkkkjiiiiikikjkiiijkkiiijkjijkijiikkikijkikikikkjjjkiiikikkjijkjkjjjikjkjkjiijjikjjijkikiijkkjijiijjjikiijjkjiikijikjjkijikkkkjjjikjkjiijjkijkkkiijikjkikjijikikiijiijikkjjiikkiiijkjjkjijjikjijijkjjkkkkkkikijijikjikkjkjijjjijiiijiijiijijiijkjijkjkkjkkikijikjijiikiiiikkikkijjiijjjkkikkkikkjjijikkkkikjjjijkijkjkjiiiiiikikkijijjkijijjkkijjikjkjjkkjkjiikijjjikiiijkjjkjkijijijjjikijiijiiiijiiiikijjkjjkjkjjjjjjiijkijjikkikjijikkkijkkijijjjkijikkjkiiiikkikjkijikkijiijkijjjijkjjijijjkjkkjjjjikjikjjiijijjjkkjjijkjkikjjjjiikjikkjjjjjkjikkkijjijjjiiiikijjijjijiiiiikjjkijkijjjjkjkjkjkkkikiikkkjjijikijkjijikijiijkjijjjkkjiijiiikkkjikjjjkkkikiikiijjikjkikjijijkjkijijijkjjkjijjikikkjjiijkjikjikikiiikijkkjijkjjikkikjikjkjiikjijkkijikjjiiiijiijkijkjjkjijjjjkikjjkkjikjiikkiikikkiikijkikkjiiijijikijjijkjijkjijkjjjkikjikijjkjjjikkkijkkikijkkkjjkiiijikkjijjkkkjkkjiijjkikjjjkjijjjjikijjjjjjijjiiijkiijijkjkjkijjkjiikkiikikkkkjikjiijkkkjkijiijkjikjjikkjkjjkjkkiikikikkjkikijjiijjkkjjiikjkikkkjjkkiijkikjijjkikkjkijijjiikjikjijkkijkjiiikjkjkjjjkjkjjiijikiijikkjiikjijikkkkjjkjijjjjjijjijiijikkkkjikjkiikijjjkjjjkjkjijkkijkkjijikjiijijikkkjkkijkkikjkkjkkkkiiiikiijjjkkjikkjikkkkikijkkiikiijkijjiijikijkkijkiiikjikjkiiiikkikkkikjijijkijjikkkjjkkikkikikiijkkiijiiikiiiiiikkikjijkijjikkkjjkjiijjjjjkijkkkkkijjkjjijikjijijjikkkiiikkikkijkjkjjjkkkjjijikjkkikiiiijkiiikjkjjjijjkijjkjkiikjjikiikkkiijikijijkijjikkkjjkjkjkikjkkkkijkkkikijikkkjjkjjiiikkiijjiijkkkjjjjijkikiiikjiiiijkjkkjkjikkijjkikiiiikijkjijikjikijkkiikjkijkiijkkkkjjkkiikkjjkijkjikijiijjiijikkiiiijkjkijjkijjiiiikkjkjijkijiikikiijjikjkjiikjijkijjkjjjjiijkkijkjjijkijkiikkiiikkkiiijkkjjiijkjkkiikjkikjikijjiijijkkijkijjjikjjkijkjjkikiikkijkiijjijikkijjjjijkkkkiikiijjjjijkkjjkijkjijjjikjjiijjiiikkjkjijkikiikjijiikjjijkjijkjkikkikjikjiikkjjkiiiijkiikkjjiiikkjkkjkikjjikkjijjjjkjkkjkjiiiiijikkjjiiikiijjjkjjjjjiijikikjjjijiikiijikkjjiikiikjjjjkikjikjkiikkikkikiiiikikkjkijkkikikkijiiijjijikikkkjkikjiijjjijkiiijjkkikkkkiiiijikiijkjikkkiijijkjkkkjkkijkkkkkjikjjijkkkikjkjjjiiiijjkijkkikijkiijikikjkijjkjkiijkkijkikikiikjikjiikkjjikiiiiiijjkjjjikjkkjkjiikkkijijkkjjijjijkjkjjikijjiikjiikjiikkkikijiijkkikkkkiiijjkikijkijijikiijkjjikjkjikjkikjkjijkiikkikiiijjiiiijijijkkikjiiijikikijkkjjkkjkikjjikjkkiijjkjkjjkiikijjkkjkiiijjkjjjjjijijkjjjiikjijjijijiikjkjijiiiiijjjijjjikjkikkkkkiikjkiikjjjjijijijiijjjiijkikkkkjikjkjjjkkkkiikjiikijkijiijkjjkiijijijkjjjiijijkkkijjkkkiiijjjkjjjijjjkkkkiiijikkkjjijijkjkkkijikijjjkkiiijjikjijikiijkkijikkjiikijjjkijkijkjkkjijkkiikiijikjiijiikjjkjkjjikikikkiiiikkkkkkikkjjjiijjjikjjjkjijiikkijkikkkiijjkjkjjiikjjkiijkijijjjkjkkiikikjkjjiiiiijkjjkkkkjikjkiiijjiijjiijijkikkijkiijiikkiikkjiikjikjikjkjkikkjjikkjjjikkjkjiijkikjkijjkiiiikkkijkiijjkjijkkjjikjkjijjijjjkikiikjiiikjkjikjjjikkkikkikiijkjkkjkijjiiiijjkjjkkkiijiiikkjkijijkjjijkjjikkikkjkkjkkkiiiijjjikijikkjkkiiijjjjkjkjkijijkiiijjijkjkjjjjikjjiiijkkjkikikjjikjkjkjjjiijiijjjkjiikijjjijijkkiiikikjijikjkkkkjjkkjjjjjkkikkkijkkjkjijjkkkikikikikkiijjkjikjjikkkjijjijikijkkikkjiijkjkkjkkkkjiiijjijiikjjkiijkiikiikkikiijkjjkkijiiijkikjijkjiikkjjiijjkikjkkijiikikjjkkijjjjjjkjiijkjjjkjkkjjiiikiijjjikkiiijjiikikiiijkikikjjikkkkijjjjkijijjkiikijjkiijiijiiijkiikjkjijkiijijjjkkkikjkijikjiijikjijkkijikiiikiijijjjijkkikikkjijkjjjijikikkkiikikjikikkkikjikikijkikikjkjkkijkjiiijkijjkkkkjijikjikijkjkjiiijkiiikjkijjkikiikkkkkijijikiikikkjijkikikkjkiiiijjikijkjkkjijjikkiikkkjjkjjjkjijikiijjkjkjkjjijjjikkiikijijikjikjikiijjiikjjkikiikkikikiiikkjiijijjkikkikjjjkjiikjijkijiikjijjkikjijkijjjjiijijijjikiiiijjjikjjijiikjijijkkjkikijijjjikjkkjjijkiiikiiiikikkijkkjkikijkikkjjjikijkiijjkkjiikjjikijikjkkijjiiijjkkikkjiiiikjjkjkjiijkijjkkijiiijjikikkjiiijkjiiijikjkjikkijjkijkiijjijjjkjjjjkijikikjjkikkjjkikiijjkkjjkjiikikkjkikjjkjjkkjiiiikijjkikijjjiijiijikkijjiikikjkkiikjkkkjjkjijjikjjjikjjkikjjjkjjiiijijkjkiiikikikjkkkikjkijjijkiijjjijkkkikiikkijjiijkiijjikkjkijijkjiijkijijkkjkjjikiiiiikjkikkkkiikkiijkjkikkjkjjjiiijkjjkijkjjjkkkikjkkikiikjijjkjjjiikikijjkijkiikjkjkkikjiijkkkkkiiijiijjkijijijjjiijijkjijiikjjkiijjkkjkijjkiikikjjjijiijkjiijkkiikiijjjiikikkjijjjikkjjiikjikjikjjkkjiiiiikkkijkjiikiikiijijiiiiikkjikkkikijkjjiijjjkjkkkkkkijijkjjjkkikjkijjjkjkkiijiiiiijiijkikjkkkkjjijkjkkjijkjijiikkjkjjikkkiikiiijjkkjikjkiijiiiikjkkjjkiijkkjijiiikijjjikkjiiiikjiikijikijkjikkjkjkiiijiijiijkijkjkjijjijkijkjjkkiiiiijjjikkiiikkijkikjijikikjkiijijkjikkkjijjjjjiiiiijjjkjjkiikjjkjjkjiijiiiikiijkiijiikijkkjikikjikjkkjiikikkkiikjjjkiiikkkiijjkkikjjkjkjjkkkkkjkijiikjijiijjjiiijjiiiikjiijjkijkijjkkikjijkjikjijijkkjiiijjkkjijiikkijkiijkikkkijjjkkjkiijkjjikkkiikjijkijikikijjjjjiikkijijjjijkijkkkkiikjkikjjjikikiijjkjjijjiijkkjjiijkkkkkkkiijjikjkjkjkjjjjjjjkjiikiikijijijkjiijkikjijjiijikjjijikkikkjjjikjikkkkjjkjikjijjiikkkjjkjjijkjkkjjjjjikkijiikiiiiii')
# solve('ijkj')
# solve('jijijijijiji')
# solve('abcdefghi')
# solve('jijijijijiji')
# print reduce('jik')
# print reduce('ik')


