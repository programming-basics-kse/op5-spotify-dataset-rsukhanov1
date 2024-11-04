lines = []

with open('top_50_2023.csv', 'r') as file:
    columns = next(file)
    print(columns)
    for line in  file:
        line = line[:-1].split(',')
        lines.append(line)
        print(line)
print(lines)