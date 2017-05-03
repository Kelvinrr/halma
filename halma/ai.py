from halma.board import Board
from halma.tree import Tree
import random

class AI(object):
    def __init__(self, board):
        self.board = board
    
    def gen_tree(self, depth, team, opp, player, move):
        children = []
        if player:
            teams = (opp, team)
            minimax = min
            score = float('inf')
        else:
            teams = (team, opp)
            minimax = max
            score = 0

        if not depth == 0:
            for src in team:
                for dest in self.board.get_valid_moves(src):
                    teamC = team.copy()
                    self.board.sub_move(dest,src, teamC)
                    child = self.gen_tree(depth - 1, opp, teamC, not player, (src, dest))
                    score = minimax(score, child.score) 
                    children.append(child)
        else:
            playerRep = 'g' if player else 'r'
            score = random.randint(0,100)
            # score = self.board.dist_to_line(playerRep) + self.board.distToGoal(playerRep) + self.board.minDistToGoal(playerRep)
                    

        return Tree(teams, score, children, move)

    def get_optimal_move(self, depth, team, opp, player):
        root = self.gen_tree(depth, team, opp, player, ())
        for child in root.children:
            if child.score == root.score:
                return child.move
        
