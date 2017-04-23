from tkinter import *

from halma.gui import HalmaGUI
from halma.board import Board

class Halma(object):
    def __init__(self, size):
        self.board = Board(size)
        self.gui = HalmaGUI(Tk(), self.board)
        self.gui.set_board(self.board)
        self.winner = None
        self.current_turn = random.choice(['R', 'G'])
        root.mainloop()

    def run_command(cmd):
        """
        commands must be in the format "b6->c7"
        """
        src, dst = cmd.split("->")
        src = self.board.coordToXY(src)
        dst = self.board.coordToXY(dst)
        self.board.move(src, dst)



if __name__ == "__main__":
    game = Halma(10)
    print(game.current_turn)
