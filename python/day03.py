import re


def parser(test):
    return open(f"./data/day03/{"test" if test else "inp"}.txt", "r").read().strip()


def part_1(test: bool = False):
    regex = re.compile(r"mul\(\d+.\d+\)")
    tot = 0
    for case in regex.findall(parser(test)):
        procd = re.compile(r"\d+").findall(case)
        tot += int(procd[0]) * int(procd[1])
    return tot


def part_2(test: bool = False):
    regexb = re.compile(r"(mul\(\d+.\d+\))|(do\(\))|(don't\(\))")
    tot = 0
    enabled = True
    for case in regexb.findall(parser(test)):
        if case[1] != "":
            enabled = True
        elif case[2] != "":
            enabled = False
        else:
            procd = re.compile(r"\d+").findall(case[0])
            if enabled:
                tot += int(procd[0]) * int(procd[1])
    return tot

if __name__ == "__main__":
    print(part_1())
    print(part_2())
