def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    book_word_count = count_words(book_text)
    chars_dict = count_characters(book_text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f"--- Begin report of {filepath} ---")
    print(f"{book_word_count} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
    
    
def get_book_text(filepath):    
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_words(book_text):
    words = book_text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def count_characters(book_text):
    char_dict = {}
    for char in book_text:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()