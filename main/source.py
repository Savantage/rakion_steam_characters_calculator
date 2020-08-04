import webbrowser
from tkinter import *

from engine.character import Character
from engine.mage import Mage
from engine.jewelry import *
from gui.displayutils import showGear

root = Tk()
root.configure(bg='gray58')
root.title('Rakion - Mage builder 1.0')
root.geometry("850x450")

options_enchanting = ["0",
                      "1",
                      "2",
                      "3",
                      "4",
                      "5",
                      "6",
                      "7",
                      "8",
                      "9",
                      "10"]

character = Character(Mage())
enchanter = character.enchanter
levelstats = character.levelStats

role_helmets = list(character.role.helmetS)
role_shoulders = list(character.role.shoulderS)
role_armors = list(character.role.armorS)
role_arms = list(character.role.armS)
role_melees = list(character.role.meleeS)
role_ranges = list(character.role.rangeS)
role_rings = list(ringS)
role_necklace = list(necklaceS)
role_beads = list(beadS)

wearable_names = {'Helmet': 'Helmet',
                  'Armor': 'Armor',
                  'Shoulder': 'Shoulder',
                  'Arm': 'Arm',
                  'Melee': 'Melee',
                  'Range': 'Range',
                  'Necklace': 'Necklace',
                  'Ring A': 'Ring A',
                  'Ring B': 'Ring B',
                  'Ring C': 'Ring C',
                  'Bead': 'Bead'}

stat_names = {'Basic': 'Basic',
              'Range': 'Range',
              'Special': 'Special',
              'Grip': 'Grip',
              'Cell dest.': 'Cell dest.',
              'Energy': 'Energy',
              'Armor': 'Armor',
              'Attack speed': 'Attack speed',
              'Movement Speed': 'Movement Speed',
              'Cell points': 'Cell points'}


# Primera columna
def setWearableLabels():
    aux = 2
    column = 0
    for wearable in wearable_names:
        Label(root, text=wearable_names[wearable], width=7, bg='gray60').grid(row=aux, column=column)
        aux = aux + 1


setWearableLabels()


# Novena columna
def setStatLabels():
    aux = 2
    column = 6
    for stat in stat_names:
        Label(root, text=stat, font="Helvetica 11 bold", width=14, bg='gray58', fg='orange').grid(row=aux,
                                                                                                  column=column)
        aux = aux + 1


setStatLabels()

Label(root, text="Points used", font="Helvetica 10 bold", bg='gray58', fg='SlateBlue4', width=14).grid(row=1, column=5)


# Opciones de vestimenta

def setStringAndSetValue(value):
    aux = StringVar()
    aux.set(value)
    return aux


wearables_string_vars = {wearable_names['Helmet']: setStringAndSetValue(character.role.helmetS['Default'].name),
                         wearable_names['Armor']: setStringAndSetValue(character.role.armorS['Default'].name),
                         wearable_names['Shoulder']: setStringAndSetValue(character.role.shoulderS['Default'].name),
                         wearable_names['Arm']: setStringAndSetValue(character.role.armS['Default'].name),
                         wearable_names['Melee']: setStringAndSetValue(character.role.meleeS['Default'].name),
                         wearable_names['Range']: setStringAndSetValue(character.role.rangeS['Default'].name),
                         wearable_names['Necklace']: setStringAndSetValue(necklaceS['Default'].name),
                         wearable_names['Ring A']: setStringAndSetValue(ringS['Default'].name),
                         wearable_names['Ring B']: setStringAndSetValue(ringS['Default'].name),
                         wearable_names['Ring C']: setStringAndSetValue(ringS['Default'].name),
                         wearable_names['Bead']: setStringAndSetValue(beadS['Default'].name)}


def optionMenuOptionsPosVar(rooot, var, options, row, column):
    aux = OptionMenu(rooot, var, *options)
    aux.grid(row=row, column=column)
    aux.config(bg='gray58')
    aux["highlightthickness"] = 0
    return aux


option_menu_vars = {
    wearable_names['Helmet']: optionMenuOptionsPosVar(root, wearables_string_vars[wearable_names['Helmet']],
                                                      role_helmets, 2, 1),

    wearable_names['Armor']: optionMenuOptionsPosVar(root, wearables_string_vars[wearable_names['Armor']],
                                                     role_armors, 3, 1),
    wearable_names['Shoulder']: optionMenuOptionsPosVar(root, wearables_string_vars[wearable_names['Shoulder']],
                                                        role_shoulders, 4, 1),
    wearable_names['Arm']: optionMenuOptionsPosVar(root, wearables_string_vars[wearable_names['Arm']], role_arms,
                                                   5, 1),
    wearable_names['Melee']: optionMenuOptionsPosVar(root, wearables_string_vars[wearable_names['Melee']],
                                                     role_melees, 6, 1),
    wearable_names['Range']: optionMenuOptionsPosVar(root, wearables_string_vars[wearable_names['Range']],
                                                     role_ranges, 7, 1),
    wearable_names['Necklace']: optionMenuOptionsPosVar(root, wearables_string_vars[wearable_names['Necklace']],
                                                        role_necklace, 8, 1),
    wearable_names['Ring A']: optionMenuOptionsPosVar(root, wearables_string_vars[wearable_names['Ring A']],
                                                      role_rings, 9, 1),
    wearable_names['Ring B']: optionMenuOptionsPosVar(root, wearables_string_vars[wearable_names['Ring B']],
                                                      role_rings, 10, 1),
    wearable_names['Ring C']: optionMenuOptionsPosVar(root, wearables_string_vars[wearable_names['Ring C']],
                                                      role_rings, 11, 1),
    wearable_names['Bead']: optionMenuOptionsPosVar(root, wearables_string_vars[wearable_names['Bead']],
                                                    role_beads, 12, 1)}

enchanting_string_vars = {wearable_names['Helmet']: setStringAndSetValue(options_enchanting[0]),
                          wearable_names['Armor']: setStringAndSetValue(options_enchanting[0]),
                          wearable_names['Shoulder']: setStringAndSetValue(options_enchanting[0]),
                          wearable_names['Arm']: setStringAndSetValue(options_enchanting[0]),
                          wearable_names['Melee']: setStringAndSetValue(options_enchanting[0]),
                          wearable_names['Range']: setStringAndSetValue(options_enchanting[0]),
                          wearable_names['Necklace']: setStringAndSetValue(options_enchanting[0]),
                          wearable_names['Ring A']: setStringAndSetValue(options_enchanting[0]),
                          wearable_names['Ring B']: setStringAndSetValue(options_enchanting[0]),
                          wearable_names['Ring C']: setStringAndSetValue(options_enchanting[0]),
                          wearable_names['Bead']: setStringAndSetValue(options_enchanting[0])}

enchanting_menu_vars = {
    wearable_names['Helmet']: optionMenuOptionsPosVar(root, enchanting_string_vars[wearable_names['Helmet']],
                                                      options_enchanting, 2, 2),
    wearable_names['Armor']: optionMenuOptionsPosVar(root, enchanting_string_vars[wearable_names['Armor']],
                                                     options_enchanting, 3, 2),
    wearable_names['Shoulder']: optionMenuOptionsPosVar(root, enchanting_string_vars[wearable_names['Shoulder']],
                                                        options_enchanting, 4, 2),
    wearable_names['Arm']: optionMenuOptionsPosVar(root, enchanting_string_vars[wearable_names['Arm']],
                                                   options_enchanting, 5, 2),
    wearable_names['Melee']: optionMenuOptionsPosVar(root, enchanting_string_vars[wearable_names['Melee']],
                                                     options_enchanting, 6, 2),
    wearable_names['Range']: optionMenuOptionsPosVar(root, enchanting_string_vars[wearable_names['Range']],
                                                     options_enchanting, 7, 2),
    wearable_names['Ring A']: optionMenuOptionsPosVar(root, enchanting_string_vars[wearable_names['Ring A']],
                                                      options_enchanting, 8, 2),
    wearable_names['Ring B']: optionMenuOptionsPosVar(root, enchanting_string_vars[wearable_names['Ring B']],
                                                      options_enchanting, 9, 2),
    wearable_names['Ring C']: optionMenuOptionsPosVar(root, enchanting_string_vars[wearable_names['Ring C']],
                                                      options_enchanting, 10, 2),
    wearable_names['Necklace']: optionMenuOptionsPosVar(root, enchanting_string_vars[wearable_names['Necklace']],
                                                        options_enchanting, 11, 2),
    wearable_names['Bead']: optionMenuOptionsPosVar(root, enchanting_string_vars[wearable_names['Bead']],
                                                    options_enchanting, 12, 2)}


def setintLabelandPos(rooot, num, row, column):
    aux = Label(rooot, text=str(num), bg='gray58', fg='dark slate blue')
    aux.grid(row=row, column=column)
    return aux


basic_stat = setintLabelandPos(root, character.getBasic(), 2, 7)
range_stat = setintLabelandPos(root, character.getRange(), 3, 7)
special_stat = setintLabelandPos(root, character.getSpecial(), 4, 7)
grip_stat = setintLabelandPos(root, character.getGrip(), 5, 7)
celldest_stat = setintLabelandPos(root, character.getCellDestruction(), 6, 7)
energy_stat = setintLabelandPos(root, character.getEnergy(), 7, 7)
armor_stat = setintLabelandPos(root, character.getArmor(), 8, 7)
attackspeed_stat = setintLabelandPos(root, character.getAttackSpeed(), 9, 7)
movspeed_stat = setintLabelandPos(root, character.getMovementSpeed(), 10, 7)
cellpoints_stat = setintLabelandPos(root, character.getCellPoints(), 11, 7)


# Funcion para actualizar los labels de los stats
def update_stats():
    basic_stat.config(text=str(character.getBasic()))
    range_stat.config(text=str(character.getRange()))
    special_stat.config(text=str(character.getSpecial()))
    grip_stat.config(text=str(character.getGrip()))
    celldest_stat.config(text=str(character.getCellDestruction()))
    energy_stat.config(text=str(character.getEnergy()))
    armor_stat.config(text=str(character.getArmor()))
    attackspeed_stat.config(text=str(character.getAttackSpeed()))
    movspeed_stat.config(text=str(character.getMovementSpeed()))
    cellpoints_stat.config(text=str(character.getCellPoints()))


# Funciones para actualizar los wearables


def change_helmets_menu(*args):
    character.setHelmet(str(wearables_string_vars[wearable_names['Helmet']].get()))
    enchanting_string_vars[wearable_names['Helmet']].set(options_enchanting[0])
    update_stats()


def change_armors_menu(*args):
    character.setArmor(str(wearables_string_vars[wearable_names['Armor']].get()))
    enchanting_string_vars[wearable_names['Armor']].set(options_enchanting[0])
    update_stats()


def change_shoulders_menu(*args):
    character.setShoulder(str(wearables_string_vars[wearable_names['Shoulder']].get()))
    enchanting_string_vars[wearable_names['Shoulder']].set(options_enchanting[0])
    update_stats()


def change_arms_menu(*args):
    character.setArm(str(wearables_string_vars[wearable_names['Arm']].get()))
    enchanting_string_vars[wearable_names['Arm']].set(options_enchanting[0])
    update_stats()


def change_melees_menu(*args):
    character.setMelee(str(wearables_string_vars[wearable_names['Melee']].get()))
    enchanting_string_vars[wearable_names['Melee']].set(options_enchanting[0])
    update_stats()


def change_range_menu(*args):
    character.setRange(str(wearables_string_vars[wearable_names['Range']].get()))
    enchanting_string_vars[wearable_names['Range']].set(options_enchanting[0])
    update_stats()


def change_necklaces_menu(*args):
    character.setNeckLace(str(wearables_string_vars[wearable_names['Necklace']].get()))
    enchanting_string_vars[wearable_names['Necklace']].set(options_enchanting[0])
    update_stats()


def change_ring1s_menu(*args):
    character.setRing1(str(wearables_string_vars[wearable_names['Ring A']].get()))
    enchanting_string_vars[wearable_names['Ring A']].set(options_enchanting[0])
    update_stats()


def change_ring2s_menu(*args):
    character.setRing2(str(wearables_string_vars[wearable_names['Ring B']].get()))
    enchanting_string_vars[wearable_names['Ring B']].set(options_enchanting[0])
    update_stats()


def change_ring3s_menu(*args):
    character.setRing3(str(wearables_string_vars[wearable_names['Ring C']].get()))
    enchanting_string_vars[wearable_names['Ring C']].set(options_enchanting[0])
    update_stats()


def change_beads_menu(*args):
    character.setBead(str(wearables_string_vars[wearable_names['Bead']].get()))
    enchanting_string_vars[wearable_names['Bead']].set(options_enchanting[0])
    update_stats()


def enchant_helmet(*args):
    enchanter.enchantHelmet(enchanting_string_vars[wearable_names['Helmet']].get())
    update_stats()


def enchant_armor(*args):
    enchanter.enchantArmor(enchanting_string_vars[wearable_names['Armor']].get())
    update_stats()


def enchant_shoulder(*args):
    enchanter.enchantShoulder(enchanting_string_vars[wearable_names['Shoulder']].get())
    update_stats()


def enchant_arm(*args):
    enchanter.enchantArm(enchanting_string_vars[wearable_names['Arm']].get())
    update_stats()


def enchant_melee(*args):
    enchanter.enchantMelee(enchanting_string_vars[wearable_names['Melee']].get())
    update_stats()


def enchant_range(*args):
    enchanter.enchantRange(enchanting_string_vars[wearable_names['Range']].get())
    update_stats()


def enchant_necklace(*args):
    enchanter.enchantNecklace(enchanting_string_vars[wearable_names['Necklace']].get())
    update_stats()


def enchant_ring1(*args):
    enchanter.enchantRing1(enchanting_string_vars[wearable_names['Ring A']].get())
    update_stats()


def enchant_ring2(*args):
    enchanter.enchantRing2(enchanting_string_vars[wearable_names['Ring B']].get())
    update_stats()


def enchant_ring3(*args):
    enchanter.enchantRing3(enchanting_string_vars[wearable_names['Ring C']].get())
    update_stats()


def enchant_bead(*args):
    enchanter.enchantBead(enchanting_string_vars[wearable_names['Bead']].get())
    update_stats()


wearables_string_vars[wearable_names['Helmet']].trace('w', change_helmets_menu)
wearables_string_vars[wearable_names['Armor']].trace('w', change_armors_menu)
wearables_string_vars[wearable_names['Shoulder']].trace('w', change_shoulders_menu)
wearables_string_vars[wearable_names['Arm']].trace('w', change_arms_menu)
wearables_string_vars[wearable_names['Melee']].trace('w', change_melees_menu)
wearables_string_vars[wearable_names['Range']].trace('w', change_range_menu)
wearables_string_vars[wearable_names['Ring A']].trace('w', change_ring1s_menu)
wearables_string_vars[wearable_names['Ring B']].trace('w', change_ring2s_menu)
wearables_string_vars[wearable_names['Ring C']].trace('w', change_ring3s_menu)
wearables_string_vars[wearable_names['Necklace']].trace('w', change_necklaces_menu)
wearables_string_vars[wearable_names['Bead']].trace('w', change_beads_menu)

enchanting_string_vars[wearable_names['Helmet']].trace('w', enchant_helmet)
enchanting_string_vars[wearable_names['Armor']].trace('w', enchant_armor)
enchanting_string_vars[wearable_names['Shoulder']].trace('w', enchant_shoulder)
enchanting_string_vars[wearable_names['Arm']].trace('w', enchant_arm)
enchanting_string_vars[wearable_names['Melee']].trace('w', enchant_melee)
enchanting_string_vars[wearable_names['Range']].trace('w', enchant_range)
enchanting_string_vars[wearable_names['Necklace']].trace('w', enchant_necklace)
enchanting_string_vars[wearable_names['Ring A']].trace('w', enchant_ring1)
enchanting_string_vars[wearable_names['Ring B']].trace('w', enchant_ring2)
enchanting_string_vars[wearable_names['Ring C']].trace('w', enchant_ring3)
enchanting_string_vars[wearable_names['Bead']].trace('w', enchant_bead)

# Puntos de nivel
level_string = Label(root, text="Mage Level", font="Helvetica 16 bold", fg="dark green", bg='gray58')
level_string.grid(row=0, column=6)

actual_level = Label(root, text=str(character.getLevel()), font="Helvetica 14 bold", fg="dark green", bg='gray58')
actual_level.grid(row=0, column=7)

available_stats_string = Label(root, text="Available stat points: ", font="Helvetica 10 bold", bg='gray40', fg='gray80')
available_stats_string.grid(row=1, column=3)

actual_available_stats = Label(root, text=str(character.getAvailableStats()), font="Helvetica 10 bold", bg='gray40',
                               fg='gray80', width=14)
actual_available_stats.grid(row=1, column=4)

level_input = Entry(root, width=4)
level_input.grid(row=1, column=6)


def setEntryandPos(aRoot, row, column):
    aux = Entry(aRoot, width=5)
    aux.grid(row=row, column=column)
    return aux


input_vars = {stat_names['Basic']: setEntryandPos(root, 2, 3),
              stat_names['Range']: setEntryandPos(root, 3, 3),
              stat_names['Special']: setEntryandPos(root, 4, 3),
              stat_names['Grip']: setEntryandPos(root, 5, 3),
              stat_names['Cell dest.']: setEntryandPos(root, 6, 3),
              stat_names['Energy']: setEntryandPos(root, 7, 3),
              stat_names['Armor']: setEntryandPos(root, 8, 3),
              stat_names['Attack speed']: setEntryandPos(root, 9, 3),
              stat_names['Movement Speed']: setEntryandPos(root, 10, 3),
              stat_names['Cell points']: setEntryandPos(root, 11, 3)
              }

stat_points = {stat_names['Basic']: setintLabelandPos(root, levelstats.basicPoints, 2, 5),
               stat_names['Range']: setintLabelandPos(root, levelstats.rangePoints, 3, 5),
               stat_names['Special']: setintLabelandPos(root, levelstats.specialPoints, 4, 5),
               stat_names['Grip']: setintLabelandPos(root, levelstats.gripPoints, 5, 5),
               stat_names['Cell dest.']: setintLabelandPos(root, levelstats.cdPoints, 6, 5),
               stat_names['Energy']: setintLabelandPos(root, levelstats.hpPoints, 7, 5),
               stat_names['Armor']: setintLabelandPos(root, levelstats.apPoints, 8, 5),
               stat_names['Attack speed']: setintLabelandPos(root, levelstats.attackSpeedPoints, 9, 5),
               stat_names['Movement Speed']: setintLabelandPos(root, levelstats.movementSpeedPoints, 10, 5),
               stat_names['Cell points']: setintLabelandPos(root, levelstats.cpPoints, 11, 5)}


def setCharacterLevel():
    character.setLevel(int(level_input.get()))
    actual_level.config(text=str(character.getLevel()))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    stat_points[stat_names['Basic']].config(text=str(levelstats.basicPoints))
    stat_points[stat_names['Range']].config(text=str(levelstats.rangePoints))
    stat_points[stat_names['Special']].config(text=str(levelstats.specialPoints))
    stat_points[stat_names['Grip']].config(text=str(levelstats.gripPoints))
    stat_points[stat_names['Cell dest.']].config(text=str(levelstats.cdPoints))
    stat_points[stat_names['Energy']].config(text=str(levelstats.hpPoints))
    stat_points[stat_names['Armor']].config(text=str(levelstats.apPoints))
    stat_points[stat_names['Attack speed']].config(text=str(levelstats.attackSpeedPoints))
    stat_points[stat_names['Movement Speed']].config(text=str(levelstats.movementSpeedPoints))
    stat_points[stat_names['Cell points']].config(text=str(levelstats.cpPoints))
    update_stats()
    level_input.delete(0, "end")


change_level = Button(root, text="Change level", command=setCharacterLevel, bg='gray58')
change_level.grid(row=1, column=7)


def addBasic():
    character.addBasic(int(input_vars[stat_names['Basic']].get()))
    stat_points[stat_names['Basic']].config(text=str(levelstats.basicPoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats()
    input_vars[stat_names['Basic']].delete(0, "end")


def addRange():
    character.addRange(int(input_vars[stat_names['Range']].get()))
    stat_points[stat_names['Range']].config(text=str(levelstats.rangePoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats()
    input_vars[stat_names['Range']].delete(0, "end")


def addSpecial():
    character.addSpecial(int(input_vars[stat_names['Special']].get()))
    stat_points[stat_names['Special']].config(text=str(levelstats.specialPoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats()
    input_vars[stat_names['Special']].delete(0, "end")


def addGrip():
    character.addGrip(int(input_vars[stat_names['Grip']].get()))
    stat_points[stat_names['Grip']].config(text=str(levelstats.gripPoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats()
    input_vars[stat_names['Grip']].delete(0, "end")


def addCd():
    character.addCellDestruction(int(input_vars[stat_names['Cell dest.']].get()))
    stat_points[stat_names['Cell dest.']].config(text=str(levelstats.cdPoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats()
    input_vars[stat_names['Cell dest.']].delete(0, "end")


def addHp():
    character.addEnergy(int(input_vars[stat_names['Energy']].get()))
    stat_points[stat_names['Energy']].config(text=str(levelstats.hpPoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats()
    input_vars[stat_names['Energy']].delete(0, "end")


def addAp():
    character.addArmor(int(input_vars[stat_names['Armor']].get()))
    stat_points[stat_names['Armor']].config(text=str(levelstats.apPoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats()
    input_vars[stat_names['Armor']].delete(0, "end")


def addAttackSpeed():
    character.addAttackSpeed(int(input_vars[stat_names['Attack speed']].get()))
    stat_points[stat_names['Attack speed']].config(text=str(levelstats.attackSpeedPoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats()
    input_vars[stat_names['Attack speed']].delete(0, "end")


def addMovSpeed():
    character.addMovementSpeed(int(input_vars[stat_names['Movement Speed']].get()))
    stat_points[stat_names['Movement Speed']].config(text=str(levelstats.movementSpeedPoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats()
    input_vars[stat_names['Movement Speed']].delete(0, "end")


def addCp():
    character.addCellPoints(int(input_vars[stat_names['Cell points']].get()))
    stat_points[stat_names['Cell points']].config(text=str(levelstats.cpPoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats()
    input_vars[stat_names['Cell points']].delete(0, "end")


Button(root, text="Basic +", command=addBasic, width=15, bg='gray58', fg='black').grid(row=2, column=4)
Button(root, text="Range +", command=addRange, width=15, bg='gray58', fg='black').grid(row=3, column=4)
Button(root, text="Special +", command=addSpecial, width=15, bg='gray58', fg='black').grid(row=4, column=4)
Button(root, text="Grip +", command=addGrip, width=15, bg='gray58', fg='black').grid(row=5, column=4)
Button(root, text="Cell dest. +", command=addCd, width=15, bg='gray58', fg='black').grid(row=6, column=4)
Button(root, text="Energy +", command=addHp, width=15, bg='gray58', fg='black').grid(row=7, column=4)
Button(root, text="Armor +", command=addAp, width=15, bg='gray58', fg='black').grid(row=8, column=4)
Button(root, text="Attack speed +", command=addAttackSpeed, width=15, bg='gray58', fg='black').grid(row=9, column=4)
Button(root, text="Movement speed +", command=addMovSpeed, width=15, bg='gray58', fg='black').grid(row=10, column=4)
Button(root, text="Cell points +", command=addCp, width=15, bg='gray58', fg='black').grid(row=11, column=4)

sorted_gear_window = None
full_gear = {wearable_names['Helmet']: character.role.helmetS,
             wearable_names['Shoulder']: character.role.shoulderS,
             wearable_names['Armor']: character.role.armorS,
             wearable_names['Arm']: character.role.armS,
             wearable_names['Melee']: character.role.meleeS,
             wearable_names['Range']: character.role.rangeS,
             'Ring': ringS,
             wearable_names['Necklace']: necklaceS,
             wearable_names['Bead']: beadS}

sorted_gear_button = Button(root, text="See full gear stats", command=lambda: showGear(sorted_gear_window, full_gear),
                            bg='SlateBlue2')
sorted_gear_button.grid(row=1, column=0)

advancedRoleOption = IntVar()


def advanceRole():
    if advancedRoleOption.get() == 1:
        character.role.advancedClass()
    else:
        character.role.normalClass()
    update_stats()


advancedCharacter = Checkbutton(root, text="Advanced class", variable=advancedRoleOption,
                                command=advanceRole, bg='gray58').grid(row=12, column=6)


def openFacebook():
    webbrowser.open("https://www.facebook.com/Anzuilu/")


def openYoutube():
    webbrowser.open("https://www.youtube.com/c/llkisamell")


def openSteam():
    webbrowser.open("https://steamcommunity.com/id/iLuAnzu")


Button(root, text="Facebook", command=openFacebook, width=8, height=1, fg="white", bg="royalblue",
       font="Helvetica 11 bold").grid(row=13, column=3)
Button(root, text="Youtube", command=openYoutube, width=8, height=1, fg="white", bg="firebrick1",
       font="System 15 bold").grid(row=13, column=4)
Button(root, text="Steam", command=openSteam, width=8, height=1, fg="white", bg="gray18", font="System 15 bold").grid(
    row=13, column=5)

root.mainloop()
