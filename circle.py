from tkinter import *

def drawCircle(canvas, centerX, centerY, radius):
    canvas.create_oval(centerX - radius, centerY - radius, centerX + radius, centerY + radius)

