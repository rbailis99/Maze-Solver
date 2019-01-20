# Maze Solver

This project is an adaptation of the age-old routing problem. This CSCI204 project was broken into two phases, which allowed us to test two different implementations. For Phase 1, the implementation of choice was recursion, but this was often computationally difficult as a new maze had to be created each time. During Phase 2, we were able to use a stack. While the concept was largly the same, the implementation and the resultant output was a bit different. The difference in shell output can be noticed [here](./docs/).

In order to run the maze solver, download the repository and run  [mouse.py] (./mouse.py). The user will be asked to enter '1', '2', or '3' which will open one of three pre-generated mazes. If you would like a randonly generated maze, type 'none'. Then input the starting row and column and the ending row and column. If any of the given coordinates are invalid, you will be prompted to reconcider. Finaly, the program will display the path. 

### Reading the maze
Example output
```
 012345678901
0************
1***!!!!*****
2***!**!!****
3***!!!*!!***
4*****!**!***
5*****!**!***
6*****!******
7*****!!!****
8****  *!****
9*   **!!****
0* * !!!*****
1************
```
- '*' indicates there is a wall
- ' ' indicates there is an opening
- '!' indicates a portion of the solved maze
