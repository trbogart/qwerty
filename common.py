from functools import reduce

fingers = ['qaz', 'wsx', 'edc', 'rfvtgb', 'yhnujm', 'ik', 'ol', 'p']
masks = {
    key: 1 << finger for finger, keys in enumerate(fingers) for key in keys
}


def get_all_words():
    with open('sowpods.txt') as file:
        for line in file:
            yield line.strip().lower()


def get_mask(s: str) -> int:
    return reduce(lambda m, c: m | masks[c], s, 0)
