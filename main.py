from stats import count_words, count_letters, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    letter_count = count_letters(book_text)
    sorted_count = sort_dict(letter_count)
    for count in sorted_count:
        print(f"{count['char']}: {count['num']}")
    print("============= END ===============")


main()
