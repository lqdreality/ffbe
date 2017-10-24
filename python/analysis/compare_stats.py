
#import numpy as np
#names = np.genfromtxt('/home/chrism/ffbe/data/unit_stats.csv', delimiter=',', usecols=(0), dtype='S15')
#stats = np.genfromtxt('/home/chrism/ffbe/data/unit_stats.csv', delimiter=',', usecols=(1,2,3,4,5,6))

from ffbe.ingest.Ingestors import load_stats
import matplotlib.pyplot as plt
import numpy as np
import sys

names = []
for i in range(1,len(sys.argv)) :
    names.append(sys.argv[i])

if len(names) == 0 :
    raise

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
    plt.plot(x, counts[n], 'x', ms=ms, mew=mew, label=names[n])
plt.xticks(x, ['HP', 'MP', 'ATK', 'DEF', 'MAG', 'SPR'])
plt.xlim((0,7))
plt.yticks(np.arange(0, len(stats)+5, 5))
plt.legend(loc=1)
plt.ylabel('# of Units w/ Stat >')
plt.title('Base Stat Comparison')
plt.grid()
plt.rc('font', **font)
plt.show()
