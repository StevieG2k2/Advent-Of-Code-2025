timelines = 0
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
        if manifold[x-1][y] == 'S':
            manifold[x][y] = 1
        if manifold[x][y] == '^' and manifold[x-1][y] != '.':
            if manifold[x][y-1] != '.':
                manifold[x][y-1] = int(manifold[x-1][y]) + int(manifold[x][y-1])
            else:
                manifold[x][y-1] = manifold[x-1][y]
            if manifold[x][y+1] != '.':
                manifold[x][y+1] = int(manifold[x-1][y]) + int(manifold[x][y+1])
            else:
                manifold[x][y+1] = manifold[x-1][y]
        else:
            if manifold[x-1][y] != '.' and manifold[x-1][y] != 'S' and manifold[x-1][y] != '^':
                if manifold[x][y] != '.':
                    manifold[x][y] = int(manifold[x-1][y]) + int(manifold[x][y])
                else:
                    manifold[x][y] = manifold[x-1][y]
                    
for a in manifold[len(manifold)-1]:
    if a != '.':
        timelines += a
print(timelines)