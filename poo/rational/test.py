
from rational import Rational

test_cases = (
    '1/2',
    '+123/456',
    '45/+43',
    '+43/-78',
    '-123/231',
    '143/-2',
    '-1/-244',
    '----1/-32',
    'ab123/45xx',
    '123/43aa',
    '1.5/3',
    '4/3.5',
    '2.3/1.4',
    'a/b',
    'abc/xyz',
    '/',
    '1/',
    '/3',
)

for s in test_cases:
    try:
        r = Rational(s)
        print('Success:', s)
    except Exception as error:
        print('Error  :', s)
        

test_cases = (
    (1,2),
    (-1,2),
    (13,-2),
    (-143,-231),
    (+12,-2),
    (-86,+254),
    (123, None),
    (-433, None),
    (1854, 0),
)

for num, den in test_cases:
    try:
        r = Rational(num, den)
        print('Success:', r)
    except Exception as error:
        print('Error  :', (num,den))
        

