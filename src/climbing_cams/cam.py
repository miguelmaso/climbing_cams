from .units import Measurements

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

    def __eq__(self, other):
        return self.brand == other.brand and self.name == other.name and self.number == other.number

    @property
    def min(self):
        return self._min * Measurements.length.factor

    @property
    def max(self):
        return self._max * Measurements.length.factor

    @property
    def avg(self):
        return 0.5 * (self.min + self.max)

    @property
    def weight(self):
        return self._weight * Measurements.weight.factor

    @property
    def strength(self):
        return self._strength * Measurements.force.factor

    @property
    def expansion_rate(self):
        return self.max / self.min

    @property
    def expansion_range(self):
        return self.max - self.min

    @property
    def range(self):
        return [self.min, self.max]

    @property
    def specific_weight(self):
        return self.weight / self.expansion_range
