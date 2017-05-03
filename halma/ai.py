from halma.board import Board
from halma.tree import Tree

class AI(object):
    
    def __init__(self, board):
        self.board = board
    
    def gen_tree(self, team, opp, depth, player, move):
        children= set()
        if player:
            teams = (opp, team)
            minimax = min
            score = float('inf')
        else:
            teams = (team, opp)
            minimax = max
            score = 0
        
        sub_tree = Tree(teams, 0, children, move)
        if depth == 0:
            sub_tree.score = 0;
            return tree

        for src in team:
            for dest in board.get_valid_moves(src):
                child = gen_tree(tree, opp, team, depth - 1, not player, (src, dest))
                score = minimax(score, child) 
                children.add(child)
        sub_tree.score = score
        return sub_tree
