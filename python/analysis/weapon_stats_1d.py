from numpy import *
import matplotlib.pyplot as plt
import operator
import sys
from Search import find_equipment
from ingest.Ingestors import load_equipment

#"""
# Atk Stats
q_equipments = ['Dagger', 'Katana', 'Sword', 'Great Sword', 'Axe', 'Spear', 'Hammer', 'Rod', 'Staff', 'Throwing Weapon', 'Bow', 'Gun', 'Fist', 'Harp', 'Mace', 'Whip']
q_stat = 'ATK'
#"""

"""
q_equipments = ['Rod', 'Staff']
q_stat = 'MAG'
"""

markers = ['x', '.', '+', '*', 'o', 'h', 'v', 'p', 'd', '|','>','8', 's', '1', '<', '_']

elist = load_equipment('/home/chrism/ffbe/data/ffbe/equipment.json')

for i in range(0, len(q_equipments)) :
    equipment = find_equipment(elist, etypes=[q_equipments[i]])
    stat_tmr = [e.stats.get_stat(q_stat) for e in equipment if e.trust]
    stat = [e.stats.get_stat(q_stat) for e in equipment if not e.trust]
    plt.plot(sort(stat_tmr), zeros(len(stat_tmr))+i, 'r'+markers[i], ms=20)
    plt.plot(sort(stat), zeros(len(stat))+i, 'b'+markers[i], label=q_equipments[i], ms=20)

plt.ylim([-4,len(q_equipments)])
plt.legend(loc='lower right', ncol=4)
plt.xlabel(q_stat)
plt.show()
