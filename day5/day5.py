maps = dict()


def process_map(lbl: str, lst: list):
    maps[lbl] = [tuple(map(int, l.split(" "))) for l in lst]


def walk_seeds(seeds: list) -> int:
    ls = list()
    for seed in seeds:
        ls.append(check_seed(seed))
    return min(ls)


def check_seed(s: int) -> int:
    for m in range(len(maps)):
        flip = True
        for r in maps[m + 1]:
            if s >= r[1] and s <= r[1] + r[2] - 1 and flip:
                flip = False
                s = r[0] + s - r[1]
    return s


def parse_file():
    lines = open("test").readlines()
    seeds = [int(i) for i in lines[0].split(":")[1].strip().split(" ")]
    lines = [line for line in lines[1:] if line.strip()]
    process_lines(lines)
    return seeds


def process_lines(lines):
    lbl = 0
    lst = list()
    for line in lines:
        if "-" in line:
            if lbl:
                process_map(lbl, lst)
            lbl += 1
            lst = list()
        else:
            lst.append(line.strip())
    process_map(lbl, lst)


def p2_seeds(seeds):
    new_seeds = list()
    for i in range(0, len(seeds), 2):
        new_seeds.append(seeds[i])
        new_seeds.append(seeds[i] + seeds[i + 1])
    return new_seeds


def narrow_range(new_seeds):
    sd = list()
    for seed in new_seeds:
        s = seed
        for m in range(len(maps)):
            flip = True
            for r in maps[m + 1]:
                if s >= r[1] and s <= r[1] + r[2] - 1 and flip:
                    flip = False
                    s = r[0] + s - r[1]
        sd.append((seed, s))
    m = None
    p = 0
    for i, s in enumerate(sd):
        if not m:
            m = s[1]
        if s[1] < m:
            m = s[1]
            p = i
    if p % 2 == 0:
        rng = range(new_seeds[p], new_seeds[p + 1])
    else:
        rng = range(new_seeds[p - 1], new_seeds[p])
    return rng


def main():
    seeds = parse_file()
    rng = narrow_range(p2_seeds(seeds))
    print("\t".join([str(i) for i in [walk_seeds(seeds), walk_seeds(rng)]]))


if __name__ == "__main__":
    main()
