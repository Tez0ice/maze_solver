from graphic import Window,Point,Line,Cell,Maze

def main():
    win = Window(800,600)
    maze = Maze(50,50,10,10,50,50,win)
    win.wait_for_close()


main()
