def count_words(txt):
    return len(txt.split())

def count_letters(txt):
    lowered_string = txt.lower()
    count_dict = {}
    for c in lowered_string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    return count_dict

def main():

    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        words_count = count_words(file_contents)
        print(f"{words_count} words found in the document\n")
        count_dict = count_letters(file_contents)
        for k in count_dict:
            if not k.isalpha():
                continue
            print(f"The '{k}' character was found {count_dict[k]} times")
    print("--- End report ---")


main()


