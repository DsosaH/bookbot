from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    sorted = get_sorted(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range(0, len(sorted)):
        if sorted[i]["char"].isalpha():
            print(f"{sorted[i]["char"]}: {sorted[i]["num"]}")      
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
