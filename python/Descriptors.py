class Stats :
    def __init__(self, stats=None, stype='') :
        self.stype = stype
        self.stats = dict()
        self.attr_list = ['HP', 'MP', 'ATK', 'MAG', 'DEF', 'SPR']
        if stats is None :
            for attr in self.attr_list :
                self.stats.update({attr:0})
        else :
            self.stats = stats

    def get_stat(self, stat) :
        if stat not in self.attr_list :
            raise ValueError('Cannot get ' + stat + '. Not in list')
        return self.stats[stat]

    def update(self, attr, value) :
        if attr not in self.stats :
            raise ValueError('Attempting to update nonexistent key')
        self.stats[attr] = value

    def print(self) :
        print('|   HP   |   MP  |  ATK  |  MAG  |  DEF  |  SPR  |')
        print('|  ' + '{0:04d}'.format(self.stats['HP']) + '  |  ' + 
              '{0:03d}'.format(self.stats['MP']) + '  |  ' + 
              '{0:03d}'.format(self.stats['ATK']) + '  |  ' +
              '{0:03d}'.format(self.stats['MAG']) + '  |  ' +
              '{0:03d}'.format(self.stats['DEF']) + '  |  ' +
              '{0:03d}'.format(self.stats['SPR']) + '  |')

    def __add__(self, other) :
        stats = self.stats.copy()
        for attr in self.attr_list :
            stats[attr] += other.stats[attr]
        return Stats(stats=stats)

class BasicStats(Stats) :
    def __init__(self, stats=None) :
        Stats.__init__(self, stats=stats, stype='Basic')

class EquipmentStats(Stats) :
    def __init__(self, stats=None) :
        Stats.__init__(self, stats=stats, stype='Equipment')

class LimitBreakerStats(Stats) :
    def __init__(self, stats=None, limits=None) :
        Stats.__init__(self, stats=stats, stype='LimitBreaker')
        self.limits = limits

class Elements :
    ELEMENTS = ['Fire', 'Ice', 'Earth', 'Lightning',
               'Wind', 'Dark', 'Holy', 'Water']
    def __init__(self, elements=None) :
        if elements is None :
            self.elements = []
        else :
            self.elements = elements

    def print(self) :
        if len(self.elements) > 0 :
            ele_print = ''
            for ele in self.elements :
                ele_print += ele + ' '
            print('Elements: ' + ele_print)

class Resistance :
    def __init__(self, resistance=dict()) :
        self.resistance = resistance.copy()
        self.attr_list = Elements.ELEMENTS
        for attr in self.attr_list :
            if attr not in resistance :
                self.resistance.update({attr:0})
        for k in resistance.keys() :
            if k not in self.attr_list :
                self.resistance.pop(k)

    def update(self, attr, value) :
        if attr not in self.resistance :
            raise ValueError('Attempting to update nonexistent key')
        self.resistance[attr] = value

    def print(self) :
        print('| Fire | Ice | Earth | Lightning | Water | Wind | Holy | Dark |')
        print('|   ' + '{0:02d}'.format(self.resistance['Fire']) + ' |  ' +
              '{0:02d}'.format(self.resistance['Ice']) + ' |    ' +
              '{0:02d}'.format(self.resistance['Earth']) + ' |        ' +
              '{0:02d}'.format(self.resistance['Lightning']) + ' |    ' +
              '{0:02d}'.format(self.resistance['Water']) + ' |   ' +
              '{0:02d}'.format(self.resistance['Wind']) + ' |   ' +
              '{0:02d}'.format(self.resistance['Holy']) + ' |   ' + 
              '{0:02d}'.format(self.resistance['Dark']) + ' |')
        #for k, v in self.resistance.items() :
        #    print(k + ': ' + str(v))
