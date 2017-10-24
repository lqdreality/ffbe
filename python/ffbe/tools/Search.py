from ffbe.classes.Equipment import *

def find_equipment(elist, 
                   names=None, 
                   etypes=[], 
                   stats=[], 
                   operators=[], 
                   comp_vals=[], 
                   verbose=False, 
                   to_dict=False) :

    n_found = 0

    if to_dict :
        found_equip = {}
    else :
        found_equip = []

    if names is not None :
        if not isinstance(names, list) :
            names = [names.lower()]
        else :
            names = [name.lower() for name in names]

    if not isinstance(etypes, list) :
        etypes = [etypes]

    if len(etypes) == 0 :
        search_all = True
    else :
        search_all = False

    for iden, equipment in elist.items() :
        if names is not None :
            if equipment.name.lower() in names :
                found = True
            else :
                found = False
        else :
            if not search_all :
                if equipment.etype not in etypes and equipment.slot not in etypes :
                    continue
            # If stats is not a list, create list
            if not isinstance(stats, list) :
                stats = [stats]
            num_stats = len(stats)

            # If operators/CVs is not a list, create a list with the same element
            if not isinstance(operators, list) :
                operators = [operators] * num_stats
            if not isinstance(comp_vals, list) :
                comp_vals = [comp_vals] * num_stats
            # if stats is one, but ops and CVs arent
            if num_stats == 1 and len(operators) > 1 and len(comp_vals) > 1 :
                assert len(operators) == len(comp_vals)
                stats = [stats[0]] * len(operators)
            found = True
            for stat, op, val in zip(stats, operators, comp_vals) :
                s_val = equipment.get_stat(stat)
                found &= op(s_val,val)

        if found :
            n_found += 1
            if to_dict :
                found_equip.update({iden:equipment})
            else :
                found_equip.append(equipment)

    if verbose :
        for equipment in found_equip :
            print('\n')
            equipment.print()
        print('\n')
        print('Found a total of ' + str(n_found) + ' matches')

    return found_equip

def find_skills() :
    pass
