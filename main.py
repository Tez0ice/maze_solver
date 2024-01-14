from graphic import Window,Point,Line,Cell

def main():
    win = Window(800,600)
    cell1 = Cell(win,has_right=False)
    cell2 = Cell(win,has_left=False,has_bot=False)
    cell1.draw(50, 50, 100, 100)
    cell2.draw(100, 50, 150, 100)
    cell1.draw_move(cell2)
    # win.draw_line(line,"black") 
    win.wait_for_close()


main()
