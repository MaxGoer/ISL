DELIMITER = ' '


def encrypt(s: str, key: int):
    # encoding logic

    return ''.join(chr(ord(ch_code) + key) for ch_code in s)


def decrypt(s: str, key: int):
    # decoding logic

    return encrypt(s, key * -1)
