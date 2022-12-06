def part1():
    inp = []

    with open("./day3") as f:
        inp = [x.strip() for x in f.readlines()]

    print(ord("z") - 96)
    print(ord("Z") - 38)
    print(ord("a"), ord("z"))
    print(ord("A"), ord("Z"))
    print(inp[:3])

    iii = "vJrwpWtwJgWrhcsFMMfFFhFp"
    print(set(iii[:int(len(iii) / 2)]).intersection(set(iii[int(len(iii) / 2):])))

    def toScore(char: str) -> int:
        if ord(char) >= 97:
            return ord(char) - 96
        else:
            return ord(char) - 38

    def intersection(ins1, ins2: str) -> str:
        out = set(ins1).intersection(set(ins2))
        if len(out) > 0:
            return out.pop()

    score = 0

    for item in inp:
        score += toScore(intersection(item[:int(len(item) / 2)], item[int(len(item) / 2):]))

    print(score)


def part2():
    score = 0

    groups = [0, 0, 0]
    g = 0

    with open("./day3") as f:
        inp = [x.strip() for x in f.readlines()]

    def toScore(char: str) -> int:
        if ord(char) >= 97:
            return ord(char) - 96
        else:
            return ord(char) - 38

    def intersection2(ins1, ins2, ins3: str) -> str:
        out = set(ins1).intersection(set(ins2)).intersection(set(ins3))
        if len(out) > 0:
            return out.pop()

    while len(inp) > 0:
        score = toScore(intersection2(inp.pop(), inp.pop(), inp.pop()))
        groups[g] += score
        g += 1
        if g > 2:
            g = 0

    print(sum(groups))
