
#import numpy as np
#names = np.genfromtxt('/home/chrism/ffbe/data/unit_stats.csv', delimiter=',', usecols=(0), dtype='S15')
#stats = np.genfromtxt('/home/chrism/ffbe/data/unit_stats.csv', delimiter=',', usecols=(1,2,3,4,5,6))

from ffbe.ingest.Ingestors import load_stats
import matplotlib.pyplot as plt
import sys

names = []
for i in range(1,len(sys.argv)) :
    names.append(sys.argv[i])

if len(names) == 0 :
    names = None
stats = load_stats('/home/chrism/ffbe/data/ffbe/units.json', names=names)

for key, val in stats.items() :
    print(key)
    val.print()


