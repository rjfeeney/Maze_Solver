from tkinter import Tk, Canvas
from window import Window
from point import Line, Point

class Cell:
    def __init__(self, x1, x2, y1, y2, win):
        self.has_top_wall = True
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.visited = False
    
    def get_center(self):
        return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
    
    def draw(self):
        if self._win:
            top_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            if self.has_top_wall:
                self._win.draw_line(top_line, "black")
            else:
                self._win.draw_line(top_line, "white")
            left_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            if self.has_left_wall:
                self._win.draw_line(left_line, "black")
            else:
                self._win.draw_line(left_line, "white")
            right_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            if self.has_right_wall:
                self._win.draw_line(right_line, "black")
            else:
                self._win.draw_line(right_line, "white")
            bottom_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            if self.has_bottom_wall:
                self._win.draw_line(bottom_line, "black")
            else:
                self._win.draw_line(bottom_line, "white")
    
    def _draw_move(self, to_cell, undo=False):
        center_line = Line(self.get_center(), to_cell.get_center())
        if undo == False:
            self._win.draw_line(center_line, "red")
        else:
            self._win.draw_line(center_line, "gray")