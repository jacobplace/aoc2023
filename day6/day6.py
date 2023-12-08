import re


def get_dist(time, goal):
    invalid_times = 0
    for i in range(time + 1):
        if i * (time - i) >= goal:
            break
        invalid_times += 1
    for i in range(time + 1, 0, -1):
        if i * (time - i) >= goal:
            break
        invalid_times += 1
    return time - invalid_times + 2


def p1(times, goals):
    wins = 1
    for i, t in enumerate(times):
        wins *= get_dist(t, goals[i])
    return wins


def parse_input(line):
    p1 = [int(t) for t in re.findall(r"\d+", line)]
    p2 = int("".join([str(i) for i in p1]))
    return p1, p2


def main():
    input = open("input").readlines()

    times, time = parse_input(input[0])
    dist, goal = parse_input(input[1])

    print(f"P1:{p1(times, dist)}\tP2:{get_dist(time, goal)}")


if __name__ == "__main__":
    main()
