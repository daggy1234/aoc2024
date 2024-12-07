def parser(test):
    fname = "test" if test else "inp"
    return [[int(v) for v in l.split(" ")] for l in open(
        f"./data/day02/{fname}.txt").read().splitlines()]


def part_1(test: bool = False):
    data = parser(test)
    linectr = 0
    for line in data:
        all = True
        inc = True
        prev = line[0]
        succ = line[1]
        if prev > succ:
            inc = False
        for y in range(1, len(line)):
            if inc:
                if not (prev + 1 <= line[y] <= prev + 3):
                    all = False
            else:
                if not (prev - 3 <= line[y] <= prev - 1):
                    all = False
            prev = line[y]
        if all:
            linectr += 1
    return linectr


def part_2(test: bool = False):
    data = parser(test)
    linectr = 0
    for line in data:
        linePass = False
        for y in range(len(line) + 1):
            cleaned = line[:y] + line[y+1:]
            des = False
            if cleaned[0] > cleaned[1]:
                des = True
            if cleaned != sorted(cleaned, reverse=des):
                continue
            prev = cleaned[0]
            cpass = True
            for z in range(1, len(cleaned)):
                if not (1 <= abs(prev - cleaned[z]) <= 3):
                    cpass = False
                prev = cleaned[z]
            if not cpass:
                continue
            linePass = True

        if linePass:
            linectr += 1
    return linectr

if __name__ == "__main__":
    print(part_1())
    print(part_2())
