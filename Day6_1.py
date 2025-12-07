from functools import reduce

sum = 0
homework = []

with open('./input6.txt', 'r') as file:
    for line in file:
        parts = (line.rstrip('\n')).split(' ')
        homework.append([var for var in parts if var])
for n in range(len(homework)-1):
    homework[n] = list(map(int, homework[n]))
    
for x in range(1,len(homework)-1):
    for y in range(len(homework[0])):
        if homework[len(homework)-1][y] == '+':
            homework[0][y] += homework[x][y]
        if homework[len(homework)-1][y] == '*':
            homework[0][y] *= homework[x][y]
print(reduce(lambda a, b: a + b, homework[0]))