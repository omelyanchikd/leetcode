def count_ones(s):
    count = 0
    for c in s:
        if c == '1':
            count += 1
    return count


def shortestBeautifulSubstring(s: str, k: int) -> str:
    ones = count_ones(s)
    if ones < k:
        return ""
    i = 0
    str_len = k
    min_len = -1
    beautiful_strings = []
    while True:
        if i + str_len > len(s):
            if min_len > - 1:
                break
            i = 0
            str_len += 1
        substr = s[i:(i + str_len)]
        if (count_ones(substr) == k):
            beautiful_strings.append(substr)
            min_len = len(substr)
        i += 1
    beautiful_strings.sort()
    return beautiful_strings[0]

if __name__ == '__main__':
    s = "1011"
    k = 2
    print(shortestBeautifulSubstring(s, k))
