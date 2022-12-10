from typing import Tuple


def wonScore(ass, bss) -> Tuple[int, int]:
    if ass == bss:
        return 3, 3

    if (ass, bss) in [
        ("Rock", "Paper"),
        ("Paper", "Scissors"),
        ("Scissors", "Rock")
    ]:
        return 0, 6
    if (ass, bss) in [
        ("Paper", "Rock"),
        ("Scissors", "Paper"),
        ("Rock", "Scissors")
    ]:
        return 6, 0

    return 0, 0


def part1():
    with open("./day2") as f:
        inp = [x.strip().split(" ") for x in f.readlines()]

    playerA = {"A": "Rock", "B": "Paper", "C": "Scissors"}
    playerB = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}

    points = {"Rock": 1, "Paper": 2, "Scissors": 3}

    plA, plB = 0, 0

    for game in inp:
        a, b = game[0], game[1]
        scA = points[playerA[a]]
        scB = points[playerB[b]]

        one, two = wonScore(playerA[a], playerB[b])

        plA += scA + one
        plB += scB + two

    print(plA, plB)


beaters = {
    "Rock": "Paper",
    "Paper": "Scissors",
    "Scissors": "Rock",
}

losers = {
    "Paper": "Rock",
    "Scissors": "Paper",
    "Rock": "Scissors",
}


def bFigCalc(aFig, result):
    if result == "draw":
        return aFig
    if result == "win":
        return beaters[aFig]
    if result == "lose":
        return losers[aFig]


def part2():
    playerA = {"A": "Rock", "B": "Paper", "C": "Scissors"}
    points = {"Rock": 1, "Paper": 2, "Scissors": 3}
    score = {"lose": 0, "draw": 3, "win": 6, }
    strategy = {"X": "lose", "Y": "draw", "Z": "win"}

    with open("./day2") as f:
        inp = [x.strip().split(" ") for x in f.readlines()]

    plA, plB = 0, 0

    for game in inp:
        a, b = game[0], game[1]
        aFig = playerA[a]
        bFig = bFigCalc(aFig, strategy[b])
        scB = points[bFig]

        two = score[strategy[b]]
        plB += scB + two

    print(plA, plB)


if __name__ == '__main__':
    part1()
    part2()
