import io
import sys

sys.setrecursionlimit(1000000)

input = open("input").readlines()
def walk_graph(pos, steps):
    steps.append(pos)
    match input[pos[0]][pos[1]]:
        case "S":
            return steps
        case "|":
            if (pos[0] + 1, pos[1]) in steps:
                new_pos = (pos[0] - 1, pos[1])
            else:
                new_pos = (pos[0] + 1, pos[1])
        case "-":
            if (pos[0], pos[1] + 1) in steps:
                new_pos = (pos[0], pos[1] - 1)
            else:
                new_pos = (pos[0], pos[1] + 1)
        case "L":
            if (pos[0] - 1, pos[1]) in steps:
                new_pos = (pos[0], pos[1] + 1)
            else:
                new_pos = (pos[0] - 1, pos[1])
        case "J":
            if (pos[0] - 1, pos[1]) in steps:
                new_pos = (pos[0], pos[1] - 1)
            else:
                new_pos = (pos[0] - 1, pos[1])
        case "7":
            if (pos[0] + 1, pos[1]) in steps:
                new_pos = (pos[0], pos[1] - 1)
            else:
                new_pos = (pos[0] + 1, pos[1])
        case "F":
            if (pos[0] + 1, pos[1]) in steps:
                new_pos = (pos[0], pos[1] + 1)
            else:
                new_pos = (pos[0] + 1, pos[1])
    return walk_graph(new_pos, steps)    

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == "S":
            if input[i-1][j] in ["|", "F", "7"]:
                pos = (i - 1, j)
            elif input[i+1][j] in ["|", "L", "J"]:
                pos = (i + 1, j)
            elif input[i][j-1] in ["-", "F", "L"]:
                pos = (i, j-1)
            elif input[i][j+1] in ["-", "7", "J"]:
                pos = (i, j+1)
            break
steps = walk_graph(pos, [])
print(len(steps)/2)
sorted(steps)

#P2
area = 0
for i in range(len(steps)-1):
    area += (steps[i][0] + steps[i+1][0]) * (steps[i][1]-steps[i+1][1])
area += (steps[-1][0] + steps[0][0]) * (steps[-1][1]-steps[0][1])
area = abs(area / 2)
print(area + 1 - len(steps)/2)
