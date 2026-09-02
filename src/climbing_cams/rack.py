from .cam import Cam


class Rack(list[Cam]):
    @property
    def min(self) -> float:
        minimums = [i.min for i in self]
        return min(minimums)

    @property
    def max(self) -> float:
        maximums = [i.max for i in self]
        return max(maximums)

    @property
    def avg(self) -> float:
        averages = [i.avg for i in self]
        return sum(averages) / len(self)

    @property
    def specific_weight(self) -> float:
        specific_weights = [i.specific_weight for i in self]
        return sum(specific_weights) / len(self)

    @property
    def weight(self) -> float:
        weights = [i.weight for i in self]
        return sum(weights)

    @property
    def min_strength(self) -> float:
        strengths = [i.strength for i in self]
        return min(strengths)

    @property
    def max_strength(self) -> float:
        strengths = [i.strength for i in self]
        return max(strengths)

    @property
    def expansion_rate(self) -> float:
        ratii = [i.expansion_rate for i in self]
        return sum(ratii) / len(self)

    @property
    def expansion_range(self) -> float:
        ranges = [i.expansion_range for i in self]
        return sum(ranges) / len(self)

    def name(self, sep: str = ' ') -> str:
        names = [i.brand + sep + i.name for i in self]
        unique_names = []
        for name in names:
            if name not in unique_names:
                unique_names.append(name)
        return ' | '.join(unique_names)

    def barh(self, ax=None, ylabel='[{number}]', numbers_inside=False):
        from . import plots
        return plots._rack_barh(self, ax=ax, ylabel=ylabel, numbers_inside=numbers_inside)

    def weight_range(self, ax=None, **kwargs):
        from . import plots
        return plots._rack_weight_range(self, ax=ax, **kwargs)


class Racks(list[Rack]):
    def barh(self, smart_ylabels=True, numbers_inside=True):
        from . import plots
        return plots._racks_barh(self, smart_ylabels=smart_ylabels, numbers_inside=numbers_inside)

    def scatter(self, xvalue: str, yvalue: str, ax=None, individual=False):
        from . import plots
        return plots._racks_scatter(self, xvalue, yvalue, ax=ax, individual=individual)

    def weight_range(self, ax=None, **kwargs):
        fig = None
        for rack in self:
            fig, ax = rack.weight_range(ax=ax, **kwargs)
        return fig, ax
