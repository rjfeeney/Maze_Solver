from cell import Cell
from window import Window
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                cell = Cell((j * self.cell_size_x),
                            (j * self.cell_size_x) + self.cell_size_x,
                            (i * self.cell_size_y),
                            (i * self.cell_size_y) + self.cell_size_y, self._win)
                column.append(cell)
            self._cells.append(column)
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self._win:
            self._win.redraw()
        time.sleep(.05)

    def break_entrace_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        exit_cell = self._cells[-1][-1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self.num_cols - 1, self.num_rows -1)

    def _in_bounds(self, i, j):
        return i >= 0 and i < self.num_cols and  j >= 0 and j < self.num_rows

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if self._in_bounds(i-1, j) and not self._cells[i-1][j].visited:
                to_visit.append((i-1,j, "above"))
            if self._in_bounds(i+1, j) and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j, "below"))
            if self._in_bounds(i, j-1) and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1, "left"))
            if self._in_bounds(i, j+1) and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1, "right"))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            chosen_index = random.randrange(len(to_visit))
            next_i, next_j, direction = to_visit[chosen_index]
            if direction == "above":
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            elif direction == "below":
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            elif direction == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            elif direction == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            self._break_walls_r(next_i, next_j)
    
    def reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False
    
    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        end_i = self.num_cols - 1
        end_j = self.num_rows - 1
        if i == end_i and j == end_j:
            return True
        if self._in_bounds(i-1, j) and not self._cells[i][j].has_top_wall and not self._cells[i-1][j].visited:
            self._cells[i][j]._draw_move(self._cells[i-1][j])
            if self._solve_r(i-1,j):
                return True
            self._cells[i][j]._draw_move(self._cells[i-1][j], undo=True)
        if self._in_bounds(i+1, j) and not self._cells[i][j].has_bottom_wall and not self._cells[i+1][j].visited:
            self._cells[i][j]._draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            self._cells[i][j]._draw_move(self._cells[i+1][j], undo=True)
        if self._in_bounds(i, j-1) and not self._cells[i][j].has_left_wall and not self._cells[i][j-1].visited:
            self._cells[i][j]._draw_move(self._cells[i][j-1])
            if self._solve_r(i,j-1):
                return True
            self._cells[i][j]._draw_move(self._cells[i][j-1], undo=True)
        if self._in_bounds(i, j+1) and not self._cells[i][j].has_right_wall and not self._cells[i][j+1].visited:
            self._cells[i][j]._draw_move(self._cells[i][j+1])
            if self._solve_r(i,j+1):
                return True
            self._cells[i][j]._draw_move(self._cells[i][j+1], undo=True)
        return False