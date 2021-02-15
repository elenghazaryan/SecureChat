def compress(data):
    encoding = ''
    prev_char = ''
    count = 1

    print(data)

    if not data:
        return ''

    for char in data:
        # If the prev and current don't match
        if char != prev_char:
            # then add the count and character to our encoding
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Or increment our counter
            # if the characters do match
            count += 1
        print(count, "\n")
    else:
        # Finish off the encoding
        encoding += str(count) + prev_char
        print(encoding)
        return encoding


def decompress(data):
    decode = ''
    count = ''
    for char in data:
        # If the character is numerical
        if char.isdigit():
            # append it to our count
            count += char
        else:
            # Otherwise we've seen a non-numerical
            # character and need to expand it for
            # the decoding
            decode += str(char * int(count))
            count = ''
    return decode
