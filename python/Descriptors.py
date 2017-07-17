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
        for k, v in self.stats.items() :
            print(k + ': ' + str(v))

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
    def __init__(self, resistance=None) :
        self.resistance = dict()
        self.attr_list = Elements.ELEMENTS
        if resistance is None :
            for attr in self.attr_list :
                self.resistance.update({attr:0})
        else :
            self.resistance = resistance

    def update(self, attr, value) :
        if attr not in self.resistance :
            raise ValueError('Attempting to update nonexistent key')
        self.resistance[attr] = value

    def print(self) :
        for k, v in self.resistance.items() :
            print(k + ': ' + str(v))
