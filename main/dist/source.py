from tkinter import *

from engine.roles.archer import Archer
from engine.roles.dualist import Dualist
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
title_dualsit = 'Dualist builder 0.1'
title_archer = 'Archer builder 0.2'

blacksmith_str = 'Blacksmith level'
swordman_str = 'Swordman level'
ninja_str = 'Ninja level'
mage_str = 'Mage level'
dualist_str = 'Dualist level'
archer_str = 'Archer level'


def main():
    choose_window = Tk()
    choose_window.geometry("320x30")
    choose_window.title(title_main)

    '''
    blacksmith_png = PhotoImage(file="../img/blacksmith.png")
    swordman_png = PhotoImage(file="../img/swordman.png")
    mage_png = PhotoImage(file="../img/mage.png")
    archer_png = PhotoImage(file="../img/archer.png")
    ninja_png = PhotoImage(file="../img/ninja.png")
    dualist_png = PhotoImage(file="../img/dualist.png")
    '''

    Button(choose_window, text='Blacksmith',
           command=lambda: displayCalculator(Blacksmith(), title_blacksmith, choose_window, blacksmith_str)).grid(row=0,
                                                                                                                  column=0)

    Button(choose_window, text='Swordman',
           command=lambda: displayCalculator(Swordman(), title_swordman, choose_window, swordman_str)).grid(row=0,
                                                                                                            column=1)

    Button(choose_window, text='Mage',
           command=lambda: displayCalculator(Mage(), title_mage, choose_window, mage_str)).grid(row=0, column=2)

    Button(choose_window, text='Archer',
           command=lambda: displayCalculator(Archer(), title_archer, choose_window, archer_str)).grid(row=0, column=3)

    Button(choose_window, text='Ninja',
           command=lambda: displayCalculator(Ninja(), title_ninja, choose_window, ninja_str)).grid(row=0, column=4)

    Button(choose_window, text='Dualist',
           command=lambda: displayCalculator(Dualist(), title_dualsit, choose_window, dualist_str)).grid(row=0,
                                                                                                         column=5)

    choose_window.mainloop()


main()
