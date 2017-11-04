
#import numpy as np
#names = np.genfromtxt('/home/chrism/ffbe/data/unit_stats.csv', delimiter=',', usecols=(0), dtype='S15')
#stats = np.genfromtxt('/home/chrism/ffbe/data/unit_stats.csv', delimiter=',', usecols=(1,2,3,4,5,6))

from ffbe.ingest.Ingestors import load_stats
import matplotlib.pyplot as plt
import numpy as np
import sys

PASSIVES_FILE = '/home/chrism/ffbe/data/ffbe/skills.json'
PASSIVES = False

names = []
for i in range(1,len(sys.argv)) :
    if sys.argv[i].lower() == '--passives' :
        print('Passives Enabled')
        PASSIVES = True
        continue
    names.append(sys.argv[i])

if len(names) == 0 :
    raise

if PASSIVES :
    stats = load_stats('/home/chrism/ffbe/data/ffbe/units.json', passives=PASSIVES_FILE)
else :
    stats = load_stats('/home/chrism/ffbe/data/ffbe/units.json')

counts = len(names)*[6*[0]]
for key, val in stats.items() :
   for n in range(0,len(names)) :
       if names[n] == key :
           continue
       comp = val > stats[names[n]]
       counts[n] = [x + y for x,y in zip(counts[n], comp)] 

x = [1,2,3,4,5,6]
ms = 20
mew = 2.5
font = {'weight': 'bold', 'size': 18}
for n in range(0,len(names)) :
    plt.plot(x, counts[n], 'o', ms=ms, mew=mew, label=names[n], alpha=0.75)
    plt.plot(x, counts[n], 'k.')
plt.xticks(x, ['HP', 'MP', 'ATK', 'DEF', 'MAG', 'SPR'])
plt.xlim((0,7))
plt.yticks(np.arange(0, len(stats)+5, 5))
plt.legend(loc=1)
plt.ylabel('# of Units w/ Stat >')
if not PASSIVES :
    plt.title('Base Stat Comparison')
else :
    plt.title('Stats + Passives')
plt.grid()
plt.rc('font', **font)
plt.show()
