from halma.game import Halma
from halma.gui import HalmaGUI
from tkinter import *
import sys
import argparse

def build_board(fh):
        board_list = []
        for line in fh:
                board_list.append(line.strip().split(" "))
        return board_list

if __name__ == "__main__": # pragma : no cover
        parser = argparse.ArgumentParser()
        parser.add_argument('--size', action='store', default=8,
                            help='Size of the board, as <size> x <size>')
        parser.add_argument('--time', action='store', default="30",
                            help='Time per move in seconds.')
        parser.add_argument('--player', action='store', default="g",
                             help='which color is the human player, can be "r" or "g"')
        parser.add_argument('--board', action='store', default=None,
                            help='')


        args = parser.parse_args().__dict__
        print('Starting with settings: {}'.format(args))

        basic_board = None
        if args["board"]:
            basic_board = build_board(open(args["board"],'r'))
            if len(basic_board) != int(args["board"]):
                    print("Size of passed board incorrect")

        root = Tk()
        game = Halma(int(args["size"]), int(args["time"]), args["player"], initial_board=basic_board)
        board = game.board
        gui = HalmaGUI(root, game)
        gui.set_board(board)
        root.mainloop()
