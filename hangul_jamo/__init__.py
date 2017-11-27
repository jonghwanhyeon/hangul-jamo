# Reference: http://www.unicode.org/versions/Unicode8.0.0/ch03.pdf#G24646

from .constants import *

def is_syllable(syllable):
    index_of_syllable = ord(syllable) - BASE_OF_SYLLABLES
    return 0 <= index_of_syllable < NUMBER_OF_SYLLABLES

def compose_jamo_characters(leading_consonant, vowel, trailing_consonant=None):
    try:
        index_of_leading_consonant_and_vowel = (INDEX_BY_LEADING_CONSONANT[leading_consonant] * NUMBER_OF_SYLLABLES_FOR_EACH_LEADING_CONSONANT) \
                                               + (INDEX_BY_VOWEL[vowel] * NUMBER_OF_TRAILING_CONSONANTS)
        index_of_syllable = index_of_leading_consonant_and_vowel + INDEX_BY_TRAILING_CONSONANT[trailing_consonant]
    except KeyError:
        raise ValueError('invalid `jamo_sequence`') from None

    return chr(BASE_OF_SYLLABLES + index_of_syllable)

def decompose_syllable(syllable):
    if not is_syllable(syllable):
        raise ValueError('`syllable` is not a hangul syllable')

    index_of_syllable = ord(syllable) - BASE_OF_SYLLABLES

    index_of_leading_consonant = index_of_syllable // NUMBER_OF_SYLLABLES_FOR_EACH_LEADING_CONSONANT
    index_of_vowel = (index_of_syllable % NUMBER_OF_SYLLABLES_FOR_EACH_LEADING_CONSONANT) // NUMBER_OF_TRAILING_CONSONANTS
    index_of_trailing_consonant = index_of_syllable % NUMBER_OF_TRAILING_CONSONANTS

    return (
        LEADING_CONSONANTS[index_of_leading_consonant],
        VOWELS[index_of_vowel],
        TRAILING_CONSONANTS[index_of_trailing_consonant]
    )
def decompose(text):
    output = ''

    for character in text:
        if is_syllable(character):
            leading_consonant, vowel, trailing_consonant = decompose_syllable(character)
            output += leading_consonant
            output += vowel
            output += trailing_consonant or ''
        else:
            output += character

    return output
