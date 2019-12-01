from Tkinter import *
from model import Model
from controller import Controller
from pubsub import Subscriber

class ButtonPanel(Subscriber):
    def __init__(self, master, controller):
        self.w = Frame(master)
        self.w.pack(side = BOTTOM)
        self.controller = controller
        self.btnNew = Button(self.w, text="Reset", command=self.btnResetClicked)
        self.btnNew.pack()
        self.lblScore = Label(self.w, text="")
        self.lblScore.pack()
        self.controller.model.subscribe(self, "moveupdate", self.onModelMoveUpdate)
        self.controller.model.subscribe(self, "init", self.onModelInit)
        menu = Menu(master)
        master.config(menu=menu)
        gameMenu = Menu(menu)
        gameMenu.add_command(label="new 6x4", command=self.newGame_6_4)
        gameMenu.add_command(label="new 8x3", command=self.newGame_8_3)
        gameMenu.add_command(label="new 10x3", command=self.newGame_10_3)
        gameMenu.add_command(label="new 12x6", command=self.newGame_12_6)
        gameMenu.add_command(label="new 15x6", command=self.newGame_15_6)
        gameMenu.add_command(label="new 20x6", command=self.newGame_20_6)
        menu.add_cascade(label="Game", menu=gameMenu)

    def btnResetClicked(self):
        self.controller.reset()

    def onModelInit(self, payload):
        self.lblScore.configure(text="")

    def onModelMoveUpdate(self, payload):
        self.lblScore.configure(text=str(payload[0])+" moves")
        
    def newGame_6_4(self):
        self.controller.new(6,4)
    def newGame_8_3(self):
        self.controller.new(8,3)
    def newGame_10_3(self):
        self.controller.new(10,3)
    def newGame_12_6(self):
        self.controller.new(12,6)
    def newGame_15_6(self):
        self.controller.new(15,6)
    def newGame_20_6(self):
        self.controller.new(20,6)
