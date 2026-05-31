from common import get_all_words, get_mask


def is_valid(s: str) -> bool:
    return len(s) == 8 and get_mask(s) == 0xFF


results = []
for word in get_all_words():
    if is_valid(word):
        results.append(word)
print(f'{len(results)}\n{'\n'.join(sorted(results))}')
