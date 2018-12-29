
import tkinter as tk
import random

from polish_word_list import words
from UDPComms import Publisher, Subscriber

PORT = 9381

BOMB = "#2C3531"
BLUE = "#4056A1"
RED = "#F13C20"
NEUTRAL = "#EFE2BA"
SECRET = "#EEEEEE"

RATE = 100

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.connection = None

        self.master = [0]*25
        self.words = [None] *25
        self.state = [False]*25

        self.widgets = [ [None]*5 for _ in range(5) ]
        self.mode = None

        for x in range(5):
            for y in range(5):

                self.widgets[x][y] = tk.Label(self.root, 
                                              text="Place holder",font=("Courier", 44),
                                              pady = 60, padx = 10, bg = SECRET, bd = 2 )
                self.widgets[x][y].grid(row=x, column=y, sticky = 'nsew', padx = 2, pady = 2)

                def callback(event, coords=(x,y) ):
                    ind = x * 5 + y
                    if self.mode == 's':
                        self.state[ind] = not self.state[ind]

                self.widgets[x][y].bind("<Button-1>", callback)

        self.new_client = tk.Button(self.root, text="New game", 
                                               command = self.new_game)
        self.new_client.grid( row=5, column = 1)

        self.new_server = tk.Button(self.root, text="New game as Codemaster", 
                                               command = self.new_codemaster)
        self.new_server.grid( row=5, column = 3)


        self.root.mainloop()

    def new_game(self):
        self.mode = None
        del self.connection
        self.connection = Subscriber(PORT)

        self.mode = "c"
        self.root.after(RATE, self.update)

    def new_codemaster(self):
        self.mode = None
        del self.connection
        self.connection = Publisher(PORT)

        self.randomize()
        self.mode = "s"
        self.root.after(RATE, self.update)

    def update(self):
        if self.mode == 's':
            self.connection.send( [ self.words, self.master, self.state] )
        elif self.mode == 'c':
            self.words, self.master, self.state = self.connection.get()
        else:
            return

        for x in range(5):
            for y in range(5):
                ind = x * 5 + y
                self.widgets[x][y].config(text = words[self.words[ind]] )

                if self.mode == 's':
                    if self.state[ind]:
                        self.widgets[x][y].config(state= tk.DISABLED)
                    else:
                        self.widgets[x][y].config(state= tk.NORMAL)

                    self.widgets[x][y].config(bg= self.master[ind])

                elif self.mode == 'c':
                    if self.state[ind]:
                        self.widgets[x][y].config(state= tk.DISABLED)
                        self.widgets[x][y].config(bg= self.master[ind])
                    else:
                        self.widgets[x][y].config(state= tk.NORMAL)
                        self.widgets[x][y].config(bg= SECRET )

        self.root.after(RATE, self.update)


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

