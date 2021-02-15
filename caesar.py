def encode(text, k):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]
        char_num = ord(char)
        sum_char = ''

        if 65 <= char_num <= 90:
            if char_num + k > 90:
                sum_char = chr(char_num + k - 26)
            else:
                sum_char = chr(char_num + k)
        elif 97 <= char_num <= 122:
            if char_num + k > 122:
                sum_char = chr(char_num + k - 26)
            else:
                sum_char = chr(char_num + k)
        else:
            sum_char = char

        result += sum_char

    return result


def decode(text, k):

    result = ""
    # traverse text
    for i in range(len(text)):
        char = text[i]
        char_num = ord(char)
        sum_char = ''

        if 65 <= char_num <= 90:
            if char_num - k < 65:
                sum_char = chr(char_num - k + 26)
            else:
                sum_char = chr(char_num - k)
        elif 97 <= char_num <= 122:
            if char_num - k < 97:
                sum_char = chr(char_num - k + 26)
            else:
                sum_char = chr(char_num - k)
        else:
            sum_char = char

        result += sum_char

    return result
