from engine.roles.blacksmith_stats import *
from engine.wearable import Wearable

blacksmith_helmetS = {'Default': Wearable(),
                      'Sparta': Wearable("Sparta", 2, 0, 0, 2, 2, 20, 20, 0.24, 0.03, 150),
                      'Noblesse': Wearable("Noblesse", 1, 1, 1, 1, 4, 8, 8, 0.45, 0.01, 1000),
                      'GReaper': Wearable("GReaper", 5, 4, 5, 4, 5, 14, 14, 0.34, 0.07, 600),
                      'Lava': Wearable("Lava", 2, 2, 3, 2, 3, 10, 10, 0.01, 0.01, 150),
                      'Legendary': Wearable("Legendary", 3, 2, 2, 3, 2, 8, 10, 0.51, 0.07, 1500),
                      'Cane': Wearable("Cane", 1, 0, 0, 0, 5, 10, 10, 0.8, 0.07, 1000),
                      'Purewhite': Wearable("Purewhite", 2, 3, 2, 4, 3, 8, 10, 0.51, 0.09, 2000),
                      'Warrior': Wearable("Warrior", 6, 5, 8, 8, 2, 10, 10, 0.34, 0.07, 200),
                      'Viking': Wearable("Viking", 4, 3, 6, 6, 2, 22, 22, 0.29, 0.06, 200),
                      'Zodiac': Wearable("Zodiac", 5, 5, 5, 5, 5, 20, 20, 0.48, 0.08, 600),
                      'Summer': Wearable("Summer", 2, 2, 2, 1, 1, 7, 7, 0.65, 0.06, 1000),
                      'Northsoul': Wearable("Northsoul", 0, 0, 1, 0, 4, 8, 8, 0.45, 0.01, 1000),
                      'Pioneer Viking': Wearable("Pioneer Viking", 6, 5, 5, 5, 1, 22, 18, 0.44, 0.1, 300)
                      }

blacksmith_shoulderS = {'Default': Wearable(),
                        'Sparta': Wearable("Sparta", 1, 0, 0, 2, 1, 15, 15, 0.23, 0.02, 80),
                        'Noblesse': Wearable("Noblesse", 1, 1, 1, 1, 0, 8, 16, 0.54, 0.01, 400),
                        'GReaper': Wearable("GReaper", 3, 4, 3, 5, 4, 17, 17, 0.44, 0.08, 480),
                        'Lava': Wearable("Lava", 1, 2, 1, 3, 2, 15, 15, 0.11, 0.01, 80),
                        'Legendary': Wearable("Legendary", 4, 2, 1, 2, 2, 3, 2, 0.55, 0.06, 1100),
                        'Cane': Wearable("Cane", 1, 0, 0, 0, 0, 10, 20, 0.2, 0, 200),
                        'Purewhite': Wearable("Purewhite", 2, 3, 2, 2, 2, 3, 2, 0.55, 0.06, 1100),
                        'Warrior': Wearable("Warrior", 6, 5, 8, 8, 2, 8, 8, 0.44, 0.08, 200),
                        'Viking': Wearable("Viking", 4, 3, 6, 6, 2, 22, 22, 0.29, 0.06, 200),
                        'Zodiac': Wearable("Zodiac", 5, 5, 5, 5, 5, 15, 15, 0.48, 0.08, 600),
                        'Summer': Wearable("Summer", 1, 2, 2, 1, 2, 5, 6, 0.46, 0.04, 800),
                        'Northsoul': Wearable("Northsoul", 0, 0, 1, 0, 0, 8, 16, 0.54, 0.01, 400),
                        'Pioneer Viking': Wearable("Pioneer Viking", 6, 5, 5, 5, 1, 22, 18, 0.44, 0.1, 300)
                        }

blacksmith_armorS = {'Default': Wearable(),
                     'Sparta': Wearable("Sparta", 1, 0, 0, 2, 2, 20, 20, 0.24, 0.03, 150),
                     'Noblesse': Wearable("Noblesse", 1, 1, 1, 1, 2, 15, 15, 0.9, 0, 800),
                     'GReaper': Wearable("GReaper", 5, 3, 4, 5, 5, 15, 15, 0.48, 0.06, 550),
                     'Lava': Wearable("Lava", 2, 1, 2, 2, 3, 10, 10, 0.12, 0.01, 150),
                     'Legendary': Wearable("Legendary", 4, 2, 1, 1, 2, 12, 11, 0.66, 0.07, 2000),
                     'Cane': Wearable("Cane", 1, 0, 0, 0, 2, 18, 18, 0.9, 0, 600),
                     'Purewhite': Wearable("Purewhite", 3, 2, 2, 2, 4, 12, 11, 0.66, 0.07, 1500),
                     'Warrior': Wearable("Warrior", 6, 5, 8, 8, 2, 12, 12, 0.48, 0.06, 200),
                     'Viking': Wearable("Viking", 4, 3, 6, 6, 2, 22, 22, 0.29, 0.06, 200),
                     'Zodiac': Wearable("Zodiac", 5, 5, 5, 5, 5, 23, 23, 0.48, 0.08, 600),
                     'Summer': Wearable("Summer", 2, 1, 1, 2, 2, 6, 6, 0.57, 0.04, 900),
                     'Northsoul': Wearable("Northsoul", 0, 0, 1, 0, 2, 15, 15, 0.90, 0, 800),
                     'Pioneer Viking': Wearable("Pioneer Viking", 6, 5, 5, 5, 1, 22, 18, 0.44, 0.1, 300)}

blacksmith_armS = {'Default': Wearable(),
                   'Sparta': Wearable("Sparta", 2, 0, 0, 1, 1, 10, 10, 0.18, 0.01, 150),
                   'Noblesse': Wearable("Noblesse", 1, 1, 1, 1, 6, 0, 12, 0.46, 0.01, 300),
                   'GReaper': Wearable("GReaper", 4, 4, 3, 3, 3, 12, 12, 0.42, 0.11, 550),
                   'Lava': Wearable("Lava", 2, 2, 1, 1, 1, 10, 10, 0.09, 0.05, 150),
                   'Legendary': Wearable("Legendary", 4, 1, 1, 1, 2, 2, 3, 0.46, 0.05, 1200),
                   'Cane': Wearable("Cane", 0, 0, 0, 0, 8, 0, 13, 0.5, 0, 300),
                   'Purewhite': Wearable("Purewhite", 2, 2, 2, 2, 2, 2, 3, 0.46, 0.06, 1200),
                   'Warrior': Wearable("Warrior", 6, 5, 8, 8, 2, 8, 8, 0.42, 0.11, 200),
                   'Viking': Wearable("Viking", 4, 3, 6, 6, 2, 22, 22, 0.29, 0.06, 200),
                   'Zodiac': Wearable("Zodiac", 5, 5, 5, 5, 5, 15, 15, 0.48, 0.08, 600),
                   'Summer': Wearable("Summer", 1, 1, 1, 2, 2, 5, 5, 0.37, 0.03, 700),
                   'Northsoul': Wearable("Northsoul", 0, 0, 0, 0, 6, 0, 12, 0.46, 0.01, 300),
                   'Pioneer Viking': Wearable("Pioneer Viking", 6, 5, 5, 5, 1, 22, 18, 0.44, 0.1, 300)}

blacksmith_meleeS = {'Default': Wearable(),
                     'Sparta': Wearable("Sparta", 6, 0, 0, 3, 0, 15, 15, 0.42, 0.04, 150),
                     'Noblesse': Wearable("Noblesse", 5, 4, 5, 4, 6, 5, 5, 0.98, 0.01, 100),
                     'GReaper': Wearable("GReaper", 9, 7, 7, 11, 7, 12, 12, 1.22, 0.13, 600),
                     'Lava': Wearable("Lava", 4, 4, 4, 4, 4, 7, 7, 0.22, 0.01, 150),
                     'Legendary': Wearable("Legendary", 5, 5, 5, 6, 2, 0, 0, 0.86, 0.07, 600),
                     'Cane': Wearable("Cane", 5, 5, 5, 5, 5, 0, 0, 0.4, 0, 0),
                     'Purewhite': Wearable("Purewhite", 8, 3, 3, 4, 5, 7, 7, 0.86, 0.08, 1500),
                     'Warrior': Wearable("Warrior", 11, 3, 10, 11, 1, 6, 6, 1.22, 0.13, 200),
                     'Viking': Wearable("Viking", 9, 1, 10, 13, 2, 13, 13, 0.37, 0.04, 200),
                     'Zodiac': Wearable("Zodiac", 11, 3, 7, 3, 8, 4, 4, 0.67, 0.08, 500),
                     'Summer': Wearable("Summer", 4, 3, 4, 4, 3, 11, 11, 0.89, 0.07, 1200),
                     'Northsoul': Wearable("Northsoul", 4, 3, 4, 3, 5, 1, 1, 1.26, 0, 100),
                     'Pioneer Viking': Wearable("Pioneer Viking", 13, 2, 8, 10, 1, 13, 10, 0.56, 0.06, 300),
                     'GReaper Fist': Wearable("GReaper Fist", 10, 7, 8, 11, 7, 12, 12, 1.22, 0.13, 600),
                     'Lava Fist': Wearable("Lava Fist", 4, 4, 4, 4, 4, 7, 7, 0.22, 0.01, 150),
                     'Sparta Fist': Wearable("Sparta Fist", 6, 0, 0, 3, 0, 15, 15, 0.42, 0.04, 150),
                     'Noblesse Fist': Wearable("Noblesse Fist", 5, 4, 5, 5, 6, 5, 5, 1.08, 0.02, 100),
                     'Legendary Fist': Wearable("Legendary Fist", 5, 5, 5, 6, 2, 0, 0, 0.86, 0.07, 600),
                     'Cane Fist': Wearable("Cane Fist", 5, 5, 5, 5, 5, 0, 0, 0.2, 0, 50),
                     'Nightwatch Fist': Wearable("Nightwatch Fist", 4, 2, 4, 4, 2, 8, 8, 0.6, 0.04, 700),
                     'Purewhite Fist': Wearable("Purewhite Fist", 8, 3, 3, 4, 5, 7, 7, 0.86, 0.08, 1500),
                     'Zodiac Fist': Wearable("Zodiac Fist", 11, 3, 7, 3, 8, 5, 5, 0.67, 0.08, 500),
                     'Viking Fist': Wearable("Viking Fist", 9, 1, 10, 13, 2, 15, 15, 0.37, 0.04, 200),
                     'Warrior Fist': Wearable("Warrior Fist", 12, 3, 10, 12, 1, 6, 6, 1.22, 0.13, 200),
                     'Pioneer Viking Fist': Wearable("Pioneer Viking Fist", 13, 2, 8, 10, 1, 15, 12, 0.56, 0.06, 300)
                     }

blacksmith_rangeS = {'Default': Wearable(),
                     'Sparta': Wearable("Sparta", 4, 0, 0, 2, 1, 10, 10, 0.24, 0.03, 150),
                     'Noblesse': Wearable("Noblesse", 3, 2, 3, 4, 4, 3, 4, 0.9, 0, 500),
                     'GReaper': Wearable("GReaper", 7, 5, 5, 7, 7, 10, 10, 1.02, 0.12, 600),
                     'Lava': Wearable("Lava", 2, 2, 2, 2, 2, 5, 5, 0.09, 0.01, 150),
                     'Legendary': Wearable("Legendary", 5, 4, 4, 3, 2, 1, 1, 0.71, 0.06, 600),
                     'Cane': Wearable("Cane", 4, 2, 3, 3, 4, 2, 2, 0.7, 0.12, 300),
                     'Purewhite': Wearable("Purewhite", 3, 7, 3, 4, 5, 6, 6, 0.71, 0.06, 1400),
                     'Warrior': Wearable("Warrior", 8, 2, 7, 10, 1, 5, 5, 1.02, 0.12, 150),
                     'Viking': Wearable("Viking", 8, 0, 8, 8, 1, 10, 10, 0.24, 0.02, 150),
                     'Zodiac': Wearable("Zodiac", 9, 3, 5, 3, 7, 2, 2, 0.51, 0.08, 400),
                     'Summer': Wearable("Summer", 2, 4, 2, 2, 4, 8, 8, 0.78, 0.06, 1100),
                     'Northsoul': Wearable("Northsoul", 2, 1, 2, 3, 3, 1, 2, 0.9, 0, 500),
                     'Pioneer Viking': Wearable("Pioneer Viking", 12, 0, 6, 6, 1, 10, 8, 0.36, 0.04, 200)
                     }


class Blacksmith:

    def __init__(self):
        self.basic = BASIC_BLACKSMITH
        self.range = RANGE_BLACKSMITH
        self.special = SPECIAL_BLACKSMITH
        self.grip = GRIP_BLACKSMITH
        self.cd = CELLDESTRUCTION_BLACKSMITH
        self.hp = ENERGY_BLACKSMITH
        self.ap = ARMOR_BLACKSMITH
        self.attackSpeed = ATTACKSPEED_BLACKSMITH
        self.movementSpeed = MOVEMENTSPEED_BLACKSMITH
        self.cp = CELLPOINTS_BLACKSMITH

        self.basicPerPoint = BASIC_PER_STATPOINT_BLACKSMITH
        self.rangePerPoint = RANGE_PER_STATPOINT_BLACKSMITH
        self.specialPerPoint = SPECIAL_PER_STATPOINT_BLACKSMITH
        self.gripPerPoint = GRIP_PER_STATPOINT_BLACKSMITH
        self.cdPerPoint = CELLDEST_PER_STATPOINT_BLACKSMITH
        self.hpPerPoint = ENERGY_PER_STATPOINT_BLACKSMITH
        self.apPerPoint = ARMOR_PER_STATPOINT_BLACKSMITH
        self.attSpeedPerPoint = ATTACKSPED_PER_STATPOINT_BLACKSMITH
        self.movSpeedPerPoint = MOVSPEED_PER_STATPOINT_BLACKSMITH
        self.cpPerPoint = CELLPOINTS_PER_STATPOINT_BLACKSMITH

        self.PAST50 = PAST50
        self.PAST80 = PAST80

        self.helmetS = blacksmith_helmetS
        self.shoulderS = blacksmith_shoulderS
        self.armorS = blacksmith_armorS
        self.armS = blacksmith_armS
        self.meleeS = blacksmith_meleeS
        self.rangeS = blacksmith_rangeS

    def advancedClass(self):
        self.basic = BASIC_BLACKSMITH + 4
        self.range = RANGE_BLACKSMITH + 6
        self.special = SPECIAL_BLACKSMITH + 6
        self.grip = GRIP_BLACKSMITH + 6
        self.cd = CELLDESTRUCTION_BLACKSMITH + 0.9
        self.hp = ENERGY_BLACKSMITH + 9
        self.ap = ARMOR_BLACKSMITH + 9
        self.attackSpeed = ATTACKSPEED_BLACKSMITH + 4.9
        self.movementSpeed = MOVEMENTSPEED_BLACKSMITH + 0.36
        self.cp = CELLPOINTS_BLACKSMITH + 150

    def normalClass(self):
        self.basic = BASIC_BLACKSMITH
        self.range = RANGE_BLACKSMITH
        self.special = SPECIAL_BLACKSMITH
        self.grip = GRIP_BLACKSMITH
        self.cd = CELLDESTRUCTION_BLACKSMITH
        self.hp = ENERGY_BLACKSMITH
        self.ap = ARMOR_BLACKSMITH
        self.attackSpeed = ATTACKSPEED_BLACKSMITH
        self.movementSpeed = MOVEMENTSPEED_BLACKSMITH
        self.cp = CELLPOINTS_BLACKSMITH
