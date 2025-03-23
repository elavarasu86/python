class Solution(object):
    def plusOne(digits):
        digit = 0
        final = []
        for index in range(0, len(digits)):
            digits[index]
            digit = (digit * 10) + digits[index]
        digit = digit + 1
        for letter in str(digit):
            final.append(int(letter))
        return final

    if __name__ == '__main__':
        digitsList = [9]
        print(plusOne(digitsList))
