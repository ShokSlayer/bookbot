import sys
from stats import num_words, count_characters, sort_char_counts


def get_book_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: The file '{filepath}' was not found."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    char_counter = count_characters(book_text)
    sorted_characters_counts = sort_char_counts(char_counter)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("---------- Word Count -----------")
    num_words(book_text)
    print("--------- Character Count -------")
    for char_info in sorted_characters_counts:
        print(f"{char_info['character']}: {char_info['count']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
