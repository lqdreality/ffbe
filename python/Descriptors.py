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

class Resistance :
    def __init__(self, res=dict()) :
        self.res = res
