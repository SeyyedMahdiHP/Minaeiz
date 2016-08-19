def pouring(X, Y, goal, start=(0, 0)):
    explored = set()
    frontier = [[start]]
    while frontier:
        path = frontier.pop()
        x, y = path[-1]
        for state, action in successor(x, y, X, Y).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if goal in state:
                    return path2
                else:
                    frontier.append(path2)
    return False


def successor(x, y, X, Y):
    return {
        (X, y): 'Fill X',
        (x, Y): 'Fill Y',
        (0, y): 'Empty X',
        (x, 0): 'Empty Y',
        (0, x + y) if x + y <= Y else (x+y - Y, Y): 'X -> Y',
        (x + y, 0) if x + y <= X else (X, x+y - X): 'X <- Y'
    }

d = {'Emtpy X': (0, 9), 'Emtpy Y': (4, 0)}
for k, v in d.items():
    x, y = v
    print(x)
print(successor(2, 8, 4, 9))
print(pouring(4, 9, 6))
# [[(0, 0), 'FILL X', (4, 0), 'FILL Y', (4, 9)]]
# (4, 9) -> (0, 9) Emtpy X
# (4, 9) -> (4, 0) Empty Y
# (4, 9) -> (4, 9) Fill X
# (4, 9) -> (4, 9) Fill Y
# (4, 9) -> (4, 9) X -> Y
# (4, 9) -> (4, 9) X <- Y

