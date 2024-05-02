from num2words import num2words


def number_to_words(num, lang="uk"):
    return num2words(num, lang=lang)

if __name__ == "__main__":
    print(number_to_words("123"))

