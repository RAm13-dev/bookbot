def numbers(num):
    number = len(num.split())
    return number

def count_characters(a_string):
    text = a_string.lower()
    counts = {}
    for ch in text:
        if ch in counts:
            counts[ch] = counts[ch] + 1
        else:
            counts[ch] = 1 
    return counts

def sort_on(item):
    return item["num"]

def build_sorted_list(counts):
    result = []
    for ch, cnt in counts.items():
        if not ch.isalpha():
            continue
        result.append({"char": ch, "num": cnt})
    result.sort(reverse=True, key=sort_on)
    return result