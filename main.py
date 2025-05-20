from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    sorted = get_sorted(num_characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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
