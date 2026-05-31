# Prints all pair of words that are typed with every finger exactly once on a QWERTY keyboard
from typing import Iterator, Tuple

from common import get_all_words, get_finger_mask


class Words:
    def __init__(self, mask: int):
        self.mask = mask
        self.count = 0

    def add_word(self, word: str) -> None:
        self.count += 1


class Qwerty:
    def __init__(self):
        self.mask_words: list[Words] = [Words(i) for i in range(256)]
        for word in get_all_words():
            mask = get_finger_mask(word)
            if mask.bit_count() == len(word):
                self.mask_words[mask].add_word(word)

    def run(self):
        counts = [self.get_count(max_words=max_words) for max_words in range(9)]
        for num_words in range(1, len(counts)):
            count = counts[num_words] - counts[num_words - 1]
            if count > 0:
                print(f'{count:,} groups of {num_words} words')

    def get_count(self, max_words: int):
        if max_words == 0:
            return 0
        mask_counts = [-1] * 256
        return self._get_count(mask=0xFF, mask_counts=mask_counts, max_words=max_words, num_words=1)

    def _get_count(self, mask: int, mask_counts: list[int], max_words: int, num_words: int) -> int:
        if mask_counts[mask] >= 0:
            return mask_counts[mask]

        count = self.mask_words[mask].count
        if num_words < max_words:
            for mask1, mask2 in self._get_sub_masks(mask):
                count1 = self._get_count(mask1, mask_counts, max_words, num_words + 1)
                if count1 > 0:
                    count2 = self._get_count(mask2, mask_counts, max_words, num_words + 1)
                    count += count1 * count2

        mask_counts[mask] = count
        return count

    @staticmethod
    def _get_sub_masks(mask: int) -> Iterator[Tuple[int, int]]:
        if mask.bit_length() > 2:
            for mask1 in range(1, 128):
                if mask1 != mask and mask1 | mask == mask:
                    mask2 = ~mask1 & mask
                    assert mask1 > 0
                    assert mask2 > 0
                    assert mask1 ^ mask2 == mask
                    yield mask1, mask2


if __name__ == '__main__':
    Qwerty().run()
