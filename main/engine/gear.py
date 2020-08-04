from engine.wearable import Wearable


class Gear:
    def __init__(self):
        self.helmet = Wearable()
        self.shoulder = Wearable()
        self.armor = Wearable()
        self.arm = Wearable()
        self.melee = Wearable()
        self.range = Wearable()
        self.necklace = Wearable()
        self.ring1 = Wearable()
        self.ring2 = Wearable()
        self.ring3 = Wearable()
        self.bead = Wearable()

        self.wearables = [self.helmet, self.shoulder, self.armor, self.arm, self.melee, self.range, self.necklace,
                          self.ring1, self.ring2, self.ring3, self.bead]

    """SETTERS"""

    def setHelmet(self, helmet):
        self.helmet = helmet
        self.wearables[0] = helmet

    def setShoulder(self, shoulder):
        self.shoulder = shoulder
        self.wearables[1] = shoulder

    def setArmor(self, armor):
        self.armor = armor
        self.wearables[2] = armor

    def setArm(self, arm):
        self.arm = arm
        self.wearables[3] = arm

    def setMelee(self, melee):
        self.melee = melee
        self.wearables[4] = melee

    def setRange(self, range):
        self.range = range
        self.wearables[5] = range

    def setNecklace(self, necklace):
        self.necklace = necklace
        self.wearables[6] = necklace

    def setRing1(self, ring1):
        self.ring1 = ring1
        self.wearables[7] = ring1

    def setRing2(self, ring2):
        self.ring2 = ring2
        self.wearables[8] = ring2

    def setRing3(self, ring3):
        self.ring3 = ring3
        self.wearables[9] = ring3

    def setBead(self, bead):
        self.bead = bead
        self.wearables[10] = bead

    """GETTERS"""

    def getBasic(self):
        total = 0
        for wearable in self.wearables:
            total = wearable.getBasic() + total
        return total

    def getRange(self):
        total = 0
        for wearable in self.wearables:
            total = wearable.getRange() + total
        return total

    def getSpecial(self):
        total = 0
        for wearable in self.wearables:
            total = wearable.getSpecial() + total
        return total

    def getGrip(self):
        total = 0
        for wearable in self.wearables:
            total = wearable.getGrip() + total
        return total

    def getCellDestruction(self):
        total = 0
        for wearable in self.wearables:
            total = wearable.getCd() + total
        return total

    def getArmor(self):
        total = 0
        for wearable in self.wearables:
            total = wearable.getAp() + total
        return total

    def getEnergy(self):
        total = 0
        for wearable in self.wearables:
            total = wearable.getHp() + total
        return total

    def getAttackSpeed(self):
        total = 0
        for wearable in self.wearables:
            total = wearable.getAttackSpeed() + total
        return total

    def getMovementSpeed(self):
        total = 0
        for wearable in self.wearables:
            total = wearable.getMovementSpeed() + total
        return total

    def getCellPoints(self):
        total = 0
        for wearable in self.wearables:
            total = wearable.getCP() + total
        return total
