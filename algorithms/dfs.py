from typing import List, Set, Tuple

from cfg import DIRECTIONS


def dfs(
    matrix: List[List[int]], row: int, col: int, visited: Set[Tuple[int, int]]
) -> None:
    """
    Perform Depth First Search (DFS) to mark connected land (1's) as visited.

    Parameters:
        matrix (List[List[int]]): The map matrix being processed.
        row (int): Current row index.
        col (int): Current column index.
        visited (Set[Tuple[int, int]]): Set to track visited cells.
    """
    # Mark the current cell as visited
    visited.add((row, col))

    # Directions: down, up, left, right
    for dr, dc in DIRECTIONS:
        new_row = row + dr
        new_col = col + dc

        # Check if the new position is within bounds and it is an island
        if (
            0 <= new_row < len(matrix)
            and 0 <= new_col < len(matrix[0])
            and (new_row, new_col) not in visited
            and matrix[new_row][new_col] == 1
        ):
            dfs(matrix, new_row, new_col, visited)
