def part1():
    with open("./day5") as f:
        inp = [x.replace('\n', "") for x in f.readlines()]

    #     [H]         [H]         [V]
    #     [V]         [V] [J]     [F] [F]
    #     [S] [L]     [M] [B]     [L] [J]
    #     [C] [N] [B] [W] [D]     [D] [M]
    # [G] [L] [M] [S] [S] [C]     [T] [V]
    # [P] [B] [B] [P] [Q] [S] [L] [H] [B]
    # [N] [J] [D] [V] [C] [Q] [Q] [M] [P]
    # [R] [T] [T] [R] [G] [W] [F] [W] [L]
    #  1   2   3   4   5   6   7   8   9

    queues = [
        ["G", "P", "N", "R"][::-1],
        ["H", "V", "S", "C", "L", "B", "J", "T", ][::-1],
        ["L", "N", "M", "B", "D", "T", ][::-1],
        ["B", "S", "P", "V", "R", ][::-1],
        ["H", "V", "M", "W", "S", "Q", "C", "G", ][::-1],
        ["J", "B", "D", "C", "S", "Q", "W", ][::-1],
        ["L", "Q", "F"][::-1],
        ["V", "F", "L", "D", "T", "H", "M", "W", ][::-1],
        ["F", "J", "M", "V", "B", "P", "L", ][::-1],
    ]
    raw_moves = inp[10:]

    moves = [x.split(" ") for x in raw_moves]

    for val in moves:
        amount = int(val[1])
        fromIdx = int(val[3])-1
        toIdx = int(val[5])-1

        while amount > 0:
            queues[toIdx].append(queues[fromIdx].pop())
            amount-=1

    print("".join([x[-1]for x in  queues]))

def part2():
    queues = [
        ["G", "P", "N", "R"][::-1],
        ["H", "V", "S", "C", "L", "B", "J", "T", ][::-1],
        ["L", "N", "M", "B", "D", "T", ][::-1],
        ["B", "S", "P", "V", "R", ][::-1],
        ["H", "V", "M", "W", "S", "Q", "C", "G", ][::-1],
        ["J", "B", "D", "C", "S", "Q", "W", ][::-1],
        ["L", "Q", "F"][::-1],
        ["V", "F", "L", "D", "T", "H", "M", "W", ][::-1],
        ["F", "J", "M", "V", "B", "P", "L", ][::-1],
    ]

    with open("./day5") as f:
        inp = [x.replace('\n', "") for x in f.readlines()]

    raw_moves = inp[10:]

    moves = [x.split(" ") for x in raw_moves]

    for val in moves:
        amount = int(val[1])
        fromIdx = int(val[3])-1
        toIdx = int(val[5])-1

        elems = queues[fromIdx][-amount:]
        queues[fromIdx] = queues[fromIdx][:-amount]
        queues[toIdx] += elems

    print("".join([x[-1]for x in queues]))