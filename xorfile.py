#!/usr/bin/python

import sys
from xorcipher import xor_byte_array

try:

    if len(sys.argv) < 4:
        raise ValueError(
            "Missing arguments : input_file output_file key")

    input_file = open(sys.argv[1], 'rb')
    output_file = open(sys.argv[2], 'wb')

    # the cast into bytearray is for windows/linux compatibility (no binary mode under unix/linux).
    data = xor_byte_array(bytearray(input_file.read()), sys.argv[3])

    output_file.write(data)

    input_file.close()
    output_file.close()

except ValueError as ve:
        print(ve)

except OSError as os:
        print(os)

