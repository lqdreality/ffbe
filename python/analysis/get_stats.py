
#import numpy as np
#names = np.genfromtxt('/home/chrism/ffbe/data/unit_stats.csv', delimiter=',', usecols=(0), dtype='S15')
#stats = np.genfromtxt('/home/chrism/ffbe/data/unit_stats.csv', delimiter=',', usecols=(1,2,3,4,5,6))

from ffbe.ingest.Ingestors import load_stats
import matplotlib.pyplot as plt
import sys

PASSIVES_FILE = '/home/chrism/ffbe/data/ffbe/skills.json'
PASSIVES = False

names = []
for i in range(1,len(sys.argv)) :
    if sys.argv[i].lower() == '--passives' :
        print('Passives enabled')
        PASSIVES = True
    names.append(sys.argv[i])

if len(names) == 0 :
    names = None

if PASSIVES :
    stats = load_stats('/home/chrism/ffbe/data/ffbe/units.json', 
                       names=names, 
                       passives=PASSIVES_FILE)
else :
    stats = load_stats('/home/chrism/ffbe/data/ffbe/units.json', names=names)

for key, val in stats.items() :
    print(key)
    val.print()


