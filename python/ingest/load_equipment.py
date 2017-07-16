import json
import operator

f = open('../../data/equipment.json', 'r')

data = json.load(f)
f.close()

atk_dict = dict()
mag_dict = dict()
for k, v in data.items() :
    atk_dict.update({v['name']:v['stats']['ATK']})
    mag_dict.update({v['name']:v['stats']['MAG']})

tmp = sorted(atk_dict.items(), key=operator.itemgetter(1))
for x in tmp :
    print('Item: ' + x[0] + ', ATK: ' + str(x[1]))
