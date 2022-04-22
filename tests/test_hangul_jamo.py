import pytest

from hangul_jamo import is_syllable, is_jamo_character, compose_jamo_characters, decompose_syllable, compose, decompose

def test_is_syllable():
    assert is_syllable('가')
    assert is_syllable('갛')
    assert is_syllable('힣')

def test_is_not_syllable():
    assert not is_syllable('0')
    assert not is_syllable('A')
    assert not is_syllable('a')

def test_is_jamo_character():
    assert is_jamo_character('ㄱ')
    assert is_jamo_character('ㅏ')
    assert is_jamo_character('ㄳ')
    assert is_jamo_character(None)

def test_is_not_jamo_character():
    assert not is_jamo_character('0')
    assert not is_jamo_character('A')
    assert not is_jamo_character('a')

def test_compose_jamo_characters():
    assert compose_jamo_characters('ㄱ', 'ㅏ') == '가'
    assert compose_jamo_characters('ㄱ', 'ㅏ', None) == '가'
    assert compose_jamo_characters('ㄱ', 'ㅏ', 'ㅎ') == '갛'

def test_decompose_syllable():
    assert decompose_syllable('가') == ('ㄱ', 'ㅏ', None)
    assert decompose_syllable('갛') == ('ㄱ', 'ㅏ', 'ㅎ')

def test_compose():
    assert compose('') == ''
    assert compose('0') == '0'
    assert compose('a') == 'a'
    assert compose('ㄱ') == 'ㄱ'
    assert compose('ㅏ') == 'ㅏ'

    assert compose('ㄱㄱ') == 'ㄱㄱ'
    assert compose('ㅏㅏ') == 'ㅏㅏ'
    assert compose('ㅏㄱ') == 'ㅏㄱ'

    assert compose('ㄱㅏ') == '가'
    assert compose('aㄱㅏ') == 'a가'
    assert compose('aaㄱㅏ') == 'aa가'
    assert compose('ㄱㅏa') == '가a'
    assert compose('ㄱㅏaa') == '가aa'
    assert compose('aㄱㅏa') == 'a가a'
    assert compose('aㄱㅏaa') == 'a가aa'
    assert compose('aaㄱㅏa') == 'aa가a'
    assert compose('aaㄱㅏaa') == 'aa가aa'
    assert compose('ㅇㄱㅏ') == 'ㅇ가'
    assert compose('ㅇㅇㄱㅏ') == 'ㅇㅇ가'

    assert compose('ㄱㅏㄴ') == '간'
    assert compose('aㄱㅏㄴ') == 'a간'
    assert compose('aaㄱㅏㄴ') == 'aa간'
    assert compose('ㄱㅏㄴa') == '간a'
    assert compose('ㄱㅏㄴaa') == '간aa'
    assert compose('aㄱㅏㄴa') == 'a간a'
    assert compose('aㄱㅏㄴaa') == 'a간aa'
    assert compose('aaㄱㅏㄴa') == 'aa간a'
    assert compose('aaㄱㅏㄴaa') == 'aa간aa'
    assert compose('ㅇㄱㅏㄴ') == 'ㅇ간'
    assert compose('ㅇㅇㄱㅏㄴ') == 'ㅇㅇ간'
    assert compose('ㄱㅏㄴㅇ') == '간ㅇ'
    assert compose('ㄱㅏㄴㅇㅇ') == '간ㅇㅇ'
    assert compose('ㅇㄱㅏㄴㅇ') == 'ㅇ간ㅇ'
    assert compose('ㅇㄱㅏㄴㅇㅇ') == 'ㅇ간ㅇㅇ'
    assert compose('ㅇㅇㄱㅏㄴㅇ') == 'ㅇㅇ간ㅇ'
    assert compose('ㅇㅇㄱㅏㄴㅇㅇ') == 'ㅇㅇ간ㅇㅇ'

    assert compose('ㄱㅏㅓㄱ') == '가ㅓㄱ'
    assert compose('aㄱㅏㅓㄱ') == 'a가ㅓㄱ'
    assert compose('aaㄱㅏㅓㄱ') == 'aa가ㅓㄱ'
    assert compose('ㄱㅏㅓㄱa') == '가ㅓㄱa'
    assert compose('ㄱㅏㅓㄱaa') == '가ㅓㄱaa'
    assert compose('aㄱㅏㅓㄱa') == 'a가ㅓㄱa'
    assert compose('aㄱㅏㅓㄱaa') == 'a가ㅓㄱaa'
    assert compose('aaㄱㅏㅓㄱa') == 'aa가ㅓㄱa'
    assert compose('aaㄱㅏㅓㄱaa') == 'aa가ㅓㄱaa'

    assert compose('ㄷㅐㅎㅏㄴㅁㅣㄴㄱㅜㄱㅇㅡㄴ ㅁㅣㄴㅈㅜㄱㅗㅇㅎㅘㄱㅜㄱㅇㅣㄷㅏ.') == '대한민국은 민주공화국이다.'
    assert compose('Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof') == 'Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof'

    assert compose('ㅇㅏ ㄴㅏㄴㅡㄴ ㄱㅡㅓㄴㄷㅔ') == '아 나는 그ㅓㄴ데'

def test_decompose():
    assert decompose('대한민국은 민주공화국이다.') == 'ㄷㅐㅎㅏㄴㅁㅣㄴㄱㅜㄱㅇㅡㄴ ㅁㅣㄴㅈㅜㄱㅗㅇㅎㅘㄱㅜㄱㅇㅣㄷㅏ.'
    assert decompose('Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof') == 'Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof'
