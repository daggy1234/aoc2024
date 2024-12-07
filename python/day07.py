def parser(test):
    lines = open(f"./data/day07/{"test" if test else "inp"}.txt", "r").readlines()
    res = []
    for l in lines:
        p = l.split(":")
        targ = int(p[0].strip())
        deps = list(map(int, p[1].strip().split(" ")))
        res.append((targ, deps))
    return res

def evaller(part_2: bool, test: bool = False):
    data = parser(test)
    summa = 0
    for p in data:
        targ = p[0]
        res = [p[1][0]]
        for i in range(1, len(p[1])):
            if part_2:
                res = [r + p[1][i] for r in res] + [r * p[1][i] for r in res] + [int(str(r) + str(p[1][i])) for r in res]
            else:
                res = [r + p[1][i] for r in res] + [r * p[1][i] for r in res]
        if targ in res:
            summa += targ
    return summa

def part_1(test: bool = False):
    return evaller(False, test)

def part_2(test: bool = False):
    return evaller(True, test)
