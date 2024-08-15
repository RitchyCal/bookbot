def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordCount = get_num_words(text)
    char_count = get_num_words(text)
    char_dict = count_of_char(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{char_count} words found in the document")

    for item in char_dict:
       print(f"The '{item}' character was found {char_dict[item]} times")
    
    print("--- End report ---")
   


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    return len(text.split())

def count_of_char(text):
    char_count = {}
    for word in text:
        lower_case = word.lower()
       
        if lower_case in char_count:
            char_count[lower_case] += 1 
        else:
            char_count[lower_case] = 1
    return char_count
main()