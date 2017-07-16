from Descriptors import *
from Equipment import *

class Character :
    def __init__(self, name='None', stats=BasicStats(), equipment=None) :
        self.name = name
        self.stats = stats
        if equipment is None :
            self.equipment = {'Lhand': None, 'Rhand': None, 
                              'Chest': None, 'Headgear': None, 
                              'Acc1': None, 'Acc2': None}
        else :
            self.equipment = equipment
        self.allowable_equip = ['Dagger']
        self.spells = 'None'
        self.traits = 'None'

    def equip(self, equipment, slot_num=1) :
        # First check if the equipment is allowed
        if equipment.etype not in self.allowable_equip :
            raise ValueError('Not allowed')

        slot = equipment.slot

        if slot not in Equipment.slots : # it's possible to make a fake slot
            raise ValueError('slot is not a recognized Equipment Slot')

        if slot == 'Accessory' :
            if self.equipment['Acc1'] is None :
                self.equipment['Acc1'] = equipment
            elif self.equipment['Acc2'] is None :
                self.equipment['Acc2'] = equipment
            else :
                if slot == 1 :
                    self.equipment['Acc1'] = equipment
                else :
                    self.equipment['Acc2'] = equipment
        elif slot == 'HandWeapon' :
            if equipment.is_2h :
                self.equipment['Rhand'] = equipment
                self.unequip('Lhand')
            else :
                if self.equipment['Rhand'] is None :
                    self.equipment['Rhand'] = equipment
                elif self.equipment['Lhand'] is None :
                    self.equipment['Lhand'] = equipment
                else :
                    if slot == 1 :
                        self.equipment['Rhand'] = equipment
                    else :
                        self.equipment['Lhand'] = equipment
        else :
            self.equipment[slot] = equipment

    def unequip(self, slot) :
        if slot not in self.equipment :
            raise ValueError(slot + ' is not a recognized slot type')
        self.equipment[slot] = None
