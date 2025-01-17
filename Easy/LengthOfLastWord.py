class Solution(object):
    def lengthOfLastWord(s):

        slist = s.split()
        lastword = slist[-1]
        if len(lastword) == 0:
            return 0
        else:
            return len(lastword)

    if __name__ == '__main__':
        sentence = "luffy is still joyboy"
        print(lengthOfLastWord(sentence))
