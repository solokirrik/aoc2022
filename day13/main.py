import json
import os

# path = os.getcwd() + "/example"
path = os.getcwd() + "/day13"


def check_pair(a, b):
    match (a, b):
        case int(), int():
            return b - a
        case int(), list():
            return check_pair([a], b)
        case list(), int():
            return check_pair(a, [b])
        case list(), list():
            for aa, bb in zip(a, b):
                r = check_pair(aa, bb)
                if r != 0:
                    return r
            return len(b) - len(a)
    raise ValueError


def part1():
    with open(path) as f:
        inp = [x.strip() for x in f.read().strip().split("\n\n")]
    inp = list(map(lambda y: [json.loads(x.strip()) for x in y.split("\n")], inp))

    total = 0
    for i, (a, b) in enumerate(inp):
        if check_pair(a, b) > 0:
            total += i + 1

    print(total)


def part2():
    with open(path) as f:
        inp = [x.strip() for x in f.read().strip().split("\n\n")]
    inp = list(map(lambda y: [json.loads(x.strip()) for x in y.split("\n")], inp))

    dp1, dp2 = 0, 0
    for a, b in inp:
        for o in (a, b):
            if check_pair(o, [[2, ]]) > 0:
                dp1 += 1
            if check_pair(o, [[6, ]]) > 0:
                dp2 += 1

    print((dp1 + 1) * (dp2 + 2))


if __name__ == '__main__':
    part1()
    part2()
