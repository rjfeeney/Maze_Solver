from tkinter import Tk, Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_one, point_two):
        self.point_one = point_one
        self.point_two = point_two

    def draw(self,canvas, fill_color):
        x1 = self.point_one.x
        x2 = self.point_two.x
        y1 = self.point_one.y
        y2 = self.point_two.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)
