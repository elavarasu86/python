class Solution(object):
    def convert( s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        L = [''] * numRows
        index, step = 0, 1
        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(L)

    if __name__ == '__main__':
        s='elavarasu'
        numRows=3
        print(convert(s,numRows))
