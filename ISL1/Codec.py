DELIMITER = ' '


def str_to_codes(s: str):
    return DELIMITER.join(str(ord(ch)) for ch in s)


def codes_to_str(s: str):
    return ''.join(chr(int(code)) for code in s.split(DELIMITER))


def encrypt(s: str, key: int):
    # encoding logic

    return ''.join(chr(ord(ch_code) + key) for ch_code in s)


def decrypt(s: str, key: int):
    # decoding logic

    return encrypt(s, key * -1)
