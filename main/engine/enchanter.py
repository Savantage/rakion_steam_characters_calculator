class Enchanter:
    def __init__(self, gear):
        self.gear = gear

    def enchantHelmet(self, level):
        self.gear.helmet.enchant(level)

    def enchantShoulder(self, level):
        self.gear.shoulder.enchant(level)

    def enchantArmor(self, level):
        self.gear.armor.enchant(level)

    def enchantMelee(self, level):
        self.gear.melee.enchant(level)

    def enchantRange(self, level):
        self.gear.range.enchant(level)

    def enchantArm(self, level):
        self.gear.arm.enchant(level)

    def enchantRing1(self, level):
        self.gear.ring1.enchant(level)

    def enchantRing2(self, level):
        self.gear.ring2.enchant(level)

    def enchantRing3(self, level):
        self.gear.ring3.enchant(level)

    def enchantNecklace(self, level):
        self.gear.necklace.enchant(level)

    def enchantBead(self, level):
        self.gear.bead.enchant(level)
