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

    def winCheck(self, green_start, red_start):

        self.red_start = red_start
        self.green_start = green_start

        if(self.green_positions == self.red_start):
            return 'r'
        elif(self.red_positions == self.green_start):
            return 'g'
        else:
            return False

<<<<<<< HEAD
    # Returns the coordinates of each adjacent valid spot to move
    def get_coordinates(self, x, y):

        # Height / Width of board
        row_length = self.width
        col_length = self.height
=======
    def moveGen(self, currentR, currentG):
        self.currentR = currentR
        self.currentG = currentG
>>>>>>> 0776e6d1429695272d01fbbd4ab2941d26c16340

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


<<<<<<< HEAD
board = Board(4, 4)
board.get_coordinates(board.green_positions, 16, 16)
=======
    def xyToCoord(self, x,y):
        return chr(y + 97) + str(self.size - x)

    def coordToXY(self, coord):
        coord = coord.strip().lower()
        return (ord(coord[0])-97, int(coord[1]))


board = Board(16)
>>>>>>> 0776e6d1429695272d01fbbd4ab2941d26c16340
print(board)
print(len(board.green_positions))
