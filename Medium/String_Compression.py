def compress(chars):
    chars.append(33)
    if len(chars) == 1:
        return 1
    count = 0
    start = 0

    for char in range(len(chars)-1):
        count += 1
        if chars[char+1] != chars[char] or char == len(chars)-1:
            chars[start] = chars[char]
            start += 1
            if count > 1:
                count_str = ''
                while count:
                    count_str = str(count%10) + count_str
                    count = count // 10
                for c in count_str:
                    chars[start] = c
                    start += 1
            count = 0
    return start
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(compress(chars))
print(chars)



