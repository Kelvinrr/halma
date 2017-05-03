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

        if initial_board:
            red_positions = set()
            green_positions = set()
            for y in range(self.size):
                for x in range(self.size):
                    if initial_board[y][x] == 'g':
                        green_positions.add((x,y))
                    elif initial_board[y][x] == 'r':
                        red_positions.add((x,y))
        else :
            red_positions = red_start.copy()
            green_positions = green_start.copy()

        self.red = (red_positions, red_start, green_start, 'r')
        self.green = (green_positions, green_start, red_start, 'g')
        

    def __str__(self): # pragma: no cover
        string = ''
        for y in range(self.size):
            l = []
            for x in range(self.size):
                found = False
                for team in [self.red, self.green]:
                    if (x,y) in team[0]:
                        l.append(team[4])
                        found = True
                if not found:
                    l.append('-')
            string += " ".join(l) + "\n"
        return string

    def winCheck(self):
        for team in [self.red, self.green]:
            if team[0] == team[3]:
                return team[4]
        return False

    def move(self, destination, location, team):
        if location in team[0] and self.is_valid(destination, location):
            team[0].remove(location)
            team[0].add(destination)
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
        for piece in team[0]:
            valid |= self.get_valid_moves(piece)
        return valid

    # Returns the coordinates of each adjacent valid spot to move
    def get_valid_moves(self, pos): # pragma: no cover
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
        if jumps and len(jumps) > 1:
            adj_pos |= jumps
        return adj_pos

    def is_valid(self, destination, location): # pragma: no cover
        adj_positions = self.get_valid_moves((location[0], location[1]))
        return not destination in (self.red[0] or self.green[0]) and destination in adj_positions


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
