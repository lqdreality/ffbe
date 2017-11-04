import json
from time import sleep
import re
from ffbe.classes.Descriptors import *
from ffbe.classes.Equipment import *
from ffbe.classes.Skills import *

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
                f.write(str(tmr[i+1]) + ',' + c['name'] + '\n')
                i += 1
    f.close()
    
def load_passives(infile) :
    f = open(infile, 'r')
    passives = json.load(f)
    f.close()
    
    output = {}
    idx = {'ATK': 0, 'DEF': 1, 'MAG': 2, 'SPR': 3, 'HP': 4, 'MP': 5}
    #regex = '((HP|MP|ATK|DEF|(^MAG|, MAG)|SPR)+.*%|^Analysis$)'
    for iden, val in passives.items() :
        #match = re.search(regex, val['name'])
        for er in val['effects_raw'] :
            if er[1] == 3 and er[2] == 1 :
                stats = BasicStats()
                effects = er[3]
                stats.data['ATK'] += effects[idx['ATK']]/100
                stats.data['DEF'] += effects[idx['DEF']]/100
                stats.data['MAG'] += effects[idx['MAG']]/100
                stats.data['SPR'] += effects[idx['SPR']]/100
                stats.data['HP'] += effects[idx['HP']]/100
                stats.data['MP'] += effects[idx['MP']]/100
                output.update({iden:stats})
    return output

def load_stats(infile, names=None, out_file=None, passives=None) :
    f = open(infile, 'r')
    data = json.load(f)
    f.close()
    
    if names is not None and not isinstance(names,list) :
        names = [names]
    
    if passives is not None :
        ps = load_passives(passives)

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
            if passives is not None :
                incr = BasicStats()
                for s in val1['skills'] :
                    key = str(s['id'])
                    if key in ps :
                        incr = incr + stats*ps[key] # not sure if %'s are stacked or they apply to base stats
                stats = stats + incr
            char_stat_dict.update({inname:stats})
    if out_file is not None :
        out_f.close()
    return char_stat_dict

def load_equipment(infile, tmr_file='/home/chrism/ffbe/data/tmr_equipment.txt',
                   pckl=None, verbose=False) :

    if infile.endswith('.pkl') :
        import pickle
        f = open(infile, 'rb')
        data = pickle.load(f)
        f.close()
        return data
    elif infile.endswith('.json') :
        f = open(infile, 'r')
        data = json.load(f)
        f.close()
    else :
        raise

    ae = ''

    tmr_items = {}
    with open(tmr_file, 'r') as f :
        tmr_lst = f.read().splitlines()
        for tmr in tmr_lst :
            info = tmr.split(',')
            tmr_items.update({info[0]:info[1]})

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
        if str(iden) in tmr_items :
            trust = tmr_items[iden]
        else :
            trust = None
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
