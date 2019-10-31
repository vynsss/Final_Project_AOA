from collections import *

def BFS(height, depth, width, maze, dimension):
    queue = deque([(height, depth, width, None)])
    while len(queue)>0:
        node = queue.popleft() #grab the first node
        height = node[0]
        depth = node[1]
        width = node[2]
        if maze[height][depth][width] == 3 and height != dimension - 1 and maze[height + 1][depth][width] == 2:
            path = []
            while(node != None):
                path.append((node[0],node[1], node[2]))
                node = node[3]
            return path[::-1], (height + 1, depth, width)
        if height == dimension - 1 and maze[height][depth][width] == 3:
            path = []
            while (node != None):
                path.append((node[0], node[1], node[2]))
                node = node[3]
            return path[::-1]
        if maze[height][depth][width] == 1:
            continue
        maze[height][depth][width]= 4 #visited
        for i in [[height, depth - 1, width], [height, depth + 1, width], [height, depth, width - 1], [height, depth, width + 1]]: #new spots to try
            if i[1] != -1 and i[2] != -1 and i[1] != dimension and i[2] != dimension:
                queue.append((i[0],i[1],i[2],node)) #create the new spot, with node as the parent
