class DictObj :
    def __init__(self, data, attr_list) :
        if not isinstance(data, dict) :
            data = dict()
        self.data = data.copy()
        self.attr_list = attr_list
        for attr in self.attr_list :
            if attr not in data :
                self.data.update({attr:0})
        for k in data.keys() :
            if k not in self.attr_list :
                self.data.pop(k)

    def get_data(self, key) :
        if key not in self.attr_list :
            raise ValueError('Cannot get ' + key + '. Not in Attribute list')
        return self.data[key]

    def update(self, attr, value) :
        if attr not in self.data :
            raise ValueError('Attempting to Update Nonexisting key ' + attr)
        self.data.update({attr:value})

class Stats(DictObj) :
    def __init__(self, stats=dict(), stype='') :
        self.stype = stype
        attr_list = ['HP', 'MP', 'ATK', 'MAG', 'DEF', 'SPR']
        DictObj.__init__(self, stats, attr_list)

    def get_stat(self, stat) :
        return self.get_data(stat)

    def print(self) :
        print('|   HP   |   MP  |  ATK  |  MAG  |  DEF  |  SPR  |')
        print('|  ' + '{0:04d}'.format(self.data['HP']) + '  |  ' + 
              '{0:03d}'.format(self.data['MP']) + '  |  ' + 
              '{0:03d}'.format(self.data['ATK']) + '  |  ' +
              '{0:03d}'.format(self.data['MAG']) + '  |  ' +
              '{0:03d}'.format(self.data['DEF']) + '  |  ' +
              '{0:03d}'.format(self.data['SPR']) + '  |')

    def __add__(self, other) :
        stats = self.data.copy()
        for attr in self.attr_list :
            stats[attr] += other.data[attr]
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

class Elements(DictObj) :
    def __init__(self, elements=dict()) :
        attr_list = ['Fire', 'Ice', 'Earth', 'Lightning',
                     'Wind', 'Dark', 'Holy', 'Water', 'Light']
        DictObj.__init__(self, elements, attr_list)
        if isinstance(elements, str) :
            self.update(elements, 1)
        elif isinstance(elements, list) :
            for e in elements :
                self.update(e, 1)
            
    def print(self) :
        out_str = '| '
        for k,v in self.data.items() :
            if v != 0 :
                out_str += k + ' | '
        if len(out_str) > 2 :
            print('Element(s): ' + out_str)

class Status(DictObj) :
    def __init__(self, status=dict()) :
        attr_list = ['Poison', 'Sleep', 'Blind', 'Silence', 'Paralyze',
                     'Confuse', 'Disease', 'Petrify']
        DictObj.__init__(self, status, attr_list)

    def print(self) :
        print('| Poison | Sleep | Blind | Silence | Paralyze | Confuse | Disease'
              ' | Petrify |')
        print('|     ' + '{0:02d}'.format(self.data['Poison']) + ' |    ' +
              '{0:02d}'.format(self.data['Sleep']) + ' |    ' +
              '{0:02d}'.format(self.data['Blind']) + ' |      ' +
              '{0:02d}'.format(self.data['Silence']) + ' |       ' +
              '{0:02d}'.format(self.data['Paralyze']) + ' |      ' +
              '{0:02d}'.format(self.data['Confuse']) + ' |      ' +
              '{0:02d}'.format(self.data['Disease']) + ' |      ' +
              '{0:02d}'.format(self.data['Petrify']) + ' |')

class Resistance(DictObj) :
    def __init__(self, resistance=dict()) :
        attr_list = ['Fire', 'Ice', 'Earth', 'Lightning',
                     'Wind', 'Dark', 'Holy', 'Water']
        DictObj.__init__(self, resistance, attr_list)

    def print(self) :
        print('| Fire | Ice | Earth | Lightning | Water | Wind | Holy | Dark |')
        print('|   ' + '{0:02d}'.format(self.data['Fire']) + ' |  ' +
              '{0:02d}'.format(self.data['Ice']) + ' |    ' +
              '{0:02d}'.format(self.data['Earth']) + ' |        ' +
              '{0:02d}'.format(self.data['Lightning']) + ' |    ' +
              '{0:02d}'.format(self.data['Water']) + ' |   ' +
              '{0:02d}'.format(self.data['Wind']) + ' |   ' +
              '{0:02d}'.format(self.data['Holy']) + ' |   ' + 
              '{0:02d}'.format(self.data['Dark']) + ' |')
