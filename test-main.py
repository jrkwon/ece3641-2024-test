def main():
    i = 10
    j = 2.21
    n = 20
    n = n/2.1
    s = 'this is Tom\'s hello'
    s1 = "this is Tom's hello"
    if i > j: 
        print('i is bigger than j')
        print('another line')

    s2 = f'i = {i}, s = {s}, s1 = {s1}, s+s1 = {s}{s1}'
    print(s2)
    # print,  hello...

    """
    this is a multi-line comment
    hello..
    hhhh
    """
    print(s + str(i) + str(j))


def test():
    scores = [90, 20, 30, 100]

    for score in scores:
        print(score)

def test2():
    roster = {
        'jaerock': 90,
        'august': 100,
        'xander': 100
    }

    print(roster['jaerock'])

test2()