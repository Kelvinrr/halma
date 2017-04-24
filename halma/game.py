from tkinter import *

import random
from halma.board import Board

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
        def in_camp(to, frm):
            invalid = [False, True]
            red = [(to in self.board.red_start), (frm in self.board.red_start)]
            green = [(to in self.board.green_start), (frm in self.board.green_start)]
            return not red == invalid if self.current_turn == 'r' else not green == invalid

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
        if self.current_turn == 'g' and src in self.board.green_positions and in_camp(src,dst):
            if not self.board.move(dst, src):
                return "Invalid Move"
        elif self.current_turn == 'r' and src in self.board.red_positions and in_camp(src,dst):
            if not self.board.move(dst, src):
                return "Invalid Move"
        else:
            return "Invalid Move"

        self.current_turn = 'r' if self.current_turn == 'g' else 'g'

        self.winner = self.board.winCheck()
        if self.winner:
            return 'The winner is: {}'.format("Red" if self.winner == 'r' else 'Green')
        return "{}'s Turn".format('Red' if self.current_turn == 'r' else 'Green')
