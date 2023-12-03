import re

num_regex = r'[0-9]+'
char_regex = r'(\#|\*|\$|\-|\+|\@|\%|\=|\&|\\|\/)'
char2_regex = r'(\*)'

num_loc = list()
num_val = list()
sym_loc = list()
sym_val = list()
p2_sym = list()

accepted_vals = set()

def match_in_row(nums: list, locs: list, row: int) -> set:
    s = set()
    for loc in locs:
        for i, num in enumerate(nums):
            if loc in range(num[0], num[1]+1):
                s.add((row, i))
    return(s)

def match_in_row_2(nums: list, locs: list, row: int) -> dict:
    sets_dict = dict()
    for loc in locs:
        if loc not in sets_dict:
            sets_dict[loc] = set()
        for i, num in enumerate(nums):
            if loc in range(num[0], num[1]+1):
                sets_dict[loc].add((row, i))
    return(sets_dict)

with open("input") as ifile:
    for line in ifile:
        num_loc.append([(m.start()-1, m.end()) for m in re.finditer(num_regex, line)])
        num_val.append([m.group() for m in re.finditer(num_regex, line)])
        sym_loc.append([m.start() for m in re.finditer(char_regex, line)])
        sym_val.append([m.group() for m in re.finditer(char_regex, line)])
        p2_sym.append([m.start() for m in re.finditer(char2_regex, line)])
# p1
for i in range(len(sym_loc)):
    if i >= 1:
        accepted_vals.update(match_in_row(num_loc[i-1], sym_loc[i], i-1))
    if i < len(sym_loc)-1:
        accepted_vals.update(match_in_row(num_loc[i+1], sym_loc[i], i+1))
    accepted_vals.update(match_in_row(num_loc[i], sym_loc[i], i))

p1 = 0
for i in accepted_vals:
    p1 += int(num_val[i[0]][i[1]])

#p2
p2 = 0
p2dict = dict()
for i in range(len(sym_loc)):
    if i >= 1:
        x = match_in_row_2(num_loc[i-1], sym_loc[i], i-1)
        for res in x:
            if (i, res) not in p2dict:
                p2dict[(i, res)] = set()
            p2dict[(i, res)].update(x[res])
    if i < len(sym_loc)-1:
        x = match_in_row_2(num_loc[i+1], sym_loc[i], i+1)
        for res in x:
            if (i, res) not in p2dict:
                p2dict[(i, res)] = set()
            p2dict[(i, res)].update(x[res])
    x = match_in_row_2(num_loc[i], sym_loc[i], i)
    for res in x:
        if (i, res) not in p2dict:
            p2dict[(i, res)] = set()
        p2dict[(i, res)].update(x[res])

# print(p1)
# print(p2)
for i in p2dict:
    t2 = 1
    if len(p2dict[i]) == 2:
        for j in p2dict[i]:
            t2 *= int(num_val[j[0]][j[1]])
        p2 += t2
print(p2)