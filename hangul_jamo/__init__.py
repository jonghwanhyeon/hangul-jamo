# Reference: http://www.unicode.org/versions/Unicode8.0.0/ch03.pdf#G24646

from .constants import *

def is_syllable(syllable):
    index_of_syllable = ord(syllable) - BASE_OF_SYLLABLES
    return 0 <= index_of_syllable < NUMBER_OF_SYLLABLES

def is_jamo_character(character):
    return (character in LEADING_CONSONANTS) or (character in VOWELS) or (character in TRAILING_CONSONANTS)

def compose_jamo_characters(leading_consonant, vowel, trailing_consonant=None):
    try:
        index_of_leading_consonant_and_vowel = (INDEX_BY_LEADING_CONSONANT[leading_consonant] * NUMBER_OF_SYLLABLES_FOR_EACH_LEADING_CONSONANT) \
                                               + (INDEX_BY_VOWEL[vowel] * NUMBER_OF_TRAILING_CONSONANTS)
        index_of_syllable = index_of_leading_consonant_and_vowel + INDEX_BY_TRAILING_CONSONANT[trailing_consonant]
    except KeyError:
        raise ValueError('given jamo character contains invalid Hangul jamo character') from None

    return chr(BASE_OF_SYLLABLES + index_of_syllable)

def decompose_syllable(syllable):
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

def compose(text):
    output = ''

    queue = []
    def do_compose():
        output = ''

        while len(queue) > 0:
            if len(queue) == 1:
                output += queue.pop(0)
            elif 2 <= len(queue) <= 3:
                try:
                    # Case 1: `queue` contains a Hangul syllable
                    # - LEADING_CONSONANT VOWEL
                    # - LEADING_CONSONANT VOWEL TRAILING_CONSONANTS
                    leading_consonant, vowel = queue[0], queue[1]
                    trailing_consonant = queue[2] if len(queue) == 3 else None

                    output += compose_jamo_characters(leading_consonant, vowel, trailing_consonant)
                except ValueError:
                    # Case 2: `queue` does not contain any Hangul syllables
                    output += ''.join(queue)

                del queue[:]
            else: # len(queue) > 4
                if (queue[0] in LEADING_CONSONANTS) and (queue[1] in VOWELS) and (queue[2] in TRAILING_CONSONANTS) and (queue[3] in LEADING_CONSONANTS):
                    # Case 1: LEADING_CONSONANT VOWEL TRAILING_CONSONANT LEADING_CONSONANT
                    output += compose_jamo_characters(queue[0], queue[1], queue[2])
                    del queue[0:3]
                elif (queue[0] in LEADING_CONSONANTS) and (queue[1] in VOWELS) and (queue[2] in LEADING_CONSONANTS) and (queue[3] in VOWELS):
                    # Case 2: LEADING_CONSONANT VOWEL LEADING_CONSONANT VOWEL
                    output += compose_jamo_characters(queue[0], queue[1])
                    del queue[0:2]
                else:
                    # Case 3: cannot compose any Hangul syllables using first four itmes in `queue`
                    output += queue.pop(0)

        return output

    for character in text:
        if is_jamo_character(character):
            queue.append(character)
        else:
            output += do_compose()
            output += character
    output += do_compose() # to handle remaining charaters in `queue`

    return output

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
