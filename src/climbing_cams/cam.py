from .units import Measurements


class Cam:
    def __init__(self, brand: str, name: str, number: any, color: str,
                 min: float, max: float, weight: float = 0, strength: float = 0):
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

    def __eq__(self, other) -> bool:
        if isinstance(other, Cam):
            return self.brand == other.brand and self.name == other.name and self.number == other.number
        else:
            return False

    @property
    def min(self) -> float:
        return self._min * Measurements.length.factor

    @property
    def max(self) -> float:
        return self._max * Measurements.length.factor

    @property
    def avg(self) -> float:
        return 0.5 * (self.min + self.max)

    @property
    def weight(self) -> float:
        return self._weight * Measurements.weight.factor

    @property
    def strength(self) -> float:
        return self._strength * Measurements.force.factor

    @property
    def expansion_rate(self) -> float:
        return self.max / self.min

    @property
    def expansion_range(self) -> float:
        return self.max - self.min

    @property
    def range(self) -> list:
        return [self.min, self.max]

    @property
    def specific_weight(self) -> float:
        return self.weight / self.expansion_range
