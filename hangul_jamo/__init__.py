# Reference: http://www.unicode.org/versions/Unicode8.0.0/ch03.pdf#G24646

from typing import NamedTuple, Optional

from hangul_jamo.constants import *
from hangul_jamo.utils import consume, ngram


class Syllable(NamedTuple):
    leading_consonant: str
    vowel: str
    trailing_consonant: Optional[str]


def is_syllable(syllable: str) -> bool:
    index_of_syllable = ord(syllable) - BASE_OF_SYLLABLES
    return 0 <= index_of_syllable < NUMBER_OF_SYLLABLES

def is_jamo_character(character: str) -> bool:
    return (character in LEADING_CONSONANTS) or (character in VOWELS) or (character in TRAILING_CONSONANTS)

def compose_jamo_characters(leading_consonant: str, vowel: str, trailing_consonant: Optional[str] = None) -> str:
    try:
        index_of_leading_consonant_and_vowel = (INDEX_BY_LEADING_CONSONANT[leading_consonant] * NUMBER_OF_SYLLABLES_FOR_EACH_LEADING_CONSONANT) \
                                               + (INDEX_BY_VOWEL[vowel] * NUMBER_OF_TRAILING_CONSONANTS)
        index_of_syllable = index_of_leading_consonant_and_vowel + INDEX_BY_TRAILING_CONSONANT[trailing_consonant]
    except KeyError:
        raise ValueError('given jamo character contains invalid Hangul jamo character') from None

    return chr(BASE_OF_SYLLABLES + index_of_syllable)

def decompose_syllable(syllable: str) -> Syllable:
    if not is_syllable(syllable):
        raise ValueError('`syllable` is not a Hangul syllable')

    index_of_syllable = ord(syllable) - BASE_OF_SYLLABLES

    index_of_leading_consonant = index_of_syllable // NUMBER_OF_SYLLABLES_FOR_EACH_LEADING_CONSONANT
    index_of_vowel = (index_of_syllable % NUMBER_OF_SYLLABLES_FOR_EACH_LEADING_CONSONANT) // NUMBER_OF_TRAILING_CONSONANTS
    index_of_trailing_consonant = index_of_syllable % NUMBER_OF_TRAILING_CONSONANTS

    return (
        LEADING_CONSONANTS[index_of_leading_consonant],
        VOWELS[index_of_vowel],
        TRAILING_CONSONANTS[index_of_trailing_consonant]
    )

def compose(text: str) -> str:
    output = ''

    iterator = ngram(text, n=4, pad_right=True)
    for first, second, third, fourth in iterator:
        if (first in LEADING_CONSONANTS) and (second in VOWELS) and (third in LEADING_CONSONANTS) and (fourth in VOWELS):
            output += compose_jamo_characters(first, second)
            consume(iterator, 1)
        elif (first in LEADING_CONSONANTS) and (second in VOWELS) and (third in TRAILING_CONSONANTS):
            output += compose_jamo_characters(first, second, third)
            consume(iterator, 2)
        elif (first in LEADING_CONSONANTS) and (second in VOWELS):
            output += compose_jamo_characters(first, second)
            consume(iterator, 1)
        else:
            output += first

    return output

def decompose(text: str) -> str:
    output = ''

    for character in text:
        if is_syllable(character):
            leading_consonant, vowel, trailing_consonant = decompose_syllable(character)
            output += leading_consonant
            output += vowel
            output += trailing_consonant if trailing_consonant is not None else ''
        else:
            output += character

    return output
