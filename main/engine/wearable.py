from engine.enchant import Enchant


class Wearable:

    def __init__(self, name="Default", basic=0, range=0, special=0, grip=0, cd=0, hp=0, ap=0, attackSpeed=0,
                 movementSpeed=0, cp=0):
        self.name = name
        self.enchantlevel = Enchant()

        self.basic = basic
        self.range = range
        self.special = special
        self.grip = grip
        self.cd = cd
        self.hp = hp
        self.ap = ap
        self.attackSpeed = attackSpeed
        self.movementSpeed = movementSpeed
        self.cp = cp

    # ENCHANT WEARABLE

    def enchant(self, level):
        self.enchantlevel.setEnchantLevel(level)

    # GET STATS
    def getBasic(self):
        return self.basic + self.enchantlevel.getBasic()

    def getRange(self):
        return self.range + self.enchantlevel.getRange()

    def getSpecial(self):
        return self.special + self.enchantlevel.getSpecial()

    def getGrip(self):
        return self.grip + self.enchantlevel.getGrip()

    def getCd(self):
        return self.cd + self.enchantlevel.getCd()

    def getHp(self):
        return self.hp + self.enchantlevel.getHP()

    def getAp(self):
        return self.ap + self.enchantlevel.getAP()

    def getAttackSpeed(self):
        return self.attackSpeed + self.enchantlevel.getAttSpeed()

    def getMovementSpeed(self):
        return self.movementSpeed + self.enchantlevel.getMovSpeed()

    def getCP(self):
        return self.cp + self.enchantlevel.getCp()