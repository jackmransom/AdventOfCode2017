#This is far from the most pythonic solution, but it works *shrug*
checksum = 0
divsum = 0
with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    for line in lines:
        line = list(map(int, line.rsplit('\t')))
        line.sort()
        checksum += int(line[-1]) - int(line[0])
        for i in range(len(line)):
            for j in range(len(line)):
                if line[i] == line[j]:
                    continue
                if line[i] % line[j] == 0:
                    divsum += line[i] / line[j]
print(checksum)
print(divsum)
        
