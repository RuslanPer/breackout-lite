from tkinter import *
import time

from SETTINGS import *
from objects import *
from PIL import Image, ImageTk
from game import Game

tk = Tk()
tk.title(GAME_NAME)
tk.resizable(0,0)
tk.wm_attributes('-topmost',1)

canvas = Canvas(tk, width = WIDTH, height = HEIGHT, highlightthickness=0)
background_color = ImageTk.PhotoImage(Image.open('background.jpg').resize((WIDTH, HEIGHT)))
canvas.create_image(WIDTH / 2, HEIGHT / 2, image=background_color)
canvas.pack()
tk.update()

game = Game(tk, canvas)

if __name__ == '__main__':
    game.game_run()
