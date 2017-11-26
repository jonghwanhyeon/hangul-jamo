# Reference: http://www.unicode.org/versions/Unicode8.0.0/ch03.pdf#G24646

BASE_OF_SYLLABLES = 0xAC00

BASE_OF_LEADING_CONSONANTS = 0x1100
BASE_OF_VOWELS = 0x1161
BASE_OF_TRAILING_CONSONANTS = 0x11A7 #  one less than the beginning of the range of trailing consonants (0x11A8)

NUMBER_OF_LEADING_CONSONANTS = 19
NUMBER_OF_VOWELS = 21
NUMBER_OF_TRAILING_CONSONANTS = 28 # one more than the number of trailing consonants

NUMBER_OF_SYLLABLES_FOR_EACH_LEADING_CONSONANT = NUMBER_OF_VOWELS * NUMBER_OF_TRAILING_CONSONANTS # 가-깋 + 1
NUMBER_OF_SYLLABLES = NUMBER_OF_LEADING_CONSONANTS * NUMBER_OF_SYLLABLES_FOR_EACH_LEADING_CONSONANT

LEADING_CONSONANTS = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
INDEX_BY_LEADING_CONSONANT = { leading_consonant: index for index, leading_consonant in enumerate(LEADING_CONSONANTS) }

VOWELS = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
INDEX_BY_VOWEL = { vowel: index for index, vowel in enumerate(VOWELS) }

TRAILING_CONSONANTS = [None, 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
INDEX_BY_TRAILING_CONSONANT = { trailing_consonant: index for index, trailing_consonant in enumerate(TRAILING_CONSONANTS) }
