file_path = "books/frankenstein.txt"

with open(file_path) as f:
    # a function that counts the words in the text
    def count_words(text):
        words = text.split()
        num_words = len(words)
        return f"The document has {num_words} words.\n"

    def sort_on(dict):
        return dict["num"]
    
    def count_characters(text):
        text = text.lower()
        character_dict = {}
        for char in text:
            if char in character_dict:
                character_dict[char] += 1
            else:
                character_dict[char] = 1
        return character_dict
    
    def get_sorted_characters(dict):
        dict_list = []
        for key, value in dict.items():
            if key.isalpha():
                dict_list.append({"char":key, "num": value})
        dict_list.sort(reverse=True, key=sort_on)
        return dict_list
    
    def print_sorted_characters(dict):
        for x in dict:
            print(f"The {x["char"]} character was found {x["num"]} times")

    print(f"--- Begin report of {file_path} ---")

    book_text = f.read()
    print(count_words(book_text))
    print_sorted_characters(get_sorted_characters(count_characters(book_text)))

    print("--- End report ---")
