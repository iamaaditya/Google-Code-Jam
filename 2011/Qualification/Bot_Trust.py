from __future__ import division
from collections import deque
from sys import argv

def solve(moves):
    current_position = {'B':1, 'O':1}
    last_moved = {'B':0, 'O':0}
    time_taken =0   
    for move in moves:
        bot, pos = move
        # print bot, pos, 
        distance = abs(current_position[bot] - pos)

        # if things weres simple, the time_taken would be equal to the number of button presses and the distance i.e
        # time_taken = 1 + distance
        # but since we can move while the other play has been moving we can reduce the distnace time by that much
        # so for that we need to find out when was the last time we pushed the button, because every time since then can be subtracted from our movement distance
        # 1 is for the button push
        time_taken += 1 + max(0,distance - (time_taken - last_moved[bot]))
        # do the move
        current_position[bot] = pos
        # update the last moved
        last_moved[bot] = time_taken

    return time_taken 
    
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
            ans = solve(get_data(l))
            print "Case #" + str(case_count) + ": " + str(ans)

def get_data(s):
    moves = []
    dq = deque(s.split(' '))
    N = dq.popleft()
    while dq:
        bot, pos = dq.popleft(),int(dq.popleft())
        moves.append((bot, pos))
    return moves
main()


