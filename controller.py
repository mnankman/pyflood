from model import Model

class Controller:
    def __init__(self, model):
        self.model = model

    def flood(self, v):
        self.model.flood(v)

    def new(self, size, numStates):
        self.model.new(size, numStates)

    def reset(self):
        self.model.init()

    def size(self):
        return self.model.getSize()

    def model(self):
        return self.model

