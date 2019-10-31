import random

def theMaze(dimension):
    # dimension = int(input("Enter the Dimension of the Maze: "))
    # maze = [[[random.randint(0, 1) for h in range(dimension)] for i in range(dimension)] for j in range(dimension)]
    maze = [[[(0 if random.randint(0, 2) else 1) for h in range(dimension)] for i in range(dimension)] for j in range(dimension)]
    maze[0][0][0] = 2
    maze[dimension-1][dimension-1][dimension-1] = 3

    for i in range(dimension-1):
        count = 0
        while count < 3:
            width = random.randint(0, dimension-2)
            depth = random.randint(0, dimension-2)
            if i != 0:
                if maze[i][depth][width] != 3 and maze[i][depth][width] != 2 and maze[i-1][depth][width] != 3:
                    maze[i][depth][width] = 3
                    count = count + 1
            else:
                if maze[i][depth][width] != 3 and maze[i][depth][width] != 2:
                    maze[i][depth][width] = 3
                    count = count + 1

            if i != dimension-1:
                if maze[i+1][depth][width] == 0:
                    maze[i + 1][depth][width] = 2
    return maze

def validation(dimension):
    checkMaze = theMaze(dimension)
    valid = True
    while True:
        for i in range(dimension-1):
            count = 0
            for j in range(dimension):
                for k in range(dimension):
                    if checkMaze[i][j][k] == 3 and checkMaze[i+1][j][k] == 2:
                        count += 1
            if count == 0:
                valid = False
            if i == dimension - 2 and valid == True:
                return checkMaze


def printmaze(maze, dimension):
    for i in range(dimension):
        print(maze[i])

def generate():
    dimension = int(input("Enter the Dimension of the Maze: "))
    maze = validation(dimension)
    printmaze(maze, dimension)