def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)

    letter_count = count_each_letter(text)
    print(f"--- Begin report of {book_path}")
    print(f"{count} words found in the document")
    for n in letter_count:
        print(f"The {n} charactor was found a {letter_count[n]} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_each_letter(text):
    letter_count = {}
    for i in range(len(text)):
        if text[i] == "":
            continue
        n = text[i].lower()

        letter_count[n] = 1 + letter_count.get(n, 0)
    return letter_count


main()
