from Equipment import *

def find_equipment(elist=None, etypes=[], stats=[], operators=[], 
                   comp_vals=[], search_all=False) :
    n_found = 0
    found_equip = []
    for equipment in elist :
        if not search_all and equipment.etype not in etypes :
            continue
        found = True
        for stat, op, val in zip(stats, operators, comp_vals) :
            s_val = equipment.get_stat(stat)
            found &= op(s_val,val)
        if found :
            n_found += 1
            found_equip.append(equipment)
    for equipment in found_equip :
        print('\n')
        equipment.print()
    print('\n')
    print('Found a total of ' + str(n_found) + ' matches')
