fresh = 0
ranges = []

with open('./input5.txt', 'r') as file:
    for line in file:
        if line.__contains__('-'):
            line = line.strip()
            parts = line.split('-')
            ranges.append([int(parts[0]), int(parts[1])])
ranges.sort(key=lambda x: x[0])
# print(ranges)

merged_ranges = []
for current in ranges:
    if not merged_ranges:
        merged_ranges.append(current)
    else:
        previous = merged_ranges[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged_ranges.append(current)

# print(ranges)
for rang in merged_ranges:
    # print(rang[1]-rang[0]+1)
    fresh += (rang[1]-rang[0]+1)
print(fresh)