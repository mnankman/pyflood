from Tkinter import *

colors = ["salmon", "palegreen", "steelblue", "gold", "orchid", "lightyellow"]

class Tile:
    def __init__(self, master, size, state, onclick):
        self.onclick = onclick
        self.state = state
        self.w = Canvas(master, width=size, height=size)
        self.rectId = self.w.create_rectangle(0,0,size,size,fill=colors[self.state])
        self.w.bind("<Button-1>", self.click)

    def widget(self):
        return self.w

    def click(self, event):
        self.onclick(self.state)

    def setState(self, state):
        self.state = state
        self.w.itemconfig(self.rectId, fill=colors[self.state])

    