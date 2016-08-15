def m_and_c(start=(3, 3, 1, 0, 0, 0), goal=(0, 0, 0, 3, 3, 1)):
    explored = set()
    frontier = [[start]]
    while frontier:
        path = frontier.pop()
        s = path[-1]
        for action, state in successor(s).items():
            if state not in explored and not is_negative(state):
                explored.add(state)
                path2 = path + [action, state]
                if goal == state:
                    return path2
                else:
                    frontier.append(path2)
    return False


deltas = {
    (1, 0, 1, -1, 0, -1): "M",
    (0, 1, 1, 0, -1, -1): "C",
    (2, 0, 1, -2, 0, -1): "MM",
    (0, 2, 1, 0, -2, -1): "CC",
    (1, 1, 1, -1, -1, -1): "MC",
}


def is_negative(state):
    return True if min(state) < 0 else False


def successor(state):
    M1, C1, B1, M2, C2, B2 = state
    if C1 > M1 > 0 or C2 > M2 > 0:
        return dict()
    if B1 == 1:
        items = [
            (a + '->', sub(state, s)) for s, a in deltas.items()
        ]
        return dict(items)
    if B2 == 1:
        items = [
            (a + '<-', add(state, s)) for s, a in deltas.items()
            ]
        return dict(items)


def sub(X, Y):
    return tuple([x - y for x, y in zip(X, Y)])


def add(X, Y):
    return tuple([x + y for x, y in zip(X, Y)])

print(m_and_c())