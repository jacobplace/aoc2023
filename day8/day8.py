import io
import math
import re

test1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

test2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

test3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def define_input():
    t1 = [l.strip() for l in io.StringIO(test1).readlines() if l.strip()]
    t2 = [l.strip() for l in io.StringIO(test2).readlines() if l.strip()]
    t3 = [l.strip() for l in io.StringIO(test3).readlines() if l.strip()]
    input = [l.strip() for l in open("input").readlines() if l.strip()]
    return t1, t2, t3, input


def define_walk(input: list):
    directions = input[0]
    paths = dict()
    initial_point = None
    for d in input[1:]:
        s, l, r = [i for i in re.findall(r"[a-zA-Z0-9]+", d)]
        if not initial_point:
            initial_point = s
        paths[s] = dict()
        paths[s]["R"] = r
        paths[s]["L"] = l
    return paths, directions


def get_steps(paths, dirs, node):
    steps = 0
    while node[-1] != "Z":
        dir = dirs[steps % len(dirs)]
        node = paths[node][dir]
        steps += 1
    return steps


def test_P1(t1, t2):
    path, steps = define_walk(t1)
    assert get_steps(path, steps, "AAA") == 2
    path, steps = define_walk(t2)
    assert get_steps(path, steps, "AAA") == 6


def test_P2(t3):
    path, steps = define_walk(t3)
    mpaths = list()
    for inode in [n for n in path.keys() if n[-1] == "A"]:
        mpaths.append(get_steps(path, steps, inode))
    assert math.lcm(*mpaths) == 6


def main():
    t1, t2, t3, input = define_input()
    test_P1(t1, t2)
    test_P2(t3)
    # P1
    path, steps = define_walk(input)
    print(get_steps(path, steps, "AAA"))

    # P2
    mpaths = list()
    for inode in [n for n in path.keys() if n[-1] == "A"]:
        mpaths.append(get_steps(path, steps, inode))
    print(math.lcm(*mpaths))


if __name__ == "__main__":
    main()
