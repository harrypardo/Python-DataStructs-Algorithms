
def bin_search(list, to_find):
    x = 0
    y = len(list)

    while x <= y:
        m = (x + y ) / 2
        m = int(m)
        if list[m] == to_find:
            return m
        if list[m] > to_find:
            y = m - 1
        else:
            x = m + 1
    return -1


aui = [2,26,31,33,35,57, 26]


print(bin_search(aui, 2))