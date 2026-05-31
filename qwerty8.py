# Prints all words that are typed with every finger exactly once on a QWERTY keyboard

from common import get_all_words, get_finger_mask


def is_match(s: str) -> bool:
    return len(s) == 8 and get_finger_mask(s) == 0xFF


results = [word for word in get_all_words() if is_match(word)]
print(f'{len(results)}\n{'\n'.join(results)}')
