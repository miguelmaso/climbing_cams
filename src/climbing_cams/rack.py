
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
