import os
import csv
import enum
import matplotlib as mpl
import matplotlib.pyplot as plt

class Units:
    class System(enum.Enum):
        INTERNATIONAL = 1
        IMPERIAL = 2

    length_factor = 1
    weight_factor = 1
    strength_factor = 1
    range = min = max = avg = expansion_range = 'mm'
    weight = 'g'
    strength = 'kN'
    expansion_rate = ''
    specific_weight = weight + '/' + range

    @classmethod
    def set_system(cls, system):
        if system == cls.System.INTERNATIONAL:
            cls.length_factor = 1
            cls.weight_factor = 1
            cls.range = cls.min = cls.max = cls.avg = cls.expansion_range = 'mm'
            cls.weight = 'g'
            cls.strength = 'kN'
            cls.expansion_rate = ''
            cls.specific_weight = cls.weight + '/' + cls.range
        elif system == cls.System.IMPERIAL:
            cls.length_factor = 0.0393701
            cls.weight_factor = 0.00220462
            cls.range = cls.min = cls.max = cls.avg = cls.expansion_range = 'in'
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
        return self._min * Units.length_factor

    @property
    def max(self):
        return self._max * Units.length_factor

    @property
    def avg(self):
        return 0.5 * (self.min + self.max)

    @property
    def weight(self):
        return self._weight * Units.weight_factor

    @property
    def strength(self):
        return self._strength * Units.strength_factor

    @property
    def expansion_rate(self):
        return self.max / self.min

    @property
    def expansion_range(self):
        return self.max - self.min

    @property
    def range(self):
        return [self.max, self.min]

    @property
    def specific_weight(self):
        return self.weight / self.expansion_range


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
    def avg(self):
        averages = [i.avg for i in self]
        return sum(averages) / len(self)

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

    @property
    def expansion_range(self):
        ranges = [i.expansion_range for i in self]
        return sum(ranges) / len(self)

    def name(self, sep=' '):
        names = [i.brand + sep + i.name for i in self]
        unique_names = []
        for name in names:
            if name not in unique_names:
                unique_names.append(name)
        return ' | '.join(unique_names)
    
    def plot_bar_chart(self, ax=None, ylabel='[{number}]', number_inside=False):
        if ax is None:
            ax = plt.gca()
        labels = [ylabel.format(brand=cam.brand, name=cam.name, number=cam.number) for cam in self]
        minimums = [cam.min for cam in self]
        maximums = [cam.max for cam in self]
        ranges = [maximum - minimum for maximum, minimum in zip(maximums, minimums)]
        colors = [cam.color for cam in self]
        bars = ax.barh(labels, width=ranges, left=minimums, height=.8, color=colors, alpha=0.7)

        for patch in reversed(bars):
            bb = patch.get_bbox()
            color = patch.get_facecolor()
            p_bbox = mpl.patches.FancyBboxPatch((bb.xmin, bb.ymin),
                                abs(bb.width), abs(bb.height),
                                boxstyle="round,pad=0,rounding_size=0.5",
                                ec="none", fc=color,
                                mutation_aspect=0.2
                                )
            patch.remove()
            ax.add_patch(p_bbox)

        if number_inside:
            numbers = [cam.number for cam in self]
            ax.bar_label(bars, numbers, label_type='center', fontsize=5, weight='bold', color='white')


class DB:
    _data = []

    @staticmethod
    def _load():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'climbing_cams.csv')) as file:
            reader = csv.reader(file)
            next(reader)
            data = [Cam(*row) for row in reader]
        DB._data += data

    @staticmethod
    def select(brand="", name="", number="", color="", expansion_range=[]):
        rack = Rack()
        for cam in DB._data:
            if ((cam.brand == brand if brand else True) and
                (cam.name == name if name else True) and
                (cam.number == number if number else True) and
                (cam.color == color if color else True) and
                (expansion_range[0] < cam.min < cam.max < expansion_range[1] if len(expansion_range)==2 else True)):
                rack.append(cam)
        return rack


class Plots:

    @staticmethod
    def plot_ranges(racks, smart_ylabels=True, numbers_inside=True):
        sizes = [len(rack) for rack in racks]
        fig, axes = plt.subplots(nrows=len(racks), sharex=True,
            gridspec_kw={'height_ratios':sizes, 'hspace':0})
        axes = [axes] if len(racks) == 1 else axes

        for rack, ax in zip(racks, axes):
            rack.plot_bar_chart(ax, number_inside=numbers_inside)
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

    @staticmethod
    def scatter_average(racks, xvalue, yvalue, ax=None):
        if not ax:
            fig, ax = plt.subplots()
        else:
            fig = ax.get_figure()
        for rack in racks:
            ax.plot([getattr(rack, xvalue)], [getattr(rack, yvalue)], label=rack.name(), marker='o', markersize=10, linewidth=0, alpha=.7)
            ax.legend()
        ax.set_xlabel(f'{xvalue.replace("_"," ").capitalize()} [{getattr(Units, xvalue)}]')
        ax.set_ylabel(f'{yvalue.replace("_"," ").capitalize()} [{getattr(Units, yvalue)}]')
        fig.tight_layout()
        return fig, ax

    @staticmethod
    def scatter_individual(racks, xvalue, yvalue, ax=None):
        if not ax:
            fig, ax = plt.subplots()
        else:
            fig = ax.get_figure()
        for rack in racks:
            x = [getattr(i, xvalue) for i in rack]
            y = [getattr(i, yvalue) for i in rack]
            ax.plot(x, y, label=rack.name(), marker='o', markersize=10, linewidth=0, alpha=.7)
            ax.legend()
        ax.set_xlabel(f'{xvalue.replace("_"," ").capitalize()} [{getattr(Units, xvalue)}]')
        ax.set_ylabel(f'{yvalue.replace("_"," ").capitalize()} [{getattr(Units, yvalue)}]')
        fig.tight_layout()
        return fig, ax

DB._load()
