import sys

def findLoopStart(s, c):
    st, nd = 0, 0
    j = 0
    for x in range(c, -1, -1):
        if s[x]==']': nd += 1
        elif s[x]=='[':
            st += 1
            j = x
        if st==nd: break
    return j

def findLoopEnd(s, c):
    st, nd = 0, 0
    j = 0
    for x in range(c, len(s)):
        if s[x]=='[': st += 1
        elif s[x]==']':
            nd += 1
            j = x
        if st==nd: break
    return j

def findLoops(s):
    indexes = {}
    for x in range(len(s)):
        if s[x] == '[':
            indexes[x] = findLoopEnd(s, x)
        elif s[x] == ']':
            indexes[x] = findLoopStart(s, x)
    return indexes

def getFileData(filename):
    f = open(filename)
    lines = f.readlines()
    return ''.join(lines)


def main(s):
    arr = 30000 * [0]
    i, c = 0, 0

    indexes = findLoops(s)

    while c<=len(s)-1:
        if s[c] == '>': i+=1
        elif s[c] == '<': i-=1
        elif s[c] == '+': arr[i] += 1
        elif s[c] == '-': arr[i] -= 1
        elif s[c] == '.': print(chr(arr[i]), end='')
        elif s[c] == ',': arr[i] = ord(input('> '))

        elif s[c] == '[':
            if arr[i] == 0:
                c = indexes[c]
        elif s[c] == ']':
            if arr[i] != 0:
                c = indexes[c]
        c += 1


if __name__ == '__main__':
    args = sys.argv
    try:
        if args[1] == '-f':
            filename = args[2]
            main(getFileData(filename))
        elif args[1] == '-l':
            main(args[2])
        else:
            print('Invalid flag')
    except IndexError:
        print('Invalid usage')