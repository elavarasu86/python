class Solution:
    def isValid(s: str):
        sta = []
        open_case = {'(','{','['}
        close_case = {')','}',']'}
        if len(s) % 2 == 1:
            return False
        boolean = False
        inc = 0
        for case in s:
            if (case in open_case):
                sta.append(case)
                boolean = False
            elif (case in close_case):
                if len(sta) != 0:
                    if case == ')' and sta[-1]=='(':
                        boolean = True
                    elif case == '}' and sta[-1]=='{':
                        boolean = True
                    elif case == ']' and sta[-1]=='[':
                        boolean = True
                    else:
                        boolean = False
                        break
                    sta.pop()
                else:
                    boolean = False
            if len(sta) >0:
                boolean = False
        return boolean

    if __name__ == '__main__':
        s = "[[[]"
        print(isValid(s))
