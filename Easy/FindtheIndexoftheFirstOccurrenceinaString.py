class Solution:

    def strStr(haystack, needle):
        position = 0
        if needle in haystack:
            a = haystack.split(needle)
            position = len(a[0])

            return position
        else:
            return -1

    if __name__ == '__main__':
        haystack = 'leetcode'
        needle = 'leeto'
        print(strStr(haystack, needle))
