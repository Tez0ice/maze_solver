from graphic import Window,Point,Line,Cell

def main():
    win = Window(800,600)
    point_1 = Point(10,50)
    point_2 = Point(50,10)
    line = Line(point_1,point_2)
    cell = Cell(point_1,point_2,win)
    cell.draw()
    # win.draw_line(line,"black") 
    win.wait_for_close()

main()
