from functools import cmp_to_key
from collections import defaultdict

def parser(test):
    rules = []
    plines = []
    rset = set()
    lines = open(f"./data/day05/{"test" if test else "inp"}.txt", "r").readlines()
    hitPlines = False
    for l in lines:
        if l.strip() == "":
            hitPlines = True
        elif hitPlines:
            plines.append([int(e) for e in l.strip().split(",")])
        else:
            itms = l.strip().split("|")
            rset.add(int(itms[0]))
            rset.add(int(itms[1]))
            rules.append((int(itms[0]), int(itms[1])))
    
    befored = defaultdict(list)
    afterd = defaultdict(list)
    rule_d = {}
    for r in rules:
        afterd[r[0]].append(r[1])
        befored[r[1]].append(r[0])
        
    return rules, plines, befored, afterd


def sorter(a, b):
    global befored, afterd
    if b in befored[a]:
        return 1
    elif a in befored[b]:
        return -1
    elif a in afterd[b]:
        return 1
    elif b in afterd[a]:
        return -1
    else:
        return 0
    
def part_1(test: bool = False):
    rules, lines, befored, afterd = parser(test)
    
    def sorter(a, b):
        if b in befored[a]:
            return 1
        elif a in befored[b]:
            return -1
        elif a in afterd[b]:
            return 1
        elif b in afterd[a]:
            return -1
        else:
            return 0
    
    summa = 0
    for l in lines:
        sl = sorted(l, key=cmp_to_key(sorter))
        if sl == l:
            med = sl[len(sl)//2]
            summa += med
    return summa

def part_2(test: bool = False):
    
    rules, lines, befored, afterd = parser(test)
    summa = 0
    
    def sorter(a, b):
        if b in befored[a]:
            return 1
        elif a in befored[b]:
            return -1
        elif a in afterd[b]:
            return 1
        elif b in afterd[a]:
            return -1
        else:
            return 0
    
    for l in lines:
        sl = sorted(l, key=cmp_to_key(sorter))
        if sl != l:
            med = sl[len(sl)//2]
            summa += med
    return summa

if __name__ == "__main__":
    print(part_1())
    print(part_2())