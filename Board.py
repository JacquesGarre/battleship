import os
clear = lambda: os.system('cls')


class Board(object):

    SIZE = 10

    def __init__(self):
        self.cells = self.generateGrid(self.SIZE)
        self.ships_positions = []

    def generateGrid(self, size):
        cells = []
        for i in range(size):
          line = []
          for j in range(size):
              line.append(" ☐ ")
          line.append("\n")
          cells.append(line)
        return cells

    def print(self):
        clear()
        for line in self.cells:
            for cell in line:
                print(cell, end = "")

    