from collections import namedtuple
from halma import utils

import random as rand
import numpy as np
import math


Team = namedtuple('Team', ['pos', 'start','goal','player', 'goalTile'])

class Board(object): # pragma: no cover
    def __init__(self, size, initial_board=None):
        if not isinstance(size, int):
            raise Exception("Width and height must both be integers, got: {} {}"
                            .format(type(size), type(size)))

        self.size = size

        red_start = set()
        green_start = set()

        green_change = set()
        red_change = set()

        pieces = size // 2 + 1
        if size == 5:
            pieces = 5

        for i in range(-pieces + 1, 0):
            row_len = i + pieces
            for j in range(row_len):
                red_start.add((size + i, j))

        for i in range(-pieces + 1, 0):
            row_len = i + pieces
            for j in range(row_len):
                green_start.add((j, size + i))

        red_goal_p = (0, self.size-1) if (self.size-1, 0) in red_start else (self.size-1, 0)
        green_goal_p = (red_goal_p[1], red_goal_p[0])

        if initial_board:
            red_positions = set()
            green_positions = set()
            for y in range(self.size):
                for x in range(self.size):
                    if initial_board[y][x] == 'g':
                        green_positions.add((x, y))
                    elif initial_board[y][x] == 'r':
                        red_positions.add((x, y))
        else:
            red_positions = red_start.copy()
            green_positions = green_start.copy()

        self.red = Team(red_positions, red_start, green_start, 'r', red_goal_p)
        self.green = Team(green_positions, green_start, red_start, 'g', green_goal_p)

    def __str__(self): # pragma: no cover
        string = ''
        for y in range(self.size):
            l = []
            for x in range(self.size):
                found = False
                for team in [self.red, self.green]:
                    if (x,y) in team.pos:
                        l.append(team.player)
                        found = True
                if not found:
                    l.append('-')
            string += " ".join(l) + "\n"
        return string

    def winCheck(self):
        for team in [self.red, self.green]:
            if team.pos == team.goal:
                return team.player
        return False

    def move(self, destination, location, team):
        return self.sub_move(destination, location, team, team.pos)

    def sub_move(self, destination, location, team, team_pos):
        if location in team_pos and self.is_valid(destination, location, team):
            team_pos.remove(location)
            team_pos.add(destination)
            return True
        return False


    def check_in_bounds(self, pos): # pragma: no cover
        return pos[0] >= 0 and pos[1] >= 0 and pos[0] < self.size and pos[1] < self.size

    def get_jumps(self, dest, visited): # pragma: no cover
        ns = self.get_neighbors(dest)
        visited.add(dest)
        for n in ns:
            pos = (2*n[0] - dest[0], 2*n[1] - dest[1])
            if pos not in (self.red[0] | self.green[0]) and self.check_in_bounds(pos) and (pos not in visited):
                self.get_jumps(pos, visited)
        return visited

    def get_neighbors(self, pos): # pragma: no cover
        ns = set()
        for i in range(-1,2):
            for j in range(-1,2):
                nx = pos[0] + i
                ny = pos[1] + j
                if (not (i == 0 and j == 0)) and self.check_in_bounds((nx,ny)) and ((nx, ny) in (self.red[0] | self.green[0])):
                    ns.add((nx,ny))
        return ns

    def get_all_valid_moves(self, team): # pragma: no cover
        valid = set()
        for piece in team.pos:
            valid.add((piece, self.get_valid_moves(piece, team)))
        return valid

    # Returns the coordinates of each adjacent valid spot to move
    def get_valid_moves(self, pos, team): # pragma: no cover
        adj_pos = set()
        row_length = self.size
        col_length = self.size

        # Height / Width of board
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_x = pos[0] + i
                new_y = pos[1] + j
                if not (i == 0 and j == 0) and self.check_in_bounds((new_x,new_y)) and ((new_x, new_y) not in (self.red[0] | self.green[0])):
                    adj_pos.add((new_x, new_y))

        jumps = self.get_jumps((pos[0],pos[1]), set())
        jumps.remove((pos[0],pos[1]))
        if jumps:
            adj_pos |= jumps
        if pos in team.goal:
            adj_pos &= team.goal
        elif pos not in team.start:
            adj_pos -= team.start
        return adj_pos

    def is_valid(self, destination, location, team): # pragma: no cover
        adj_positions = self.get_valid_moves((location[0], location[1]), team)
        valid_camp = (destination not in team.start and location in team.start) or (destination in team.goal or location not in team.goal)
        return not destination in (self.red[0] or self.green[0]) and destination in adj_positions and valid_camp


    def xyToCoord(self, x,y):
        if (x,y) >= (self.size, self.size) or (x,y) < (0,0):
            raise Exception("X and Y are out of bounds, got {} {} with size {}"
                            .format(x,y,self.size))

        return chr(x + 97) + str(self.size - y)

    def coordToXY(self, coord):
        coord = coord.strip().lower()
        return (ord(coord[0])-97, self.size - int(coord[1:]))

    def moveToString(self, src, dest):
        return self.xyToCoord(src[0],src[1]) + "->" + self.xyToCoord(dest[0], dest[1])

    def calcDistToGoal(self, pos, campPos): # pragma: no cover
        dist = float('inf')
        for cPos in campPos:
            cur_dist = ((cPos[0]-pos[0])**2 + (cPos[1]-pos[1])**2)**(1/2)
            dist = min(dist, cur_dist)
        return dist

    def evaluation(self, point_one, point_two):
        sumSquares = 0
        for point in point_one:
            sumSquares = sumSquares + (((point_two[0] - point[0])**2) + ((point_two[1] - point[1]))**2)
        return sumSquares

    def calculate_line(self, x, y):
        #  P1(0, size) P2(size, 0)

        x_diff = self.size - 1
        y_diff = -(self.size - 1)

        numerator = abs(y_diff*x - (x_diff*y) + ((self.size - 1)**2))
        denominator = math.sqrt(y_diff**2 + x_diff**2)
        distance = numerator/denominator
        return distance


    def dist_to_line(self, team, team_pos, opp_pos):
        score = utils.line_score(team_pos, self.red.goalTile, self.green.goalTile)
        return 1/math.sqrt(score) if score != 0 else 1
        # sumLineSquare = 0
        # if(player == 'r'):
        #     for point in self.red[0]:
        #         minDist = 0
        #         for move in self.get_valid_moves(point):
        #             if(minDist < self.calculate_line(move[0], move[1])):
        #                 minDist = self.calculate_line(move[0], move[1])
        #         distance = minDist
        #         sumLineSquare += distance**2
        #     return sumLineSquare
        #
        # if(player == 'g'):
        #     for point in self.green[0]:
        #         distance = self.calculate_line(point[0], point[1])
        #         sumLineSquare = distance ** 2
        #     return sumLineSquare
        # else:
        #     print("Invalid Player")


    def distToGoal(self, player):
        if (player == 'r'):
            return self.evaluation(self.red[0], self.red_goal)
        if (player == 'g'):
            return self.evaluation(self.green[0], self.green_goal)

    # Generates best min possible move and returns the sum of all of least min

    # TEMP H-FUNCTION FOR TESTING!
    def minDistToGoalPoint(self, team, team_pos):
        def eval_dist(p1, p2):
            return (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2

        sumLineSquare = 0
        for piece in team_pos:
            bonus = 5 if piece in team.goal else 0
            dist = eval_dist(piece, team.goalTile)
            if dist == 0:
                dist = 0.5
            sumLineSquare += 1/dist + bonus
        return sumLineSquare

    def num_pieces_in_goal(self, team, team_pos, opp_pos):
        num = len([pos for pos in team_pos if pos in team.goal])
        return num * 100

    def maxDistToGoal(self, team, team_pos, opp_pos):
        score = utils.camp_score(team_pos,utils.filter_camp(team, team_pos, opp_pos))
<<<<<<< HEAD
        return 1/score if score != 0 else .0001
=======
        return 1/math.sqrt(score) if score != 0 else 2

    def randomGoal(self, team, team_pos, opp_pos):
        return rand.randint(0, 100)
>>>>>>> 6fd06228ceadd5775ded5d1db33daa6216e73bb6
