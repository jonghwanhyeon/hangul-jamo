# Reference: http://www.unicode.org/versions/Unicode8.0.0/ch03.pdf#G24646

from .constants import *

def is_hangul_syllable(syllable):
    index_of_syllable = ord(syllable) - BASE_OF_SYLLABLES
    return 0 <= index_of_syllable < NUMBER_OF_SYLLABLES
def decompose_hangul_syllable(syllable):
    if not is_hangul_syllable(syllable):
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
