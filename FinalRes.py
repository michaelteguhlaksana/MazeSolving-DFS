import matplotlib.pyplot as plt
import matplotlib.colors as col
import numpy as np
import sys

'''
The algorithm

The algorithm used is the Depth first search algorithm.
Built using recursion.

:param maze: The maze. Represented as a nested list.
    ex:
    1 represent path and 0 represent walls
maze=[[0,1,0,0,0,0,0],
      [0,1,1,1,1,1,0],
      [0,1,0,1,0,1,0],
      [0,0,1,1,1,0,0],
      [1,1,1,0,1,0,0],
      [0,1,0,0,1,0,0],
      [0,0,0,0,0,0,0]]

:param destination: the desired final position. Represented using a tuple in the form of (row,column).
                        The row and column are the index of the component in the maze.
:param start: The starting position. Represented the same way as :param destination is.
:param path: The path from the start to destination. The path is represented using a list filled with the tuple of indexes.
            The default value is an empty list.
:param passed: list of passed positions. To prevent the algorithm from going in circles.

Program:
For the point currently tested:
1. Add the cell position to path
2. Check if the cell is the destination or not
    if yes:
        return the path traversed
    if not:
        1. Check neighboring cell whether it is available(not a wall and have not been passed). if it is a path, 
            add to a queue. Pass otherwise
        2. If the queue is empty (a dead end. Surrounded by 3 walls and a passed path), backtrack until it is not a dead
            end  and continue by calling the function.
        3. if it is not a dead end: For each cell in queue:
            a.Call the function, starting from that point to the final destination.


'''

# setting the maximum recursion allowed by python. The normal recursion limit can be reached if we choose a point too
# far from the destination
sys.setrecursionlimit(2550)

def DFSsolver(maze, destination, start, path=[], passed=[]):
    (x,y) = start # set variable x and y as the index of the starting point

    # Ensuring the passed cell is not included in the path during backtracking and add a new cell to the passed queue
    # and path

    if (x,y) not in passed:
        path.append((x, y))
        passed.append((x, y))

    # If the current cell is the destination, return the path
    if (x,y) == destination:
        return path

    # Otherwise, check neighbouring cell.
    else:
        pointqueue = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
        queue = []
        for point in pointqueue:
            # Ensuring the point is not outside the cell
            if len(maze)-1 >= point[1] >= 0 and len(maze[0])-1 >= point[0] >= 0:
                # Conditions of an available cell:
                # - The cell is a path and not a wall
                # - The cell has not been passed
                if maze[point[1]][point[0]] == 1 and point not in passed:
                    queue.append(point)

        # if any of the neighbouring cell is available, check the call the function again, starting from the
        # neighbouring cell to the destination
        if len(queue)!= 0:
            for point in queue:
                return DFSsolver(maze, destination, point, path)

        # Otherwise, start backtracking: remove the cell from path start the function again from the previous cell. THe
        # neighbouring cell number would decrease since it has been passed, hence it will start checking a different
        # cell
        else:
            path.remove((x, y))
            return DFSsolver(maze, destination, path[-1], path)


'''
Making the maze
'''

f = open("maze.txt", "r")
count = 0
maze = []
row = []

contents = f.readlines()

for line in contents:
    if eval(line):
        row.append(0)
        count += 1
    else:
        row.append(1)
        count += 1
    if count > 50:
        maze.append(row)
        row = []
        count = 0
f.close()
maze = np.rot90(maze).tolist()

#solving the maze
# To prevent out of range coordinate/wall coordinate
while True:
    try:
        # Inputting the start and end point
        x1 = int(input("What is the x-coordinate of the starting point: "))
        y1 = int(input("What is the y-coordinate of the starting point: "))
        x2 = int(input("What is the x-coordinate of the ending point: "))
        y2 = int(input("What is the y-coordinate of the ending point: "))

        # Checking whether coordinate is wall or not
        if maze [y1][x1] == 0 or maze[y2][x2] == 0:
            print()
            print("The point is a wall, please input another point")

        # If coordinate is within the maze boundaries, break
        elif maze [y1][x1] == 1 and maze [y2][x2] == 1:
            start=(x1,y1)
            destination=(x2,y2)
            break

    # Use except function to deal with out of range coordinates
    except:
        print()
        print("Coordinate is out of the range.")
        print()
        print("Please input another coordinates!")

result=DFSsolver(maze, destination, start)
print(result)

#plotting the resulting maze

#changing the value in the maze for coloring the plot
maze_res = maze[:][:]
for point in result:
    #setting value 2 as path in the maze
    maze_res[point[1]][point[0]]=2
#setting value 3 as destination in the maze
maze_res[destination[1]][destination[0]]=3

Cmap1 = col.ListedColormap(["black", "white", "green", "red"])
#plt.xticks([]) #Removing the x axis
#plt.yticks([]) #Removing the y axis
plt.axes().set_aspect('equal')
plt.pcolormesh(maze, cmap=Cmap1)

plt.show()

