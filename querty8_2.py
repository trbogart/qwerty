# Prints all pair of words that are typed with every finger exactly once on a QWERTY keyboard

from collections import defaultdict

from common import get_all_words, get_finger_mask

words = defaultdict(list)  # mask -> list of words with that mask and no repeats
for word in get_all_words():
    mask = get_finger_mask(word)
    if mask.bit_count() == len(word):
        words[mask].append(word)


def get_words(mask: int) -> list[str]:
    # return words with finger mask
    return words[mask]


# both counts are doubled
count = 0
unique_words = 0
for mask1 in range(1, 256):
    words1 = get_words(mask1)
    if words1:
        mask2 = ~mask1 & 0xFF
        words2 = get_words(mask2)
        unique_words += len(words1)

        if words2:
            count += len(words1) * len(words2)
            for word1 in words1:
                print('-' * 40)
                for word2 in words2:
                    print(f'   {word1} {word2}')
print('-' * 40)
print(f'{count // 2:,} word pairs with {unique_words // 2:,} unique words')
