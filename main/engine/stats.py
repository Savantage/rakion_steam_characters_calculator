# FUNCION CALCULA STATS


def validPoints(actualPoints, pointsToAdd, availableStatPoints):
    if pointsToAdd > availableStatPoints or actualPoints + pointsToAdd > 100 or pointsToAdd < 0:
        return False
    else:
        return True


class Stats:
    def __init__(self, character):
        # character stat gained per level point
        self.basicPerPoint = character.basicPerPoint
        self.rangePerPoint = character.rangePerPoint
        self.specialPerPoint = character.specialPerPoint
        self.gripPerPoint = character.gripPerPoint
        self.cdPerPoint = character.cdPerPoint
        self.hpPerPoint = character.hpPerPoint
        self.apPerPoint = character.apPerPoint
        self.attSpeedPerPoint = character.attSpeedPerPoint
        self.movSpedPerPoint = character.movSpeedPerPoint
        self.cpPerPoint = character.cpPerPoint
        self.past50 = character.PAST50
        self.past80 = character.PAST80

        self.bonusStats = 0
        self.availablestatPoints = 0
        self.level = 1

        # stat points bonuses
        self.basic = 0
        self.range = 0
        self.special = 0
        self.grip = 0
        self.cd = 0
        self.hp = 0
        self.ap = 0
        self.attackSpeed = 0
        self.movementSpeed = 0
        self.cp = 0

        # stat points used
        self.basicPoints = 0
        self.rangePoints = 0
        self.specialPoints = 0
        self.gripPoints = 0
        self.cdPoints = 0
        self.hpPoints = 0
        self.apPoints = 0
        self.attackSpeedPoints = 0
        self.movementSpeedPoints = 0
        self.cpPoints = 0

    def addStatsLogic(self, gained, points):
        totalAdded = 0

        # Si hay menos de 51 puntos de stat
        if 0 < points < 51:
            totalAdded = gained * points
        # Si hay mas de 50 puntos de stat
        elif 50 < points < 81:
            pointspast50 = points - 50
            totalAdded = gained * 50 + self.past50 * gained * pointspast50
        # Si hay mas de 80 puntos de stat
        elif 80 < points < 101:
            pointspast80 = points - 80
            pointspast50 = points - pointspast80 - 50
            totalAdded = gained * 50 + self.past50 * gained * pointspast50 + self.past80 * gained * pointspast80

        return totalAdded

    # Elegir nivel
    def setLevel(self, level):
        self.statReset()
        if 0 < level < 100:
            self.level = level
            self.availablestatPoints = (level * 3) - 3 + self.bonusStats

    def activateBonusStats(self):
        self.bonusStats = 200
        self.availablestatPoints = self.availablestatPoints + self.bonusStats

    def deactivateBonusStats(self):
        self.statReset()
        self.bonusStats = 0
        self.setLevel(self.level)

    def getAvailableStatPoints(self):
        return self.availablestatPoints

    # Getters para cada stat

    def getBasic(self):
        return self.basic

    def getRange(self):
        return self.range

    def getSpecial(self):
        return self.special

    def getGrip(self):
        return self.grip

    def getCellDestruction(self):
        return self.cd

    def getEnergy(self):
        return self.hp

    def getArmor(self):
        return self.ap

    def getAttackSpeed(self):
        return self.attackSpeed

    def getMovementSpeed(self):
        return self.movementSpeed

    def getCellPoints(self):
        return self.cp

    # Resetea los stats
    def statReset(self):
        self.basicPoints = 0
        self.rangePoints = 0
        self.specialPoints = 0
        self.gripPoints = 0
        self.cdPoints = 0
        self.hpPoints = 0
        self.apPoints = 0
        self.attackSpeedPoints = 0
        self.movementSpeedPoints = 0
        self.cpPoints = 0

        self.basic = 0
        self.range = 0
        self.special = 0
        self.grip = 0
        self.cd = 0
        self.hp = 0
        self.ap = 0
        self.attackSpeed = 0
        self.movementSpeed = 0
        self.cp = 0

    # 10 funciones para añadir los puntos de stat
    def addBasic(self, pointsToAdd):
        if validPoints(self.basicPoints, pointsToAdd, self.availablestatPoints):
            self.basicPoints = self.basicPoints + pointsToAdd
            self.availablestatPoints = self.availablestatPoints - pointsToAdd
            self.basic = self.addStatsLogic(self.basicPerPoint, self.basicPoints)

    def addRange(self, pointsToAdd):
        if validPoints(self.rangePoints, pointsToAdd, self.availablestatPoints):
            self.rangePoints = self.rangePoints + pointsToAdd
            self.availablestatPoints = self.availablestatPoints - pointsToAdd
            self.range = self.addStatsLogic(self.rangePerPoint, self.rangePoints)

    def addSpecial(self, pointsToAdd):
        if validPoints(self.specialPoints, pointsToAdd, self.availablestatPoints):
            self.specialPoints = self.specialPoints + pointsToAdd
            self.availablestatPoints = self.availablestatPoints - pointsToAdd
            self.special = self.addStatsLogic(self.specialPerPoint, self.specialPoints)

    def addGrip(self, pointsToAdd):
        if validPoints(self.gripPoints, pointsToAdd, self.availablestatPoints):
            self.gripPoints = self.gripPoints + pointsToAdd
            self.availablestatPoints = self.availablestatPoints - pointsToAdd
            self.grip = self.addStatsLogic(self.gripPerPoint, self.gripPoints)

    def addCellDestruction(self, pointsToAdd):
        if validPoints(self.cdPoints, pointsToAdd, self.availablestatPoints):
            self.cdPoints = self.cdPoints + pointsToAdd
            self.availablestatPoints = self.availablestatPoints - pointsToAdd
            self.cd = self.addStatsLogic(self.cdPerPoint, self.cdPoints)

    def addHealthPoints(self, pointsToAdd):
        if validPoints(self.hpPoints, pointsToAdd, self.availablestatPoints):
            self.hpPoints = self.hpPoints + pointsToAdd
            self.availablestatPoints = self.availablestatPoints - pointsToAdd
            self.hp = self.addStatsLogic(self.hpPerPoint, self.hpPoints)

    def addArmorPoints(self, pointsToAdd):
        if validPoints(self.apPoints, pointsToAdd, self.availablestatPoints):
            self.apPoints = self.apPoints + pointsToAdd
            self.availablestatPoints = self.availablestatPoints - pointsToAdd
            self.ap = self.addStatsLogic(self.apPerPoint, self.apPoints)

    def addAttackSpeed(self, pointsToAdd):
        if validPoints(self.attackSpeedPoints, pointsToAdd, self.availablestatPoints):
            self.attackSpeedPoints = self.attackSpeedPoints + pointsToAdd
            self.availablestatPoints = self.availablestatPoints - pointsToAdd
            self.attackSpeed = self.addStatsLogic(self.attSpeedPerPoint, self.attackSpeedPoints)

    def addMovementSpeed(self, pointsToAdd):
        if validPoints(self.movementSpeedPoints, pointsToAdd, self.availablestatPoints):
            self.movementSpeedPoints = self.movementSpeedPoints + pointsToAdd
            self.availablestatPoints = self.availablestatPoints - pointsToAdd
            self.movementSpeed = self.addStatsLogic(self.movSpedPerPoint, self.movementSpeedPoints)

    def addCellPoints(self, pointsToAdd):
        if validPoints(self.cpPoints, pointsToAdd, self.availablestatPoints):
            self.cpPoints = self.cpPoints + pointsToAdd
            self.availablestatPoints = self.availablestatPoints - pointsToAdd
            self.cp = self.addStatsLogic(self.cpPerPoint, self.cpPoints)
