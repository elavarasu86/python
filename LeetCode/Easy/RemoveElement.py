from typing import List


class RemoveElement:

    def removeGivenElement(nums: List[int], val: int) -> int:
        rt = 0
        for i in range(0, len(nums)):
            if (nums[i] != val):
                nums[rt] = nums[i]
                rt = rt + 1
        return rt

    print("Program to Remove Given Elements")
    val = 2
    inpt = [0, 1, 2, 2, 3, 0, 4, 2]
    print(removeGivenElement(inpt, val))
