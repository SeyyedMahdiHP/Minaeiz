# in the name of God
# Seyyed Mahdi HassanPour
# SeyyedMahdiHP@gmail.com
"""
check_max_length():
in this solution we use dfs that it means the final answer is not always the smaller, and in some case solver return
none , it may be no correct. you can see answer pp(solver(39,40,1))
then for correct answer we have to make a bfs answer
"""
from pprint import pprint as pp


def solver(X, Y, goal, start=(0, 0)):
    counter = 0
    seen = set()
    frontier = [[start]]
    while frontier:
        path = frontier.pop()
        x, y = path[-1]
        for state, action in successor(x, y, X, Y).items():
            if state not in seen:
                counter += 1
                seen.add(state)
                path2 = path + [action, state]
                if goal in state:
                    return [path2, counter]
                else:
                    frontier.append(path2)
        # print(frontier)


def successor(x, y, X, Y):
    return {
        (X, y): 'Fill X',
        (x, Y): 'Fill Y',
        (0, y): 'Empty X',
        (x, 0): 'Empty Y',
        (0, x + y) if (x + y <= Y) else ((x + y) - Y, Y): 'X -> Y',
        (x + y, 0) if (y + x <= X) else (X, (x + y) - X): 'X <- Y',
    }


def check_max_length():
    store_index = list()
    none_state = list()
    maxcount = 0
    for i in range(1, 40):
        for j in range(i + 1, 41):
            for k in range(1, 41):
                if k < j:
                    try:
                        curcount = solver(i, j, k)[1]
                        if curcount > maxcount:
                            maxcount = curcount
                            store_index = [i, j, k]
                    except Exception:
                        none_state += [(i, j, k)]
                        continue

    return (store_index, maxcount), none_state


print(check_max_length())
#pp(solver(39, 40, 1))  # this solution is not right




# print([i for i in range(40)])
# frontier = [[state, action, state, action], [], [], [], [], [], []]
# [[(0, 0), 'Fill X', (9, 0), 'Fill Y', (9, 4)], []]

# d = {(0, 1): 's1', (2, 3): 's2'}
#
# for a, b in d.items():
#     print(a, b)
