from copy import copy


class Board(object):
    def __init__(self, size):
        self.state = [['o' for x in range(size)] for y in range(size)]

        if not isinstance(size, int):
            raise Exception("Width and height must both be integers, got: {} {}"
                            .format(type(size), type(size)))

        self.size = size
        self.red_start = set()
        self.green_start = set()

        self.green_change = set()
        self.red_change = set()

        pieces = size // 2 + 1
        for i in range(-pieces + 1, 0):
            row_len = i + pieces
            for j in range(row_len):
                self.state[i][j] = 'r'
                self.red_start.add((size + i, j))

        for i in range(-pieces + 1, 0):
            row_len = i + pieces
            for j in range(row_len):
                self.state[j][i] = 'g'
                self.green_start.add((j, size + i))

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

        if (self.green_positions == self.red_start):
            return 'r'
        elif (self.red_positions == self.green_start):
            return 'g'
        else:
            return False

    def move(self, destination, location):
        if location in self.red_positions:
            self.red_positions.remove(location)
            self.red_positions.add(destination)
        if location in self.green_positions:
            self.green_positions.remove(location)
            self.green_positions.add(destination)
        self.state[destination[0]][destination[1]] = self.state[location[0]][location[1]]
        self.state[location[0]][location[1]] = "o"

        # Returns the coordinates of each adjacent valid spot to move
        def get_coordinates(self, x, y):

            # Height / Width of board
            row_length = self.width
            col_length = self.height
            adj_pos = []

            def is_valid(self, destination, location):


                # Generates the possible moves through Cartesian Product
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        else:
                            if is_valid(y + i, x + j):
                                adj_pos.append((y + i, x + j))

                if (destination not in (self.green_positions or self.red_positions)):
                    raise Exception("Destination is not a valid move")

                if x >= 0 and y >= 0 and x < col_length and y < row_length:
                    return True

                if (location in adj_pos):
                    self.move(self, destination, location)
                    return True

                else:
                    return False

            return adj_pos

    def xyToCoord(self, x,y):
        return chr(y + 97) + str(self.size - x)

    def coordToXY(self, coord):
        coord = coord.strip().lower()
        return (ord(coord[0])-97, self.size - int(coord[1]))

if __name__ == "__main__":
    board = Board(16)
    print(board)
    print(len(board.green_positions))
    print(board.green_positions)
    print(board.red_positions)

    arr = [['o' for x in range(16)] for y in range(16)]
    for pos in board.green_positions:
        arr[pos[0]][pos[1]] = 'g'
    print(arr)
