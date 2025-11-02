def numbers(num):
    number = len(num.split())
    return number

def count_characters(a_string):
    text = a_string.lower()
    counts = {}
    for ch in text:
        if ch in "abcdefghijklmnopqrstuvwxyz":
            counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_on(item):
    return item["num"]

def build_sorted_list(counts):
    result = [{"char": ch, "num": cnt} for ch, cnt in counts.items()]
    result.sort(reverse=True, key=sort_on)
    return result