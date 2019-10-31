import random


def theMaze(N):
    maze = [[[(0 if random.randint(0, 5) else 1) for h in range(N)] for i in range(N)] for j in range(N)]
    maze[0][0][0] = 2
    maze[N-1][N-1][N-1] = 3

    for i in range(N-1):
        count = 0
        while count < 3:
            width = random.randint(0, N-2)
            depth = random.randint(0, N-2)
            if i != 0:
                if maze[i][depth][width] != 3 and maze[i][depth][width] != 2 and maze[i-1][depth][width] != 3:
                    maze[i][depth][width] = 3
                    count = count + 1
            else:
                if maze[i][depth][width] != 3 and maze[i][depth][width] != 2:
                    maze[i][depth][width] = 3
                    count = count + 1

            if i != N-1:
                if maze[i+1][depth][width] == 0:
                    maze[i + 1][depth][width] = 2
    return maze

def validation(N):
    checkMaze = theMaze(N)
    valid = True
    while True:
        for i in range(N-1):
            count = 0
            for j in range(N):
                for k in range(N):
                    if checkMaze[i][j][k] == 3 and checkMaze[i+1][j][k] == 2:
                        count += 1
            if count == 0:
                valid = False
            if i == N - 2 and valid == True:
                return checkMaze

        for k in range(N):
            counter = 0
            counter1 = 0
            for i in range(N):
                for j in range(N):
                    if checkMaze[k][i][j] == 2 and counter == 0:
                        startlayer = k
                        startRow = i
                        startCol = j
                        start = (k, i, j)
                        counter == 1
                    if checkMaze[k][i][j] == 3 and counter1 == 0:
                        endlayer = k
                        endRow = i
                        endCol = j
                        end = (k, i, j)
                        counter1 = 1

        visited = [[[False] * N for i in range(N)] * N for i in range(N)]

        def recursiveSolve(z, x, y):
            # if end == 3:
            if z == endlayer and x == endRow and y == endCol:
                return True

            if checkMaze[z][x][y] == 1 or visited[z][x][y]:
                return False

            visited[z][x][y] = True

            if x != 0:
                if recursiveSolve(z, x - 1, y):
                    return True
            if x != N - 1:
                if recursiveSolve(z, x + 1, y):
                    return True
            if y != 0:
                if recursiveSolve(z, x, y - 1) == True:
                    return True
            if y != N - 1:
                if recursiveSolve(z, x, y + 1) == True:
                    return True

            return False

        if recursiveSolve(startlayer, startRow, startCol) == False:
            theMaze(N)

def printmaze(maze, N):
    for i in range(N):
        print(maze[i])

def generate():
    dimension = int(input("Enter the Dimension of the Maze: "))
    maze = validation(dimension)
    printmaze(maze, dimension)
    return maze, dimension