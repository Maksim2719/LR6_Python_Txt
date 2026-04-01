import re

UKR_ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
LAT_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

UKR_INDEX = {ch: i for i, ch in enumerate(UKR_ALPHABET)}
LAT_INDEX = {ch: i for i, ch in enumerate(LAT_ALPHABET)}


def get_word_type(word: str) -> int:
    """
    0 -> українське слово
    1 -> латинське слово
    2 -> інше
    """
    lower_word = word.lower()

    has_ukr = any(ch in UKR_INDEX for ch in lower_word)
    has_lat = any(ch in LAT_INDEX for ch in lower_word)

    if has_ukr and not has_lat:
        return 0
    elif has_lat and not has_ukr:
        return 1
    elif has_ukr:
        return 0
    elif has_lat:
        return 1
    return 2


def char_priority(ch: str, word_type: int) -> int:
    ch = ch.lower()

    if word_type == 0:  # українські слова
        if ch in UKR_INDEX:
            return UKR_INDEX[ch]
        elif ch in LAT_INDEX:
            return 100 + LAT_INDEX[ch]
    elif word_type == 1:  # латинські слова
        if ch in LAT_INDEX:
            return LAT_INDEX[ch]
        elif ch in UKR_INDEX:
            return 100 + UKR_INDEX[ch]

    return 1000 + ord(ch)


def sort_key(word: str):
    word_type = get_word_type(word)
    chars_key = tuple(char_priority(ch, word_type) for ch in word.lower())
    return word_type, chars_key, word.lower()


def extract_words(text: str):
    return re.findall(r"[A-Za-zА-Яа-яІіЇїЄєҐґ_'\-’]+", text)


def main():
    filename = "input_text.txt"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return

    print("ПОЧАТКОВИЙ ТЕКСТ:\n")
    print(text)

    words = extract_words(text)

    print("\nСПИСОК СЛІВ ДО СОРТУВАННЯ:\n")
    print(words)

    sorted_words = sorted(words, key=sort_key)

    print("\nВІДСОРТОВАНИЙ СПИСОК СЛІВ:\n")
    print(sorted_words)

    print("\nВІДСОРТОВАНИЙ ТЕКСТ:\n")
    print(" ".join(sorted_words))


if __name__ == "__main__":
    main()