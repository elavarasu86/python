class Solution(object):
    def searchInsert(nums, target):

        for index in range(0, len(nums)):
            if (nums[-1] < target):
                return len(nums)
            elif (nums[index] < target):
                continue
            else:
                return index

    if __name__ == '__main__':
        nums = [1, 3, 5, 6]
        target = 7
        print(searchInsert(nums, target))
