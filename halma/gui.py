from tkinter import *
from halma.board import Board

class HalmaGUI(Frame):

    def __init__(self, root, board_size, **options):
        super().__init__(root)
        self.root = root
        self.pack(expand=YES,fill=BOTH)
        self._places = []
        self._banner = StringVar()
        self._banner.set("TESTING")

        upper_frame = Frame(self)
        banner = Label(upper_frame, text='', textvariable=self._banner, height=2, width=5, padx=30, bg="#FFFFFF")
        banner.pack(side=LEFT, expand=YES,fill=BOTH)

        game_frame = Frame(self)
        for row in range(board_size):
            self._places.append([])
            for col in range(board_size):
                backg = "#505050"
                label = Label(game_frame, text='', bg=backg)
                self._places[row].append(label)
                label.grid(row=row,column=col, stick='nsew')
                game_frame.columnconfigure(col,weight=1)
            game_frame.rowconfigure(row,weight=1)

        lower_frame = Frame(self)

        def handle_entry(event):
            if event.widget.get():
                print(event.widget.get())
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

    def set_board(self, board):
        for row in range(len(board)):
            for col in range(len(board)):
                widget = self._places[row][col]

                if board[row][col] == 'g':
                    widget.config(bg="#20FF20")
                elif board[row][col] == 'r':
                    widget.config(bg="#FF2020")
                else:
                    widget.config(bg="#505050")

def main():
    root = Tk()
    size = 15
    gui = HalmaGUI(root, size)
    board = Board(15,15)
    print(board.state)
    gui.set_board(board.state)
    root.mainloop()

if __name__ == "__main__":
    main()
