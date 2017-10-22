import json
from time import sleep
from Descriptors import *
from Equipment import *
from Skills import *

def write_tmr_equipment_file(infile, outfile) :
    f = open(infile, 'r')
    data = json.load(f)
    f.close()

    f = open(outfile, 'w')
    for iden, c in data.items() :
        tmr = c['TMR']
        if tmr is None :
            continue
        for i in range(0, len(tmr)) :
            if tmr[i] == 'EQUIP' :
                f.write(str(tmr[i+1])+'\n')
                i += 1
    f.close()

def load_stats(infile, names=None, out_file=None) :
    f = open(infile, 'r')
    data = json.load(f)
    f.close()

    if out_file is not None :
        out_f = open(out_file, 'w')

    char_stat_dict = {}
    for iden1, val1 in data.items() :
        if names is not None :
            if val1['name'] not in names :
                continue
        inname = val1['name']
        for iden2, val2 in val1['entries'].items() :
            if val2['rarity'] != 6 :
                continue
            atk = val2['stats']['ATK'][1]
            mag = val2['stats']['MAG'][1]
            deff = val2['stats']['DEF'][1]
            spr = val2['stats']['SPR'][1]
            hp = val2['stats']['HP'][1]
            mp = val2['stats']['MP'][1]
            if out_file is not None :
                out_f.write(inname + ',' + str(hp) + ',' + str(mp) + ',' + \
                            str(atk) + ',' + str(deff) + ',' + str(mag) + ',' + \
                            str(spr) + '\n')
            stats = BasicStats({'HP': hp, 'MP': mp, 'ATK': atk, 'DEF': deff, 'MAG': mag, 'SPR': spr})
            char_stat_dict.update({inname:stats})
    if out_file is not None :
        out_f.close()
    return char_stat_dict

def load_equipment(infile, tmr_file='/home/chrism/ffbe/data/tmr_equipment.txt',
                   pckl=None, verbose=False) :
    f = open(infile, 'r')
    data = json.load(f)
    f.close()

    ae = ''

    with open(tmr_file, 'r') as f :
        tmr_lst = f.read().splitlines()

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
        if str(iden) in tmr_lst :
            trust = True
        else :
            trust = False
        equipment = None
        if slot == 'Headgear' :
            equipment = Headgear(name=name, etype=etype, 
                                 stats=EquipmentStats(stats=stats),
                                 element=Elements(elements=element),
                                 status_inflict=Status(status=status_inflict),
                                 resistance=Resistance(resistance=resistance), 
                                 trust=trust,
                                 ae=ae)
        elif slot == 'Chest' :
            equipment = Chest(name=name, etype=etype, 
                              stats=EquipmentStats(stats=stats),
                              element=Elements(elements=element), 
                              status_inflict=Status(status=status_inflict),
                              resistance=Resistance(resistance=resistance), 
                              trust=trust,
                              ae=ae)
        elif slot == 'Accessory' :
            equipment = Accessory(name=name, etype=etype,
                                  stats=EquipmentStats(stats=stats),
                                  element=Elements(elements=element),
                                  status_inflict=Status(status=status_inflict),
                                  resistance=Resistance(resistance=resistance), 
                                  trust=trust,
                                  ae=ae)
        elif slot == 'Shield' :
            equipment = Shield(name=name, etype=etype,
                               stats=EquipmentStats(stats=stats),
                               element=Elements(elements=element),
                               status_inflict=Status(status=status_inflict),
                               resistance=Resistance(resistance=resistance),
                               trust=trust,
                               ae=ae)
        elif slot == 'Weapon' :
            is_2h = e['is_twohanded']
            equipment = Weapon(name=name, etype=etype,
                               stats=EquipmentStats(stats=stats),
                               element=Elements(elements=element),
                               status_inflict=Status(status=status_inflict),
                               resistance=Resistance(resistance=resistance),
                               trust=trust,
                               ae=ae,
                               is_2h=is_2h)
        elif verbose :
            print(slot + ' NYI')

        if equipment is not None :
            if verbose :
                equipment.print()
            equipment_dict.update({iden:equipment})

    if pckl is not None :
        import pickle
        print('Pickling up the list')
        f_pckl = open(pckl, 'wb')
        pickle.dump(equipment_dict, f_pckl)
        f_pckl.close()

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
