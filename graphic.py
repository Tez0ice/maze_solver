from tkinter import Tk, BOTH, Canvas
import time

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
    def __init__(self,window,has_left=True,has_top=True,has_bot=True,has_right=True):
        self.__has_left_wall = has_left
        self.__has_right_wall = has_right
        self.__has_top_wall = has_top
        self.__has_bot_wall = has_bot
        self.visited = False
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__win = window

    def draw(self,x1,y1,x2,y2): 
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.__has_left_wall:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x1,self.__y2)),"black")
        if self.__has_right_wall:
            self.__win.draw_line(Line(Point(self.__x2,self.__y1),Point(self.__x2,self.__y2)),"black")
        if self.__has_top_wall:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x2,self.__y1)),"black")
        if self.__has_bot_wall:
            self.__win.draw_line(Line(Point(self.__x1,self.__y2),Point(self.__x2,self.__y2)),"black")

    def draw_move(self,to_cell,undo=False):
        initial_mid_x = (self.__x1 + self.__x2) // 2
        initial_mid_y = (self.__y1 + self.__y2) // 2
        initial_mid_x_next = (to_cell.__x1 + to_cell.__x2) // 2
        initial_mid_y_next = (to_cell.__y1 + to_cell.__y2) // 2

        fill_color = "red"
        if undo == True:
            fill_color = "grey"

        # line = Line(Point(initial_mid_x, initial_mid_y), Point(self.__x2, initial_mid_y))
        # self.__win.draw_line(line, fill_color)
        # line = Line(Point(to_cell.__x1, initial_mid_y_next), Point(initial_mid_x_next, initial_mid_y_next))
        # self.__win.draw_line(line, fill_color)


        line = Line(Point(initial_mid_x,initial_mid_y),Point(initial_mid_x_next,initial_mid_y_next))
        self.__win.draw_line(line,"red")
    

class Maze:
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows 
        self._num_cols = num_cols 
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
    
    def _create_cells(self):

        i = self._x1 
        j = self._y1

        for col in range(self._num_cols):
            cell_col = []
            for row in range(self._num_rows):
                cell_col.append([])
            self._cells.append(cell_col)
        
        # for col in range(len(self._cells)):
        #     cell = Cell(self._win)
        #     cell.draw(i,j,i+self._cell_size_x,j)
        #     for row in range(col+1,len(self._cells[col])):
        #         cell.draw(i,j,i+self._cell_size_x,j+self._cell_size_y)
        #         j += self.cell_size_y
        #     i += self.cell_size_x
        
        i = self._x1

        for col in range(len(self._cells)):
            j = self._y1
            self._draw_cell(i,j)
            for row in range(1,len(self._cells[col])):
                self._draw_cell(i,j + self._cell_size_y)
                j += self._cell_size_y
            i += self._cell_size_x

    def _draw_cell(self,i,j):   
        cell = Cell(self._win)
        cell.draw(i, j, self._cell_size_x + i, self._cell_size_y + j)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.5)

