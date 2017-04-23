from copy import copy

class Board(object):

    def __init__(self, w, h):
        self.state = [['o' for x in range(w)] for y in range(h)]

        if w != h:
            raise Exception("Width and height must be equal, got: ", w, h)
        elif not isinstance(w, int) or not isinstance(h, int):
            raise Exception("Width and height must both be integers, got: {} {}"
                            .format(type(w), type(h)))

        pieces = w//2 + 1

        self.width = w
        self.height = h

        self.red_start = set()
        self.green_start = set()

        for i in range(-pieces+1,0):
            row_len = i + pieces
            for j in range(row_len):
                self.state[i][j] = 'r'
                self.green_start.add((i, j))

        for i in range(-pieces+1,0):
            row_len = i + pieces
            for j in range(row_len):
                self.state[j][i] = 'g'
                self.red_start.add((i, j))

        self.red_positions = self.red_start.copy()
        self.green_positions = self.green_start.copy()

    def __str__(self):
        string = ''
        for c in range(len(self.state)):
            string = string + str(self.state[c]) + '\n'
        return string

    def winCheck(self, green_start, red_start):

        self.red_start = red_start
        self.green_start = green_start

        if(self.green_positions == self.red_start):
            return 'r'
        elif(self.red_positions == self.green_start):
            return 'g'
        else:
            return False

    # Returns the coordinates of each adjacent valid spot to move
    def get_coordinates(self, x, y):

        # Height / Width of board
        row_length = self.width
        col_length = self.height

        def is_valid(destination, location):

            # Generates the possible moves through Cartesian Product
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    else:
                        if is_valid(y + i, x + j):
                            adj_pos.append((y + i, x + j))

            if(destination not in (self.green_positions or self.red_positions)):
                raise Exception("Destination is not a valid move")

            if x >= 0 and y >= 0 and x < col_length and y < row_length:
                return True

            if(location in adj_pos):
                return True

            else:
                return False

        adj_pos = []

        print(adj_pos)
        return adj_pos


board = Board(4, 4)
board.get_coordinates(board.green_positions, 16, 16)
print(board)
print(len(board.green_positions))
