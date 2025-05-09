from typing import List


class RemoveDuplicateFromSortedArray:
    def removeDuplicate(nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1

        return j

    print("Program to remove duplicate from given array!")
    numb = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(removeDuplicate(numb))
