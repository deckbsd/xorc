#!/usr/bin/python

from xorcipher import *


text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 |@#{[^{}°)-_$^[]"
bytes_data = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 @:,;'
key = "thisisatest"

result = xor_char_array(text, key)

print("text XOR")
print("crypt result :")
print(result)

print("\n")

print("uncrypt result :")
print(xor_char_array(result, key))

print("\n\n")

print("bytes XOR")
result_bytes = xor_byte_array(bytes_data, key)

print("crypt result :")
print(result_bytes)

print("\n")

print("uncrypt result :")
print(xor_byte_array(result_bytes, key))