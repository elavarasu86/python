from tempfile import tempdir


class Solution:
    def longestCommonPrefix(strs: list[str]):
        strs.sort()
        firstvalue = strs[0]
        lastvalue = strs[-1]
        inc = 0
        comm = ''
        if (len(firstvalue) == 0 and len(lastvalue) == 0):
            return ""
        else:
            while  len(firstvalue) > inc and len(lastvalue) > inc and (firstvalue[inc] == lastvalue[inc]):

                if firstvalue[inc] == lastvalue[inc]:
                    comm = comm + firstvalue[inc]
                else:
                    break
                inc = inc + 1
        return comm

    if __name__ == '__main__':
        mylist = ["a"]

        print(longestCommonPrefix(mylist))
