import re
import sys
import unicodedata


def get_words(text):
    word_pattern = r"(?:[a-z]+(?:[\-.][a-z]+)*[a-z])|[a-z]"
    words = re.findall(word_pattern, text)
    return words


def unicode_category_lists():
    result = {"letters": [], "non-separators": []}
    for i in range(sys.maxunicode):
        category = unicodedata.category(chr(i))

        if category.startswith('L'):
            result["letters"].append(chr(i))

        if not category.startswith('Z'):  # Z means separator
            result["non-separators"].append(chr(i))

    return result


if __name__ == '__main__':
    norwegian_nonsense = ("jeg- jeg er. t-skjortene er ikke. jeg...og du. "
                          "han-som-ser er her. a leve.")
    words = get_words(norwegian_nonsense)
