class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(start, end, maze):
    #
    # # Create start and end node
    # for x in range(N):
    #     print("hello")
    #     for y in range(N):
    #         print(y)
    #         for z in range(N):
    #             if maze[x][y][z] == 2 and x == 0:
    #                 start = (x,y,z)
    #             elif maze[x][y][z] == 2 and x > 0:
    #                 start = end
    #             if maze[x][y][z] == 3:
    #                 end = (x,y,z)

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []
    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            # print(item.f)
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)

        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0,0, -1), (0,0, 1), (0,-1, 0), (0,1, 0)]: # Adjacent squares
            # Get node position
            node_position = (current_node.position[0], current_node.position[1] + new_position[1], current_node.position[2] + new_position[2])

            # Make sure within range
            if node_position[1] > (len(maze) - 1) or node_position[1] < 0 or node_position[2] > (len(maze[len(maze)-1]) -1) or node_position[2] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]][node_position[2]] == 1:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[1] - end_node.position[1]) ** 2) + ((child.position[2] - end_node.position[2]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)



# Create start and end node
# for x in range(N):
#     start = end = 0
#     for y in range(N):
#         for z in range(N):
#             if maze[x][y][z] == 2 and x==0:
#                 start = (x,y,z)
#             if maze[x][y][z] == 3:
#                 end = (x,y,z)
#
#             if start != 0 and end != 0:
#                 paths = astar(start, end, maze)
#                 print(paths)

#
# listOfEnd = []
# paths = []
# temp = []
# for height in range(N):
#     endArray = []
#     for depth in range(N):
#         for width in range(N):
#             if height == 0:
#                 start = (0, 0, 0)
#             else:
#                 h, d, w = temp[len(temp)-1]
#                 start = (h+1, d, w)
#             if maze[height][depth][width] == 3 and height != N-1 and maze[height+1][depth][width] == 2:
#                 end = (height, depth, width)
#                 paths = astar(start, end, maze)
#                 endArray.append(paths)
#
#     for i in range(len(endArray)):
#         temp = endArray[0]
#         if i < (len(endArray)-1) and len(endArray[i]) > len(endArray[i+1]):
#             temp = endArray[i+1]
#         elif len(endArray) == 1:
#             temp = endArray[0]
#
#     print(temp)
