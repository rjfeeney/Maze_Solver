import unittest
from maze import Maze
from window import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        win = Window(800, 600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

import unittest

class TestMaze(unittest.TestCase):
    def test_reset_cells_visited(self):
        win = Window(800, 600)
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        # Assume maze has a grid structure accessible like maze._cells
        # For testing, you might need to mock or use an existing setup method
        
        # Manually set some cells as visited
        for row in m1._cells:
            for cell in row:
                cell.visited = True
        
        # Call the reset method
        m1.reset_cells_visited()
        
        # Assert all cells have visited set to False
        for row in m1._cells:
            for cell in row:
                self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main()