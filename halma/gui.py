from board import Board
from game import Halma
from tkinter import *

class HalmaGUI(Frame):

    def __init__(self, root, game, **options):
        super().__init__(root)
        self.root = root
        self.pack(expand=YES,fill=BOTH)
        self._places = []
        self._banner = StringVar()
        self._banner.set("TESTING")
        self._cur_move = ""
        board = game.board
        board_size = board.size

        upper_frame = Frame(self)
        banner = Label(upper_frame, text='', textvariable=self._banner, height=2, width=5, padx=30, bg="#FFFFFF")
        banner.pack(side=LEFT, expand=YES,fill=BOTH)

        piece_config = {'width': 5, 'height': 2, 'foreground': 'black', 'borderwidth': 1, 'relief': GROOVE}

        game_frame = Frame(self)
        piece_frame = Frame(game_frame)
        
        game_frame.rowconfigure(0, weight=1)
        game_frame.columnconfigure(0, weight=1)
        for row in range(board_size):
            label = Label(game_frame, text=str(board_size-row))
            label.grid(row=row+1, column=0, stick='nsew')
            game_frame.rowconfigure(row+1, weight=1)
                
        for col in range(board_size):
            label = Label(game_frame, text=chr(col+65))
            label.grid(row=0, column=col+1, stick='nsew')
            game_frame.columnconfigure(col+1, weight=1)


        piece_frame.grid(row=1,column=1,rowspan=board_size,columnspan=board_size, stick='nsew')

        def handle_label(x,y):
            def _handle_label(event):
                label = (board.xyToCoord(x,y), event.widget)
                if self._cur_move:
                    cmd = self._cur_move[0] + "->" + label[0]
                    print(cmd)
                    self.set_board(game.board)
                    game.run_command(cmd)
                    self._cur_move[1].config(state=NORMAL)
                    self._cur_move = None
                else:
                    self._cur_move = label
                    label[1].config(state=ACTIVE)

            return _handle_label
                
                
        for row in range(board_size):
            self._places.append([])
            for col in range(board_size):
                backg = "#505050"
                label = Label(piece_frame, text='', bg=backg, **piece_config)
                label.bind("<Button-1>", handle_label(row, col))
                self._places[row].append(label)
                label.grid(row=row,column=col, stick='nsew')
                piece_frame.columnconfigure(col,weight=1)
            piece_frame.rowconfigure(row,weight=1)

        lower_frame = Frame(self)

        def handle_entry(event):
            if event.widget.get():
                cmd = event.widget.get()
                print(cmd)
                game.run_command(cmd)

                event.widget.delete(0,END)

        def quit_command():
            exit(0)
        
        entry = Entry(lower_frame)
        entry.pack(side=TOP, expand=YES,fill=X)
        entry.bind("<Return>", handle_entry)
        qButton = Button(lower_frame, text="quit", command=quit_command)
        qButton.pack(side=TOP, expand=YES)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5)
        self.rowconfigure(2, weight=1)

        self.columnconfigure(0, weight=1)

        upper_frame.grid(row=0,column=0,stick="nswe")
        game_frame.grid(row=1,column=0,stick="nswe")
        lower_frame.grid(row=2,column=0,stick="nswe")
        self.set_board(board)

    def set_board(self, board):
        for row in range(board.size):
            for col in range(board.size):
                widget = self._places[row][col]
                if (col,row) in board.green_positions:
                    widget.config(bg="#20FF20")
                elif (col, row) in board.red_positions:
                    widget.config(bg="#FF2020")
                else:
                    widget.config(bg="#505050")
                    
    def update_board(self, board):
        for row in range(len(board)):
            for col in range(len(board)):
                widget = self._places[row][col]
                
                if board[row][col] == 'g':
                    widget.config(bg="#20FF20")
                elif board[row][col] == 'r':
                    widget.config(bg="#FF2020")
                else:
                    widget.config(bg="#505050")

    def set_banner(self, text):
        self._banner.set(text)
        

def main():
    root = Tk()
    size = 15
    game = Halma(size)
    board = game.board
    gui = HalmaGUI(root, game)
    gui.set_board(board)
    root.mainloop()

if __name__ == "__main__":
    main()
