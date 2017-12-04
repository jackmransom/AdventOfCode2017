import re
def partOne(passList):
    uniques = 0
    for passphrase in passList:
        words = re.sub("[^\w]", " ",  passphrase).split()
        if len(words) == len(set(words)):
            uniques += 1
    print(uniques)

def partTwo(passList):
    valid = 0
    for passphrase in passList:
        words = re.sub("[^\w]", " ",  passphrase).split()
        sortedWords = [''.join(sorted(s)) for s in words]
        if len(sortedWords) == len(set(sortedWords)):
            valid += 1
    
    print(valid)
    
def main():
    passList = []
    with open('input.txt') as f:
        passList = f.read().splitlines()

    partOne(passList)
    partTwo(passList)

if __name__ == '__main__':
    main()
