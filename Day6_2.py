from functools import reduce

result = 0
homework = []
skip = False
i = 0

with open('./input6.txt', 'r') as file:
    for line in file:
        homework.append(line.strip('\n'))
# print(homework)

no = ['']
for x in range(len(homework[0])-1, -1, -1):
    if skip:
        i = 0
        no = ['']
        skip = False
        continue
    for y in range(len(homework)-1):
        no[i] += homework[y][x]
    i += 1
    # print(no)
    if homework[len(homework)-1][x] != ' ':
        if homework[len(homework)-1][x] == '+':
            for n in no:
                result += int(n)
        tmp = 1
        if homework[len(homework)-1][x] == '*':
            for n in no:
                tmp *= int(n)
            result += tmp
        skip = True
    no.append('')
print(result)