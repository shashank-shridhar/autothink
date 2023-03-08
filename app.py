from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests
import random

app = Tk()  #Creates a window instance of the GUI
app.geometry("800x800")
app.title("Autothink")
app.config(background="gold")

Games = ["Dark Souls","Sekiro","Bloodborne","Civilization VI","CS:GO"]
Movies = ["Pulp Fiction","Godfather","End of Evangelion"]
Food = ["Ramen","Pizza","Burger","Thukpa"]

def pick_random_food(Food):
    return random.choice(Food)
def pick_random_game(Games):
    return random.choice(Games)
def pick_random_movies(Movies):
    return random.choice(Movies)

intro_text = Label(app,text="Autothink",font=("Comic Sans MS",50),width=80)
intro_text.pack()

movie_button = Button(app,text="Movies",height=-3,width=10,fg = "black",font=("Arial",35),command=lambda: messagebox.showinfo("Movie Choice",pick_random_movies(Movies)))
games_button = Button(app,text="Games",height=-3,width=10,fg = "black",font=("Arial",35),command=lambda: messagebox.showinfo("Game choice",pick_random_game(Games)))
food_button = Button(app,text="Food",height=-3,width=10,fg = "black",font=("Arial",35),command=lambda: messagebox.showinfo("Food choice",pick_random_food(Food)))

movie_button.pack(side=RIGHT,padx=5,pady=0)
games_button.pack(side=LEFT,padx=5,pady=0)
food_button.pack(side=LEFT,padx=30)

app.mainloop()
