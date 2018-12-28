
import tkinter as tk
import random

from polish_word_list import words

SIDE = 100

BOMB = "#2C3531"
BLUE = "#4056A1"
RED = "#F13C20"
NEUTRAL = "#EFE2BA"

wordz = '''
244
23
42
317
227
320
196
98
360
374
31
334
299
347
185
184
157
205
268
18
352
257
359
276
240
'''

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

                w.bind("<Button-1>", callback)

        self.root.mainloop()

    def randomize(self):
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

