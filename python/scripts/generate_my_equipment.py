from ffbe.tools.Search import *
from ffbe.ingest.Ingestors import load_equipment
import pickle
import sys

EQUIPMENT_FILE = '/home/chrism/ffbe/data/equipment.pkl'
MY_EQUIPMENT_FILE = '/home/chrism/ffbe/data/my_equipment.txt'
MY_EQUIPMENT_FILE_OUT = '/home/chrism/ffbe/data/my_equipment.pkl'

if len(sys.argv) > 1 :
    VERBOSE = True
else :
    VERBOSE = False

names = []
f = open(MY_EQUIPMENT_FILE, 'r')
data = f.read()
data = data.split('\n')
data = data[:-1]
for d in data :
    if d[0] == '#' :
        continue
    names.append(d.split(',')[0])
f.close()

equipment = load_equipment(EQUIPMENT_FILE)

result = find_equipment(equipment, names=names, to_dict=True)
if VERBOSE :
    for key, val in result.items() :
        val.print()

f = open(MY_EQUIPMENT_FILE_OUT, 'wb')
pickle.dump(result,f)
f.close()
