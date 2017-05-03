from halma.board import Board
from halma.tree import Tree

class AI(object):
    
    def __init__(self, board):
        self.board = board
    
    def gen_tree(self, team, opp, depth, player, move):
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
                    child = self.gen_tree(opp, teamC, depth - 1, not player, (src, dest))
                    score = minimax(score, child.score) 
                    children.append(child)
        
        return Tree(teams, score, children, move)
