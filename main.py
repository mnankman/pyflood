from Tkinter import *
from board import Board
from buttonpanel import ButtonPanel
from model import Model
from controller import Controller
from log import *

log = Log()
#log.setVerbosity(Log.VERBOSITY_VERBOSE)

root = Tk()
root.title("Flood")
model = Model()
controller = Controller(model)
b = Board(root, controller, 30)
bp = ButtonPanel(root, controller)

#for i in range(1,3): Board(Tk(), controller, 15)

controller.new(12, 6)

root.mainloop()
root.destroy()
