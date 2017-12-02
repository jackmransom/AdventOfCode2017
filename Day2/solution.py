checksum = 0
with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    for line in lines:
        line = list(map(int, line.rsplit('\t')))
        line.sort()
        checksum += int(line[-1]) - int(line[0])
print(checksum)
        
