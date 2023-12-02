import math

max = {"blue": 14, "red": 12, "green": 13}


def p1(line: str) -> int:
    game, plays = line.split(":")
    for play in plays.split(";"):
        for cube in play.split(","):
            cnt, clr = cube.strip().split(" ", 2)
            if max[clr] < int(cnt):
                return 0
    return int(game.split(" ")[1])


def p2(line: str):
    min = {"blue": 0, "red": 0, "green": 0}
    _, plays = line.replace(";", ",").split(":")
    for play in plays.split(","):
        cnt, clr = play.strip().split(" ")
        if min[clr] < int(cnt):
            min[clr] = int(cnt)
    return math.prod(min.values())


def test():
    t1 = "Game 42: 3 blue; 4 red; 2 blue, 2 green"
    t2 = "Game 42: 99 blue; 4 red; 2 blue, 2 green"
    assert p1(t1) == 42
    assert p1(t2) == 0
    assert p2(t1) == 24


def main():
    test()
    with open("input.2") as ifile:
        p1total = 0
        p2total = 0
        for line in ifile:
            p1total += p1(line)
            p2total += p2(line)
    print(f"p1:\t{p1total}")
    print(f"p2:\t{p2total}")


if __name__ == "__main__":
    main()
