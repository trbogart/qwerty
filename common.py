from functools import reduce
from typing import Iterable

layout = 'qwerty'

fingers = {
    'qwerty': ['qaz', 'wsx', 'edc', 'rfvtgb', 'yhnujm', 'ik', 'ol', 'p'],
    'dvorak': ['a', 'oq', 'ej', 'pukyix', 'fdbghm', 'ctw', 'rnv', 'lsz'],
    'colemak': ['qaz', 'wrx', 'fsc', 'ptvgdb', 'jhklnm', 'ue', 'yi', 'o'],
}

finger_masks = {
    key: 1 << finger for finger, keys in enumerate(fingers[layout]) for key in keys
}


def get_all_words() -> Iterable[str]:
    # return all words from SOWPODS dictionary
    with open('sowpods.txt') as file:
        for line in file:
            yield line.strip().lower()


def get_finger_mask(word: str) -> int:
    # return finger bit mask for word
    return reduce(lambda m, c: m | finger_masks[c], word, 0)
