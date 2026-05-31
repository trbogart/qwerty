from functools import reduce

fingers = ['qaz', 'wsx', 'edc', 'rfvtgb', 'yhnujm', 'ik', 'ol', 'p']
finger_masks = {
    key: 1 << finger for finger, keys in enumerate(fingers) for key in keys
}


def get_all_words():
    # return all words from SOWPODS dictionary
    with open('sowpods.txt') as file:
        for line in file:
            yield line.strip().lower()


def get_finger_mask(word: str) -> int:
    # return finger bit mask for word
    return reduce(lambda m, c: m | finger_masks[c], word, 0)
