import webbrowser
from tkinter import *

from engine.character import Character
from engine.jewelry import *
from gui.displayutils import showGear

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


def on_closing(root):
    root.destroy()


def setWearableLabels(window):
    aux = 2
    column = 0
    for wearable in wearable_names:
        Label(window, text=wearable_names[wearable], width=7, bg='gray60').grid(row=aux, column=column)
        aux = aux + 1


def setStatLabels(window):
    aux = 2
    column = 6
    for stat in stat_names:
        Label(window, text=stat, font="Helvetica 11 bold", width=14, bg='gray58', fg='orange').grid(row=aux,
                                                                                                    column=column)
        aux = aux + 1


def setStringAndSetValue(value):
    aux = StringVar()
    aux.set(value)
    return aux


def setEntryandPos(aRoot, row, column):
    aux = Entry(aRoot, width=5)
    aux.grid(row=row, column=column)
    return aux


def setintLabelandPos(rooot, num, row, column):
    aux = Label(rooot, text=str(num), bg='gray58', fg='dark slate blue')
    aux.grid(row=row, column=column)
    return aux


def optionMenuOptionsPosVar(rooot, var, options, row, column):
    aux = OptionMenu(rooot, var, *options)
    aux.grid(row=row, column=column)
    aux.config(bg='gray58')
    aux["highlightthickness"] = 0
    return aux


def update_stats(stat_labels, character):
    stat_labels[stat_names['Basic']].config(text=str(character.getBasic()))
    stat_labels[stat_names['Range']].config(text=str(character.getRange()))
    stat_labels[stat_names['Special']].config(text=str(character.getSpecial()))
    stat_labels[stat_names['Grip']].config(text=str(character.getGrip()))
    stat_labels[stat_names['Cell dest.']].config(text=str(character.getCellDestruction()))
    stat_labels[stat_names['Energy']].config(text=str(character.getEnergy()))
    stat_labels[stat_names['Armor']].config(text=str(character.getArmor()))
    stat_labels[stat_names['Attack speed']].config(text=str(character.getAttackSpeed()))
    stat_labels[stat_names['Movement Speed']].config(text=str(character.getMovementSpeed()))
    stat_labels[stat_names['Cell points']].config(text=str(character.getCellPoints()))


def updateStatpoints(stat_points, levelstats):
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


def setCharacterLevel(character, level_input, actual_level, actual_available_stats, levelstats, stat_points,
                      stat_labels):
    try:
        character.setLevel(int(level_input.get()))
    except ValueError:
        pass
    actual_level.config(text=str(character.getLevel()))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    updateStatpoints(stat_points, levelstats)
    update_stats(stat_labels, character)
    level_input.delete(0, "end")


def change_helmets_menu(character, wearablestringvars, statlabels, enchanting_string_vars):
    character.setHelmet(str(wearablestringvars[wearable_names['Helmet']].get()))
    enchanting_string_vars[wearable_names['Helmet']].set(options_enchanting[0])
    update_stats(statlabels, character)


def change_armors_menu(character, wearablestringvars, statlabels, enchanting_string_vars):
    character.setArmor(str(wearablestringvars[wearable_names['Armor']].get()))
    enchanting_string_vars[wearable_names['Armor']].set(options_enchanting[0])
    update_stats(statlabels, character)


def change_shoulders_menu(character, wearablestringvars, statlabels, enchanting_string_vars):
    character.setShoulder(str(wearablestringvars[wearable_names['Shoulder']].get()))
    enchanting_string_vars[wearable_names['Shoulder']].set(options_enchanting[0])
    update_stats(statlabels, character)


def change_arms_menu(character, wearablestringvars, statlabels, enchanting_string_vars):
    character.setArm(str(wearablestringvars[wearable_names['Arm']].get()))
    enchanting_string_vars[wearable_names['Arm']].set(options_enchanting[0])
    update_stats(statlabels, character)


def change_melees_menu(character, wearablestringvars, statlabels, enchanting_string_vars):
    character.setMelee(str(wearablestringvars[wearable_names['Melee']].get()))
    enchanting_string_vars[wearable_names['Melee']].set(options_enchanting[0])
    update_stats(statlabels, character)


def change_range_menu(character, wearablestringvars, statlabels, enchanting_string_vars):
    character.setRange(str(wearablestringvars[wearable_names['Range']].get()))
    enchanting_string_vars[wearable_names['Range']].set(options_enchanting[0])
    update_stats(statlabels, character)


def change_necklaces_menu(character, wearablestringvars, statlabels, enchanting_string_vars):
    character.setNeckLace(str(wearablestringvars[wearable_names['Necklace']].get()))
    enchanting_string_vars[wearable_names['Necklace']].set(options_enchanting[0])
    update_stats(statlabels, character)


def change_ring1s_menu(character, wearablestringvars, statlabels, enchanting_string_vars):
    character.setRing1(str(wearablestringvars[wearable_names['Ring A']].get()))
    enchanting_string_vars[wearable_names['Ring A']].set(options_enchanting[0])
    update_stats(statlabels, character)


def change_ring2s_menu(character, wearablestringvars, statlabels, enchanting_string_vars):
    character.setRing2(str(wearablestringvars[wearable_names['Ring B']].get()))
    enchanting_string_vars[wearable_names['Ring B']].set(options_enchanting[0])
    update_stats(statlabels, character)


def change_ring3s_menu(character, wearablestringvars, statlabels, enchanting_string_vars):
    character.setRing3(str(wearablestringvars[wearable_names['Ring C']].get()))
    enchanting_string_vars[wearable_names['Ring C']].set(options_enchanting[0])
    update_stats(statlabels, character)


def change_beads_menu(character, wearablestringvars, statlabels, enchanting_string_vars):
    character.setBead(str(wearablestringvars[wearable_names['Bead']].get()))
    enchanting_string_vars[wearable_names['Bead']].set(options_enchanting[0])
    update_stats(statlabels, character)


def enchant_helmet(enchanter, enchantingstringvars, statlabels, character):
    enchanter.enchantHelmet(enchantingstringvars[wearable_names['Helmet']].get())
    update_stats(statlabels, character)


def enchant_armor(enchanter, enchantingstringvars, statlabels, character):
    enchanter.enchantArmor(enchantingstringvars[wearable_names['Armor']].get())
    update_stats(statlabels, character)


def enchant_shoulder(enchanter, enchantingstringvars, statlabels, character):
    enchanter.enchantShoulder(enchantingstringvars[wearable_names['Shoulder']].get())
    update_stats(statlabels, character)


def enchant_arm(enchanter, enchantingstringvars, statlabels, character):
    enchanter.enchantArm(enchantingstringvars[wearable_names['Arm']].get())
    update_stats(statlabels, character)


def enchant_melee(enchanter, enchantingstringvars, statlabels, character):
    enchanter.enchantMelee(enchantingstringvars[wearable_names['Melee']].get())
    update_stats(statlabels, character)


def enchant_range(enchanter, enchantingstringvars, statlabels, character):
    enchanter.enchantRange(enchantingstringvars[wearable_names['Range']].get())
    update_stats(statlabels, character)


def enchant_necklace(enchanter, enchantingstringvars, statlabels, character):
    enchanter.enchantNecklace(enchantingstringvars[wearable_names['Necklace']].get())
    update_stats(statlabels, character)


def enchant_ring1(enchanter, enchantingstringvars, statlabels, character):
    enchanter.enchantRing1(enchantingstringvars[wearable_names['Ring A']].get())
    update_stats(statlabels, character)


def enchant_ring2(enchanter, enchantingstringvars, statlabels, character):
    enchanter.enchantRing2(enchantingstringvars[wearable_names['Ring B']].get())
    update_stats(statlabels, character)


def enchant_ring3(enchanter, enchantingstringvars, statlabels, character):
    enchanter.enchantRing3(enchantingstringvars[wearable_names['Ring C']].get())
    update_stats(statlabels, character)


def enchant_bead(enchanter, enchantingstringvars, statlabels, character):
    enchanter.enchantBead(enchantingstringvars[wearable_names['Bead']].get())
    update_stats(statlabels, character)


def addBasic(character, input_vars, stat_points, levelstats, actual_available_stats, stat_labels):
    try:
        character.addBasic(int(input_vars[stat_names['Basic']].get()))
    except ValueError:
        pass
    stat_points[stat_names['Basic']].config(text=str(levelstats.basicPoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats(stat_labels, character)
    input_vars[stat_names['Basic']].delete(0, "end")


def addRange(character, input_vars, stat_points, levelstats, actual_available_stats, stat_labels):
    try:
        character.addRange(int(input_vars[stat_names['Range']].get()))
    except ValueError:
        pass
    stat_points[stat_names['Range']].config(text=str(levelstats.rangePoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats(stat_labels, character)
    input_vars[stat_names['Range']].delete(0, "end")


def addSpecial(character, input_vars, stat_points, levelstats, actual_available_stats, stat_labels):
    try:
        character.addSpecial(int(input_vars[stat_names['Special']].get()))
    except ValueError:
        pass
    stat_points[stat_names['Special']].config(text=str(levelstats.specialPoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats(stat_labels, character)
    input_vars[stat_names['Special']].delete(0, "end")


def addGrip(character, input_vars, stat_points, levelstats, actual_available_stats, stat_labels):
    try:
        character.addGrip(int(input_vars[stat_names['Grip']].get()))
    except ValueError:
        pass
    stat_points[stat_names['Grip']].config(text=str(levelstats.gripPoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats(stat_labels, character)
    input_vars[stat_names['Grip']].delete(0, "end")


def addCd(character, input_vars, stat_points, levelstats, actual_available_stats, stat_labels):
    try:
        character.addCellDestruction(int(input_vars[stat_names['Cell dest.']].get()))
    except ValueError:
        pass
    stat_points[stat_names['Cell dest.']].config(text=str(levelstats.cdPoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats(stat_labels, character)
    input_vars[stat_names['Cell dest.']].delete(0, "end")


def addHp(character, input_vars, stat_points, levelstats, actual_available_stats, stat_labels):
    try:
        character.addEnergy(int(input_vars[stat_names['Energy']].get()))
    except ValueError:
        pass
    stat_points[stat_names['Energy']].config(text=str(levelstats.hpPoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats(stat_labels, character)
    input_vars[stat_names['Energy']].delete(0, "end")


def addAp(character, input_vars, stat_points, levelstats, actual_available_stats, stat_labels):
    try:
        character.addArmor(int(input_vars[stat_names['Armor']].get()))
    except ValueError:
        pass
    stat_points[stat_names['Armor']].config(text=str(levelstats.apPoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats(stat_labels, character)
    input_vars[stat_names['Armor']].delete(0, "end")


def addAttackSpeed(character, input_vars, stat_points, levelstats, actual_available_stats, stat_labels):
    try:
        character.addAttackSpeed(int(input_vars[stat_names['Attack speed']].get()))
    except ValueError:
        pass
    stat_points[stat_names['Attack speed']].config(text=str(levelstats.attackSpeedPoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats(stat_labels, character)
    input_vars[stat_names['Attack speed']].delete(0, "end")


def addMovSpeed(character, input_vars, stat_points, levelstats, actual_available_stats, stat_labels):
    try:
        character.addMovementSpeed(int(input_vars[stat_names['Movement Speed']].get()))
    except ValueError:
        pass
    stat_points[stat_names['Movement Speed']].config(text=str(levelstats.movementSpeedPoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats(stat_labels, character)
    input_vars[stat_names['Movement Speed']].delete(0, "end")


def addCp(character, input_vars, stat_points, levelstats, actual_available_stats, stat_labels):
    try:
        character.addCellPoints(int(input_vars[stat_names['Cell points']].get()))
    except ValueError:
        pass
    stat_points[stat_names['Cell points']].config(text=str(levelstats.cpPoints))
    actual_available_stats.config(text=str(character.getAvailableStats()))
    update_stats(stat_labels, character)
    input_vars[stat_names['Cell points']].delete(0, "end")


def advanceRole(advancedRoleOption, character, stat_labels):
    if advancedRoleOption.get() == 1:
        character.role.advancedClass()
    else:
        character.role.normalClass()
    update_stats(stat_labels, character)


def bonusStats(stats, option, label, character, stat_labels, stat_points):
    if option.get() == 1:
        stats.activateBonusStats()
    else:
        stats.deactivateBonusStats()
    label.config(text=str(character.getAvailableStats()))
    update_stats(stat_labels, character)
    updateStatpoints(stat_points, character.stats)


def openFacebook():
    webbrowser.open("https://www.facebook.com/Anzuilu/")


def openYoutube():
    webbrowser.open("https://www.youtube.com/c/llkisamell")


def openSteam():
    webbrowser.open("https://steamcommunity.com/id/iLuAnzu")


def displayCalculator(role, tittle, window, character_level_str):
    window.withdraw()

    calculatorwindow = Toplevel()
    calculatorwindow.protocol("WM_DELETE_WINDOW", lambda: on_closing(window))

    calculatorwindow.configure(bg='gray58')
    calculatorwindow.title(tittle)
    calculatorwindow.geometry("850x450")

    character = Character(role)
    enchanter = character.enchanter
    stats = character.stats

    role_helmets = list(character.role.helmetS)
    role_shoulders = list(character.role.shoulderS)
    role_armors = list(character.role.armorS)
    role_arms = list(character.role.armS)
    role_melees = list(character.role.meleeS)
    role_ranges = list(character.role.rangeS)
    role_rings = list(ringS)
    role_necklace = list(necklaceS)
    role_beads = list(beadS)

    setWearableLabels(calculatorwindow)
    setStatLabels(calculatorwindow)

    Label(calculatorwindow, text="Points used", font="Helvetica 10 bold", bg='gray58', fg='SlateBlue4', width=14).grid(
        row=1,
        column=5)

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

    input_vars = {stat_names['Basic']: setEntryandPos(calculatorwindow, 2, 3),
                  stat_names['Range']: setEntryandPos(calculatorwindow, 3, 3),
                  stat_names['Special']: setEntryandPos(calculatorwindow, 4, 3),
                  stat_names['Grip']: setEntryandPos(calculatorwindow, 5, 3),
                  stat_names['Cell dest.']: setEntryandPos(calculatorwindow, 6, 3),
                  stat_names['Energy']: setEntryandPos(calculatorwindow, 7, 3),
                  stat_names['Armor']: setEntryandPos(calculatorwindow, 8, 3),
                  stat_names['Attack speed']: setEntryandPos(calculatorwindow, 9, 3),
                  stat_names['Movement Speed']: setEntryandPos(calculatorwindow, 10, 3),
                  stat_names['Cell points']: setEntryandPos(calculatorwindow, 11, 3)
                  }

    stat_points = {stat_names['Basic']: setintLabelandPos(calculatorwindow, stats.basicPoints, 2, 5),
                   stat_names['Range']: setintLabelandPos(calculatorwindow, stats.rangePoints, 3, 5),
                   stat_names['Special']: setintLabelandPos(calculatorwindow, stats.specialPoints, 4, 5),
                   stat_names['Grip']: setintLabelandPos(calculatorwindow, stats.gripPoints, 5, 5),
                   stat_names['Cell dest.']: setintLabelandPos(calculatorwindow, stats.cdPoints, 6, 5),
                   stat_names['Energy']: setintLabelandPos(calculatorwindow, stats.hpPoints, 7, 5),
                   stat_names['Armor']: setintLabelandPos(calculatorwindow, stats.apPoints, 8, 5),
                   stat_names['Attack speed']: setintLabelandPos(calculatorwindow, stats.attackSpeedPoints, 9, 5),
                   stat_names['Movement Speed']: setintLabelandPos(calculatorwindow, stats.movementSpeedPoints, 10,
                                                                   5),
                   stat_names['Cell points']: setintLabelandPos(calculatorwindow, stats.cpPoints, 11, 5)}

    option_menu_vars = {
        wearable_names['Helmet']: optionMenuOptionsPosVar(calculatorwindow,
                                                          wearables_string_vars[wearable_names['Helmet']],
                                                          role_helmets, 2, 1),

        wearable_names['Armor']: optionMenuOptionsPosVar(calculatorwindow,
                                                         wearables_string_vars[wearable_names['Armor']],
                                                         role_armors, 3, 1),
        wearable_names['Shoulder']: optionMenuOptionsPosVar(calculatorwindow,
                                                            wearables_string_vars[wearable_names['Shoulder']],
                                                            role_shoulders, 4, 1),
        wearable_names['Arm']: optionMenuOptionsPosVar(calculatorwindow, wearables_string_vars[wearable_names['Arm']],
                                                       role_arms,
                                                       5, 1),
        wearable_names['Melee']: optionMenuOptionsPosVar(calculatorwindow,
                                                         wearables_string_vars[wearable_names['Melee']],
                                                         role_melees, 6, 1),
        wearable_names['Range']: optionMenuOptionsPosVar(calculatorwindow,
                                                         wearables_string_vars[wearable_names['Range']],
                                                         role_ranges, 7, 1),
        wearable_names['Necklace']: optionMenuOptionsPosVar(calculatorwindow,
                                                            wearables_string_vars[wearable_names['Necklace']],
                                                            role_necklace, 8, 1),
        wearable_names['Ring A']: optionMenuOptionsPosVar(calculatorwindow,
                                                          wearables_string_vars[wearable_names['Ring A']],
                                                          role_rings, 9, 1),
        wearable_names['Ring B']: optionMenuOptionsPosVar(calculatorwindow,
                                                          wearables_string_vars[wearable_names['Ring B']],
                                                          role_rings, 10, 1),
        wearable_names['Ring C']: optionMenuOptionsPosVar(calculatorwindow,
                                                          wearables_string_vars[wearable_names['Ring C']],
                                                          role_rings, 11, 1),
        wearable_names['Bead']: optionMenuOptionsPosVar(calculatorwindow, wearables_string_vars[wearable_names['Bead']],
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
        wearable_names['Helmet']: optionMenuOptionsPosVar(calculatorwindow,
                                                          enchanting_string_vars[wearable_names['Helmet']],
                                                          options_enchanting, 2, 2),
        wearable_names['Armor']: optionMenuOptionsPosVar(calculatorwindow,
                                                         enchanting_string_vars[wearable_names['Armor']],
                                                         options_enchanting, 3, 2),
        wearable_names['Shoulder']: optionMenuOptionsPosVar(calculatorwindow,
                                                            enchanting_string_vars[wearable_names['Shoulder']],
                                                            options_enchanting, 4, 2),
        wearable_names['Arm']: optionMenuOptionsPosVar(calculatorwindow, enchanting_string_vars[wearable_names['Arm']],
                                                       options_enchanting, 5, 2),
        wearable_names['Melee']: optionMenuOptionsPosVar(calculatorwindow,
                                                         enchanting_string_vars[wearable_names['Melee']],
                                                         options_enchanting, 6, 2),
        wearable_names['Range']: optionMenuOptionsPosVar(calculatorwindow,
                                                         enchanting_string_vars[wearable_names['Range']],
                                                         options_enchanting, 7, 2),
        wearable_names['Ring A']: optionMenuOptionsPosVar(calculatorwindow,
                                                          enchanting_string_vars[wearable_names['Ring A']],
                                                          options_enchanting, 8, 2),
        wearable_names['Ring B']: optionMenuOptionsPosVar(calculatorwindow,
                                                          enchanting_string_vars[wearable_names['Ring B']],
                                                          options_enchanting, 9, 2),
        wearable_names['Ring C']: optionMenuOptionsPosVar(calculatorwindow,
                                                          enchanting_string_vars[wearable_names['Ring C']],
                                                          options_enchanting, 10, 2),
        wearable_names['Necklace']: optionMenuOptionsPosVar(calculatorwindow,
                                                            enchanting_string_vars[wearable_names['Necklace']],
                                                            options_enchanting, 11, 2),
        wearable_names['Bead']: optionMenuOptionsPosVar(calculatorwindow,
                                                        enchanting_string_vars[wearable_names['Bead']],
                                                        options_enchanting, 12, 2)}

    stat_labels = {stat_names['Basic']: setintLabelandPos(calculatorwindow, character.getBasic(), 2, 7),
                   stat_names['Range']: setintLabelandPos(calculatorwindow, character.getRange(), 3, 7),
                   stat_names['Special']: setintLabelandPos(calculatorwindow, character.getSpecial(), 4, 7),
                   stat_names['Grip']: setintLabelandPos(calculatorwindow, character.getGrip(), 5, 7),
                   stat_names['Cell dest.']: setintLabelandPos(calculatorwindow, character.getCellDestruction(), 6, 7),
                   stat_names['Energy']: setintLabelandPos(calculatorwindow, character.getEnergy(), 7, 7),
                   stat_names['Armor']: setintLabelandPos(calculatorwindow, character.getArmor(), 8, 7),
                   stat_names['Attack speed']: setintLabelandPos(calculatorwindow, character.getAttackSpeed(), 9, 7),
                   stat_names['Movement Speed']: setintLabelandPos(calculatorwindow, character.getMovementSpeed(), 10,
                                                                   7),
                   stat_names['Cell points']: setintLabelandPos(calculatorwindow, character.getCellPoints(), 11, 7)}

    wearables_string_vars[wearable_names['Helmet']].trace('w',
                                                          lambda a, b, c: change_helmets_menu(character,
                                                                                              wearables_string_vars,
                                                                                              stat_labels,
                                                                                              enchanting_string_vars))
    wearables_string_vars[wearable_names['Armor']].trace('w', lambda a, b, c: change_armors_menu(character,
                                                                                                 wearables_string_vars,
                                                                                                 stat_labels,
                                                                                                 enchanting_string_vars))
    wearables_string_vars[wearable_names['Shoulder']].trace('w', lambda a, b, c: change_shoulders_menu(character,
                                                                                                       wearables_string_vars,
                                                                                                       stat_labels,
                                                                                                       enchanting_string_vars))
    wearables_string_vars[wearable_names['Arm']].trace('w', lambda a, b, c: change_arms_menu(character,
                                                                                             wearables_string_vars,
                                                                                             stat_labels,
                                                                                             enchanting_string_vars))
    wearables_string_vars[wearable_names['Melee']].trace('w', lambda a, b, c: change_melees_menu(character,
                                                                                                 wearables_string_vars,
                                                                                                 stat_labels,
                                                                                                 enchanting_string_vars))
    wearables_string_vars[wearable_names['Range']].trace('w', lambda a, b, c: change_range_menu(character,
                                                                                                wearables_string_vars,
                                                                                                stat_labels,
                                                                                                enchanting_string_vars))
    wearables_string_vars[wearable_names['Ring A']].trace('w', lambda a, b, c: change_ring1s_menu(character,
                                                                                                  wearables_string_vars,
                                                                                                  stat_labels,
                                                                                                  enchanting_string_vars))
    wearables_string_vars[wearable_names['Ring B']].trace('w', lambda a, b, c: change_ring2s_menu(character,
                                                                                                  wearables_string_vars,
                                                                                                  stat_labels,
                                                                                                  enchanting_string_vars))
    wearables_string_vars[wearable_names['Ring C']].trace('w', lambda a, b, c: change_ring3s_menu(character,
                                                                                                  wearables_string_vars,
                                                                                                  stat_labels,
                                                                                                  enchanting_string_vars))
    wearables_string_vars[wearable_names['Necklace']].trace('w', lambda a, b, c: change_necklaces_menu(character,
                                                                                                       wearables_string_vars,
                                                                                                       stat_labels,
                                                                                                       enchanting_string_vars))
    wearables_string_vars[wearable_names['Bead']].trace('w', lambda a, b, c: change_beads_menu(character,
                                                                                               wearables_string_vars,
                                                                                               stat_labels,
                                                                                               enchanting_string_vars))

    enchanting_string_vars[wearable_names['Helmet']].trace('w', lambda a, b, c: enchant_helmet(enchanter,
                                                                                               enchanting_string_vars,
                                                                                               stat_labels, character))
    enchanting_string_vars[wearable_names['Armor']].trace('w', lambda a, b, c: enchant_armor(enchanter,
                                                                                             enchanting_string_vars,
                                                                                             stat_labels, character))
    enchanting_string_vars[wearable_names['Shoulder']].trace('w', lambda a, b, c: enchant_shoulder(enchanter,
                                                                                                   enchanting_string_vars,
                                                                                                   stat_labels,
                                                                                                   character))
    enchanting_string_vars[wearable_names['Arm']].trace('w', lambda a, b, c: enchant_arm(enchanter,
                                                                                         enchanting_string_vars,
                                                                                         stat_labels, character))
    enchanting_string_vars[wearable_names['Melee']].trace('w', lambda a, b, c: enchant_melee(enchanter,
                                                                                             enchanting_string_vars,
                                                                                             stat_labels, character))
    enchanting_string_vars[wearable_names['Range']].trace('w', lambda a, b, c: enchant_range(enchanter,
                                                                                             enchanting_string_vars,
                                                                                             stat_labels, character))
    enchanting_string_vars[wearable_names['Necklace']].trace('w', lambda a, b, c: enchant_necklace(enchanter,
                                                                                                   enchanting_string_vars,
                                                                                                   stat_labels,
                                                                                                   character))
    enchanting_string_vars[wearable_names['Ring A']].trace('w', lambda a, b, c: enchant_ring1(enchanter,
                                                                                              enchanting_string_vars,
                                                                                              stat_labels, character))
    enchanting_string_vars[wearable_names['Ring B']].trace('w', lambda a, b, c: enchant_ring2(enchanter,
                                                                                              enchanting_string_vars,
                                                                                              stat_labels, character))
    enchanting_string_vars[wearable_names['Ring C']].trace('w', lambda a, b, c: enchant_ring3(enchanter,
                                                                                              enchanting_string_vars,
                                                                                              stat_labels, character))
    enchanting_string_vars[wearable_names['Bead']].trace('w', lambda a, b, c: enchant_bead(enchanter,
                                                                                           enchanting_string_vars,
                                                                                           stat_labels, character))

    level_string = Label(calculatorwindow, text=character_level_str, font="Helvetica 16 bold", fg="dark green",
                         bg='gray58')
    level_string.grid(row=0, column=6)

    actual_level = Label(calculatorwindow, text=str(character.getLevel()), font="Helvetica 14 bold", fg="dark green",
                         bg='gray58')
    actual_level.grid(row=0, column=7)

    available_stats_string = Label(calculatorwindow, text="Available stat points: ", font="Helvetica 10 bold",
                                   bg='gray40',
                                   fg='gray80')
    available_stats_string.grid(row=1, column=3)

    actual_available_stats = Label(calculatorwindow, text=str(character.getAvailableStats()), font="Helvetica 10 bold",
                                   bg='gray40',
                                   fg='gray80', width=14)
    actual_available_stats.grid(row=1, column=4)

    level_input = Entry(calculatorwindow, width=4)
    level_input.grid(row=1, column=6)

    change_level = Button(calculatorwindow, text="Change level",
                          command=lambda: setCharacterLevel(character, level_input, actual_level,
                                                            actual_available_stats, stats, stat_points,
                                                            stat_labels), bg='gray58')
    change_level.grid(row=1, column=7)

    Button(calculatorwindow, text="Basic +",
           command=lambda: addBasic(character, input_vars, stat_points, stats, actual_available_stats,
                                    stat_labels), width=15, bg='gray58', fg='black').grid(row=2, column=4)
    Button(calculatorwindow, text="Range +",
           command=lambda: addRange(character, input_vars, stat_points, stats, actual_available_stats,
                                    stat_labels), width=15, bg='gray58', fg='black').grid(row=3, column=4)
    Button(calculatorwindow, text="Special +",
           command=lambda: addSpecial(character, input_vars, stat_points, stats, actual_available_stats,
                                      stat_labels), width=15, bg='gray58', fg='black').grid(row=4, column=4)
    Button(calculatorwindow, text="Grip +",
           command=lambda: addGrip(character, input_vars, stat_points, stats, actual_available_stats,
                                   stat_labels), width=15, bg='gray58', fg='black').grid(row=5, column=4)
    Button(calculatorwindow, text="Cell dest. +",
           command=lambda: addCd(character, input_vars, stat_points, stats, actual_available_stats, stat_labels),
           width=15, bg='gray58', fg='black').grid(row=6, column=4)
    Button(calculatorwindow, text="Energy +",
           command=lambda: addHp(character, input_vars, stat_points, stats, actual_available_stats, stat_labels),
           width=15, bg='gray58', fg='black').grid(row=7, column=4)
    Button(calculatorwindow, text="Armor +",
           command=lambda: addAp(character, input_vars, stat_points, stats, actual_available_stats, stat_labels),
           width=15, bg='gray58', fg='black').grid(row=8, column=4)
    Button(calculatorwindow, text="Attack speed +",
           command=lambda: addAttackSpeed(character, input_vars, stat_points, stats, actual_available_stats,
                                          stat_labels), width=15, bg='gray58', fg='black').grid(row=9, column=4)
    Button(calculatorwindow, text="Movement speed +",
           command=lambda: addMovSpeed(character, input_vars, stat_points, stats, actual_available_stats,
                                       stat_labels), width=15, bg='gray58', fg='black').grid(row=10, column=4)
    Button(calculatorwindow, text="Cell points +",
           command=lambda: addCp(character, input_vars, stat_points, stats, actual_available_stats,
                                 stat_labels),
           width=15, bg='gray58', fg='black').grid(row=11, column=4)

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

    sorted_gear_button = Button(calculatorwindow, text="See full gear stats",
                                command=lambda: showGear(sorted_gear_window, full_gear),
                                bg='SlateBlue2')
    sorted_gear_button.grid(row=1, column=0)

    advancedRoleOption = IntVar()
    Checkbutton(calculatorwindow, text="Advanced class", variable=advancedRoleOption,
                command=lambda: advanceRole(advancedRoleOption, character, stat_labels),
                bg='gray58').grid(row=12, column=6)

    bonusStatOption = IntVar()
    Checkbutton(calculatorwindow, text="Bonus stat", variable=bonusStatOption,
                command=lambda: bonusStats(stats, bonusStatOption, actual_available_stats, character, stat_labels,
                                           stat_points),
                bg='gray58').grid(row=0, column=3)

    Button(calculatorwindow, text="Facebook", command=openFacebook, width=8, height=1, fg="white", bg="royalblue",
           font="Helvetica 11 bold").grid(row=13, column=3)
    Button(calculatorwindow, text="Youtube", command=openYoutube, width=8, height=1, fg="white", bg="firebrick1",
           font="System 15 bold").grid(row=13, column=4)
    Button(calculatorwindow, text="Steam", command=openSteam, width=8, height=1, fg="white", bg="gray18",
           font="System 15 bold").grid(
        row=13, column=5)
