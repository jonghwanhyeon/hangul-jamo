from hangul_jamo import is_syllable, is_jamo_character, compose_jamo_characters, decompose_syllable, compose, decompose

# 1. CHECKING HANGUL SYLLABLES
print('is_syllable("가") ==', is_syllable('가'))
# is_syllable("가") == True
print('is_syllable("갛") ==', is_syllable('갛'))
# is_syllable("갛") == True
print('is_syllable("ㄱ") ==', is_syllable('ㄱ'))
# is_syllable("ㄱ") == False

# 2. CHECKING HANGUL JAMO CHARACTERS
print('is_jamo_character("ㄱ") ==', is_jamo_character('ㄱ'))
# is_jamo_character("ㄱ") == True
print('is_jamo_character("ㅏ") ==', is_jamo_character('ㅏ'))
# is_jamo_character("ㅏ") == True
print('is_jamo_character("ㄳ") ==', is_jamo_character('ㄳ'))
# is_jamo_character("ㄳ") == True
print('is_jamo_character("갃") ==', is_jamo_character('갃'))
# is_jamo_character("갃") == False

# 3. COMPOSING HANGUL JAMO CHARACTERS
print('compose_jamo_characters("ㄱ", "ㅏ", None) ==', compose_jamo_characters('ㄱ', 'ㅏ', None))
# compose_jamo_characters("ㄱ", "ㅏ", None) == 가
print('compose_jamo_characters("ㄱ", "ㅏ") ==', compose_jamo_characters('ㄱ', 'ㅏ'))
# compose_jamo_characters("ㄱ", "ㅏ") == 가
print('compose_jamo_characters("ㄱ", "ㅏ", "ㅎ") ==', compose_jamo_characters('ㄱ', 'ㅏ', 'ㅎ'))
# compose_jamo_characters("ㄱ", "ㅏ", "ㅎ") == 갛

# 4. DECOMPOSING HANGUL SYLLABLES
print('decompose_syllable("가") ==', decompose_syllable('가'))
# decompose_syllable("가") == ('ㄱ', 'ㅏ', None)
print('decompose_syllable("갛") ==', decompose_syllable('갛'))
# decompose_syllable("갛") == ('ㄱ', 'ㅏ', 'ㅎ')

# 4.1. USING UNPACKING ARGUMENTS OPERATOR *
print('compose_jamo_characters(*decompose_syllable("가")) ==', compose_jamo_characters(*decompose_syllable('가')))
# compose_jamo_characters(*decompose_syllable("가")) == 가
print('compose_jamo_characters(*decompose_syllable("갛")) ==', compose_jamo_characters(*decompose_syllable('갛')))
# compose_jamo_characters(*decompose_syllable("갛")) == 갛

# 5. COMPOSING TEXT
print('compose("ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ! Hello!") ==', compose('ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ! Hello!'))
# compose("ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ! Hello!") == 안녕하세요! Hello!

# 6. DECOMPOSING TEXT
print('decompose("안녕하세요! Hello!") ==', decompose('안녕하세요! Hello!'))
# decompose("안녕하세요! Hello!") == ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ! Hello!
