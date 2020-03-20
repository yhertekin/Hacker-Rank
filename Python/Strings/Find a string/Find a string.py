def count_substring(string, sub_string):
    count = a = 0
    while sub_string in string[a:]:
        a += string[a:].find(sub_string)+1
        count += 1
    return count

    # return string.count(sub_string)
