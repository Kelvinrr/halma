from halma.board import Board
from halma.tree import Tree
import random

class AI(object):
    def __init__(self, board):
        self.board = board

    def gen_tree(self, depth, team_pos, opp_pos, maxNode, team_info, opp_info, move, prune, alpha):
        children = []
        if maxNode:
            teams = (team_pos, opp_pos)
            minimax = max
            compVal = -1
            score = 0
        else:
            teams = (opp_pos, team_pos)
            minimax = min
            compVal = 1
            score = float('inf')

        if not depth == 0:
            for src in team_pos:
                for dest in self.board.get_valid_moves(src, team_info):
                    teamC = team_pos.copy()
                    self.board.sub_move(dest, src, team_info, teamC)
                    child = self.gen_tree(depth - 1, opp_pos, teamC, not maxNode, opp_info, team_info, (src, dest), prune, score)
                    children.append(child)
                    score = minimax(score, child.score)
                    if prune and self.compare(score, alpha) == compVal:
                        return Tree(teams, score, children, move)
        else:
            score = self.board.minDistToGoalPoint(team_info, team_pos) if maxNode\
                else self.board.minDistToGoalPoint(opp_info, opp_pos)
            # score = self.board.dist_to_line(playerRep) + self.board.distToGoal(playerRep) + self.board.minDistToGoal(playerRep)


        return Tree(teams, score, children, move)

    def compare(self, a,b):
        return (a > b) - (b > a)

    def get_optimal_move(self, depth, team, opp, max_root, alpha_beta):
        root = self.gen_tree(depth, team.pos, opp.pos, max_root, team, opp, (), alpha_beta, 0 if max_root else float('inf'))
        for child in root.children:
            if child.score == root.score:
                return child.move
        return ((0,0),(0,0))
