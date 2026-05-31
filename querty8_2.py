from collections import defaultdict

from common import get_all_words, get_mask

# length -> mask -> list of words
words = defaultdict(lambda: defaultdict(list))
for word in get_all_words():
    mask = get_mask(word)
    length = len(word)
    if mask.bit_count() == length:
        words[length][mask].append(word)


def get_words(mask: int) -> list[str]:
    return words[mask.bit_count()][mask]


reverse_order = False # put word with P first instead of second?
count = 0
unique_words = 0
mask1_range = range(128, 256) if reverse_order else range(0, 128)
mask2_range = range(0, 128) if reverse_order else range(128, 256)
for mask1 in mask1_range:  # word with letter 7 (p) second
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
for mask2 in mask2_range:
    unique_words += len(get_words(mask2))
print('-' * 40)
print(f'{count:,} word pairs with {unique_words:,} unique words')
