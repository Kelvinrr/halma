from tkinter import *

import random

from board import Board

class Halma(object):
    def __init__(self, size):
        self.board = Board(size)
        self.winner = None
        self.current_turn = 'g'

    def run_command(self, cmd):
        """
        commands must be in the format "b6->c7"
        """
        if self.winner:
            print('The winner is: {}'.format("Red" if self.winner == 'r' else 'Green'))
            return

        src, dst = cmd.split("->")
        src = self.board.coordToXY(src)
        dst = self.board.coordToXY(dst)

        if self.current_turn == 'g' and src in self.board.green_positions:
            self.board.move(dst, src)
        elif self.current_turn == 'r' and src in self.board.red_positions:
            self.board.move(dst, src)
        else:
            print("Invalid Move")
            return

        self.winner = self.board.winCheck()
        self.current_turn = 'r' if self.current_turn == 'g' else 'g'
        if self.winner:
            print('The winner is: {}'.format("Red" if self.winner == 'r' else 'Green'))

if __name__ == "__main__":
    game = Halma(15)
    print(game.current_turn)
