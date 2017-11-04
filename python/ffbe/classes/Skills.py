from ffbe.classes.Descriptors import *

class Skills :
    def __init__(self, name=None,
                 stype='MAGIC',
                 active=True) :
        self.name = name
        self.stype = stype
        self.active = active
    def print(self) :
        print('Skill: ' + self.name)

class PassiveSkills(Skills) :
    def __init__(self) :
        Skills.__init__(self, active=False)
        self.bonuses = Stats()
