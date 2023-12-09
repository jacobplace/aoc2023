import io
import re


def process_line(line):
    if set(line) == {0}:
        return [0]
    diffs = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    diffs = new_process_line(diffs)
    line.append(line[-1] + diffs[-1])
    l = [line[0] - diffs[0]]
    l.extend(line)
    return l


def test():
    test_input = """0 3 6 9 12 15
    1 3 6 10 15 21
    10 13 16 21 30 45"""
    test_input = [l.strip() for l in io.StringIO(test_input).readlines() if l.strip()]
    s1, s2 = agg_input(test_input)
    assert s1 == 114
    assert s2 == 2


def agg_input(lines):
    s1 = 0
    s2 = 0
    for l in lines:
        r = process_line([int(i) for i in l.split(" ")])
        s1 += r[-1]
        s2 += r[0]
    return s1, s2


def main():
    test()
    input = open("input").readlines()
    s1, s2 = agg_input(input)
    print(f"P1:{s1}\tP2:{s2}")


if __name__ == "__main__":
    main()
