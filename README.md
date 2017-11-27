# hangul-jamo
A library to compose and decompose Hangul syllables using Hangul jamo characters

## Requirements
- Python 3+

## Installation
  pip install hangul-jamo

## Usage
    >>> import hangul_jamo
    >>> print(hangul_jamo.decompose('Jonghwan님, 안녕하세요!'))
    Jonghwanㄴㅣㅁ, ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ!
    >>> print(hangul_jamo.compose('Jonghwanㄴㅣㅁ, ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ!'))
    Jonghwan님, 안녕하세요!

## API
### hangul_jamo.is_syllable(syllable)
Checks whether `syllable` is a Hangul syllable or not. Returns the evaluation as `bool`
#### Parameter
- `syllable`: any character to check

### hangul_jamo.is_jamo_character(character)
Checks whether `character` is a Hangul jamo character or not. Returns the evaluation as `bool`
#### Parameter
- `character`: any character to check

### hangul_jamo.compose_jamo_characters(leading_consonant, vowel, trailing_consonant=None)
Composes a Hangul syllable using `leading_consonant`, `vowel`, and `trailing_consonant`. Returns the composed Hangul syllable.
#### Parameters
- `leading_consonant`: Hangul leading consonant as known as choseng
- `vowel`: Hangul vowel as known as jongseong
- `trailing_consonant`: Hangul trailing consonant as known as jungseong (optional)

### hangul_jamo.decompose_syllable(syllable)
Decomposes given Hangul `syllable` into Hangul jamo characters. Returns the decomposed Hangul jamo characters as 3-tuple `(leading consonant, vowel, trailing consonant)`. Returned trailing consonant can be None.
#### Parameter
- `syllable`: Hangul syllable to decompose

### hangul_jamo.compose(text)
Composes Hangul jamo characters within `text` into Hangul syllables. Characters other than Hangul jamo are ignored. Returns the composed text.
#### Parameter
- `text`: text containing Hangul jamo characters

### hangul_jamo.decompose(text)
Decomposes Hangul syllables within `text` into Hangul jamo characters. Characters other than Hangul syllable are ignored. Returns the decomposed text.
#### Parameter
- `text`: text containing Hangul syllables

## Reference
- [http://www.unicode.org/versions/Unicode8.0.0/ch03.pdf#G24646](http://www.unicode.org/versions/Unicode8.0.0/ch03.pdf#G24646)
