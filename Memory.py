
import tkinter as tk
import random
from tkinter import messagebox

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")
        self.buttons = []
        self.values = []
        self.first_choice = None
        self.create_board()

    def create_board(self):
        self.values = list(range(1, 9)) * 2
        random.shuffle(self.values)
        for i in range(4):
            row = []
            for j in range(4):
                btn = tk.Button(self.root, text="", width=8, height=4, command=lambda x=i, y=j: self.reveal(x, y))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

    def reveal(self, x, y):
        if self.buttons[x][y]["state"] == "disabled":
            return
        self.buttons[x][y].config(text=self.values[x * 4 + y], state="disabled")
        if not self.first_choice:
            self.first_choice = (x, y)
        else:
            x1, y1 = self.first_choice
            if self.values[x * 4 + y] != self.values[x1 * 4 + y1]:
                self.root.after(1000, self.hide, x, y, x1, y1)
            self.first_choice = None

    def hide(self, x, y, x1, y1):
        self.buttons[x][y].config(text="", state="normal")
        self.buttons[x1][y1].config(text="", state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()