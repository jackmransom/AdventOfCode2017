def partOne(maze):
    i = 0
    prevOffset = i
    steps = 0
    while i < len(maze):
        prevOffset = i
        i += maze[i]
        maze[prevOffset] +=1
        steps += 1
    print(steps)
    
def partTwo(maze):
    i = 0
    prevOffset = i
    steps = 0
    while i < len(maze):
        prevOffset = i
        i += maze[i]
        
        if maze[prevOffset] >= 3:
            maze[prevOffset] -=1
        else:
            maze[prevOffset] +=1
        
        steps += 1
    print(steps)

def main():
    with open('input.txt') as f:
        maze = f.read().splitlines()
        maze = [int(i) for i in maze]
        maze2 = [int(i) for i in maze]
        partOne(maze)
        partTwo(maze2)

if __name__ == '__main__':
    main()
