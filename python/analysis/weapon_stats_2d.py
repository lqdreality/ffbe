from numpy import *
import matplotlib.pyplot as plt
import operator
import sys
from Search import find_equipment
from ingest.Ingestors import load_equipment

"""
q_equipments = ['Dagger', 'Katana', 'Sword', 'Great Sword', 'Axe', 'Spear', 'Hammer', 'Rod', 'Staff', 'Throwing Weapon', 'Bow', 'Gun', 'Fist', 'Harp', 'Mace', 'Whip']
q_stat = ['ATK','MAG']
"""

#"""
#q_equipments = ['Helm', 'Hat']
#q_equipments = ['Light Shield', 'Heavy Shield']
q_equipments = ['Robe', 'Heavy Armor', 'Light Armor', 'Cloth']
q_stat = ['DEF', 'SPR']
#"""

markers = ['.', '*', 'o', 'h', 'v', 'p', 'd', '|','>','8', 's', '1', '<', '_', 'x', '+']

elist = load_equipment('/home/chrism/ffbe/data/ffbe/equipment.json')

for i in range(0, len(q_equipments)) :
    equipment = find_equipment(elist, etypes=[q_equipments[i]])
    stat_tmr_1 = [e.stats.get_stat(q_stat[0]) for e in equipment if e.trust]
    stat_1 = [e.stats.get_stat(q_stat[0]) for e in equipment if not e.trust]
    stat_tmr_2 = [e.stats.get_stat(q_stat[1]) for e in equipment if e.trust]
    stat_2 = [e.stats.get_stat(q_stat[1]) for e in equipment if not e.trust]
    plt.plot(stat_tmr_1, stat_tmr_2, 'r'+markers[i], ms=20)
    plt.plot(stat_1, stat_2, 'b'+markers[i], label=q_equipments[i], ms=20)

plt.ylim(ymin=-1)
plt.legend(loc='upper right', ncol=4)
plt.xlabel(q_stat[0])
plt.ylabel(q_stat[1])
plt.show()
