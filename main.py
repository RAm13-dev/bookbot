from stats import numbers
from stats import count_characters
from stats import build_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text()
    text_number = numbers(text)
    letters_number = count_characters(text)
    alist = build_sorted_list(letters_number)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {text_number} total words")
    print("--------- Character Count -------")
    for item in alist:  # from build_sorted_list(letters_number)
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()