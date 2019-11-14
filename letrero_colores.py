def vcolor(data, pattern):
    
    ret = []
    l = len(pattern)
    c = 0
    for info, value in data:
        ret.append((info, value, pattern[c]))
        c = (c + 1) % l
    return ret
