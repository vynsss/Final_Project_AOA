import matplotlib.pyplot as plt
import matplotlib.patches as patches


def plot(startz, maze, results):
    layer = results
    curentMaze = maze

    print("Maze", maze)

    fig = plt.figure(startz)
    plt.clf()
    ax = fig.add_subplot(111)
    ax.plot(0, 0)
    ax.plot(len(maze), len(maze), alpha=0.0)
    ax.set_facecolor('green')
    # plt.axis('off')
    for i in range(0, len(layer)):
        for z in range(len(layer[i])):
            y = layer[i][1]
            x = layer[i][2]
            rect = patches.Rectangle((x, y), 1, 1, color="white")
            ax.add_patch(rect)

    for i in range(0, len(curentMaze)):
        for x in range(len(curentMaze)):
            for y in range(len(curentMaze[0])):
                pX = y
                pY = x
                if curentMaze[x][y] == 1:
                    rect = patches.Rectangle((pX, pY), 1, 1, color="k")  # black
                elif curentMaze[x][y] == 2:
                    rect = patches.Rectangle((pX, pY), 1, 1, color="r")
                elif curentMaze[x][y] == 3:
                    rect = patches.Rectangle((pX, pY), 1, 1, color="y")
                elif curentMaze[x][y] == 5:
                    plt.ion()
                    plt.show()
                    rect = patches.Rectangle((pX, pY), 1, 1, color="blue")
                    plt.pause(0.01)

                    # plt.pause(0.00001)
                else:
                    continue
                ax.add_patch(rect)

        plt.show()

plt.close()
