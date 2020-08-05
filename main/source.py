from tkinter import *

from engine.roles.mage import Mage
from engine.roles.blacksmith import Blacksmith
from engine.roles.swordman import Swordman
from engine.roles.ninja import Ninja

from gui.displaycalculator import displayCalculator

title_main = 'Rakion Characters builder 1.1'
title_mage = 'Mage builder 1.0'
title_blacksmith = 'Blacksmith builder 1.0'
title_swordman = 'Swordman builder 1.2'
title_ninja = 'Ninja builder 0.1'

choose_window = Tk()
choose_window.geometry("250x750")
choose_window.title(title_main)

blacksmith_png = PhotoImage(file="img/blacksmith.png")
swordman_png = PhotoImage(file="img/swordman.png")
mage_png = PhotoImage(file="img/mage.png")
archer_png = PhotoImage(file="img/archer.png")
ninja_png = PhotoImage(file="img/ninja.png")
dualist_png = PhotoImage(file="img/dualist.png")

Button(choose_window, image=blacksmith_png,
       command=lambda: displayCalculator(Blacksmith(), title_blacksmith, choose_window)).pack()

Button(choose_window, image=swordman_png,
       command=lambda: displayCalculator(Swordman(), title_swordman, choose_window)).pack()

Button(choose_window, image=mage_png,
       command=lambda: displayCalculator(Mage(), title_mage, choose_window)).pack()

Button(choose_window, image=archer_png).pack()

Button(choose_window, image=ninja_png,
       command=lambda: displayCalculator(Ninja(), title_ninja, choose_window)).pack()

Button(choose_window, image=dualist_png).pack()

choose_window.mainloop()
