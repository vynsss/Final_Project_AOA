import random


def theMaze(dimension):
    maze = [[[(0 if random.randint(0, 5) else 1) for h in range(dimension)] for i in range(dimension)] for j in range(dimension)]
    maze[0][0][0] = 2
    maze[dimension - 1][dimension - 1][dimension - 1] = 3

    for height in range(dimension - 1):
        count = 0
        while count < 3:
            width = random.randint(0, dimension - 2)
            depth = random.randint(0, dimension - 2)
            if height != 0:
                if maze[height][depth][width] != 3 and maze[height][depth][width] != 2 and maze[height-1][depth][width] != 3:
                    maze[height][depth][width] = 3
                    count = count + 1
            else:
                if maze[height][depth][width] != 3 and maze[height][depth][width] != 2:
                    maze[height][depth][width] = 3
                    count = count + 1

            if height != dimension-1:
                if maze[height+1][depth][width] == 0:
                    maze[height + 1][depth][width] = 2
    return maze

def validation(dimension):
    valid = True
    while True:
        checkMaze = theMaze(dimension)
        for height in range(dimension - 1):
            count = 0
            for depth in range(dimension):
                for width in range(dimension):
                    if checkMaze[height][depth][width] == 3 and checkMaze[height+1][depth][width] == 2:
                        count += 1
            if count == 0:
                valid = False
            if height == dimension - 2 and valid == True:
                return checkMaze

        for height in range(dimension):
            counter = 0
            counter1 = 0
            for depth in range(dimension):
                for width in range(dimension):
                    if checkMaze[height][depth][width] == 2 and counter == 0:
                        startlayer = height
                        startRow = depth
                        startCol = width
                        start = (height, depth, width)
                        counter == 1
                    if checkMaze[height][depth][width] == 3 and counter1 == 0:
                        endlayer = height
                        endRow = depth
                        endCol = width
                        end = (height, depth, width)
                        counter1 = 1

        visited = [[[False] * dimension for i in range(dimension)] * dimension for i in range(dimension)]

        def recursiveSolve(height, depth, width):
            # if end == 3:
            if height == endlayer and depth == endRow and width == endCol:
                return True

            if checkMaze[height][depth][width] == 1 or visited[height][depth][width]:
                return False

            visited[height][depth][width] = True

            if depth != 0:
                if recursiveSolve(height, depth - 1, width):
                    return True
            if depth != dimension - 1:
                if recursiveSolve(height, depth + 1, width):
                    return True
            if width != 0:
                if recursiveSolve(height, depth, width - 1) == True:
                    return True
            if width != dimension - 1:
                if recursiveSolve(height, depth, width + 1) == True:
                    return True

            return False

        if recursiveSolve(startlayer, startRow, startCol) == False:
            theMaze(dimension)
        else:
            continue

def printmaze(maze, dimension):
    for i in range(dimension):
        print(maze[i])

def generate(dimension):
    # dimension = int(input("Enter the Dimension of the Maze: "))
    maze = validation(dimension)
    printmaze(maze, dimension)
    return maze, dimension