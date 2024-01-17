from graphic import Window,Point,Line,Cell,Maze

def main():
    win = Window(800,600)
    maze = Maze(50,50,5,5,50,50,win)
    maze._break_entrace_and_exit()
    win.wait_for_close()


main()
