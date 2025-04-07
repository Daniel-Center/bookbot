def count_words(file_contents):
    file_split = file_contents.split()
    word_count = len(file_split)
    return word_count

def char_count(file_contents):
    file_split = file_contents.split()
    char_count = {}
    for w in file_split:
        for c in w.lower():
            if c in char_count:
                n = int(char_count[c])
                char_count[c] = n + 1
            else:
                char_count[c] = 1
    return char_count

def pretty_report(file):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(file)} total words")
    print("--------- Character Count -------")
    sorted_items = {k: v for k, v in sorted(char_count(file).items(), key=lambda item: item[1], reverse=True)}
    for k, v in sorted_items.items():
        print(f"{k}: {v}")

