""" Day 3 """

def move(pos):
    x,y = 0, 0
    directionX = {'L':-1, 'R':1}
    directionY = {'U':1, 'D':-1}
    for step in pos:
        yield (x, y)
        curr, nex = step[0], int(step[1:])
        for i in range(nex):
            if curr in directionX.keys():
                x += directionX[curr]
            else:
                y += directionY[curr]
    yield (x,y)


def partOne(lines):
    result = 0
    resultDict = {}
    for i, line in enumerate(lines):
        print(line)
        for x,y in move(line):
            if (x,y) not in resultDict.keys():
                resultDict[(x,y)] = i
            if (x or y) and resultDict[(x,y)] != i:
                man = abs(x) + abs(y)
                if result == 0 or result > man:
                    result = man
    return result

if __name__ == '__main__':
    with open('input.txt', 'rt') as f_obj:
        lines = []
        for line in f_obj:
            lines.append(line.split(',')[:-1])
    print(partOne(lines))
    print(lines)

