# Prints all words that are typed with every finger exactly once on a QWERTY keyboard

from common import get_all_words

results = [word for word, mask in get_all_words() if len(word) == 8 and mask == 0xFF]
print(f'{len(results)} words:\n{'\n'.join(results)}')
