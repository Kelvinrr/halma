from tkinter import *
import re

import random

from board import Board

class Halma(object):
    def __init__(self, size):
        self.board = Board(size)
        self.winner = None
        self.current_turn = 'g'
        self.regExp = re.compile('[a-z]{1}\d{1}->[a-z]{1}\d{1}')

    def run_command(self, cmd):
        """
        commands must be in the format "b6->c7"
        """
        if not cmd:
            return 'Empty Command'

        cmd = cmd.strip().lower()

        if self.winner:
            return 'The winner is: {}'.format("Red" if self.winner == 'r' else 'Green')
        if not self.regExp.match(cmd.strip().lower()):
            return 'Invalid Command'

        src, dst = cmd.split("->")
        src = self.board.coordToXY(src)
        dst = self.board.coordToXY(dst)

        if self.current_turn == 'g' and src in self.board.green_positions:
            self.board.move(dst, src)
        elif self.current_turn == 'r' and src in self.board.red_positions:
            self.board.move(dst, src)
        else:
            return "Invalid Move"

        self.current_turn = 'r' if self.current_turn == 'g' else 'g'
        self.winner = self.board.winCheck()
        if self.winner:
            return 'The winner is: {}'.format("Red" if self.winner == 'r' else 'Green')
        return "Move Successful"

if __name__ == "__main__":
    game = Halma(15)
    print(game.current_turn)
