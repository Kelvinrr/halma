from halma.game import Halma
from halma.gui import HalmaGUI
from tkinter import *
import sys

def build_board(fh):
        board_list = []
        for line in fh:
                board_list.append(line.strip().split(" "))
        return board_list

if __name__ == "__main__": # pragma : no cover
        argv = sys.argv
        
        basic_board = None
        if len(argv) < 4:
                print(len(argv))
                print("Invalid arguments")
                exit(1)
        try:
                basic_board = build_board(open(argv[4],'r'))
                if (len(basic_board) != int(argv[1])):
                        print("Size of passed board incorrect")
        except FileNotFoundError:
                pass
        except IndexError:
                pass
                
        root = Tk()
        game = Halma(int(argv[1]), int(argv[2]), argv[3], initial_board=basic_board)
        board = game.board
        gui = HalmaGUI(root, game)
        gui.set_board(board)
        root.mainloop()
