from typing import Tuple


def part1():
    inp = []

    with open("./day2") as f:
        inp = [x.strip().split(" ") for x in f.readlines()]

    playerA = {"A": "Rock", "B": "Paper", "C": "Scissors"}
    playerB = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}

    points = {"Rock": 1, "Paper": 2, "Scissors": 3}
    score = {
        "lose": 0,
        "draw": 3,
        "win": 6,
    }

    beaters = {
        "Rock": "Paper",
        "Paper": "Scissors",
        "Scissors": "Rock",
    }

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

    def calcScore(a: int, b: int) -> Tuple[int, int]:
        scoreA = points[playerA[a]]
        scoreB = points[playerB[b]]

        onew, two = wonScore(playerA[a], playerB[b])

        return scoreA + onew, scoreB + two

    plA, plB = 0, 0

    for game in inp:
        a, b = game[0], game[1]
        scA = points[playerA[a]]
        scB = points[playerB[b]]

        onew, two = wonScore(playerA[a], playerB[b])

        plA += scA + onew
        plB += scB + two

    print(plA, plB)


def part2():
    playerA = {"A": "Rock", "B": "Paper", "C": "Scissors"}
    playerB = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}

    points = {"Rock": 1, "Paper": 2, "Scissors": 3}
    score = {"lose": 0, "draw": 3, "win": 6, }
    strat = {"X": "lose", "Y": "draw", "Z": "win"}
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

    inp = []

    with open("./day2") as f:
        inp = [x.strip().split(" ") for x in f.readlines()]

    plA, plB = 0, 0

    for game in inp:
        a, b = game[0], game[1]
        # scA = points[playerA[a]]
        aFig = playerA[a]
        bFig = bFigCalc(aFig, strat[b])
        scB = points[bFig]

        two = score[strat[b]]
        # plA += scA + onew
        plB += scB + two
        # print(a, b, aFig, scB, two, plB)

    print(plA, plB)
