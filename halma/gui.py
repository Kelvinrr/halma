import sys
import os
import time

from halma.board import Board
from halma.game import Halma
from tkinter import *

class HalmaGUI(Frame): # pragma: no cover

    def __init__(self, root, game, **options):
        super().__init__(root)
        self.game = game
        self.root = root
        self.pack(expand=YES, fill=BOTH)
        self._places = []
        self._banner = StringVar()
        self._banner.set("Game Start")
        self._cur_move = ""
        self._last_move = None

        board = game.board
        board_size = board.size

        upper_frame = Frame(self)
        banner = Label(upper_frame, text='', textvariable=self._banner, height=2, width=5, padx=30, bg="#FFFFFF")
        banner.pack(side=LEFT, expand=YES,fill=BOTH)

        piece_config = {'width': 5, 'height': 2, 'foreground': 'black', 'borderwidth': 1, 'relief': GROOVE}

        game_frame = Frame(self)
        piece_frame = Frame(game_frame)

        game_frame.rowconfigure(0, weight=0, minsize=10)
        game_frame.columnconfigure(0, weight=0, minsize=10)
        for row in range(board_size):
            label = Label(game_frame, text=str(board_size-row))
            label.grid(row=row+1, column=0, stick='ns')
            game_frame.rowconfigure(row+1, weight=1)

        for col in range(board_size):
            label = Label(game_frame, text=chr(col+65))
            label.grid(row=0, column=col+1, stick='ew')
            game_frame.columnconfigure(col+1, weight=1)

        piece_frame.grid(row=1,column=1,rowspan=board_size,columnspan=board_size, stick='nsew')

        def handle_label(x,y):
            def adjust_bg(widget, func):
                widget.config(bg="#%02x%02x%02x" % tuple(map(func, widget.winfo_rgb(widget.cget("bg")))))

            def _handle_label(event):
                label = (board.xyToCoord(x,y), event.widget)
                if self._cur_move:
                    self.set_board(self.game.board)
                    cmd = self._cur_move[0] + "->" + label[0]
                    report = handle_command(cmd)
                    self._cur_move[1].config(state=NORMAL)

                    print("Turn" in report)
                    if "Turn" in report:
                        
                        adjust_bg(self._cur_move[1], lambda x: x//2)
                        adjust_bg(label[1], lambda x: x//2)
                        self._last_move = (self._cur_move[1], label[1])
                    else:
                        self._last_move = None

                    self._cur_move = None
                    self.after(100, ai_play)
                else:
                    self._cur_move = label
                    label[1].config(state=ACTIVE)

            return _handle_label


        for row in range(board_size):
            self._places.append([])
            for col in range(board_size):
                backg = "#505050"
                label = Label(piece_frame, text='', bg=backg, **piece_config)
                label.bind("<Button-1>", handle_label(col, row))
                self._places[row].append(label)
                label.grid(row=row,column=col, stick='nsew')
                piece_frame.columnconfigure(col,weight=1)
                piece_frame.rowconfigure(row,weight=1)

        lower_frame = Frame(self)

        def handle_entry(event):
            if event.widget.get():
                cmd = event.widget.get()
                handle_command(cmd)
                self.after(100, ai_play)
                event.widget.delete(0,END)

        def quit_command():
            exit(0)

        def handle_command(cmd):
            print(cmd)
            report = self.game.run_command(cmd)
            if self.game.winner:
                stats = self.game.get_win_stats()
                report += "\nMove Cycles: {}\nGreen Score: {}\nRed Score: {}".format(stats[0],stats[1],stats[2])
            print(report)
            self.set_banner(report)
            self.set_board(self.game.board)
            return report

        # AI TESTING STUFF HERE
        self.team_turn = not self.game.ai_team == board.green
        self.teams = [board.green, board.red]
        self.hFuncs = [board.value_func, board.value_func]
        ai_vs = True
        if ai_vs:
            self.team_turn = not self.team_turn
        def ai_play():
            if board.winCheck() or (self.game.current_turn != self.game.ai_team.player and not ai_vs):
                return
            
            src, dest = self.game.ai.get_optimal_move(3, self.teams[self.team_turn], self.teams[not self.team_turn], True, True, self.hFuncs[self.team_turn], time.time(), self.game.time)
            if ai_vs:
                self.team_turn = not self.team_turn
            cmd = board.moveToString(src, dest)
            handle_command(cmd)
            self.after(1, ai_play)
        self.after(1000, ai_play)
        # END AI TESTING STUFF

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
                if (col,row) in board.green[0]:
                    widget.config(bg="#20FF20")
                elif (col, row) in board.red[0]:
                    widget.config(bg="#FF2020")
                else:
                    widget.config(bg="#505050")

    def update_board(self, board):
        raise NotImplementedException()

    def set_banner(self, text):
        self._banner.set(text)
