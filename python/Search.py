from Equipment import *

def find_equipment(elist=None, etypes=[], stats=[], operators=[], comp_vals=[]) :
    found_equip = []
    for equipment in elist :
        if equipment.etype not in etypes :
            continue
        found = True
        for stat, op, val in zip(stats, operators, comp_vals) :
            s_val = equipment.get_stat(stat)
            found &= op(s_val,val)
        if found :
            found_equip.append(equipment)
    for equipment in found_equip :
        equipment.print()
