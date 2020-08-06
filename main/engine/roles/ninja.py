from engine.roles.ninja_stats import *
from engine.wearable import Wearable

ninja_helmetS = {'Default': Wearable(),
                 'Sparta': Wearable("Sparta", 2, 0, 0, 2, 2, 20, 20, 0.24, 0.03, 150),
                 'Noblesse': Wearable("Noblesse", 1, 1, 1, 1, 4, 8, 8, 0.45, 0.01, 1000),
                 'GReaper': Wearable("GReaper", 5, 4, 5, 4, 5, 14, 14, 0.34, 0.07, 600),
                 'Lava': Wearable("Lava", 2, 2, 3, 2, 3, 10, 10, 0.01, 0.01, 150),
                 'Legendary': Wearable("Legendary", 2, 3, 3, 3, 2, 8, 10, 0.52, 0.08, 1500),
                 'Cane': Wearable("Cane", 0, 1, 0, 0, 5, 9, 9, 0.9, 0.1, 1300),
                 'Purewhite': Wearable("Purewhite", 2, 3, 2, 4, 3, 8, 10, 0.51, 0.09, 2000),
                 'Warrior': Wearable("Warrior", 6, 5, 8, 8, 2, 10, 10, 0.34, 0.07, 200),
                 'Viking': Wearable("Viking", 4, 3, 6, 6, 2, 22, 22, 0.29, 0.06, 200),
                 'Zodiac': Wearable("Zodiac", 5, 5, 5, 5, 5, 20, 20, 0.48, 0.08, 600),
                 'Summer': Wearable("Summer", 2, 2, 2, 1, 1, 7, 7, 0.65, 0.06, 1000),
                 'Northsoul': Wearable("Northsoul", 0, 0, 1, 0, 4, 8, 8, 0.45, 0.01, 1000),
                 'Pioneer Viking': Wearable("Pioneer Viking", 6, 5, 5, 5, 1, 22, 18, 0.44, 0.1, 300)
                 }

ninja_shoulderS = {'Default': Wearable(),
                   'Sparta': Wearable("Sparta", 1, 0, 0, 2, 1, 15, 15, 0.23, 0.02, 80),
                   'Noblesse': Wearable("Noblesse", 1, 1, 1, 1, 0, 8, 16, 0.54, 0.01, 400),
                   'GReaper': Wearable("GReaper", 3, 4, 3, 5, 4, 17, 17, 0.44, 0.08, 480),
                   'Lava': Wearable("Lava", 1, 2, 1, 3, 2, 15, 15, 0.11, 0.01, 80),
                   'Legendary': Wearable("Legendary", 1, 3, 2, 2, 2, 3, 2, 0.56, 0.06, 1100),
                   'Cane': Wearable("Cane", 0, 1, 0, 0, 0, 9, 18, 0.2, 0, 490),
                   'Purewhite': Wearable("Purewhite", 2, 3, 2, 2, 2, 3, 2, 0.55, 0.06, 1100),
                   'Warrior': Wearable("Warrior", 6, 5, 8, 8, 2, 8, 8, 0.44, 0.08, 200),
                   'Viking': Wearable("Viking", 4, 3, 6, 6, 2, 22, 22, 0.29, 0.06, 200),
                   'Zodiac': Wearable("Zodiac", 5, 5, 5, 5, 5, 15, 15, 0.48, 0.08, 600),
                   'Summer': Wearable("Summer", 1, 2, 2, 1, 2, 5, 6, 0.46, 0.04, 800),
                   'Northsoul': Wearable("Northsoul", 0, 0, 1, 0, 0, 8, 16, 0.54, 0.01, 400),
                   'Pioneer Viking': Wearable("Pioneer Viking", 6, 5, 5, 5, 1, 22, 18, 0.44, 0.1, 300)
                   }

ninja_armorS = {'Default': Wearable(),
                'Sparta': Wearable("Sparta", 1, 0, 0, 2, 2, 20, 20, 0.24, 0.03, 150),
                'Noblesse': Wearable("Noblesse", 1, 1, 1, 1, 2, 15, 15, 0.9, 0, 800),
                'GReaper': Wearable("GReaper", 5, 3, 4, 5, 5, 15, 15, 0.48, 0.06, 550),
                'Lava': Wearable("Lava", 2, 1, 2, 2, 3, 10, 10, 0.12, 0.01, 150),
                'Legendary': Wearable("Legendary", 1, 3, 4, 1, 2, 12, 11, 0.67, 0.07, 2000),
                'Cane': Wearable("Cane", 0, 1, 0, 0, 3, 18, 17, 0.8, 0, 800),
                'Purewhite': Wearable("Purewhite", 3, 2, 2, 2, 4, 12, 11, 0.65, 0.07, 1500),
                'Warrior': Wearable("Warrior", 6, 5, 8, 8, 2, 12, 12, 0.48, 0.06, 200),
                'Viking': Wearable("Viking", 4, 3, 6, 6, 2, 22, 22, 0.29, 0.06, 200),
                'Zodiac': Wearable("Zodiac", 5, 5, 5, 5, 5, 23, 23, 0.48, 0.08, 600),
                'Summer': Wearable("Summer", 2, 1, 1, 2, 2, 6, 6, 0.57, 0.04, 900),
                'Northsoul': Wearable("Northsoul", 0, 0, 1, 0, 2, 15, 15, 0.90, 0, 800),
                'Pioneer Viking': Wearable("Pioneer Viking", 6, 5, 5, 5, 1, 22, 18, 0.44, 0.1, 300)}

ninja_armS = {'Default': Wearable(),
              'Sparta': Wearable("Sparta", 2, 0, 0, 1, 1, 10, 10, 0.18, 0.01, 150),
              'Noblesse': Wearable("Noblesse", 1, 1, 1, 1, 6, 0, 12, 0.46, 0.01, 300),
              'GReaper': Wearable("GReaper", 4, 4, 3, 3, 3, 12, 12, 0.42, 0.11, 550),
              'Lava': Wearable("Lava", 2, 2, 1, 1, 1, 10, 10, 0.09, 0.05, 150),
              'Legendary': Wearable("Legendary", 1, 3, 1, 1, 2, 2, 3, 0.53, 0.05, 1200),
              'Cane': Wearable("Cane", 0, 0, 0, 0, 6, 0, 11, 0.4, 0, 350),
              'Purewhite': Wearable("Purewhite", 2, 2, 2, 2, 2, 2, 3, 0.46, 0.06, 1200),
              'Warrior': Wearable("Warrior", 6, 5, 8, 8, 2, 8, 8, 0.42, 0.11, 200),
              'Viking': Wearable("Viking", 4, 3, 6, 6, 2, 22, 22, 0.29, 0.06, 200),
              'Zodiac': Wearable("Zodiac", 5, 5, 5, 5, 5, 15, 15, 0.48, 0.08, 600),
              'Summer': Wearable("Summer", 1, 1, 1, 2, 2, 5, 5, 0.37, 0.03, 700),
              'Northsoul': Wearable("Northsoul", 0, 0, 0, 0, 6, 0, 12, 0.46, 0.01, 300),
              'Pioneer Viking': Wearable("Pioneer Viking", 6, 5, 5, 5, 1, 22, 18, 0.44, 0.1, 300)}

ninja_meleeS = {'Default': Wearable(),
                'Sparta': Wearable("Sparta", 6, 0, 0, 3, 0, 15, 15, 0.42, 0.04, 150),
                'Noblesse': Wearable("Noblesse", 5, 4, 5, 4, 6, 5, 5, 0.98, 0.01, 100),
                'GReaper': Wearable("GReaper", 9, 7, 7, 11, 7, 12, 12, 1.22, 0.13, 600),
                'Lava': Wearable("Lava", 4, 4, 4, 4, 4, 7, 7, 0.22, 0.01, 150),
                'Legendary': Wearable("Legendary", 4, 5, 5, 6, 2, 0, 0, 0.86, 0.07, 600),
                'Cane': Wearable("Cane", 5, 5, 3, 5, 5, 0, 0, 0.25, 0, 100),
                'Purewhite': Wearable("Purewhite", 8, 3, 3, 4, 5, 7, 7, 0.86, 0.08, 1500),
                'Warrior': Wearable("Warrior", 5, 11, 9, 8, 3, 4, 4, 1.22, 0.13, 300),
                'Viking': Wearable("Viking", 4, 9, 8, 9, 3, 12, 12, 1.08, 0.09, 300),
                'Zodiac': Wearable("Zodiac", 3, 11, 7, 3, 8, 2, 2, 0.89, 0.1, 700),
                'Summer': Wearable("Summer", 4, 3, 4, 4, 3, 11, 11, 0.89, 0.07, 1200),
                'Northsoul': Wearable("Northsoul", 4, 3, 4, 3, 5, 1, 1, 1.26, 0, 100),
                'Pioneer Viking': Wearable("Pioneer Viking", 6, 14, 6, 7, 2, 12, 10, 1.62, 0.14, 500),
                'GReaper Hoz': Wearable("GReaper Hoz", 10, 7, 8, 11, 7, 12, 12, 1.22, 0.13, 600),
                'Lava Hoz': Wearable("Lava Hoz", 4, 4, 4, 4, 4, 7, 7, 0.22, 0.01, 150),
                'Sparta Hoz': Wearable("Sparta Hoz", 6, 0, 0, 3, 0, 15, 15, 0.42, 0.04, 150),
                'Noblesse Hoz': Wearable("Noblesse Hoz", 5, 4, 5, 5, 6, 5, 5, 1.08, 0.02, 100),
                'Legendary Hoz': Wearable("Legendary Hoz", 4, 5, 5, 6, 2, 0, 0, 0.86, 0.07, 600),
                'Cane Hoz': Wearable("Cane Hoz", 5, 5, 5, 5, 5, 0, 0, 0.2, 0, 50),
                'Nightwatch Hoz': Wearable("Nightwatch Hoz", 4, 2, 4, 4, 2, 8, 8, 0.6, 0.04, 700),
                'Purewhite Hoz': Wearable("Purewhite Hoz", 8, 3, 3, 4, 5, 7, 7, 0.86, 0.08, 1500),
                'Zodiac Hoz': Wearable("Zodiac Hoz", 3, 11, 7, 3, 8, 5, 5, 0.89, 0.1, 700),
                'Viking Hoz': Wearable("Viking Hoz", 6, 9, 8, 9, 3, 13, 13, 1.08, 0.09, 300),
                'Warrior Hoz': Wearable("Warrior Hoz", 5, 12, 10, 8, 3, 4, 4, 1.22, 0.13, 300),
                'Pioneer Viking Hoz': Wearable("Pioneer Viking Hoz", 6, 14, 7, 7, 2, 13, 10, 1.62, 0.14, 400)
                }

ninja_rangeS = {'Default': Wearable(),
                'Sparta': Wearable("Sparta", 4, 0, 0, 2, 1, 10, 10, 0.24, 0.03, 150),
                'Noblesse': Wearable("Noblesse", 3, 2, 3, 4, 4, 3, 4, 0.9, 0, 500),
                'GReaper': Wearable("GReaper", 7, 5, 5, 7, 7, 10, 10, 1.02, 0.12, 600),
                'Lava': Wearable("Lava", 2, 2, 2, 2, 2, 5, 5, 0.09, 0.01, 150),
                'Legendary': Wearable("Legendary", 4, 5, 3, 3, 2, 1, 1, 0.71, 0.06, 600),
                'Cane': Wearable("Cane", 3, 2, 4, 2, 2, 1, 1, 0.5, 0.12, 800),
                'Purewhite': Wearable("Purewhite", 3, 7, 3, 4, 5, 6, 6, 0.71, 0.06, 1400),
                'Warrior': Wearable("Warrior", 2, 11, 8, 5, 3, 3, 3, 1.02, 0.12, 150),
                'Viking': Wearable("Viking", 3, 9, 1, 9, 2, 10, 10, 0.09, 0.09, 150),
                'Zodiac': Wearable("Zodiac", 2, 9, 5, 3, 7, 1, 1, 0.73, 0.09, 400),
                'Summer': Wearable("Summer", 2, 4, 2, 2, 4, 8, 8, 0.78, 0.06, 1100),
                'Northsoul': Wearable("Northsoul", 2, 1, 2, 3, 3, 1, 2, 0.9, 0, 500),
                'Pioneer Viking': Wearable("Pioneer Viking", 4, 14, 6, 6, 1, 10, 8, 1.35, 0.13, 200)
                }


class Ninja:

    def __init__(self):
        self.basic = BASIC_NINJA
        self.range = RANGE_NINJA
        self.special = SPECIAL_NINJA
        self.grip = GRIP_NINJA
        self.cd = CELLDESTRUCTION_NINJA
        self.hp = ENERGY_NINJA
        self.ap = ARMOR_NINJA
        self.attackSpeed = ATTACKSPEED_NINJA
        self.movementSpeed = MOVEMENTSPEED_NINJA
        self.cp = CELLPOINTS_NINJA

        self.basicPerPoint = BASIC_PER_STATPOINT_NINJA
        self.rangePerPoint = RANGE_PER_STATPOINT_NINJA
        self.specialPerPoint = SPECIAL_PER_STATPOINT_NINJA
        self.gripPerPoint = GRIP_PER_STATPOINT_NINJA
        self.cdPerPoint = CELLDEST_PER_STATPOINT_NINJA
        self.hpPerPoint = ENERGY_PER_STATPOINT_NINJA
        self.apPerPoint = ARMOR_PER_STATPOINT_NINJA
        self.attSpeedPerPoint = ATTACKSPED_PER_STATPOINT_NINJA
        self.movSpeedPerPoint = MOVSPEED_PER_STATPOINT_NINJA
        self.cpPerPoint = CELLPOINTS_PER_STATPOINT_NINJA

        self.PAST50 = PAST50
        self.PAST80 = PAST80

        self.helmetS = ninja_helmetS
        self.shoulderS = ninja_shoulderS
        self.armorS = ninja_armorS
        self.armS = ninja_armS
        self.meleeS = ninja_meleeS
        self.rangeS = ninja_rangeS

    def advancedClass(self):
        self.basic = BASIC_NINJA + 4
        self.range = RANGE_NINJA + 5
        self.special = SPECIAL_NINJA + 5
        self.grip = GRIP_NINJA + 5
        self.cd = CELLDESTRUCTION_NINJA
        self.hp = ENERGY_NINJA + 7
        self.ap = ARMOR_NINJA + 6
        self.attackSpeed = ATTACKSPEED_NINJA + 4.9
        self.movementSpeed = MOVEMENTSPEED_NINJA + 0.38
        self.cp = CELLPOINTS_NINJA + 80

    def normalClass(self):
        self.basic = BASIC_NINJA
        self.range = RANGE_NINJA
        self.special = SPECIAL_NINJA
        self.grip = GRIP_NINJA
        self.cd = CELLDESTRUCTION_NINJA
        self.hp = ENERGY_NINJA
        self.ap = ARMOR_NINJA
        self.attackSpeed = ATTACKSPEED_NINJA
        self.movementSpeed = MOVEMENTSPEED_NINJA
        self.cp = CELLPOINTS_NINJA
