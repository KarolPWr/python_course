def get_alphabet_dict():
    """
    Tip:
        ord('a') == 97
        chr(97) == 'a'
    :return: dict(a=1, b=2, ..., z=26)
    """
    numbers = range(1, 27)
    letters = (chr(number + 96) for number in numbers)
    return dict(zip(letters, numbers))


if __name__ == '__main__':
    # Exercise: make it work
    alphabet_dict = get_alphabet_dict()
    assert alphabet_dict['a'] == 1
    assert alphabet_dict['z'] == 26
    assert list(alphabet_dict.values()) == list(range(1, 27))
