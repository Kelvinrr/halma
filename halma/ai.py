from halma.board import Board
from halma.tree import Tree
import random
import time

nodes = 0
class AI(object):
    def __init__(self, board):
        self.board = board

    def gen_tree(self, depth, team_pos, opp_pos, maxNode, team_info, opp_info, move, prune, alpha, evalFunc, cur_time, max_time):
        global nodes
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
                    child = self.gen_tree(depth - 1, opp_pos, teamC, not maxNode, opp_info, team_info, (src, dest), prune, score, evalFunc, cur_time, max_time)
                    children.append(child)
                    score = minimax(score, child.score)
                    
                    if prune and self.compare(score, alpha) == compVal:
                        return Tree(teams, score, children, move)
        else:
            if time.time() - cur_time > max_time:
                raise ValueError()
            score = evalFunc(opp_info, opp_pos, team_pos)
            nodes = nodes + 1
        return Tree(teams, score, children, move)

    def compare(self, a,b):
        return (a > b) - (b > a)

    def get_optimal_move(self, max_depth, team, opp, max_root, alpha_beta, evalFunc, cur_time, max_time):
        global nodes
        root = None
        deepest_depth = 0
        try:
            for depth in [x for x in range(max_depth + 1) if x % 2 == 1]:
                nodes = 0
                root = self.gen_tree(depth, team.pos, opp.pos, max_root, team, opp, (), alpha_beta, 0 if max_root else float('inf'), evalFunc, cur_time, max_time)
                deepest_depth = depth
        except ValueError:
            pass
        print("Depth: {} Taken {}".format(deepest_depth, time.time() - cur_time))
        print("Alpha beta leaf nodes: {}".format(nodes))
        nodes = 0
        root = self.gen_tree(depth, team.pos, opp.pos, max_root, team, opp, (), False, 0 if max_root else float('inf'), evalFunc, cur_time, max_time)
        print("Non-Alpha beta leaf nodes: {}".format(nodes))
        
        for child in root.children:
            if child.score == root.score:
                return child.move
            
        return ((0,0),(0,0))
