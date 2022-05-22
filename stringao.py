import jarowinkler

__ALL__ = [
    'LazyString',
    'startswith',
    'endswith']


class LazyString(str):
    def get(self, idx, dist=None):
        if not self:
            return None
        if idx < 0 or idx >= len(self):
            return None
        if dist:
            if idx + dist > len(self):
                return None
            return self[idx:idx+dist]
        return self[idx]


def startswith(source, matchwith):
    return all(map(lambda x: x[0] == x[1], zip(source, matchwith)))


def endswith(source, matchwith):
    return all(map(lambda x: x[0] == x[1], zip(source[::-1], matchwith[::-1])))



__ALL__ = [
    'metaphone',
    'dmetaphone']


def metaphone(source):
    return dmetaphone(source)[0].lower()


def check_start(s):
    return ('', '', 0)


def process_B(s, idx, last):
    if s.get(idx + 2) == '-':
        return (s[idx + 3], '', 4)
        # return (s[idx:2]+'-', '', 3) #ambil karakter sebanyak 2 dari idx
    if s.get(idx + 3) == '-':
        if s.get(idx + 1) == 'A':
            return ('*', '', 4)
        else:
            return (s[idx + 1], '', 4)
        # return (s[idx:3] + '-', '', 3)
    return (s[idx], s[idx], 1)


def process_A(s, idx, last):
    return ('*', '*', 1)


process_C = process_B
process_D = process_B
process_F = process_B
process_G = process_B
process_H = process_B
process_I = process_B
process_J = process_B
process_K = process_B
process_L = process_B
process_M = process_B
process_N = process_B
process_P = process_B
process_Q = process_B
process_R = process_B
process_S = process_B
process_T = process_B
process_U = process_B
process_V = process_B
process_W = process_B
process_Y = process_B
process_Z = process_B
process_O = process_A


def dmetaphone(source):
    source = LazyString(source.upper())
    # slavogermanic = isslavogermanic(source)
    last = len(source) - 1
    primary, secondary, index = check_start(source)
    while index < len(source):
        func = globals().get('process_{}'.format(source[index]))
        if func:
            result = func(source, index, last)
            if not result:
                index += 1
                continue
            if result[0]:
                primary += result[0]
            if result[1]:
                secondary += result[1]
            index += result[2]
        else:
            index += 1

    if primary == secondary:
        secondary = " "

    if primary == "":
        return " "

    return (primary, secondary)
