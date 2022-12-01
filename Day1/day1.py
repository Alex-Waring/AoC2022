elves = [[]]
with open("input.txt") as f:
    i = 0
    for line in f:
        if line == "\n":
            i += 1
            elves.append([])
        else:
            elves[i].append(int(line[:-1]))

totals = []

for elf in elves:
    totals.append(sum(elf))

totals = sorted(totals, reverse=True)

print(totals)

print(sum(totals[:3]))