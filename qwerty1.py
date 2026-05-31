# Prints all words that are typed with exactly one finger, in descending length

from collections import defaultdict

from common import get_all_words, get_finger_mask


def is_valid(s: str) -> bool:
    return get_finger_mask(s).bit_count() == 1


matches_by_length = defaultdict(list)
for word in get_all_words():
    if is_valid(word):
        matches_by_length[len(word)].append(word)
for length in sorted(matches_by_length.keys(), reverse=True):
    matches = matches_by_length[length]
    print('-' * 40)
    print(f'{len(matches)} matches with length {length}:')
    for word in sorted(matches):
        print(f'- {word}')
