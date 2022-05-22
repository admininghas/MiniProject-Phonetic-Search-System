import jarowinkler

__ALL__ = [
    'LazyString',
    'startswith',
    'endswith',
    'isvowel',
    # 'isslavogermanic',
    'issymbol',
    'ista',
    'ishub'
    ]


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


def isvowel(c):
    return c and c.upper() in {'A', 'E', 'I', 'O', 'U'}


# def isslavogermanic(s):
#     if not s:
#         return False
#     s = s.upper()
#     return "W" in s or "K" in s or "CZ" in s or "WITZ" in s

#sendiri
def issymbol(c):
    return c and c.upper() in "'"

def ista(c):
    return c and c.upper() in '('

def ishub(c):
    return c and c.upper() in '-'

__ALL__ = [
    'metaphone',
    'dmetaphone']

SILENT_LETTERS = {'KN', 'GN', 'PN', 'PS', 'WR'}


def metaphone(source):
    return dmetaphone(source)[0]


def check_start(s):
    if s[:2] in SILENT_LETTERS:
        return ('', '', 1)
    elif s.get(0) == 'X':
        return ('S', 'S', 1)
    return ('', '', 0)


def process_B(s, idx, last):
    if s.get(idx, 3) == 'BI-':
        return ('B', s[idx+3], 3)
    if ishub(s.get(idx+1)) and s.get(idx+2) == s[idx]:
        return ('', '' , 1)
    return ('B', 'B', (s.get(idx + 1) == 'B') + 1)


def process_D(s, idx, last):
    if s.get(idx, 2) == 'DH':
        return ('D', 'D', 2)
    if s.get(idx, 2) in {'DZ'}:
        return ('Z', 'J', 2)
    if ishub(s.get(idx+1)) and s.get(idx+2) == s[idx]:
        return ('', '' , 1)
    return ('D', 'D', (s.get(idx + 1) == 'D') + 1)


def process_F(s, idx, last):
    if s.get(idx, 3) == 'FA-':
        return ('F', '', 3)
    if idx == 0 and s.get(idx, 2) == 'FA':
        return ('F', 'F', 2)
    if ishub(s.get(idx+1)) and s.get(idx+2) == s[idx]:
        return ('', '' , 1)
    return ('F', 'F', (s.get(idx + 1) == 'F') + 1)

def process_G(s, idx, last):
    if s.get(idx + 1) == 'H':
        return ('G', 'G', 2)
    if ishub(s.get(idx+1)) and s.get(idx+2) == s[idx]:
        return ('', '' , 1)
    return ('G', 'G', (s.get(idx + 1) == 'G') + 1)



def process_H(s, idx, last):
    if ishub(s.get(idx+1)) and s.get(idx+2) == s[idx]:
        return ('', '' , 1)
    return ('H', 'H', (s.get(idx + 1) == 'H') + 1)


def process_J(s, idx, last):
    if ishub(s.get(idx+1)) and s.get(idx+2) == s[idx]:
        return ('', '' , 1)
    return ('J', 'J', (s.get(idx + 1) == 'J') + 1)


def process_K(s, idx, last):
    if ishub(s.get(idx+1)) and s.get(idx+2) == s[idx]:
        return ('', '' , 1)
    if s.get(idx, 2) == 'KH':
        return ('H', 'H', 2)
    if s.get(idx+1) == 'O':
        return ('Q', 'Q', 1)
    # if s.get(idx + 1) == 'O':
    #     return ('Q', 'K', 1)
    return (s[idx], 'Q', (s.get(idx + 1) == s[idx]) + 1)


def process_L(s, idx, last):
    if ishub(s.get(idx+1)) and s.get(idx+2) == s[idx]:
        return ('', '' , 1)
    if idx == last:
        return ('L', 'N', 1)
    return ('L', 'L', (s.get(idx + 1) == 'L') + 1)



def process_M(s, idx, last):
    if ishub(s.get(idx+1)) and s.get(idx+2) == s[idx]:
        return ('', '' , 1)
    return ('M', 'M', (s.get(idx + 1) == 'M') + 1)



def process_N(s, idx, last):
    if s.get(idx, 2) == 'NB':
        return ('N', 'M', 1)
    if s.get(idx, 2) == 'NG':
        return ('N', 'N', 2)
    if ista(s.get(idx-1)) or ista(s.get(idx-2)):
        return ('', '', 1)
    if idx == last:
        return ('N', 'M', (s.get(idx + 1) == 'N') + 1)
    if ishub(s.get(idx+1)) and s.get(idx+2) == s[idx]:
        return ('', '' , 1)
    return ('N', 'N', (s.get(idx + 1) == 'N') + 1)


def process_Q(s, idx, last):
    if ishub(s.get(idx+1)) and s.get(idx+2) == s[idx]:
        return ('', '' , 1)
    return ('Q', 'Q', (s.get(idx + 1) == s[idx]) + 1)


def process_R(s, idx, last):
    if ishub(s.get(idx+1)) and s.get(idx+2) == s[idx]:
        return ('', '' , 1)
    return ('R', 'R', (s.get(idx + 1) == s[idx]) + 1)


def process_S(s, idx, last):
    if ishub(s.get(idx+1)) and s.get(idx+2) == s[idx]:
        return ('', '' , 1)
    if s.get(idx+1) == 'H' or s.get(idx+1) == 'Y':
        return ('S', 'S', 2)
    return ('S', 'S', (s.get(idx + 1) == s[idx]) + 1)


def process_T(s, idx, last):
    if s.get(idx+1) == 'S':
        return ('S', 'S', 2)
    if s.get(idx+1) == 'H':
        return ('T', 'T', 2)
    if ista(s.get(idx+1)):
        return ('H', 'T', 1)
    if ishub(s.get(idx+1)) and s.get(idx+2) == s[idx]:
        return ('', '' , 1)
    return ('T', 'T', (s.get(idx + 1) == s[idx]) + 1)


def process_W(s, idx, last):
    if s.get(idx, 4) == 'WAL-':
        return ('W', s[idx+1], 4)
    if s.get(idx, 3) == 'WA-':
        return (s[idx+3], 'W', 3)
    if idx == 0 and s.get(idx, 2) == 'WA':
        return ('W', 'W', 2)
    if s.get(idx +1) == 'L':
        return ('L', 'L', 2)
    if ishub(s.get(idx+1)) and s.get(idx+2) == s[idx]:
        return ('', '' , 1)
    return ('W', 'W', (s.get(idx + 1) == s[idx]) + 1)


def process_Y(s, idx, last):
    if ishub(s.get(idx+1)) and s.get(idx+2) == s[idx]:
        return ('', '' , 1)
    return ('Y', 'Y', (s.get(idx + 1) == s[idx]) + 1)


def process_Z(s, idx, last):
    if ishub(s.get(idx+1)) and s.get(idx+2) == s[idx]:
        return ('', '' , 1)
    return ('Z', 'J', (s.get(idx + 1) == s[idx]) + 1)


def process_A(s, idx, last):
    if idx == 0 and not issymbol(s.get(idx+1)):
        return ('A', 'A', (s.get(idx + 1) == 'A') + 1)
    elif (idx == 0 and issymbol(s.get(idx+1))) or (idx == 1 and issymbol(s.get(idx-1))):
        return ('X', 'A', (s.get(idx + 1) == 'A') + 1)
    if s.get(idx-1) == 'U' or s.get(idx+1) == 'U':
        return ('W', 'W', 1)
    if s.get(idx+1) == 'I' or s.get(idx,2) == 'AY':
        return ('Y', 'Y', 2)
    if (issymbol(s.get(idx-1))) or (issymbol(s.get(idx+1)) and not isvowel(s.get(idx+2))):
        return ('X', '', 1)
    elif issymbol(s.get(idx+1)) and s.get(idx+2) == 'A':
        return ('', '', 1)
    if ista(s.get(idx-1)):
        return ('', '', 1)
    if idx == last:
        return ('', '',1)
    if ishub(s.get(idx+1)) and s.get(idx+2) == s[idx]:
        return ('', '' , 1)
    # return ('0', '0', (s.get(idx + 1) == s[idx]) + 1)

def process_I(s, idx, last):
    if idx == 0:
        return ('I', 'X', (s.get(idx + 1) == 'I') + 1)
    if issymbol(s.get(idx-1)) or (issymbol(s.get(idx+1)) and not isvowel(s.get(idx+2))):
        return ('X', '', 1)


def process_U(s, idx, last):
    if idx == 0:
        return ('U', 'X', (s.get(idx + 1) == 'U') + 1)
    if issymbol(s.get(idx-1)) or issymbol(s.get(idx+1)):
        return ('X', '', 1)


def process_O(s, idx, last):
    if idx == last:
        return ('', '', 1)
    if s.get(idx-1) == 'U' or s.get(idx+1) == 'U':
        return ('W', 'W', 1)
    if s.get(idx+1) == 'I' or s.get(idx,2) == 'OY':
        return ('Y', '', 2)
    # return ('0', '0', (s.get(idx + 1) == s[idx]) + 1)


def process_symbol(s, idx, last):
    if issymbol(s.get(idx)):
        return ('X', 'X', 1)
    return ('', '', (s.get(idx + 1) == s[idx]) + 1)


process_V = process_F
process_P = process_F


def dmetaphone(source):
    source = LazyString(source.upper())
    # slavogermanic = isslavogermanic(source)
    last = len(source) - 1
    primary, secondary, index = check_start(source)
    while index < len(source) and len(primary) <= 4:
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