import enum


class System(enum.Enum):
    INTERNATIONAL = 1
    IMPERIAL = 2


class Unit:
    def __init__(self, label: str, factor: float):
        self.factor = factor
        self.label = label

    def __truediv__(self, other):
        if isinstance(other, Unit):
            label = self.label + '/' + other.label
            factor = self.factor / other.factor
            return Unit(label, factor)
        else:
            raise Exception(f'Unknown operator </> between {Unit} and {type(other)}')


class Measurements:
    length = Unit('mm', 1)
    weight = Unit('g', 1)
    force = Unit('kN', 1)
    dimless = Unit('-', 1)

    _measurements = {
        'min': lambda cls: cls.length,
        'max': lambda cls: cls.length,
        'avg': lambda cls: cls.length,
        'range': lambda cls: cls.length,
        'expansion_range': lambda cls: cls.length,
        'expansion_rate': lambda cls: cls.dimless,
        'weight': lambda cls: cls.weight,
        'strength': lambda cls: cls.force,
        'specific_weight': lambda cls: cls.weight / cls.length,
    }

    @classmethod
    def set_system(cls, system: System):
        if system == System.INTERNATIONAL:
            cls.length = Unit('mm', 1)
            cls.weight = Unit('g', 1)
        elif system == System.IMPERIAL:
            cls.length = Unit('in', 0.0393701)
            cls.weight = Unit('lb', 0.00220462)

    @classmethod
    def get_label(cls, measurement: str):
        return cls._measurements[measurement](cls).label
