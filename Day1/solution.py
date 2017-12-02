sum = 0
sumhalf = 0
with open('input.txt') as f:
    digits = [list(line.rstrip()) for line in f][0] #This is dumb
    for i in range(len(digits)):
        if i == len(digits) - 1:
            if digits[i] == digits[0]:
                sum += int(digits[i])
                break;
        if digits[i] == digits[i+1]:
            sum += int(digits[i])
        jump = int(len(digits)/2)
        if digits[i] == digits[(i+jump) % len(digits)]:
            sumhalf += int(digits[i])
print(sum)
print(sumhalf)
