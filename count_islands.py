from typing import List, Set, Tuple

from algorithms.dfs import dfs

def count_islands(grid: List[List[int]]) -> int:
    """
    Counts the number of islands in a given grid where '1' represents land and '0' represents water.
    
    Parameters:
        grid (List[List[int]]): 2D list representing a map of '1's (land) and '0's (water)
    
    Returns:
        int: Number of islands
    """
    
    # Edge case: if grid is empty
    if not grid or not grid[0]:
        return 0
    
    visited: Set[Tuple[int, int]] = set()  # Set to keep track of visited cells
    island_count = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited and grid[i][j] == 1:
                dfs(grid, i, j, visited)
                island_count += 1
                
    return island_count