import re

swap = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


def test():
    assert extract_numbers("8ee4wd2") == "842"
    assert convert_numbers("eightwo") == "e8t2o"
    assert score("853") == 83
    assert score("5") == 55


def extract_numbers(s: str) -> str:
    return "".join([n for n in re.findall(r"(\d)", s)])


def convert_numbers(s: str) -> str:
    for key in swap.keys():
        s = s.replace(key, swap[key])
    return s


def score(s: str) -> int:
    try:
        return int(s[0] + s[-1])
    except:
        raise ValueError


def main():
    test()
    s1 = 0
    s2 = 0
    with open("input.1") as ifile:
        for line in ifile:
            s1 += score(extract_numbers(line))
            s2 += score(extract_numbers(convert_numbers(line)))
    print(f"s1:\t{s1}")
    print(f"s2:\t{s2}")


if __name__ == "__main__":
    main()
