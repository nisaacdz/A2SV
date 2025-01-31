def swap_case(s):
    result = []
    for c in s:
        if 'A' <= c <= 'Z':
            result.append(chr(ord(c) + (ord('a') - ord('A'))))
        elif 'a' <= c <= 'z':
            result.append(chr(ord(c) - (ord('a') - ord('A'))))
        else:
            result.append(c)
    return ''.join(result)
