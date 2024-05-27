 = start
    while start < end:

        if last_index[s[start]] > result:
            result = last_index[s[start]]
        start += 1
    return result