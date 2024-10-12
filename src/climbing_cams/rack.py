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
