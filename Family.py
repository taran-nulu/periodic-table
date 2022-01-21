from enum import *

class Family(Enum):
    NONMETAL = auto()
    NOBLE_GAS = auto()
    ALKALI_METAL = auto()
    ALKALINE_EARTH_METAL = auto()
    METALLOID = auto()
    HALOGEN = auto()
    METAL = auto()
    TRANSITION_METAL = auto()
    LANTHANOID = auto()
    ACTINOID = auto()


familyColors = {
    Family.NONMETAL : '#FCDBDB',
    Family.NOBLE_GAS : '#FFE6C2',
    Family.ALKALI_METAL : '#F2F9B5',
    Family.ALKALINE_EARTH_METAL : '#CFF897',
    Family.METALLOID : '#B5F9BB',
    Family.HALOGEN : '#AAF8E6',
    Family.METAL : '#AAE6F8',
    Family.TRANSITION_METAL : '#AAB8F8',
    Family.LANTHANOID : '#C6AAF8',
    Family.ACTINOID : '#EEAAF8',
}