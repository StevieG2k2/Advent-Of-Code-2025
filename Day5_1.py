from urllib.request import urlopen

fresh = 0
ranges = []

with open('./input5.txt', 'r') as file:
    for line in file:
        if line.rstrip('\n') == '': continue
        if line.__contains__('-'):
            ranges.append((line.rstrip('\n')).split('-'))
        else:
            for range in ranges:
                if int(range[0]) <= int(line.rstrip('\n')) <= int(range[1]):
                    fresh += 1
                    break
print(fresh)