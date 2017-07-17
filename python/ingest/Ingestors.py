import json
from time import sleep
from Descriptors import *
from Equipment import *

def load_equipment(infile, pckl=None) :
    f = open(infile, 'r')
    data = json.load(f)
    f.close()

    equipment_list = []

    for iden, e in data.items() :
        name = e['name']
        print('Loading ' + e['name'])
        stats = e['stats']
        element = stats.pop('element_inflict')
        resistance = stats.pop('element_resist')
        ae = stats.pop('status_inflict')
        stats.pop('status_resist')
        etype = e['type']
        slot = e['slot']
        equipment = None
        if slot == 'Headgear' :
            equipment = Headgear(name=name, etype=etype, 
                                 stats=EquipmentStats(stats=stats),
                                 element=Elements(elements=element),
                                 resistance=Resistance(resistance=resistance), 
                                 ae=ae)
        elif slot == 'Chest' :
            equipment = Chest(name=name, etype=etype, 
                              stats=EquipmentStats(stats=stats),
                              element=Elements(elements=element), 
                              resistance=Resistance(resistance=resistance), 
                              ae=ae)
        elif slot == 'Accessory' :
            equipment = Accessory(name=name, etype=etype,
                                  stats=EquipmentStats(stats=stats),
                                  element=Elements(elements=element),
                                  resistance=Resistance(resistance=resistance), 
                                  ae=ae)
        elif slot == 'Shield' :
            equipment = Shield(name=name, etype=etype,
                               stats=EquipmentStats(stats=stats),
                               element=Elements(elements=element),
                               resistance=Resistance(resistance=resistance),
                               ae=ae)
        elif slot == 'Weapon' :
            is_2h = e['is_twohanded']
            equipment = Weapon(name=name, etype=etype,
                               stats=EquipmentStats(stats=stats),
                               element=Elements(elements=element),
                               resistance=Resistance(resistance=resistance),
                               ae=ae,
                               is_2h=is_2h)
        else :
            print(slot + ' NYI')

        if equipment is not None :
            #equipment.print()
            equipment_list.append(equipment)
        #sleep(3)

    if pckl is not None :
        print('Pickling up the list')

    return equipment_list


"""atk_dict = dict()
mag_dict = dict()
for k, v in data.items() :
    atk_dict.update({v['name']:v['stats']['ATK']})
    mag_dict.update({v['name']:v['stats']['MAG']})

tmp = sorted(atk_dict.items(), key=operator.itemgetter(1))
for x in tmp :
    print('Item: ' + x[0] + ', ATK: ' + str(x[1]))
"""
