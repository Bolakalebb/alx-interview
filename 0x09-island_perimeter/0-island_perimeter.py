#!/usr/bin/python3
"""This module contains the function island_perimeter problem solution
"""


def island_perimeter(grid):
    """This function returns the perimeter of the island described in grid
    """

    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Start with 4 sides
                
                # Check left and top neighbors
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 for shared side
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 for shared side
    
    return perimeter