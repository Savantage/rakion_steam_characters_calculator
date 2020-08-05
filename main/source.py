import webbrowser
from tkinter import *

from engine.mage import Mage

from gui.displaycalculator import displayCalculator

choose_window = Tk()
choose_window.geometry("300x300")

photo = PhotoImage(file="img/mage.png")

Button(choose_window, image=photo,
       command=lambda: displayCalculator(Mage(), 'Rakion - Mage builder 1.0', choose_window)).pack()

choose_window.mainloop()
