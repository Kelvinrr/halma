from tkinter import *

import random

from board import Board

class Halma(object):
    def __init__(self, size):
        self.board = Board(size)
        self.winner = None
        self.current_turn = random.choice(['R', 'G'])

    def run_command(self, cmd):
        """
        commands must be in the format "b6->c7"
        """
        src, dst = cmd.split("->")
        src = self.board.coordToXY(src)
        dst = self.board.coordToXY(dst)
        self.board.move(src, dst)


if __name__ == "__main__":
    game = Halma(15)
    print(game.current_turn)
