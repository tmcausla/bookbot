def count_words(book_text):
    return len(book_text.split())


def count_letters(book_text):
    counts = {}

    for c in book_text:
        char = c.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def sort_on(items):
    return items["num"]

def sort_dict(d):
    result = []
    for c in d:
        if c.isalpha():
            result.append({"char": c, "num": d[c]})
    result.sort(reverse=True, key=sort_on)

    return result
