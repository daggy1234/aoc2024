from collections import Counter


def parser(test: bool):
    fname = "test" if test else "inp"
    l_pairs = []
    r_pairs = []
    [[v := l.split("   "), l_pairs.append(int(v[0])), r_pairs.append(int(v[1]))] for l in open(
        f"./data/day01/{fname}.txt").read().splitlines()]
    return l_pairs, r_pairs


def part_1(test: bool = False) -> int:
    l_pairs, r_pairs = parser(test)
    l_pairs.sort()
    r_pairs.sort()
    summa = 0
    for x, y in zip(l_pairs, r_pairs):
        summa += abs(x - y)
    return summa


def part_2(test: bool = False) -> int:
    l_pairs, r_pairs = parser(test)

    r_ctr = dict(Counter(r_pairs))
    return sum(x * r_ctr.get(x, 0) for x in l_pairs)

if __name__ == "__main__":
    print(part_1())
    print(part_2())
