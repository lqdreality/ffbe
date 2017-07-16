from Descriptors import *

class Equipment :
    slots = ['HandWeapon', 'Chest', 'Headgear', 'Accessory']
    def __init__(self, slot=None, etype=None, stats=EquipmentStats(), ele='', 
                 res=Resistance(), ae='None') :
        self.slot = slot # [Hand, Accessory, Headgear, Chest]
        self.etype = etype # Sword, dagger, etc
        self.stats = stats
        self.ele = ele
        self.res = res
        self.ae = ae

class Chest(Equipment) :
    def __init__(self, etype=None, stats=EquipmentStats(), ele='', 
                 res=Resistance(), ae='None') :
        Equipment.__init__(self, slot='Chest', etype=etype,  stats=stats, 
                           ele=ele, res=res, ae=ae)

class Headgear(Equipment) :
    def __init__(self, etype=None, stats=EquipmentStats(), ele='', 
                 res=Resistance(), ae='None') :
        Equipment.__init__(self, slot='Headgear', etype=etype,  stats=stats, 
                           ele=ele, res=res, ae=ae)

class HandWeapon(Equipment) :
    def __init__(self, etype=None, stats=EquipmentStats(), ele='', 
                 res=Resistance(), ae='None', is_2h=False) :
        Equipment.__init__(self, slot='HandWeapon', etype=etype,  stats=stats, 
                           ele=ele, res=res, ae=ae)
        self.is_2h = is_2h

class Accessory(Equipment) :
    def __init__(self, etype=None, stats=EquipmentStats(), ele='', 
                 res=Resistance(), ae='None') :
        Equipment.__init__(self, slot='Accessory', etype=etype,  stats=stats, 
                           ele=ele, res=res, ae=ae)
