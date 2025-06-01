import sys
from stats import get_word_count
from stats import get_character_count
from stats import sort_character_count


def get_book_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            contents = f.read()
        return contents
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file at '{filepath}' was not found.")

def main():
    try:
        filepath = sys.argv[1]  # Attempt to get the file path from command-line arguments
    except IndexError:
        print("Error: Please provide a file path as a command-line argument.")
        print("Usage: python3 main.py <path_to_book>")
        print("Example: python3 main.py /path/to/book.txt")
        sys.exit(1)
    except Exception as e:
         print(f"An unexpected error occurred: {e}")
    
    contents = get_book_text(filepath)
    count = get_word_count(contents)
    char_count = get_character_count(contents)
    char_count_sorted = sort_character_count(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    print("Dictionary of characters found in the document")
    for line in char_count_sorted:
        print(line)
    print("============= END ===============")

main()