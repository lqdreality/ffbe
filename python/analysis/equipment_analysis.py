from ffbe.tools.Search import find_equipment
from ffbe.tools.load_pickle import load_pickle
import matplotlib.pyplot as plt

#EQUIPMENT_FILE = '/home/chrism/ffbe/data/my_equipment.pkl'
EQUIPMENT_FILE = '/home/chrism/ffbe/data/equipment.pkl'

equipment = load_pickle(EQUIPMENT_FILE)

ms = 25
a = 0.5
deff = []
spr = []
result = find_equipment(equipment, etypes='Accessory')
for r in result :
    deff.append(r.get_stat('DEF'))
    spr.append(r.get_stat('SPR'))
plt.plot(deff, spr, 'b.', ms=ms, alpha=a, label='Accessory')

deff = []
spr = []
result = find_equipment(equipment, etypes='Headgear')
for r in result :
    deff.append(r.get_stat('DEF'))
    spr.append(r.get_stat('SPR'))
plt.plot(deff, spr, 'm.', ms=ms, alpha=a, label='Headgear')

deff = []
spr = []
result = find_equipment(equipment, etypes='Shield')
for r in result :
    deff.append(r.get_stat('DEF'))
    spr.append(r.get_stat('SPR'))
plt.plot(deff, spr, 'r.', ms=ms, alpha=a, label='Shield')

deff = []
spr = []
result = find_equipment(equipment, etypes='Chest')
for r in result :
    deff.append(r.get_stat('DEF'))
    spr.append(r.get_stat('SPR'))
plt.plot(deff, spr, 'g.', ms=ms, alpha=a, label='Chest')

plt.title('Non-weapon DEF/SPR Spread')
plt.xlim([-2,80])
plt.ylim([-2,80])
plt.grid()
plt.xlabel('DEF')
plt.ylabel('SPR')
plt.legend(loc=2)
font = {'size': 24, 'weight': 'bold' }
plt.rc('font', **font)
plt.show()
