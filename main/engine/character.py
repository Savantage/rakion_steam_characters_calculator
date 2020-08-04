from copy import deepcopy

from engine.enchanter import Enchanter
from engine.gear import Gear
from engine.levelstats import LevelStats
from engine.jewelry import *


class Character:

    def __init__(self, role):
        self.role = role
        self.gear = Gear()
        self.levelStats = LevelStats(role)
        self.enchanter = Enchanter(self.gear)

    def setHelmet(self, helmetName):
        if helmetName in self.role.helmetS:
            aux = deepcopy(self.role.helmetS[helmetName])
            self.gear.setHelmet(aux)

    def setShoulder(self, shoulderName):
        if shoulderName in self.role.shoulderS:
            aux = deepcopy(self.role.shoulderS[shoulderName])
            self.gear.setShoulder(aux)

    def setArmor(self, armorName):
        if armorName in self.role.armorS:
            aux = deepcopy(self.role.armorS[armorName])
            self.gear.setArmor(aux)

    def setArm(self, armName):
        if armName in self.role.armS:
            aux = deepcopy(self.role.armS[armName])
            self.gear.setArm(aux)

    def setMelee(self, meleeName):
        if meleeName in self.role.meleeS:
            aux = deepcopy(self.role.meleeS[meleeName])
            self.gear.setMelee(aux)

    def setRange(self, rangeName):
        if rangeName in self.role.rangeS:
            aux = deepcopy(self.role.rangeS[rangeName])
            self.gear.setRange(aux)

    def setRing1(self, ringName):
        if ringName in ringS:
            aux = deepcopy(ringS[ringName])
            self.gear.setRing1(aux)

    def setRing2(self, ringName):
        if ringName in ringS:
            aux = deepcopy(ringS[ringName])
            self.gear.setRing2(aux)

    def setRing3(self, ringName):
        if ringName in ringS:
            aux = deepcopy(ringS[ringName])
            self.gear.setRing3(aux)

    def setNeckLace(self, necklaceName):
        if necklaceName in necklaceS:
            aux = deepcopy(necklaceS[necklaceName])
            self.gear.setNecklace(aux)

    def setBead(self, beadName):
        if beadName in beadS:
            aux = deepcopy(beadS[beadName])
            self.gear.setBead(aux)

    # SET LEVEL
    def setLevel(self, level):
        self.levelStats.setLevel(level)

    # Añadir stats al personaje
    def addBasic(self, points):
        self.levelStats.addBasic(points)

    def addRange(self, points):
        self.levelStats.addRange(points)

    def addSpecial(self, points):
        self.levelStats.addSpecial(points)

    def addGrip(self, points):
        self.levelStats.addGrip(points)

    def addCellDestruction(self, points):
        self.levelStats.addCellDestruction(points)

    def addCellPoints(self, points):
        self.levelStats.addCellPoints(points)

    def addAttackSpeed(self, points):
        self.levelStats.addAttackSpeed(points)

    def addMovementSpeed(self, points):
        self.levelStats.addMovementSpeed(points)

    def addEnergy(self, points):
        self.levelStats.addHealthPoints(points)

    def addArmor(self, points):
        self.levelStats.addArmorPoints(points)

    # Getters stats individuales
    def getBasic(self):
        return self.role.basic + self.gear.getBasic() + self.levelStats.getBasic()

    def getRange(self):
        return self.role.range + self.gear.getRange() + self.levelStats.getRange()

    def getSpecial(self):
        return self.role.special + self.gear.getSpecial() + self.levelStats.getSpecial()

    def getGrip(self):
        return self.role.grip + self.gear.getGrip() + self.levelStats.getGrip()

    def getCellDestruction(self):
        return self.role.cd + self.gear.getCellDestruction() + self.levelStats.getCellDestruction()

    def getCellPoints(self):
        return self.role.cp + self.gear.getCellPoints() + self.levelStats.getCellPoints()

    def getAttackSpeed(self):
        return self.role.attackSpeed + self.gear.getAttackSpeed() + self.levelStats.getAttackSpeed()

    def getMovementSpeed(self):
        return self.role.movementSpeed + self.gear.getMovementSpeed() + self.levelStats.getMovementSpeed()

    def getEnergy(self):
        return self.role.hp + self.gear.getEnergy() + self.levelStats.getEnergy()

    def getArmor(self):
        return self.role.ap + self.gear.getArmor() + self.levelStats.getArmor()

    # Stats
    def getLevel(self):
        return self.levelStats.level

    def getAvailableStats(self):
        return self.levelStats.availablestatPoints

    # Funcion testeo
    def mostrarStats(self):
        print(self.getBasic())
        print(self.getRange())
        print(self.getSpecial())
        print(self.getGrip())
        print(self.getCellDestruction())
        print(self.getEnergy())
        print(self.getArmor())
        print(self.getAttackSpeed())
        print(self.getMovementSpeed())
        print(self.getCellPoints())
