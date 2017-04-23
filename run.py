from halma.game import Halma
from halma.gui import HalmaGUI
from tkinter import *

if __name__ == "__main__": # pragma : no cover
        root = Tk()
        game = Halma(5)
        board = game.board
        gui = HalmaGUI(root, game)
        gui.set_board(board)
        root.mainloop()
