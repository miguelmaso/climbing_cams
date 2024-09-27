import matplotlib as mpl
from matplotlib import pyplot as plt


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
