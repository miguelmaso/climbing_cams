import enum

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

def set_system(cls, system):
    if system == cls.System.INTERNATIONAL:
        length_factor = 1
        weight_factor = 1
        range = cls.min = cls.max = cls.avg = cls.expansion_range = 'mm'
        weight = 'g'
        strength = 'kN'
        expansion_rate = ''
        specific_weight = cls.weight + '/' + cls.range
    elif system == cls.System.IMPERIAL:
        length_factor = 0.0393701
        weight_factor = 0.00220462
        range = cls.min = cls.max = cls.avg = cls.expansion_range = 'in'
        weight = 'lb'
        strength = 'kN'
        expansion_rate = ''
        specific_weight = cls.weight + '/' + cls.range
