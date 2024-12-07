import argparse

def main():
    parser = argparse.ArgumentParser(description='Advent of Code 2024 Runner')
    parser.add_argument('day', type=int, help='Day of the challenge to run', default=0)
    parser.add_argument('--test', action='store_true', help='Run in test mode')

    args = parser.parse_args()
    if args.day == 0:
        drgl = [i for i in range(1, 6)]
    else:
        drgl = [args.day]
    for drg in drgl:
        if drg < 10:
            drgs = f"0{drg}"
        else:
            drgs = str(drg)
        file = __import__(f"python.day{drgs}")
        mod = getattr(file, f"day{drgs}")
        print(getattr(mod, "part_1")(args.test))
        print(getattr(mod, "part_2")(args.test))

if __name__ == "__main__":
    main()