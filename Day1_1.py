from urllib.request import urlopen

dial = 50
code = 0
low = 0
high = 99

with open('./input.txt', 'r') as file:
    for line in file:
        turn = int(line[1:]) % 100
        if line[0] == 'R':
            dial += turn
            if dial > high:
                dial -= 100
            if dial == 0:
                code += 1
        else:
            dial -= turn
            if dial < low:
                dial += 100
            if dial == 0:
                code += 1
print(code)