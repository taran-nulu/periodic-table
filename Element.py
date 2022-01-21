from tkinter import *
from math import *

from circle import *
from Family import *
from Orbitals import *

textHeight = 40
padding = 5
elementPadding = 5

elementWidth = 200
elementHeight = textHeight * 2 + elementWidth

cellWidth = elementWidth + elementPadding
cellHeight = elementHeight + elementPadding

class Element:
    def __init__(self, name, symbol, number, mass, family, row, column):
        self.name = name
        self.symbol = symbol
        self.number = number
        self.mass = mass
        self.family = family
        self.row = row
        self.column = column
        self.orbitals = Orbitals(number)
        self.energyLevels = self.orbitals.getShells()

    def printDetailed(self):
        print(f"Name: {self.name}")
        print(f"Abbreviation: {self.symbol}")
        print(f"Atomic Number: {self.number}")
        print(f"Atomic Mass: {self.mass}")
        print(f"Energy Levels{self.energyLevels}")
    
    def printCompact(self):
        print(f"{self.name}, {self.symbol}, {self.number}, {self.mass}, {self.energyLevels}")

    def draw(self, canvas):
        color = familyColors[self.family]
        cellX = cellWidth * self.column
        cellY = cellHeight * self.row
        x = cellX + elementPadding
        y = cellY + elementPadding
        font = 'Helvetica 16'
        canvas.create_rectangle(x, y, x + elementWidth, y + elementHeight, fill=color)
        # Row 1 text
        row1TextHeight = textHeight * 0.5
        # Name.
        canvas.create_rectangle(x, y, x + elementWidth, y + textHeight, fill=color)
        canvas.create_text(x + elementWidth / 2, y + row1TextHeight, text=self.name, font=font)
        # Row 2 text.
        row2TextHeight = textHeight * 1.5
        # Symbol.
        canvas.create_rectangle(x, y + textHeight, x + elementWidth, y + textHeight * 2, fill=color)
        canvas.create_text(x + elementWidth / 2, y + row2TextHeight, text=self.symbol, font=font)
        # Number.
        canvas.create_text(x + padding, y + row2TextHeight, text=self.number, font=font, anchor=W)
        # Mass.
        canvas.create_text(x + elementWidth - padding, y + row2TextHeight, text=self.mass, font=font, anchor=E)
        # Rings.
        centerX = x + elementWidth / 2
        centerY = y + textHeight * 2 + elementWidth / 2
        self.drawShells(canvas, centerX, centerY)

    def drawShells(self, canvas, centerX, centerY):
        shellPadding = 12
        shell1R = 20
        shells = self.orbitals.getShells()
        shellCount = len(shells)
        for i in range(0, shellCount):
            r = shell1R + shellPadding * i
            drawCircle(canvas, centerX, centerY, r)
            self.drawElectrons(shells[i], canvas, centerX, centerY, r)

    def drawElectrons(self, electronsCount, canvas, centerX, centerY, radius):
        radiansGap = 2 * pi / electronsCount
        radians = 0
        for i in range(0, electronsCount):
            electronX = radius * cos(radians) + centerX
            electronY = radius * sin(radians) + centerY
            drawCircle(canvas, electronX, electronY, 2)
            radians += radiansGap
