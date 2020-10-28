# Graph-Search-Comparative-Analysis

Artifical Intelligence maze solver inspired by Berkeley CS 188 Repository: https://inst.eecs.berkeley.edu/~cs188/sp11/projects/search/search.html
Generates a graph from a maze representation and implements A*, BFS, DFS traversal to generate solution pathways.

Analysis (see Analysis_Report.pdf)
--------
BFS and DFS are exhaustive algorithms but reach solutions in different order, first returned solution not necessarily optimal
A* search uses manhattan distance between regions of maze as heuristic function
Logging is kept of:
  - Generated solution paths and cost
  - The number of nodes expanded during traversal
  - The maximum size of the fringe/exploration frontier

Input/Output
------------
Maze files are represented as 2D image .lay files of the maze to be solved in input/
Input is parsed into graph nodes and traversed
Solutions are exhaustively generated for A*, BFS, DFS algorithms and redrawn onto .lay files of the maze image with the solution path


