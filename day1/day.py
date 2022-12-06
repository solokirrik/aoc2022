def run():
    inp = ""

    with open("./task1") as f:
        inp = f.read()

    numberstr = [x.split("\n") for x in inp.split("\n\n")]

    cals = []

    for item in numberstr:
        cals.append(sum([int(x) for x in item]))

    print(sorted(cals)[-1])
    print(sum(sorted(cals)[-3:]))

