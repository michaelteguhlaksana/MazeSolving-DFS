# MazeSolving-DFS
Maze solving using DFS with plotting using matplotlib. 
This is the result of a mini-project at course MS1008 Intro to Computational Thinking at Nanyang Technological University (year 2019, team 13, T4).
This code is a bit deffective as the default recursion limit can be reached for solving medium sized mazes.
(I tested 50 x 50 maze and some point will reach the recursion limit).
I'm planning to add a non-recursive method instead of using recursion. Feel free to help me improve this program.

This program is built using Python version 3.7

Libraries used:
- numpy -- Apparently the maze given to us in the assignment require flipping to actually use, hence we use the numpy.rot90() 
            to rotate the maze. However, this is unneccesarry by normal standard.
- matplotlib -- For plotting purposes only. Looking at a large array of size 51 x 51 is quite a troublesome thing to do, hence we use plotting
                from matplotlib to handle the trouble
- sys -- For increasing the recursion limit. I'm planning to not use this library by increasing the memory efficiency of the function
                

The Solver
The code consists of a function called DFSsolver. This function is designed to solve a maze and returns the path between the starting point 
to the destination in the form of a list filled by tuples of coordinates.
Ex: [(1,1),(1,2),(1,3),(2,3)]
The input maze has to be in the form of an array/ nested list.
