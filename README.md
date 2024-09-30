# Island Counter with DFS

This project implements a solution to count the number of islands in a 2D grid using Depth-First Search (DFS).

## Table of Contents
1. [Introduction](#introduction)
2. [How it Works](#how-it-works)
   - [Key Components](#key-components)
3. [DFS Algorithm and Complexity](#dfs-algorithm-and-complexity)
   - [Depth-First Search (DFS)](#depth-first-search-dfs)
   - [Pseudocode Outline](#pseudocode-outline)
   - [Time Complexity](#time-complexity)
   - [Space Complexity](#space-complexity)
4. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Steps](#steps)


## Introduction

Given a 2D grid of '1's (representing land) and '0's (representing water), the program counts the number of distinct islands. An island is a group of adjacent lands connected horizontally or vertically. Islands are considered disconnected if separated by water ('0').

## How it Works

The program uses **Depth-First Search (DFS)** to explore the grid. The basic steps involved are:
1. Loop through each cell in the grid.
2. When a '1' (land) is found that hasn’t been visited, this is the start of a new island. Increment the island count.
3. Use DFS to explore all connected '1's (land) and mark them as visited.
4. Repeat until all cells in the grid have been checked.

### Key Components:
- **`count_islands`**: Counts the number of islands in the grid.
- **`dfs`**: A helper function that performs the depth-first search to explore all land cells connected to the current land.
- **`config.py`**: Stores the movement directions for DFS (down, up, left, right).

## DFS Algorithm and Complexity

### Depth-First Search (DFS)
DFS is a graph traversal algorithm that explores as far as possible along each branch before backtracking. In the context of this problem, the grid can be thought of as a 2D graph where each cell is a node and edges exist between adjacent land cells ('1').

### Pseudocode Outline
1. Start at a land cell ('1').
2. Mark it as visited (either by adding it to a `visited` set or by setting the cell's value to '0' to modify the grid directly).
3. Recursively explore its adjacent cells (up, down, left, right).
4. Repeat the process for each unvisited land cell to ensure all land cells in the island are visited.

### Time Complexity
The time complexity of the DFS algorithm is **O(m * n)**, where:
- `m` is the number of rows in the grid.
- `n` is the number of columns in the grid.

In the worst case, every cell in the grid is visited exactly once. DFS explores all adjacent land cells for each unvisited land cell, making the time complexity proportional to the number of cells in the grid.

### Space Complexity
The space complexity of the DFS algorithm depends on how the "visited" cells are marked and the depth of recursion:
- If a `visited` set is used to track visited cells, the space complexity is **O(m * n)** to store up to `m * n` cells.
- If the grid is modified in place (e.g., by marking visited land cells as '0'), the additional space needed is reduced, and space complexity is **O(1)** for marking cells.
- **Recursive Stack Space**: DFS uses a recursive call stack that can go as deep as the number of cells in the grid in the worst case (all land). Therefore, the space complexity due to recursion is **O(m * n)**.


## Installation
### Prerequisites
- **Python>=3.5**

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/EvelinaAlexiutenko/counting-islands-task.git
    cd counting-islands-task
    ```