class Board(object): # pragma: no cover
    def __init__(self, size, initial_board=None):
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
                self.red_start.add((size + i, j))

        for i in range(-pieces + 1, 0):
            row_len = i + pieces
            for j in range(row_len):
                self.green_start.add((j, size + i))

        if initial_board:
            self.red_positions = set()
            self.green_positions = set()
            for y in range(self.size):
                for x in range(self.size):
                    if initial_board[y][x] == 'g':
                        self.green_positions.add((x,y))
                    elif initial_board[y][x] == 'r':
                        self.red_positions.add((x,y))
        else :
            self.red_positions = self.red_start.copy()
            self.green_positions = self.green_start.copy()

    def __str__(self): # pragma: no cover
        string = ''
        for y in range(self.size):
            l = []
            for x in range(self.size):
                if (x,y) in self.red_positions:
                    l.append('r')
                elif (x,y) in self.green_positions:
                    l.append('g')
                else:
                    l.append('-')
            string += " ".join(l) + "\n"
        return string

    def winCheck(self):
        if (self.green_positions == self.red_start):
            return 'g'
        elif (self.red_positions == self.green_start):
            return 'r'
        else:
            return False

    def move(self, destination, location):
        if not self.is_valid(destination, location):
            return False

        if location in self.red_positions:
            self.red_positions.remove(location)
            self.red_positions.add(destination)
        if location in self.green_positions:
            self.green_positions.remove(location)
            self.green_positions.add(destination)
        return True

    def check_in_bounds(self, pos): # pragma: no cover
        return pos[0] >= 0 and pos[1] >= 0 and pos[0] < self.size and pos[1] < self.size

    def get_jumps(self, dest, visited): # pragma: no cover
        ns = self.get_neighbors(dest)
        visited.add(dest)
        for n in ns:
            pos = (2*n[0] - dest[0], 2*n[1] - dest[1])
            if pos not in (self.red_positions | self.green_positions) and self.check_in_bounds(pos) and (pos not in visited):
                self.get_jumps(pos, visited)
        return visited

    def get_neighbors(self, pos): # pragma: no cover
        ns = set()
        x = pos[0]
        y = pos[1]
        for i in range(-1,2):
            for j in range(-1,2):
                if (not (i == 0 and j == 0)) and self.check_in_bounds((x+i,y+j)) and ((x + i, y + j) in (self.red_positions | self.green_positions)):
                    ns.add((x+i,y+j))
        return ns

    def get_all_valid_moves(self, positions): # pragma: no cover
        valid = set()
        for piece in positions:
            valid = valid | self.get_valid_moves(piece)
        return valid

    # Returns the coordinates of each adjacent valid spot to move
    def get_valid_moves(self, pos): # pragma: no cover

        x = pos[0]
        y = pos[1]
        adj_pos = set()
        row_length = self.size
        col_length = self.size

        # Height / Width of board
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0) and self.check_in_bounds((x+i,y+j)) and ((x + i, y + j) not in (self.red_positions | self.green_positions)):
                    adj_pos.add((x + i, y + j))
        jumps = self.get_jumps((x,y), set())
        if jumps:
            adj_pos = adj_pos | jumps
        return adj_pos

    def is_valid(self, destination, location): # pragma: no cover
        adj_positions = self.get_valid_moves((location[0], location[1]))
        return not destination in (self.red_positions or self.green_positions) and destination in adj_positions


    def xyToCoord(self, x,y):
        if (x,y) >= (self.size, self.size) or (x,y) < (0,0):
            raise Exception("X and Y are out of bounds, got {} {} with size {}"
                            .format(x,y,self.size))

        return chr(x + 97) + str(self.size - y)

    def coordToXY(self, coord):
        coord = coord.strip().lower()
        return (ord(coord[0])-97, self.size - int(coord[1]))

    def calcDistToGoal(self, pos, campPos): # pragma: no cover
        dist = float('inf')
        for cPos in campPos:
            cur_dist = ((cPos[0]-pos[0])**2 + (cPos[1]-pos[1])**2)**(1/2)
            dist = min(dist, cur_dist)
        return dist
