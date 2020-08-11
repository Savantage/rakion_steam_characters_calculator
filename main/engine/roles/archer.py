from engine.roles.archer_stats import *
from engine.wearable import Wearable

archer_helmetS = {'Default': Wearable(),
                  'Sparta': Wearable("Sparta", 2, 0, 0, 2, 2, 20, 20, 0.24, 0.03, 150),
                  'Noblesse': Wearable("Noblesse", 1, 1, 1, 1, 4, 8, 8, 0.45, 0.01, 1000),
                  'GReaper': Wearable("GReaper", 5, 4, 5, 4, 5, 14, 14, 0.34, 0.07, 600),
                  'Lava': Wearable("Lava", 2, 2, 3, 2, 3, 10, 10, 0.01, 0.01, 150),
                  'Legendary': Wearable("Legendary", 2, 3, 2, 3, 2, 8, 10, 0.52, 0.08, 1500),
                  'Cane': Wearable("Cane", 0, 1, 0, 0, 5, 9, 8, 1.05, 0.09, 1250),
                  'Purewhite': Wearable("Purewhite", 2, 3, 2, 4, 3, 8, 10, 0.51, 0.09, 2000),
                  'Warrior': Wearable("Warrior", 6, 5, 8, 8, 2, 10, 10, 0.34, 0.07, 200),
                  'Viking': Wearable("Viking", 4, 3, 6, 6, 2, 22, 22, 0.29, 0.06, 200),
                  'Zodiac': Wearable("Zodiac", 5, 5, 5, 5, 5, 20, 20, 0.48, 0.08, 600),
                  'Summer': Wearable("Summer", 2, 2, 2, 1, 1, 7, 7, 0.65, 0.06, 1000),
                  'Northsoul': Wearable("Northsoul", 0, 0, 1, 0, 4, 8, 8, 0.45, 0.01, 1000),
                  'Pioneer Viking': Wearable("Pioneer Viking", 6, 5, 5, 5, 1, 22, 18, 0.44, 0.1, 300)
                  }

archer_shoulderS = {'Default': Wearable(),
                    'Sparta': Wearable("Sparta", 1, 0, 0, 2, 1, 15, 15, 0.23, 0.02, 80),
                    'Noblesse': Wearable("Noblesse", 1, 1, 1, 1, 0, 8, 16, 0.54, 0.01, 400),
                    'GReaper': Wearable("GReaper", 3, 4, 3, 5, 4, 17, 17, 0.44, 0.08, 480),
                    'Lava': Wearable("Lava", 1, 2, 1, 3, 2, 15, 15, 0.11, 0.01, 80),
                    'Legendary': Wearable("Legendary", 1, 4, 2, 2, 2, 3, 2, 0.56, 0.06, 1100),
                    'Cane': Wearable("Cane", 0, 1, 0, 0, 0, 8, 15, 0.2, 0, 500),
                    'Purewhite': Wearable("Purewhite", 2, 3, 2, 2, 2, 3, 2, 0.55, 0.06, 1100),
                    'Warrior': Wearable("Warrior", 6, 5, 8, 8, 2, 8, 8, 0.44, 0.08, 200),
                    'Viking': Wearable("Viking", 4, 3, 6, 6, 2, 22, 22, 0.29, 0.06, 200),
                    'Zodiac': Wearable("Zodiac", 5, 5, 5, 5, 5, 15, 15, 0.48, 0.08, 600),
                    'Summer': Wearable("Summer", 1, 2, 2, 1, 2, 5, 6, 0.46, 0.04, 800),
                    'Northsoul': Wearable("Northsoul", 0, 0, 1, 0, 0, 8, 16, 0.54, 0.01, 400),
                    'Pioneer Viking': Wearable("Pioneer Viking", 6, 5, 5, 5, 1, 22, 18, 0.44, 0.1, 300)
                    }

archer_armorS = {'Default': Wearable(),
                 'Sparta': Wearable("Sparta", 1, 0, 0, 2, 2, 20, 20, 0.24, 0.03, 150),
                 'Noblesse': Wearable("Noblesse", 1, 1, 1, 1, 2, 15, 15, 0.9, 0, 800),
                 'GReaper': Wearable("GReaper", 5, 3, 4, 5, 5, 15, 15, 0.48, 0.06, 550),
                 'Lava': Wearable("Lava", 2, 1, 2, 2, 3, 10, 10, 0.12, 0.01, 150),
                 'Legendary': Wearable("Legendary", 1, 4, 2, 1, 2, 12, 11, 0.67, 0.07, 2000),
                 'Cane': Wearable("Cane", 0, 1, 0, 0, 2, 16, 16, 0.95, 0, 800),
                 'Purewhite': Wearable("Purewhite", 3, 2, 2, 2, 4, 12, 11, 0.66, 0.07, 1500),
                 'Warrior': Wearable("Warrior", 6, 5, 8, 8, 2, 12, 12, 0.48, 0.06, 200),
                 'Viking': Wearable("Viking", 4, 3, 6, 6, 2, 22, 22, 0.29, 0.06, 200),
                 'Zodiac': Wearable("Zodiac", 5, 5, 5, 5, 5, 23, 23, 0.48, 0.08, 600),
                 'Summer': Wearable("Summer", 2, 1, 1, 2, 2, 6, 6, 0.57, 0.04, 900),
                 'Northsoul': Wearable("Northsoul", 0, 0, 1, 0, 2, 15, 15, 0.90, 0, 800),
                 'Pioneer Viking': Wearable("Pioneer Viking", 6, 5, 5, 5, 1, 22, 18, 0.44, 0.1, 300)}

archer_armS = {'Default': Wearable(),
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

archer_meleeS = {'Default': Wearable(),
                 'Sparta': Wearable("Sparta", 4, 0, 0, 2, 1, 10, 10, 0.24, 0.03, 150),
                 'Noblesse': Wearable("Noblesse", 3, 2, 3, 4, 4, 3, 4, 0.90, 0, 500),
                 'GReaper': Wearable("GReaper", 7, 5, 5, 7, 7, 10, 10, 1.02, 0.12, 600),
                 'Lava': Wearable("Lava", 2, 2, 2, 2, 2, 5, 5, 0.09, 0.01, 150),
                 'Legendary': Wearable("Legendary", 3, 5, 4, 3, 2, 1, 1, 0.71, 0.06, 600),
                 'Cane': Wearable("Cane", 2, 4, 3, 3, 4, 1, 1, 0.72, 0.12, 300),
                 'Purewhite': Wearable("Purewhite", 3, 7, 3, 4, 5, 6, 6, 0.71, 0.06, 1400),
                 'Warrior': Wearable("Warrior", 2, 11, 8, 5, 3, 3, 3, 1.02, 0.12, 150),
                 'Viking': Wearable("Viking", 3, 9, 7, 8, 2, 10, 10, 0.9, 0.09, 150),
                 'Zodiac': Wearable("Zodiac", 2, 9, 5, 3, 7, 1, 1, 0.73, 0.09, 400),
                 'Summer': Wearable("Summer", 2, 4, 2, 2, 4, 8, 8, 0.78, 0.06, 1100),
                 'Northsoul': Wearable("Northsoul", 2, 1, 2, 3, 3, 1, 2, 0.9, 0, 500),
                 'Pioneer Viking': Wearable("Pioneer Viking", 4, 14, 6, 6, 1, 10, 8, 1.35, 0.13, 200)
                 }

archer_rangeS = {'Default': Wearable(),
                 'Sparta': Wearable("Sparta", 6, 0, 0, 3, 0, 15, 15, 0.42, 0.04, 150),
                 'Noblesse': Wearable("Noblesse", 5, 4, 5, 4, 6, 5, 5, 0.98, 0.01,100),
                 'GReaper': Wearable("GReaper", 9, 7, 7, 11, 7, 12, 12, 1.22, 0.13, 600),
                 'Lava': Wearable("Lava", 4, 4, 4, 4, 4, 7, 7, 0.22, 0.01, 150),
                 'Legendary': Wearable("Legendary", 4, 5, 5, 6, 2, 0, 0, 0.86, 0.07, 600),
                 'Cane': Wearable("Cane", 5, 5, 4, 5, 5, 1, 1, 0.3, 0, 50),
                 'Purewhite': Wearable("Purewhite", 8, 3, 3, 4, 5, 7, 7, 0.86, 0.08, 1500),
                 'Warrior': Wearable("Warrior", 5, 12, 10, 8, 3, 4, 4, 1.22, 0.13, 300),
                 'Viking': Wearable("Viking", 4, 9, 8, 9, 3, 12, 12, 1.08, 0.09, 300),
                 'Zodiac': Wearable("Zodiac", 3, 11, 7, 3, 8, 2, 2, 0.89, 0.1, 700),
                 'Summer': Wearable("Summer", 4, 3, 4, 4, 3, 11, 11, 0.89, 0.07, 1200),
                 'Northsoul': Wearable("Northsoul", 4, 3, 4, 3, 5, 1, 1, 1.26, 0, 100),
                 'Pioneer Viking': Wearable("Pioneer Viking", 6, 14, 6, 7, 2, 12, 10, 1.62, 0.14, 500),
                 'GReaper Ballesta': Wearable("GReaper Ballesta", 10, 7, 8, 11, 7, 12, 12, 1.22, 0.13, 600),
                 'Lava Ballesta': Wearable("Lava Ballesta", 4, 4, 4, 4, 4, 7, 7, 0.22, 0.01, 150),
                 'Sparta Ballesta': Wearable("Sparta Ballesta", 6, 0, 0, 3, 0, 15, 15, 0.42, 0.04, 150),
                 'Noblesse Ballesta': Wearable("Noblesse Ballesta", 5, 4, 5, 5, 6, 5, 5, 1.08, 0.02, 100),
                 'Legendary Ballesta': Wearable("Legendary Ballesta", 4, 5, 5, 6, 2, 0, 0, 0.86, 0.07, 600),
                 'Cane Ballesta': Wearable("Cane Ballesta", 5, 5, 4, 5, 5, 0, 0, 0.3, 0, 50),
                 'Nightwatch Ballesta': Wearable("Nightwatch Ballesta", 4, 2, 4, 4, 2, 8, 8, 0.6, 0.04, 700),
                 'Purewhite Ballesta': Wearable("Purewhite Ballesta", 8, 3, 3, 4, 5, 7, 7, 0.86, 0.08, 1500),
                 'Zodiac Ballesta': Wearable("Zodiac Ballesta", 3, 11, 7, 3, 8, 5, 5, 0.89, 0.1, 700),
                 'Viking Ballesta': Wearable("Viking Ballesta", 4, 9, 9, 9, 3, 13, 13, 1.08, 0.09, 250),
                 'Warrior Ballesta': Wearable("Warrior Ballesta", 5, 13, 11, 8, 3, 4, 4, 1.22, 0.13, 300),
                 'Pioneer Viking Ballesta': Wearable("Pioneer Viking Ballesta", 6, 14, 7, 7, 2, 13, 10, 1.62, 0.14, 400)
                 }


class Archer:

    def __init__(self):
        self.basic = BASIC_ARCHER
        self.range = RANGE_ARCHER
        self.special = SPECIAL_ARCHER
        self.grip = GRIP_ARCHER
        self.cd = CELLDESTRUCTION_ARCHER
        self.hp = ENERGY_ARCHER
        self.ap = ARMOR_ARCHER
        self.attackSpeed = ATTACKSPEED_ARCHER
        self.movementSpeed = MOVEMENTSPEED_ARCHER
        self.cp = CELLPOINTS_ARCHER

        self.basicPerPoint = BASIC_PER_STATPOINT_ARCHER
        self.rangePerPoint = RANGE_PER_STATPOINT_ARCHER
        self.specialPerPoint = SPECIAL_PER_STATPOINT_ARCHER
        self.gripPerPoint = GRIP_PER_STATPOINT_ARCHER
        self.cdPerPoint = CELLDEST_PER_STATPOINT_ARCHER
        self.hpPerPoint = ENERGY_PER_STATPOINT_ARCHER
        self.apPerPoint = ARMOR_PER_STATPOINT_ARCHER
        self.attSpeedPerPoint = ATTACKSPED_PER_STATPOINT_ARCHER
        self.movSpeedPerPoint = MOVSPEED_PER_STATPOINT_ARCHER
        self.cpPerPoint = CELLPOINTS_PER_STATPOINT_ARCHER

        self.PAST50 = PAST50
        self.PAST80 = PAST80

        self.helmetS = archer_helmetS
        self.shoulderS = archer_shoulderS
        self.armorS = archer_armorS
        self.armS = archer_armS
        self.meleeS = archer_meleeS
        self.rangeS = archer_rangeS

    def advancedClass(self):
        self.basic = BASIC_ARCHER + 3
        self.range = RANGE_ARCHER + 4
        self.special = SPECIAL_ARCHER + 6
        self.grip = GRIP_ARCHER + 5
        self.cd = CELLDESTRUCTION_ARCHER + 0.2
        self.hp = ENERGY_ARCHER + 7
        self.ap = ARMOR_ARCHER + 7
        self.attackSpeed = ATTACKSPEED_ARCHER + 4.9
        self.movementSpeed = MOVEMENTSPEED_ARCHER + 0.36
        self.cp = CELLPOINTS_ARCHER + 100

    def normalClass(self):
        self.basic = BASIC_ARCHER
        self.range = RANGE_ARCHER
        self.special = SPECIAL_ARCHER
        self.grip = GRIP_ARCHER
        self.cd = CELLDESTRUCTION_ARCHER
        self.hp = ENERGY_ARCHER
        self.ap = ARMOR_ARCHER
        self.attackSpeed = ATTACKSPEED_ARCHER
        self.movementSpeed = MOVEMENTSPEED_ARCHER
        self.cp = CELLPOINTS_ARCHER
