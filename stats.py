def num_words(text):
    words = text.split()
    count = len(words)
    print(f"Found {count} total words")

def count_characters(book_text):
    book_text = book_text.lower()
    char_count = {}
    for char in book_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_counts(char_count):
    sorted_chars = [{'character': char, 'count': count} for char, count in char_count.items() if char.isalpha()]
    #Vyrovná list od největšího po nejmenší
    sorted_chars.sort(key=lambda x: x["count"], reverse = True)
    return sorted_chars