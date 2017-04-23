from tkinter import *

from halma.gui import HalmaGui
from halma.board import Board

def Halma(object):
    def __init__(self, size):
        self.board = Board(size)
        self.gui = HalmaGUI(Tk(), board)
        self.gui.set_board(board.state)
        self.winner = None
        root.mainloop()

    def run_command(cmd):
        """
        commands must be in the format "b6->c7"
        """
        def xyToCoord(x,y):
            return chr(y + 97) + str(self.size - x)

        def coordToXY(coord):
            coord = coord.strip().lower()
            return (ord(coord[0])-97, int(coord[1]))

        src, dst = cmd.split("->")
        src = coordToXY(src)
        dst = coordToXY(dst)
        self.board.move(src, dst)
