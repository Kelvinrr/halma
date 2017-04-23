class Board(object):

    def __init__(self, w, h):
        self.state = [['x' for x in range(w)] for y in range(h)]

        if w != h:
            raise Exception("Width and height must be equal, got: ", w, h)

        pieces = 5 if w == 8 else 6

        self.width = w
        self.height = h


        startG = []
        startR = []

        for i in range(-pieces+1,0):
            row_len = i + pieces
            for j in range(row_len):
                self.state[i][j] = 'r'
                startG.append((i, j))

        for i in range(-pieces+1,0):
            row_len = i + pieces
            for j in range(row_len):
                self.state[j][i] = 'g'
                startR.append((i, j))

        for c in range(len(self.state)):
            print(self.state[c])


    def winCheck(self, state, startG, startR):

        self.state = state
        self.startG = startG
        self.startR = startR

        if(startG == startR):
            print("Green is the winner!")
            return True

        elif(startR == startG):
            print("Red is the winner!")
            return True

        else:
            print("No one has one yet")
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



board = Board(10, 10)
