import os
import csv
import matplotlib.pyplot as plt

class Units:
    length_converter = 1
    weight_converter = 1
    strength_converter = 1
    range = min = max = 'mm'
    weight = 'g'
    strength = 'kN'
    expansion_rate = ''
    specific_weight = weight + '/' + range

    @classmethod
    def set_si(cls):
        cls.length_converter = 1
        cls.weight_converter = 1
        cls.range = cls.min = cls.max = 'mm'
        cls.weight = 'g'
        cls.strength = 'kN'
        cls.expansion_rate = ''
        cls.specific_weight = cls.weight + '/' + cls.range

    @classmethod
    def set_imperial(cls):
        cls.length_converter = 0.0393701
        cls.weight_converter = 0.00220462
        cls.range = cls.min = cls.max = 'in'
        cls.weight = 'lb'
        cls.strength = 'kN'
        cls.expansion_rate = ''
        cls.specific_weight = cls.weight + '/' + cls.range


class Cam:
    def __init__(self, brand, name, number, color, min, max, weight=0, strength=0):
        self.brand = brand
        self.name = name
        self.number = number
        self.color = color
        self._min = float(min)
        self._max = float(max)
        self._weight = float(weight)
        self._strength = float(strength)
        if self._min > self._max:
            self._min, self._max = self._max, self._min
            print(f'The cam {self.brand} {self.name} [{self.number}] has been defined with a negative range. New range:')
            print(f'min: {self._min}')
            print(f'max: {self._max}')

    @property
    def min(self):
        return self._min * Units.length_converter

    @property
    def max(self):
        return self._max * Units.length_converter

    @property
    def weight(self):
        return self._weight * Units.weight_converter

    @property
    def strength(self):
        return self._strength * Units.strength_converter

    @property
    def expansion_rate(self):
        return self.max / self.min

    @property
    def range(self):
        return [self.max, self.min]

    @property
    def specific_weight(self):
        return self.weight / (self.max - self.min)


class Rack(list):
    @property
    def min(self):
        minimums = [i.min for i in self]
        return min(minimums)

    @property
    def max(self):
        maximums = [i.max for i in self]
        return max(maximums)

    @property
    def specific_weight(self):
        specific_weights = [i.specific_weight for i in self]
        return sum(specific_weights) / len(self)

    @property
    def weight(self):
        weights = [i.weight for i in self]
        return sum(weights)
    
    @property
    def min_strength(self):
        strengths = [i.strength for i in self]
        return min(strengths)
    
    @property
    def max_strength(self):
        strengths = [i.strength for i in self]
        return max(strengths)

    @property
    def expansion_rate(self):
        ratii = [i.expansion_rate for i in self]
        return sum(ratii) / len(self)

    def name(self, sep=' '):
        names = [i.brand + sep + i.name for i in self]
        unique_names = []
        for name in names:
            if name not in unique_names:
                unique_names.append(name)
        return ' | '.join(unique_names)


def load_data():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'climbing_cams.csv')) as file:
        reader = csv.reader(file)
        next(reader)
        data = [Cam(*row) for row in reader]
    return data

def select_cams(data, brand="", name="", number="", color="", expansion_range=[]):
    rack = Rack()
    for cam in data:
        if ((cam.brand == brand if brand else True) and
            (cam.name == name if name else True) and
            (cam.number == number if number else True) and
            (cam.color == color if color else True) and
            (expansion_range[0] < cam.min < cam.max < expansion_range[1] if len(expansion_range)==2 else True)):
            rack.append(cam)
    return rack

def bar_chart(rack, ax=None, ylabel='[{number}]'):
    if ax is None:
        ax = plt.gca()
    labels = [ylabel.format(brand=cam.brand, name=cam.name, number=cam.number) for cam in rack]
    minimums = [cam.min for cam in rack]
    maximums = [cam.max for cam in rack]
    ranges = [maximum - minimum for maximum, minimum in zip(maximums, minimums)]
    colors = [cam.color for cam in rack]
    ax.barh(labels, width=ranges, left=minimums, height=1, color=colors)

def plot_ranges(racks_list, smart_ylabels=False):
    sizes = [len(rack) for rack in racks_list]
    fig, axes = plt.subplots(nrows=len(racks_list), sharex=True,
        gridspec_kw={'height_ratios':sizes, 'hspace':0})
    axes = [axes] if len(racks_list) == 1 else axes

    for rack, ax in zip(racks_list, axes):
        bar_chart(rack, ax)
        sep = '\n'
        ax.set_ylabel(f'{rack.name(sep)}')
        ax.spines.right.set_visible(False)
        ax.spines.left.set_visible(False)
        ax.spines.top.set_visible(False)
        ax.tick_params(length=0)
        ax.xaxis.grid()
        ax.set_axisbelow(True)
        if smart_ylabels:
            ax.set_yticklabels([])
            ax.set_ylabel(f'{rack.name(sep)}', rotation=0, horizontalalignment='right', verticalalignment='center')
    fig.tight_layout()
    return fig, axes

def scatter_average(racks_list, xvalue, yvalue):
    fig, axes = plt.subplots()
    for rack in racks_list:
        axes.plot([getattr(rack, xvalue)], [getattr(rack, yvalue)], label=rack.name(), marker='o', markersize=10, linewidth=0, alpha=.7)
        axes.legend()
    axes.set_xlabel(f'{xvalue.replace("_"," ").capitalize()} [{getattr(Units, xvalue)}]')
    axes.set_ylabel(f'{yvalue.replace("_"," ").capitalize()} [{getattr(Units, yvalue)}]')
    fig.tight_layout()
    return fig, axes

def scatter_individual(racks_list, xvalue, yvalue):
    fig, axes = plt.subplots()
    for rack in racks_list:
        x = [getattr(i, xvalue) for i in rack]
        y = [getattr(i, yvalue) for i in rack]
        axes.plot(x, y, label=rack.name(), marker='o', markersize=10, linewidth=0, alpha=.7)
        axes.legend()
    axes.set_xlabel(f'{xvalue.replace("_"," ").capitalize()} [{getattr(Units, xvalue)}]')
    axes.set_ylabel(f'{yvalue.replace("_"," ").capitalize()} [{getattr(Units, yvalue)}]')
    fig.tight_layout()
    return fig, axes

