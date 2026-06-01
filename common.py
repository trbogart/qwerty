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


def get_all_words() -> Iterable[tuple[str, int]]:
    # return all words from SOWPODS dictionary, along with finger bit mask
    with open('sowpods.txt') as file:
        for line in file:
            word = line.strip().lower()
            mask = reduce(lambda m, c: m | finger_masks[c], word, 0)
            yield word, mask
