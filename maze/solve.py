from algo.Astar import *
from algo.BFS import *
from maze.GUI import *

def solve_astar(maze, dimension):
    temp = []
    for height in range(dimension):
        endArray = []
        for depth in range(dimension):
            for width in range(dimension):
                if height == 0:
                    start = (0, 0, 0)
                else:
                    h, d, w = temp[len(temp) - 1]
                    start = (h + 1, d, w)
                if maze[height][depth][width] == 3 and height != dimension - 1 and maze[height + 1][depth][width] == 2:
                    end = (height, depth, width)
                    paths = astar(start, end, maze)
                    endArray.append(paths)
                elif maze[height][depth][width] == 3 and height == dimension - 1:
                    end = (height, depth, width)
                    paths = astar(start, end, maze)
                    endArray.append(paths)

        for i in range(len(endArray)):
            temp = endArray[0]
            if i < (len(endArray) - 1) and len(endArray[i]) > len(endArray[i + 1]):
                temp = endArray[i + 1]
            elif len(endArray) == 1:
                temp = endArray[0]
        print(temp)
        plot(i, maze[i], temp)


def solve_BFS(maze, dimension):
    start = 0
    for height in range(dimension):
        counter = 0
        for depth in range(dimension):
            for width in range(dimension):
                if height == 0 and counter == 0:
                    path, start = BFS(0, 0, 0, maze, dimension)
                    plot(height, maze[height], path)
                    print(path)
                    counter = 1
                elif height < dimension-1 and counter == 0:
                    h,d,w = start
                    path, start = BFS(h, d, w, maze, dimension)
                    plot(height, maze[height], path)
                    print(path)
                    counter = 1
                elif height == dimension-1 and counter == 0:
                    h,d,w = start
                    path = BFS(h, d, w, maze, dimension)
                    plot(height, maze[height], path)
                    print(path)
                    counter = 1
