# 0x1C-island_perimeter
This interview algorithm project represents an island as a grid of integers. The list of list of integers contains 0s, that represent water, and 1s, that represent land.  Each cell in the grid is a square with side length of 1.  Cells are connected horizontally/vertically (not diagonally).  The grid itself is rectangular, with its width and height not exceeding 100.  The grid is completely surrounded by water.  There is either one island or nothing in the grid.  There are no "lakes" (water inside that isn't connected to the water surrounding the island).

[Island Perimeter](/0x1C-island_perimeter/0-island_perimeter.py)
* Write a function in Python `def island_perimeter(grid)` that finds the perimeter of the island represented by the given grid:
  * The grid is a list of list of integers:
    * 0s represent water
    * 1s represent land
    * Each cell is a square with side length of 1
    * Cells are connected horizontally/vertically (not diagonally)
  * The grid is completely surrounded by water.
  * There is only one island (or nothing).
  * The island doesn't have water inside that isn't connected to the water surrounding the island.

### test_files
The [test_files](/0x1C-island_perimeter/test_files/) directory contains files used to test the output of the algorithm locally.
