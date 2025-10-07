import re

def validateRA(ra):
    if len(ra) != 20:
        return False
    if not ra.startswith('RA'):
        return False
    if not ra[2:].isdigit():
        return False
    return True


def generatePassword_v1(ra):
    if not validateRA(ra):
        return 'INVALID DATA'
    
    return str(int(ra[2:]))


def generatePassword_v2(ra):
    if not validateRA(ra):
        return 'INVALID DATA'

    for i in range(2, len(ra)):
        if ra[i] != '0':
            return ra[i:]
    return ''


def generatePassword_v3(ra):
    m = re.match(r'^RA0*\d+$', ra)
    if m is None:
        return 'INVALID DATA'
        
    return m.groups()[0]

test_cases = int(input())
while test_cases > 0:
    test_cases -= 1
    
    ra = input().strip()
    print(generatePassword_v2(ra))
    
