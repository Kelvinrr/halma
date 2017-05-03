from tkinter import *

import random
from halma.board import Board
from halma.ai import AI

class Halma(object): # pragma: no cover
    def __init__(self, size, time, player, initial_board=None):
        self.board = Board(size, initial_board=initial_board)
        self.ai = AI(self.board)
        self.winner = None
        self.time = time
        self.player = player
        self.current_turn = 'g'
        self.regExp = re.compile('[a-z]{1}\d{1}->[a-z]{1}\d{1}')
        self.cycles = 0

    def get_win_stats(self):
        if not self.winner:
            return None
        red_score = 0
        for red in self.board.red_positions:
            p_score = self.board.calcDistToGoal(red, self.board.green_start)
            red_score += 1/p_score if p_score != 0 else 1

        green_score = 0
        for green in self.board.green_positions:
            p_score = self.board.calcDistToGoal(green, self.board.red_start)
            green_score += 1/p_score if p_score != 0 else 1
        return (self.cycles, green_score, red_score)

    def run_command(self, cmd):
        """
        commands must be in the format "b6->c7"
        """
        def in_camp(to, frm, team):
            return to in team.goal or not frm in team.goal 

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
        
        if (not src in team.pos) or not in_camp(src,dst,team) or (not self.board.move(dst, src, team)):
            return "Invalid Move"

        src, dest = self.ai.get_optimal_move(3, self.board.red.pos, self.board.green.pos, False)
        self.board.move(dest, src, self.board.red)
            
        
        # self.current_turn = 'r' if self.current_turn == 'g' else 'g'
        self.cycles += 1 if self.current_turn == 'g' else 0

        self.winner = self.board.winCheck()
        if self.winner:
            return 'The winner is: {}'.format("Red" if self.winner == 'r' else 'Green')
        return "{}'s Turn".format('Red' if self.current_turn == 'r' else 'Green')
