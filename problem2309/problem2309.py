import sys

dwarf = list()

for _ in range(9):
    dwarf.append(int(input()))

dwarf_sum = sum(dwarf)
dwarf.sort()

for i in range(9):
    for j in range(i + 1, 9):
        if (dwarf_sum - dwarf[i] - dwarf[j]) == 100:
            for k in range(9):
                if i == k or j == k:
                    continue
                print(dwarf[k])
            sys.exit()
