from Descriptors import *

class Equipment :
    slots = ['Weapon', 'Chest', 'Headgear', 'Accessory', 'Shield']
    def __init__(self, name=None, 
                 slot=None, 
                 etype=None, 
                 stats=EquipmentStats(),
                 element=Elements(), 
                 resistance=Resistance(), 
                 ae='None') :
        self.name = name
        self.slot = slot # [Weapon, Accessory, Headgear, Chest, Shield]
        self.etype = etype # Sword, dagger, etc
        self.stats = stats
        self.element = element
        self.resistance = resistance
        self.ae = ae

    def get_stat(self, stat) :
        return self.stats.get_stat(stat)

    def print(self) :
        print('Name: ' + self.name)
        print('Type: ' + self.etype)
        self.stats.print()
        self.element.print()
        self.resistance.print()
        #print('Additional Notes: ' + self.ae)

class Chest(Equipment) :
    def __init__(self, name=None, 
                 etype=None, 
                 stats=EquipmentStats(), 
                 element=Elements(), 
                 resistance=Resistance(), 
                 ae='None') :
        Equipment.__init__(self, name=name, 
                           slot='Chest', 
                           etype=etype,  
                           stats=stats, 
                           element=element, 
                           resistance=resistance, 
                           ae=ae)

class Headgear(Equipment) :
    def __init__(self, name=None, 
                 etype=None, 
                 stats=EquipmentStats(), 
                 element=Elements(), 
                 resistance=Resistance(), 
                 ae='None') :
        Equipment.__init__(self, name=name, 
                           slot='Headgear', 
                           etype=etype, 
                           stats=stats, 
                           element=element, 
                           resistance=resistance, 
                           ae=ae)

class Weapon(Equipment) :
    def __init__(self, name=None, 
                 etype=None, 
                 stats=EquipmentStats(), 
                 element=Elements(), 
                 resistance=Resistance(), 
                 ae='None', 
                 is_2h=False) :
        Equipment.__init__(self, name=name, 
                           slot='Weapon', 
                           etype=etype, 
                           stats=stats, 
                           element=element,
                           resistance=resistance, 
                           ae=ae)
        self.is_2h = is_2h

    def print(self) :
        Equipment.print(self)
        print('2h: ' + str(self.is_2h))

class Accessory(Equipment) :
    def __init__(self, name=None, 
                 etype=None, 
                 stats=EquipmentStats(), 
                 element=Elements(),
                 resistance=Resistance(), 
                 ae='None') :
        Equipment.__init__(self, name=name, 
                           slot='Accessory', 
                           etype=etype, 
                           stats=stats, 
                           element=element, 
                           resistance=resistance, 
                           ae=ae)

class Shield(Equipment) :
    def __init__(self, name=None,
                 etype=None,
                 stats=EquipmentStats(),
                 element=Elements(),
                 resistance=Resistance(),
                 ae='None') :
        Equipment.__init__(self, name=name,
                           slot='Shield',
                           etype=etype,
                           stats=stats,
                           element=element,
                           resistance=resistance,
                           ae=ae)
