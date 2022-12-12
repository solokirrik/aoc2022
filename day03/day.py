def toScore(char: str) -> int:
    if ord(char) >= 97:
        return ord(char) - 96
    else:
        return ord(char) - 38


def intersection(ins1, ins2: str) -> str:
    out = set(ins1).intersection(set(ins2))
    if len(out) > 0:
        return out.pop()


def part1():
    with open("./day3") as f:
        inp = [x.strip() for x in f.readlines()]

    print(ord("z") - 96)
    print(ord("Z") - 38)
    print(ord("a"), ord("z"))
    print(ord("A"), ord("Z"))
    print(inp[:3])

    score = 0

    for item in inp:
        leftPart = item[:int(len(item) / 2)]
        rightPart = item[int(len(item) / 2):]

        score += toScore(intersection(leftPart, rightPart))

    print(score)


def intersection2(ins1, ins2, ins3: str) -> str:
    out = set(ins1).intersection(set(ins2)).intersection(set(ins3))
    if len(out) > 0:
        return out.pop()


def part2():
    with open("./day3") as f:
        inp = [x.strip() for x in f.readlines()]

    g = 0
    groups = [0, 0, 0]

    while len(inp) > 0:
        score = toScore(intersection2(inp.pop(), inp.pop(), inp.pop()))
        groups[g] += score
        g += 1
        if g > 2:
            g = 0

    print(sum(groups))

if __name__=='__main__':
    part1()
    part2()
