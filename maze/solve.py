from algo.Astar import *
from algo.BFS import *
from maze.GUI import *

def solve_astar(maze, N):
    temp = []
    for height in range(N):
        endArray = []
        for depth in range(N):
            for width in range(N):
                if height == 0:
                    start = (0, 0, 0)
                else:
                    h, d, w = temp[len(temp) - 1]
                    start = (h + 1, d, w)
                if maze[height][depth][width] == 3 and height != N - 1 and maze[height + 1][depth][width] == 2:
                    end = (height, depth, width)
                    paths = astar(start, end, maze)
                    plot(height, maze[height], paths)
                    endArray.append(paths)
                elif maze[height][depth][width] == 3 and height == N - 1:
                    end = (height, depth, width)
                    paths = astar(start, end, maze)
                    plot(height, maze[height], paths)
                    endArray.append(paths)

        for i in range(len(endArray)):
            temp = endArray[0]
            if i < (len(endArray) - 1) and len(endArray[i]) > len(endArray[i + 1]):
                temp = endArray[i + 1]
            elif len(endArray) == 1:
                temp = endArray[0]
        print(temp)

def solve_BFS(maze, N):
    start = 0
    for i in range(N):
        counter = 0
        for j in range(N):
            for k in range(N):
                # if maze[i][j][k] == 2 and counter == 0:
                #     path = BFS(i, j, k, maze)
                #     print(path)
                #     counter = 1
                if i == 0 and counter == 0:
                    path, start = BFS(0, 0, 0, maze, N)
                    plot(i, maze[i], path)
                    print(path)
                    counter = 1
                elif i < N-1 and counter == 0:
                    h,d,w = start
                    path, start = BFS(h, d, w, maze, N)
                    plot(i, maze[i], path)
                    print(path)
                    counter = 1
                elif i == N-1 and counter == 0:
                    h,d,w = start
                    path = BFS(h, d, w, maze, N)
                    plot(i, maze[i], path)
                    print(path)
                    counter = 1

