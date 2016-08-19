#!/usr/bin/python


def xor_char_array(text, key):
    output = ""
    size_t = len(key)

    for index in range(len(text)):
        output += chr(ord(text[index]) ^ ord(key[index % size_t]))

    return output


def xor_byte_array(bytes_array, key):
    output = bytearray()
    size_t = len(key)

    for index in range(len(bytes_array)):
        output.append(bytes_array[index] ^ ord(key[index % size_t]))

    return output




