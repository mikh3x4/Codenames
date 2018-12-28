import Tkinter as tk
import random

from polish_word_list import words

import sys

SIDE = 100

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.word_list = []

        for x in range(5):
            for y in range(5):
                ind = random.choice( range( len(words) ) )
                self.word_list.append(ind)
                word = words.pop(ind)
                w = tk.Label(self.root, text=word,font=("Courier", 44),
                            pady = 60, padx = 10)
                w.grid(row=x, column=y)


        for word in self.word_list:
            sys.stdout.write(str(word) + "\n")
            # print(word)

        sys.stdout.flush()

        self.root.mainloop()

if __name__ == "__main__":
    a = Window()





