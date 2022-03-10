"""
Introduction to binary, ascii, unicode

Count in Decimal (0-15)
Learn to count to binary from 0 - 15 (0000-1111)
(8 4 2 1)
(0 0 0 1) = 1
(0 0 1 0) = 2
(0 0 1 1) = 3
(0 1 0 0) = 4
(0 1 0 1) = 5
(0 1 1 0) = 6
(1 0 0 0) = 8
(1 1 1 0) = 14
Learn to count in hex from 0 - 15 (0-F) and 16 (10)
Dec  Hex  Bin
 1 =  1 = 0000 0001
 2 =  2 = 0000 0010
 9 =  9 = 0000 1001
10 =  A = 0000 1010
11 =  B = 0000 1011
15 =  F = 0000 1111
16 = 10 = 0001 0000
Hex  FF = 1111 1111
"""


def convert_engine(phrase, format):
    print(phrase)
    phrase_encode = phrase.encode(format, "replace")
    print(phrase_encode.decode(format))
    print(format.upper() + " ", phrase_encode)

    print("Hexadecimal ", end=" ")
    for byte in phrase_encode:
        print(hex(byte), end=" \\ ")
    print()

    print("Binary ", end=" ")
    for byte in phrase_encode:
        print(bin(byte), end=" \\ ")
    print()

    print("Integer ", end=" ")
    for byte in phrase_encode:
        print(byte, end=" \\ ")
    print()


def convert(phrase):
    # http://www.fileformat.info/info/charset/US-ASCII/list.htm
    convert_engine(phrase, "ascii")
    print()
    # http://www.fileformat.info/info/charset/UTF-8/list.htm
    convert_engine(phrase, "utf-8")
    print()
    # http://www.fileformat.info/info/charset/UTF-16/list.htm
    # convert_engine(phrase, "utf-16")
    # print()


def main():
    # whitespace = ' \t\n\r\v\f'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_letters = ascii_lowercase + ascii_uppercase
    digits = '0123456789'
    hexdigits = digits + 'abcdef' + 'ABCDEF'
    octdigits = '01234567'
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    # printable = digits + ascii_letters + punctuation + whitespace

    convert(ascii_lowercase[0:4])
    convert(ascii_uppercase[0:4])
    # convert(ascii_letters)
    convert(digits)
    convert(punctuation)
    # convert(printable)

    monkey_head = "ʕ༼ ◕_◕ ༽ʔ"
    monkey_chin = "  \\_⎏_/ "
    monkey_body = "  ++1++ "
    monkey_legs = "   ⌋ ⌊  "
    monkey = monkey_head + monkey_chin + monkey_body + monkey_legs
    convert(monkey_head)
    # convert(monkey)

    pictograms = "象形字 xiàngxíngzì"
    ideograms = "指事字 zhǐshìzì"
    idea_characters = "会意字 / 會意字 huìyìzì"
    rebus = "假借字 jiǎjièzì"
    chinese_characters = pictograms + ideograms + idea_characters + rebus
    convert(pictograms)
    # convert(chinese_characters)

    apple = u"🍏"
    fruits = "🍊🍌🍉"
    sports = "🏄🏼‍♂️🏄🏽‍♀️🚣🏻⛹🏾"
    emojis = fruits + sports
    convert(apple)
    # convert(emojis)
