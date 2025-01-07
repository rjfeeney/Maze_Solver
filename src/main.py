from window import Window
from point import Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(x1=0, y1=0, num_rows=10, num_cols=10, cell_size_x=20, cell_size_y=20, win=win)
    maze._create_cells()
    maze._break_walls_r(0, 0)
    maze.break_entrace_and_exit()
    maze.reset_cells_visited()
    maze.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()