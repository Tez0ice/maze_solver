from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root,width=self.width,height=self.height)
        self.canvas.pack(fill=BOTH,expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW",self.close) 

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self,line,fill_color):
        line.draw(self.canvas,fill_color)


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line:
    def __init__(self,point_1,point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self,canvas,fill_color):
        canvas.create_line(self.point_1.x,self.point_1.y,self.point_2.x,self.point_2.y,fill=fill_color,width=2)
        canvas.pack(fill=BOTH,expand=1)


class Cell:
    def __init__(self,point1,point2,window,has_left=True,has_top=True,has_bot=True,has_right=True):
        self.__has_left_wall = has_left
        self.__has_right_wall = has_right
        self.__has_top_wall = has_top
        self.__has_bot_wall = has_bot
        self.__x1 = point1.x
        self.__y1 = point1.y
        self.__x2 = point2.x
        self.__y2 = point2.y
        self.__win = window

    def draw(self):
        if self.__has_left_wall:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x1,self.__y2)),"black")
        if self.__has_right_wall:
            self.__win.draw_line(Line(Point(self.__x2,self.__y1),Point(self.__x2,self.__y2)),"black")
        if self.__has_top_wall:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x2,self.__y1)),"black")
        if self.__has_bot_wall:
            self.__win.draw_line(Line(Point(self.__x1,self.__y2),Point(self.__x2,self.__y2)),"black")
