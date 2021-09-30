import itertools
perms = list(itertools.permutations([1, 2, 3, 4, 5, 6 ,7, 8, 9]))

print(perms[1][2])

count = 0

for i in perms:
    if i[0] == 1 or i[2] == 3 or i[4] == 5 or i[6] == 7 or i[8] == 9:
            count = count + 1
            
print(count)

