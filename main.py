def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = word_count(text)
    character_counts = count_characters(text)
    new_count = count_character_report(character_counts)
    report = (
        f"--- Begin report of {book_path} ---\n"
        f"{num_words} words found in the document\n\n"
        f"{new_count}\n"
        f"--- End report ---"
    )
    print(report)


def get_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def word_count(words_in_book):
    number_of_words = len(words_in_book.split())
    return number_of_words

def count_characters(count):
    characters = count.lower()
    letters = {}
    for character in characters:
        if character.isalpha():
            if character in letters:
                letters[character] += 1
            else:
                letters[character] = 1
    return letters

def count_character_report(character_counts):
    list_of_items = list(character_counts.items())
    sorted_items = sorted(list_of_items, key=lambda item: item[1], reverse=True)
    report_lines = []
    for character, count in sorted_items:
        report_lines.append(f"The '{character}' character was found {count} times")
    full_report = "\n".join(report_lines)
    return full_report



main()




