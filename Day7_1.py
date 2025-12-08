splits = 0
manifold = []

with open('./input7.txt', 'r') as file:
    for line in file:
        manifold.append(list(line.rstrip('\n')))

# for a in manifold:
#     for i in a:
#         print(i, end="")
#     print()
# print('\n')
for x in range(1,len(manifold)):
    for y in range(len(manifold[x])):
        if manifold[x][y] == '^' and manifold[x-1][y] == '|':
            manifold[x][y-1] = '|'
            manifold[x][y+1] = '|'
            splits += 1
            continue
        if manifold[x-1][y] == 'S' or manifold[x-1][y] == '|':
            manifold[x][y] = '|'

# for a in manifold:
#     for i in a:
#         print(i, end="")
#     print()
print(splits)