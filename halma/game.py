from tkinter import *

import random
from halma.board import Board
from halma.ai import AI
from time import sleep

class Halma(object): # pragma: no cover
    def __init__(self, size, time, player, initial_board=None):
        self.board = Board(size, initial_board=initial_board)
        self.ai = AI(self.board)
        self.winner = None
        self.time = time - 0.1
        self.player = player
        self.current_turn = 'g'
        self.regExp = re.compile('[a-z]{1}\d{1,2}->[a-z]{1}\d{1,2}')
        self.cycles = 0
        self.ai_team = self.board.green if player != 'g' else self.board.red

    def get_win_stats(self):
        if not self.winner:
            return None
        red_score = 0
        scores = [0,0]
        teams = [self.board.green, self.board.red]
        for i in range(2):
            team = teams[i]
            for pos in team.pos:
                p_score = self.board.calcDistToGoal(pos, team.goal)
                scores[i] += 1/p_score if p_score != 0 else 1

        return (self.cycles, scores[0], scores[1])

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
        team = self.board.green if self.current_turn == 'g' else self.board.red

        if (src not in team.pos) or (not self.board.move(dst, src, team)):
            return "Invalid Move"

        self.current_turn = 'r' if self.current_turn == 'g' else 'g'
        self.cycles += 1 if self.current_turn == 'g' else 0

        self.winner = self.board.winCheck()
        if self.winner:
            return 'The winner is: {}'.format("Red" if self.winner == 'r' else 'Green')
        return "{}'s Turn".format('Red' if self.current_turn == 'r' else 'Green')
