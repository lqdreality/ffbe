from ffbe.classes.Descriptors import *
from ffbe.classes.Equipment import *

class Character :
    def __init__(self, name='None', 
                 level=0,
                 star=6,
                 max_star=6,
                 base_stats=BasicStats(), 
                 equipment=None,
                 allowable_equip=[]) :
        self.name = name
        self.level = level
        self.star = star
        self.max_star = star
        self.base_stats = base_stats
        if equipment is None :
            self.equipment = {'Lhand': None, 'Rhand': None, 
                              'Chest': None, 'Headgear': None, 
                              'Acc1': None, 'Acc2': None}
        else :
            self.equipment = equipment
        self.allowable_equip = allowable_equip
        self.spells = 'None'
        self.traits = 'None'

    def get_stats(self, stat=None) :
        if stat is None :
            return self.get_combined_stats()

    def get_combined_stats(self) :
        pass

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
        elif slot == 'Shield' :
            if self.equipment['Lhand'] is None :
                if self.equipment['Rhand'] is not None and 
                   self.equipment['Rhand'].slot == 'Shield' :
                    self.equipment['Rhand'] = equipment
                else :
                    self.equipment['Lhand'] = equipment
            elif self.equipment['Rhand'] is None :
                if self.equipment['Lhand'].slot == 'Shield' :
                    self.equipment['Lhand'] = equipment
                else :
                    self.equipment['Rhand'] = equipment
            else :
                if slot == 1 :
                    self.equipment['Rhand'] = equipment
                else :
                    self.equipment['Lhand'] = equipment
        elif slot == 'Weapon' :
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
