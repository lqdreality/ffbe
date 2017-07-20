import json
from time import sleep
from Descriptors import *
from Equipment import *
from Skills import *

def load_equipment(infile, pckl=None, verbose=False) :
    f = open(infile, 'r')
    data = json.load(f)
    f.close()

    ae = ''

    equipment_dict = dict()

    for iden, e in data.items() :
        name = e['name']
        if verbose :
            print('Loading ' + e['name'])
        stats = e['stats']
        element = stats.pop('element_inflict')
        resistance = stats.pop('element_resist')
        status_inflict = stats.pop('status_inflict')
        stats.pop('status_resist')
        etype = e['type']
        slot = e['slot']
        equipment = None
        if slot == 'Headgear' :
            equipment = Headgear(name=name, etype=etype, 
                                 stats=EquipmentStats(stats=stats),
                                 element=Elements(elements=element),
                                 status_inflict=Status(status=status_inflict),
                                 resistance=Resistance(resistance=resistance), 
                                 ae=ae)
        elif slot == 'Chest' :
            equipment = Chest(name=name, etype=etype, 
                              stats=EquipmentStats(stats=stats),
                              element=Elements(elements=element), 
                              status_inflict=Status(status=status_inflict),
                              resistance=Resistance(resistance=resistance), 
                              ae=ae)
        elif slot == 'Accessory' :
            equipment = Accessory(name=name, etype=etype,
                                  stats=EquipmentStats(stats=stats),
                                  element=Elements(elements=element),
                                  status_inflict=Status(status=status_inflict),
                                  resistance=Resistance(resistance=resistance), 
                                  ae=ae)
        elif slot == 'Shield' :
            equipment = Shield(name=name, etype=etype,
                               stats=EquipmentStats(stats=stats),
                               element=Elements(elements=element),
                               status_inflict=Status(status=status_inflict),
                               resistance=Resistance(resistance=resistance),
                               ae=ae)
        elif slot == 'Weapon' :
            is_2h = e['is_twohanded']
            equipment = Weapon(name=name, etype=etype,
                               stats=EquipmentStats(stats=stats),
                               element=Elements(elements=element),
                               status_inflict=Status(status=status_inflict),
                               resistance=Resistance(resistance=resistance),
                               ae=ae,
                               is_2h=is_2h)
        elif verbose :
            print(slot + ' NYI')

        if equipment is not None :
            if verbose :
                equipment.print()
            equipment_dict.update({iden:equipment})

    if pckl is not None :
        print('Pickling up the list')

    return equipment_dict

def load_skills(infile, pckl=None, verbose=False) :
    f = open(infile, 'r')
    data = json.load(f)
    f.close()

    skill_dict = dict()

    for iden, s in data.items() :
        skill = None
        name = s['name']
        stype = s['type']
        active = s['active']
        skill = Skills(name=name, stype=stype, active=active)
        if skill is not None :
            if verbose :
                skill.print()
            skill_dict.update({iden:skill})
