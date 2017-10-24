import json
import numpy as np
import matplotlib.pyplot as plt

def disp_stats(data, title) :
    stat_h = np.bincount(data)
    N = stat_h.shape[0]
    am = np.nonzero(stat_h)[0][0]
    stat_x = np.arange(am, N)
    stat_h = stat_h[am:]
    font = {'weight' : 'bold', 'size'   : 18}
    plt.bar(stat_x,stat_h)
    #plt.xticks(np.arange(am, N, 3))
    plt.grid()
    plt.title(title)
    plt.rc('font', **font)
    plt.show()

def load_stats(name=None) :
    f = open('../data/ffbe/units.json', 'r')
    data = json.load(f)
    f.close()

    atk_stats = []
    mag_stats = []
    def_stats = []
    spr_stats = []
    hp_stats = []
    mp_stats = []
    for iden1, val1 in data.items() :
        if name is not None :
            if val1['name'] == name :
                continue
        for iden2, val2 in val1['entries'].items() :
            if val2['rarity'] != 6 :
                continue
            atk_stats.append(val2['stats']['ATK'][1])
            mag_stats.append(val2['stats']['MAG'][1])
            def_stats.append(val2['stats']['DEF'][1])
            spr_stats.append(val2['stats']['SPR'][1])
            hp_stats.append(val2['stats']['HP'][1])
            mp_stats.append(val2['stats']['MP'][1])
    stats = {'ATK': np.array(atk_stats), 'MAG': np.array(mag_stats), 'DEF': np.array(def_stats), 'SPR': np.array(spr_stats), 'MP': np.array(mp_stats), 'HP': np.array(hp_stats)}
    return stats

def main() :
    font = {'weight' : 'bold', 'size'   : 18}
    stats = load_stats(name='Olive')
    stats_ai = load_stats(name='Aileen')
    hp = 3296
    mp = 150
    atk = 156
    deff = 124
    mag = 106
    spr = 102
    hpp = 3698
    mpp = 149
    atkk = 155
    defff = 120
    magg = 122
    sprr = 119
    x = [1,2,3,4,5,6]
    y = [np.sum(stats['HP'] > hp), np.sum(stats['MP'] > mp), np.sum(stats['ATK'] > atk), np.sum(stats['DEF'] > deff), np.sum(stats['MAG'] > mag), np.sum(stats['SPR'] > spr)]
    yy = [np.sum(stats_ai['HP'] > hpp), np.sum(stats_ai['MP'] > mpp), np.sum(stats_ai['ATK'] > atkk), np.sum(stats_ai['DEF'] > defff), np.sum(stats_ai['MAG'] > magg), np.sum(stats_ai['SPR'] > sprr)]
    plt.plot(x, y, 'x', ms=20, mew=5, label='Olive')
    plt.plot(x,yy,'x', ms=20, mew=5, label='Aileen')
    plt.xticks(x, ('HP', 'MP', 'ATK', 'DEF', 'MAG', 'SPR'))
    plt.yticks(np.arange(0,180,5))
    plt.xlim((0,7))
    plt.ylabel('# of 6* units with strictly better stat')
    plt.grid()
    plt.rc('font', **font)
    plt.title('Olive vs Aileen')
    plt.legend(loc=4)
    plt.show()

def main2() :
    disp_stats(np.array(atk_stats), 'ATK')
    disp_stats(np.array(mag_stats), 'MAG')
    disp_stats(np.array(mag_stats), 'MAG')
    disp_stats(np.array(def_stats), 'DEF')
    disp_stats(np.array(spr_stats), 'SPR')
    disp_stats(np.array(hp_stats), 'HP')
    disp_stats(np.array(mp_stats), 'MP')

if __name__ == '__main__' :
    main()
