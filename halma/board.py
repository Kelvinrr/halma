# Edit this or whatever

class Board(object):

    def __init__(self, w, h):
        self.state = [[False for x in range(w)] for y in range(h)]

        if w != h:
            raise Exception("Width and height must be equal, got: ", w, h)

        pieces = 5 if w == 5 else 6

        self.width = w
        self.height = h

        for i in range(-pieces+1,0):
            row_len = i + pieces
            for j in range(row_len):
                self.state[i][j] = 'r'

        for i in range(-pieces+1,0):
            row_len = i + pieces
            for j in range(row_len):
                self.state[j][i] = 'g'
