from tkinter import Tk, BOTH, Canvas
import time

class Window:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root,width=self.width,height=self.height,background="white")
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
    def __init__(self,window=None,has_left=True,has_top=True,has_bot=True,has_right=True):
        self._has_left_wall = has_left
        self._has_right_wall = has_right
        self._has_top_wall = has_top
        self._has_bot_wall = has_bot
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window

    def draw(self,x1,y1,x2,y2):
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self._win is None:
            return

        if self._has_left_wall:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x1,self._y2)),"black")
        else:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x1,self._y2)),"white")
            
        if self._has_right_wall:
            self._win.draw_line(Line(Point(self._x2,self._y1),Point(self._x2,self._y2)),"black")
        else:
            self._win.draw_line(Line(Point(self._x2,self._y1),Point(self._x2,self._y2)),"white")

        if self._has_top_wall:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x2,self._y1)),"black")
        else:
            self._win.draw_line(Line(Point(self._x1,self._y1),Point(self._x2,self._y1)),"white")

        if self._has_bot_wall:
            self._win.draw_line(Line(Point(self._x1,self._y2),Point(self._x2,self._y2)),"black")
        else:
            self._win.draw_line(Line(Point(self._x1,self._y2),Point(self._x2,self._y2)),"white")


    def draw_move(self,to_cell,undo=False):
        if self._win is None:
            return

        initial_mid_x = (self._x1 + self._x2) // 2
        initial_mid_y = (self._y1 + self._y2) // 2
        initial_mid_x_next = (to_cell._x1 + to_cell._x2) // 2
        initial_mid_y_next = (to_cell._y1 + to_cell._y2) // 2

        fill_color = "red"
        if undo == True:
            fill_color = "grey"

        # line = Line(Point(initial_mid_x, initial_mid_y), Point(self.__x2, initial_mid_y))
        # self.__win.draw_line(line, fill_color)
        # line = Line(Point(to_cell.__x1, initial_mid_y_next), Point(initial_mid_x_next, initial_mid_y_next))
        # self.__win.draw_line(line, fill_color)


        line = Line(Point(initial_mid_x,initial_mid_y),Point(initial_mid_x_next,initial_mid_y_next))
        self._win.draw_line(line,"red")


class Maze:
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows 
        self._num_cols = num_cols 
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()
        self._break_entrace_and_exit()
    
    def _create_cells(self):

        for col in range(self._num_cols):
            cell_col = []
            for row in range(self._num_rows):
                cell_col.append(Cell(self._win))
            self._cells.append(cell_col)
        
        for i,col in enumerate(self._cells):
            for j,rows in enumerate(col):
                x = self._x1 + (i*self._cell_size_x)
                y = self._y1 + (j*self._cell_size_y)
                self._draw_cell(rows,x,y)

    def _draw_cell(self,cell,i,j):
        cell.draw(i, j, self._cell_size_x + i, self._cell_size_y + j)
        self._animate()

    def _animate(self):

        if self._win is None:
            return None

        self._win.redraw()
        time.sleep(0.1)

    def _break_entrace_and_exit(self):
        top_cell = self._cells[0][0]
        bot_cell = self._cells[-1][-1]
        top_cell._has_top_wall = False
        bot_cell._has_bot_wall = False
        self._draw_cell(top_cell,top_cell._x1,top_cell._y1)
        self._draw_cell(bot_cell,bot_cell._x1,bot_cell._y1)


