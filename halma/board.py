from copy import copy

class Board(object):

    def __init__(self, size):
        self.state = [['o' for x in range(size)] for y in range(size)]

        if not isinstance(size, int):
            raise Exception("Width and height must both be integers, got: {} {}"
                            .format(type(w), type(h)))

        self.size = size
        self.red_start = set()
        self.green_start = set()
        
        self.green_change = set()
        self.red_change = set()

        pieces = size//2 + 1
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

    def winCheck(self, state, startG, startR):
        if(self.green_posisitions == self.red_start):
            return 'r'
        elif(self.red_positions == self.green_start):
            return 'g'
        else:
            return False

    def moveGen(self, currentR, currentG):
        self.currentR = currentR
        self.currentG = currentG

        # Returns the coordinates of each adjacent valid spot to move
        def get_coordinates(board, x, y):

            # Height / Width of board
            row_length = len(board)
            col_length = len(board[0])

        def is_valid(w, h, col_length, row_length):

            if w >= 0 and h >= 0 and w < col_length and h < row_length:
                return True
            else:
                return False

            adj_pos = []

    def xyToCoord(self, x,y):
        return chr(y + 97) + str(self.size - x)

    def coordToXY(self, coord):
        coord = coord.strip().lower()
        return (ord(coord[0])-97, int(coord[1]))


board = Board(16)
print(board)
print(len(board.green_positions))
