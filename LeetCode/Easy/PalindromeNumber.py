class PalindromeNumber():

    def checkPalindrome(givenNumber):
        palindromNumb = 0
        givenNumberCopy = givenNumber
        while givenNumber > 0:
            # % gives remainder of a given number
            remainder = givenNumber % 10
            # returns quotient as a whole number
            givenNumber = givenNumber // 10
            palindromNumb = (palindromNumb * 10) + remainder
            #print(palindromNumb)
        return palindromNumb == givenNumberCopy

    if __name__ == '__main__':
        print(f'Given Number is Palindrome? {checkPalindrome(119911)}')
