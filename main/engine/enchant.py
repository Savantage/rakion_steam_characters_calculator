def oneStats(level):
    return (level ** 2) / 50


def calcMovSpeed(level):
    return (level ** 2) / 50 * 0.024


def calcAttSpeed(level):
    return (level ** 2) / 50 * 0.16


def calcCp(level):
    return (level ** 2) / 50 * 200


class Enchant:
    def __init__(self):
        self.level = 0

    def setEnchantLevel(self, level):
        self.level = int(level)

    """GETTERS"""
    def getBasic(self):
        return oneStats(self.level)

    def getRange(self):
        return oneStats(self.level)

    def getSpecial(self):
        return oneStats(self.level)

    def getGrip(self):
        return oneStats(self.level)

    def getCd(self):
        return oneStats(self.level)

    def getAP(self):
        return oneStats(self.level)

    def getHP(self):
        return oneStats(self.level)

    def getAttSpeed(self):
        return calcAttSpeed(self.level)

    def getMovSpeed(self):
        return calcMovSpeed(self.level)

    def getCp(self):
        return calcCp(self.level)
