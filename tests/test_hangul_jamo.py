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
    assert compose('ㄷㅐㅎㅏㄴㅁㅣㄴㄱㅜㄱㅇㅡㄴ ㅁㅣㄴㅈㅜㄱㅗㅇㅎㅘㄱㅜㄱㅇㅣㄷㅏ.') == '대한민국은 민주공화국이다.'
    assert compose('Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof') == 'Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof'

def test_decompose():
    assert decompose('대한민국은 민주공화국이다.') == 'ㄷㅐㅎㅏㄴㅁㅣㄴㄱㅜㄱㅇㅡㄴ ㅁㅣㄴㅈㅜㄱㅗㅇㅎㅘㄱㅜㄱㅇㅣㄷㅏ.'
    assert decompose('Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof') == 'Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof'
