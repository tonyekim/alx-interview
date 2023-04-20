#!/usr/bin/python3
'''Explains if a given data set represents a valid UTF-8 encoding'''


def validUTF8(data):
    '''
    Determines if a given data set is a valid UTF-8 encoding
    Args:
        data (list): List of integers representing the data set
    Returns:
        True if data is a valid UTF-8 encoding, otherwise False
    '''

    # Counter variable to determine the number of
    # corresponding 1's in the current byte
    num_1s = 0

    for byte in data:
        # Check for the continuability of the curent byte via bit manipulation
        if (byte >> 6) == 0b10:  # Binary representation of 2

            # Returns False if 1st byte of char
            if num_1s == 0:
                return False

            # Since its a continuation byte decrement the 1's
            num_1s -= 1
        else:
            # Return False if byte is continuous
            if num_1s != 0:
                return False

            # Checks for the byte of a single-byte char
            if (byte >> 7) == 0:
                num_1s = 0

                # Checks for 1st byte of two-byte char
            elif (byte >> 5) == 0b110:  # Binary representation 6
                num_1s = 1

                # Checks for 1st byte of three-byte char
            elif (byte >> 4) == 0b1110:  # Binary representation of 14
                num_1s = 2

                # Checks for 1st byte of four-byte char
            elif (byte >> 3) == 0b11110:  # Binary representation of 30
                num_1s = 3
            else:
                return False  # For invalid byte

    # When all bytes in the data set are a valid UTF-8 encoding
    return True