from tkinter import *

from tabulate import tabulate

TABLE_HEADERS = ["Set", "Basic", "Range", "Special", "Grip", "Cell dest.", "Energy", "Armor", "Attack Speed",
                 "Mov Speed",
                 "Cell points"]


def buildList(wearables):
    displayed_gear = []
    for wearable in wearables:
        displayed_gear.append(
            [wearables[wearable].name,
             wearables[wearable].getBasic(),
             wearables[wearable].getRange(),
             wearables[wearable].getSpecial(),
             wearables[wearable].getGrip(),
             wearables[wearable].getCd(),
             wearables[wearable].getHp(),
             wearables[wearable].getAp(),
             wearables[wearable].getAttackSpeed(),
             wearables[wearable].getMovementSpeed(),
             wearables[wearable].getCP()])
    return displayed_gear


def tabletoString(list, table_headers, textable):
    string = tabulate(list, headers=table_headers)
    textable.delete('1.0', END)
    textable.insert(INSERT, string)


def showWearables(gear_list, geardic, texttable):
    # Se construye una lista con los wearables
    gear_list[0] = buildList(geardic)

    # Se convierten los wearables a lista y se los inserta en la textable
    tabletoString(gear_list[0], TABLE_HEADERS, texttable)


def sortBasic(gear_list, textable):
    if gear_list[0]:
        tabletoString(sorted(gear_list[0], key=lambda stat: stat[1]), TABLE_HEADERS, textable)


def sortRange(gear_list, textable):
    if gear_list[0]:
        tabletoString(sorted(gear_list[0], key=lambda stat: stat[2]), TABLE_HEADERS, textable)


def sortSpecial(gear_list, textable):
    if gear_list[0]:
        tabletoString(sorted(gear_list[0], key=lambda stat: stat[3]), TABLE_HEADERS, textable)


def sortGrip(gear_list, textable):
    if gear_list[0]:
        tabletoString(sorted(gear_list[0], key=lambda stat: stat[4]), TABLE_HEADERS, textable)


def sortCD(gear_list, textable):
    if gear_list[0]:
        tabletoString(sorted(gear_list[0], key=lambda stat: stat[5]), TABLE_HEADERS, textable)


def sortHP(gear_list, textable):
    if gear_list[0]:
        tabletoString(sorted(gear_list[0], key=lambda stat: stat[6]), TABLE_HEADERS, textable)


def sortAP(gear_list, textable):
    if gear_list[0]:
        tabletoString(sorted(gear_list[0], key=lambda stat: stat[7]), TABLE_HEADERS, textable)


def sortAS(gear_list, textable):
    if gear_list[0]:
        tabletoString(sorted(gear_list[0], key=lambda stat: stat[8]), TABLE_HEADERS, textable)


def sortMS(gear_list, textable):
    if gear_list[0]:
        tabletoString(sorted(gear_list[0], key=lambda stat: stat[9]), TABLE_HEADERS, textable)


def sortCP(gear_list, textable):
    if gear_list[0]:
        tabletoString(sorted(gear_list[0], key=lambda stat: stat[10]), TABLE_HEADERS, textable)


def showGear(gearwindow, geardic):
    if gearwindow:
        gearwindow.destroy()
    gearwindow = Toplevel()
    gearwindow.title("Full gear stats")

    gear_list = [None]

    text_table = Text(gearwindow, height=17, width=145)
    text_table.config(state="normal")
    text_table.grid(row=0, column=3, columnspan=10, rowspan=10)

    Button(gearwindow, text="Helmet", command=lambda: showWearables(gear_list, geardic['Helmet'], text_table)).grid(
        row=0,
        column=0)
    Button(gearwindow, text="Shoulder", command=lambda: showWearables(gear_list, geardic['Shoulder'], text_table)).grid(
        row=1, column=0)
    Button(gearwindow, text="Armor", command=lambda: showWearables(gear_list, geardic['Armor'], text_table)).grid(row=2,
                                                                                                                  column=0)
    Button(gearwindow, text="Arm", command=lambda: showWearables(gear_list, geardic['Arm'], text_table)).grid(row=3,
                                                                                                              column=0)
    Button(gearwindow, text="Melee", command=lambda: showWearables(gear_list, geardic['Melee'], text_table)).grid(row=4,
                                                                                                                  column=0)
    Button(gearwindow, text="Range", command=lambda: showWearables(gear_list, geardic['Range'], text_table)).grid(row=5,
                                                                                                                  column=0)
    Button(gearwindow, text="Necklace", command=lambda: showWearables(gear_list, geardic['Necklace'], text_table)).grid(
        row=6, column=0)
    Button(gearwindow, text="Ring", command=lambda: showWearables(gear_list, geardic['Ring'], text_table)).grid(row=7,
                                                                                                                column=0)
    Button(gearwindow, text="Bead", command=lambda: showWearables(gear_list, geardic['Bead'], text_table)).grid(row=8,
                                                                                                                column=0)

    Button(gearwindow, text="Basic", command=lambda: sortBasic(gear_list, text_table)).grid(row=0, column=2)
    Button(gearwindow, text="Range", command=lambda: sortRange(gear_list, text_table)).grid(row=1, column=2)
    Button(gearwindow, text="Special", command=lambda: sortSpecial(gear_list, text_table)).grid(row=2, column=2)
    Button(gearwindow, text="Grip", command=lambda: sortGrip(gear_list, text_table)).grid(row=3, column=2)
    Button(gearwindow, text="Cell Destruction", command=lambda: sortCD(gear_list, text_table)).grid(row=4, column=2)
    Button(gearwindow, text="Energy", command=lambda: sortHP(gear_list, text_table)).grid(row=5, column=2)
    Button(gearwindow, text="Armor", command=lambda: sortAP(gear_list, text_table)).grid(row=6, column=2)
    Button(gearwindow, text="Attack Speed", command=lambda: sortAS(gear_list, text_table)).grid(row=7, column=2)
    Button(gearwindow, text="Movement speed", command=lambda: sortMS(gear_list, text_table)).grid(row=8, column=2)
    Button(gearwindow, text="Cell points", command=lambda: sortCP(gear_list, text_table)).grid(row=9, column=2)
