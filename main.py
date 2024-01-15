from graphic import Window,Point,Line,Cell,Maze

def main():
    win = Window(800,600)
    # cell1 = Cell(win,has_right=False)
    # cell2 = Cell(win,has_left=False,has_bot=False)
    # cell1.draw(50, 50, 100, 100)
    # cell2.draw(100, 50, 150, 100)
    # cell1.draw_move(cell2)
    maze = Maze(50,50,5,5,50,50,win)
    maze._create_cells()
    # win.draw_line(line,"black") 
    win.wait_for_close()


main()
