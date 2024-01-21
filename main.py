def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dictionary_all_chars = get_num_char(text)
    print(get_report(dictionary_all_chars, num_words, text, book_path))


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_char(text):
    dictionary = {}    
    for char in text.lower():
        if char in dictionary:            
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary

def get_report(dictionary_all_chars,num_words, text, book_path):
    dictionary_list = list(dictionary_all_chars.items())
    dictionary_list.sort(key=lambda item: item[1], reverse=True)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document \n")
    for item in dictionary_list:        
        if item[0].isalpha():
            print(f"The '{item[0]}' character was found {item[1]} times") 
    return "--- End report ---"           

main()