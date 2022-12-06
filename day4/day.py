def part1():
    with open("./day4") as f:
        inp = [x.strip().split(",") for x in f.readlines()]

    contains = 0

    for item in inp:
        a = item[0].split("-")
        b = item[1].split("-")

        if int(a[0])<= int(b[0]) and int(a[1]) >= int(b[1]):
            contains+=1
            continue

        if int(b[0]) <= int(a[0]) and int(b[1]) >= int(a[1]):
            contains += 1
            continue

    print(contains)

def part2():
    contains = 0
    with open("./day4") as f:
        inp = [x.strip().split(",") for x in f.readlines()]

    for item in inp:
        a = [int(x) for x in item[0].split("-")]
        b = [int(x) for x in item[1].split("-")]

        aset = set(range(a[0], a[1]+1))
        bset = set(range(b[0], b[1]+1))

        if len(aset.intersection(bset))>0:
            contains += 1
            continue

    print(contains)
