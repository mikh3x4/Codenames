
import tkinter as tk
import random

from polish_word_list import words
from UDPComms import Publisher, Subscriber

PORT = 9381


BOMB = "#2C3531"
BLUE = "#4056A1"
RED = "#F13C20"
NEUTRAL = "#EFE2BA"

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.word_list = list(map(int, wordz.strip().split('\n')))

        self.master = [0]*25
        self.randomize()

        for x in range(5):
            for y in range(5):
                ind = x * 5 + y
                color = self.master[ind]
                ind = self.word_list[ind]
                word = words.pop(ind)
                w = tk.Label(self.root, text=word,font=("Courier", 44),
                            pady = 60, padx = 10, bg = color, bd =2 )
                w.grid(row=x, column=y, sticky = 'nsew', padx = 2, pady = 2)

                def callback(event, wi=w):
                    wi.config(state=tk.DISABLED)
                    print(wi.state)

                w.bind("<Button-1>", callback)

        self.new_client = tk.Button(self.root, text="New game")
        self.new_client.grid( row=5, column = 1)
        self.new_server = tk.Button(self.root, text="New game as Codemaster")
        self.new_server.grid( row=5, column = 3)

        self.root.mainloop()


    def new_game(self):
        pass
        self.sub = Subscriber(PORT)

    def new_codemaster(self):
        self.randomize()
        self.mode = "server"
        self.pub = Publisher(PORT)

    def randomize(self):
        self.words = []
        for _ in range(25):
            while 1:
                cand = random.choice( range( len(words) ) )
                if cand not in self.words:
                    break
            self.words.append(cand)

        self.state = [False] * 25

        bomb = random.choice( range(25) )
        self.master[ bomb ] = BOMB

        for _ in range(9):
            while 1:
                cand = random.choice( range(25) )
                if self.master[cand] == 0:
                    self.master[cand] = RED
                    break

        for _ in range(8):
            while 1:
                cand = random.choice( range(25) )
                if self.master[cand] == 0:
                    self.master[cand] = BLUE
                    break

        for cand in range(25):
            if self.master[cand] == 0:
                self.master[cand] = NEUTRAL



if __name__ == "__main__":
    a = Window()

