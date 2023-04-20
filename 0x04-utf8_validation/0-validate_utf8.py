def validUTF8(data):
    skip = 0
    n = len(data)
    for i in range(n):
        if skip > 0:
            skip -= 1
            continue
        if data[i] < 0 or data[i] > 255:
            return False
        if data[i] <= 0x7F:
            # 1-byte encoding (0xxxxxxx)
            pass
        elif data[i] <= 0xDF and i+1 < n and 0x80 <= data[i+1] <= 0xBF:
            # 2-byte encoding (110xxxxx 10xxxxxx)
            skip = 1
        elif data[i] <= 0xEF and i+2 < n and 0x80 <= data[i+1] <= 0xBF and 0x80 <= data[i+2] <= 0xBF:
            # 3-byte encoding (1110xxxx 10xxxxxx 10xxxxxx)
            skip = 2
        elif data[i] <= 0xF4 and i+3 < n and 0x80 <= data[i+1] <= 0xBF and 0x80 <= data[i+2] <= 0xBF and 0x80 <= data[i+3] <= 0xBF:
            # 4-byte encoding (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
            skip = 3
        else:
            return False
    return True
