from collections import *


# maze = [[1,1,1,1,1,1,1],
#         [1,0,0,0,1,0,1],
#         [1,0,1,0,1,0,1],
#         [1,0,0,0,0,0,1],
#         [1,1,1,1,0,1,1],
#         [1,1,2,0,0,0,1],
#         [1,3,0,1,1,0,1]]
#
# maze = [[[1, 0, 0, 1, 1], [1, 2, 0, 0, 0], [0, 1, 1, 0, 0], [0, 0, 3, 0, 0], [3, 0, 0, 1, 0]],
#         [[1, 1, 1, 0, 1], [0, 0, 2, 1, 1], [0, 0, 1, 1, 1], [1, 0, 0, 0, 1], [0, 0, 3, 1, 1]],
#         [[2, 0, 1, 1, 0], [0, 3, 2, 3, 1], [0, 3, 0, 1, 1], [1, 0, 1, 1, 1], [0, 1, 0, 0, 0]],
#         [[3, 0, 0, 3, 0], [0, 2, 3, 2, 0], [0, 2, 0, 0, 1], [0, 1, 2, 2, 1], [0, 1, 1, 1, 0]],
#         [[1, 1, 1, 2, 1], [1, 1, 1, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 1, 1], [1, 1, 0, 0, 3]]]


N = 5

def BFS(z,x,y,maze,n):
        queue = deque([(z,x,y,None)])
        while len(queue)>0:
            node = queue.popleft() #grab the first node
            z = node[0]
            x = node[1]
            y = node[2]
            if maze[z][x][y] == 3 and z != n - 1 and maze[z+1][x][y] == 2:
                path = []
                while(node != None):
                    path.append((node[0],node[1], node[2]))
                    node = node[3]
                return path[::-1], (z+1, x, y)
            if z == n - 1 and maze[z][x][y] == 3:
                path = []
                while (node != None):
                    path.append((node[0], node[1], node[2]))
                    node = node[3]
                return path[::-1]
            # if maze[z][x][y] == 3 and (maze[z+1][x][y] != 2 or maze[z+1][x][y] != 0):
            #     continue
            if maze[z][x][y] == 1:
                continue
            maze[z][x][y]= 4 #visited
            for i in [[z,x-1,y],[z,x+1,y],[z,x,y-1],[z,x,y+1]]: #new spots to try
                if i[1] != -1 and i[2] != -1 and i[1] != N and i[2] != N:
                    queue.append((i[0],i[1],i[2],node)) #create the new spot, with node as the parent