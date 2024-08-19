def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words =count_words(text)
    chars_dict = get_chars_dict(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("\n")
    final_list = convert_dict(chars_dict)
    for item in final_list:
        print(f"The '{item["char"]}' character was found {item["num"]} times")
    print("--- End report ---")

def get_text(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    words = text.split()
    chars = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0, 
        'j': 0, 
        'k': 0,
        'l': 0, 
        'm': 0, 
        'n': 0, 
        'o': 0, 
        'p': 0, 
        'q': 0, 
        'r': 0, 
        's': 0, 
        't': 0, 
        'u': 0, 
        'v': 0, 
        'w': 0, 
        'y': 0, 
        'x': 0, 
        'z': 0
    }

    for word in words:
        lower_word = word.lower()
        for char in lower_word:
                if char in chars:
                    chars[char] += 1

    return chars

# A function that takes a dictionary and returns the value of the "num" key
def sort_on(d):
     return d["num"]

def convert_dict(dict):
    new_list = []
    for key in dict:
        new_dict = {
            "char": key,
            "num": dict[key]
        }
        new_list.append(new_dict)
    # gotta sort it before returning otherwise it doesn't evaluate -> a good question is why???
    new_list.sort(reverse=True, key=sort_on)
    return new_list


main()
