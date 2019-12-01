from Tkinter import *
from tile import Tile
from model import Model
from controller import Controller
from pubsub import Subscriber
from log import Log

log = Log()

# An instance of this class is a Tk Frame showing a grid of coloured tiles
# It inherits the Subscriber class to be able to observe and handle model events
class Board(Subscriber):
    def __init__(self, master, controller, tilesize):
        self.master = master
        self.w = Frame(master)
        self.w.pack(side = TOP)
        self.tilesize = tilesize
        self.controller = controller
        self.controller.model.subscribe(self, "init", self.onModelInit)
        self.controller.model.subscribe(self, "change", self.onModelChange)
        self.tiles = []

    # handles the occurance of the model's "init" event
    # - payload: tuple (size, numStates) - only size is used by the handler
    def onModelInit(self, payload):
        log.trace("Board.onModelInit" + str(payload))
        self.w.pack_forget()
        self.w.destroy()
        del self.tiles
        self.w = Frame(self.master)
        self.w.pack(side = TOP)
        size = payload[0]
        self.tiles = []
        if size>0:
            for r in range(1, size+1):
                row = []
                for c in range(1, size+1):
                    t = Tile(self.w, self.tilesize, 0, self.tileClicked)
                    t.widget().grid(column=c, row=r)
                    row.append(t)
                self.tiles.append(row)

    # handles the occurance of the model's "change" event
    # - payload: a tuple (row, col, newValue) 
    def onModelChange(self, payload):
        log.trace("Board.onModelChange" + str(payload))
        row = payload[0]
        col = payload[1]
        newValue = payload[2]
        self.tiles[row-1][col-1].setState(newValue)

    # called when the player clicks on a tile
    def tileClicked(self, v):
        self.controller.flood(v)

