from engine.roles.dualist_stats import *
from engine.wearable import Wearable

dualist_helmetS = {'Default': Wearable(),
                   'Legendary': Wearable("Legendary", 2, 3, 3, 3, 2, 8, 10, 0.52, 0.08, 1500),
                   'Lava': Wearable("Lava", 2, 2, 3, 2, 3, 10, 10, 0.01, 0.01, 150),
                   'Mercenary': Wearable("Lava", 2, 2, 3, 2, 3, 10, 10, 0.01, 0.01, 150),
                   'Sparta': Wearable("Sparta", 2, 0, 0, 2, 2, 20, 20, 0.24, 0.03, 150),
                   'Zodiac': Wearable("Zodiac", 5, 5, 5, 5, 5, 20, 20, 0.48, 0.08, 600),
                   'Viking': Wearable("Viking", 4, 3, 6, 6, 2, 22, 22, 0.29, 0.06, 200),
                   'Warrior': Wearable("Warrior", 6, 5, 8, 8, 2, 10, 10, 0.34, 0.07, 200),
                   'Pioneer Viking': Wearable("Pioneer Viking", 6, 5, 5, 5, 1, 22, 18, 0.44, 0.1, 300)
                   }

dualist_shoulderS = {'Default': Wearable(),
                     'Mercenary': Wearable("Lava", 2, 2, 3, 2, 3, 10, 10, 0.01, 0.01, 150),
                     'Sparta': Wearable("Sparta", 1, 0, 0, 2, 1, 15, 15, 0.23, 0.02, 80),
                     'Lava': Wearable("Lava", 1, 2, 1, 3, 2, 15, 15, 0.11, 0.01, 80),
                     'Legendary': Wearable("Legendary", 1, 3, 2, 2, 2, 3, 2, 0.56, 0.06, 1100),
                     'Warrior': Wearable("Warrior", 6, 5, 8, 8, 2, 8, 8, 0.44, 0.08, 200),
                     'Viking': Wearable("Viking", 4, 3, 6, 6, 2, 22, 22, 0.29, 0.06, 200),
                     'Zodiac': Wearable("Zodiac", 5, 5, 5, 5, 5, 15, 15, 0.48, 0.08, 600),
                     'Pioneer Viking': Wearable("Pioneer Viking", 6, 5, 5, 5, 1, 22, 18, 0.44, 0.1, 300)
                     }

dualist_armorS = {'Default': Wearable(),
                  'Mercenary': Wearable("Lava", 2, 2, 3, 2, 3, 10, 10, 0.01, 0.01, 150),
                  'Sparta': Wearable("Sparta", 1, 0, 0, 2, 2, 20, 20, 0.24, 0.03, 150),
                  'Lava': Wearable("Lava", 2, 1, 2, 2, 3, 10, 10, 0.12, 0.01, 150),
                  'Legendary': Wearable("Legendary", 1, 3, 4, 1, 2, 12, 11, 0.67, 0.07, 2000),
                  'Warrior': Wearable("Warrior", 6, 5, 8, 8, 2, 12, 12, 0.48, 0.06, 200),
                  'Viking': Wearable("Viking", 4, 3, 6, 6, 2, 22, 22, 0.29, 0.06, 200),
                  'Zodiac': Wearable("Zodiac", 5, 5, 5, 5, 5, 23, 23, 0.48, 0.08, 600),
                  'Pioneer Viking': Wearable("Pioneer Viking", 6, 5, 5, 5, 1, 22, 18, 0.44, 0.1, 300)}

dualist_armS = {'Default': Wearable(),
                'Sparta': Wearable("Sparta", 2, 0, 0, 1, 1, 10, 10, 0.18, 0.01, 150),
                'Mercenary': Wearable("Lava", 2, 2, 3, 2, 3, 10, 10, 0.01, 0.01, 150),
                'Lava': Wearable("Lava", 2, 2, 1, 1, 1, 10, 10, 0.09, 0.05, 150),
                'Legendary': Wearable("Legendary", 1, 3, 1, 1, 2, 2, 3, 0.53, 0.05, 1200),
                'Warrior': Wearable("Warrior", 6, 5, 8, 8, 2, 8, 8, 0.42, 0.11, 200),
                'Viking': Wearable("Viking", 4, 3, 6, 6, 2, 22, 22, 0.29, 0.06, 200),
                'Zodiac': Wearable("Zodiac", 5, 5, 5, 5, 5, 15, 15, 0.48, 0.08, 600),
                'Pioneer Viking': Wearable("Pioneer Viking", 6, 5, 5, 5, 1, 22, 18, 0.44, 0.1, 300)}

dualist_meleeS = {'Default': Wearable(),
                  'Mercenary': Wearable("Lava", 2, 2, 3, 2, 3, 10, 10, 0.01, 0.01, 150),
                  'Sparta': Wearable("Sparta", 6, 0, 0, 3, 0, 15, 15, 0.42, 0.04, 150),
                  'Lava': Wearable("Lava", 4, 4, 4, 4, 4, 7, 7, 0.22, 0.01, 150),
                  'Legendary': Wearable("Legendary", 4, 5, 5, 6, 2, 0, 0, 0.86, 0.07, 600),
                  'Warrior': Wearable("Warrior", 5, 11, 9, 8, 3, 4, 4, 1.22, 0.13, 300),
                  'Viking': Wearable("Viking", 4, 9, 8, 9, 3, 12, 12, 1.08, 0.09, 300),
                  'Zodiac': Wearable("Zodiac", 3, 11, 7, 3, 8, 2, 2, 0.89, 0.1, 700),
                  'Pioneer Viking': Wearable("Pioneer Viking", 6, 14, 6, 7, 2, 12, 10, 1.62, 0.14, 500),
                  }

dualist_rangeS = {'Default': Wearable(),
                  'Mercenary': Wearable("Lava", 2, 2, 3, 2, 3, 10, 10, 0.01, 0.01, 150),
                  'Sparta': Wearable("Sparta", 4, 0, 0, 2, 1, 10, 10, 0.24, 0.03, 150),
                  'Lava': Wearable("Lava", 2, 2, 2, 2, 2, 5, 5, 0.09, 0.01, 150),
                  'Legendary': Wearable("Legendary", 4, 5, 3, 3, 2, 1, 1, 0.71, 0.06, 600),
                  'Warrior': Wearable("Warrior", 2, 11, 8, 5, 3, 3, 3, 1.02, 0.12, 150),
                  'Viking': Wearable("Viking", 3, 9, 1, 9, 2, 10, 10, 0.09, 0.09, 150),
                  'Zodiac': Wearable("Zodiac", 2, 9, 5, 3, 7, 1, 1, 0.73, 0.09, 400),
                  'Pioneer Viking': Wearable("Pioneer Viking", 4, 14, 6, 6, 1, 10, 8, 1.35, 0.13, 200)
                  }


class Dualist:

    def __init__(self):
        self.basic = BASIC_DUALIST
        self.range = RANGE_DUALIST
        self.special = SPECIAL_DUALIST
        self.grip = GRIP_DUALIST
        self.cd = CELLDESTRUCTION_DUALIST
        self.hp = ENERGY_DUALIST
        self.ap = ARMOR_DUALIST
        self.attackSpeed = ATTACKSPEED_DUALIST
        self.movementSpeed = MOVEMENTSPEED_DUALIST
        self.cp = CELLPOINTS_DUALIST

        self.basicPerPoint = BASIC_PER_STATPOINT_DUALIST
        self.rangePerPoint = RANGE_PER_STATPOINT_DUALIST
        self.specialPerPoint = SPECIAL_PER_STATPOINT_DUALIST
        self.gripPerPoint = GRIP_PER_STATPOINT_DUALIST
        self.cdPerPoint = CELLDEST_PER_STATPOINT_DUALIST
        self.hpPerPoint = ENERGY_PER_STATPOINT_DUALIST
        self.apPerPoint = ARMOR_PER_STATPOINT_DUALIST
        self.attSpeedPerPoint = ATTACKSPED_PER_STATPOINT_DUALIST
        self.movSpeedPerPoint = MOVSPEED_PER_STATPOINT_DUALIST
        self.cpPerPoint = CELLPOINTS_PER_STATPOINT_DUALIST

        self.PAST50 = PAST50
        self.PAST80 = PAST80

        self.helmetS = dualist_helmetS
        self.shoulderS = dualist_shoulderS
        self.armorS = dualist_armorS
        self.armS = dualist_armS
        self.meleeS = dualist_meleeS
        self.rangeS = dualist_rangeS

    def advancedClass(self):
        self.basic = BASIC_DUALIST + 0
        self.range = RANGE_DUALIST + 0
        self.special = SPECIAL_DUALIST + 0
        self.grip = GRIP_DUALIST + 0
        self.cd = CELLDESTRUCTION_DUALIST + 0
        self.hp = ENERGY_DUALIST + 0
        self.ap = ARMOR_DUALIST + 0
        self.attackSpeed = ATTACKSPEED_DUALIST + 0
        self.movementSpeed = MOVEMENTSPEED_DUALIST + 0
        self.cp = CELLPOINTS_DUALIST + 0

    def normalClass(self):
        self.basic = BASIC_DUALIST
        self.range = RANGE_DUALIST
        self.special = SPECIAL_DUALIST
        self.grip = GRIP_DUALIST
        self.cd = CELLDESTRUCTION_DUALIST
        self.hp = ENERGY_DUALIST
        self.ap = ARMOR_DUALIST
        self.attackSpeed = ATTACKSPEED_DUALIST
        self.movementSpeed = MOVEMENTSPEED_DUALIST
        self.cp = CELLPOINTS_DUALIST
