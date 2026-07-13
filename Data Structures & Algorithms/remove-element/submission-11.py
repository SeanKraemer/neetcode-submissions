class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        length = len(nums)
        i = 0

        while i < length:
            if nums[i] == val:
                for j in range(i + 1, length):
                    nums[j - 1] = nums[j]
                nums[length - 1] = 0
                length -= 1
                i -= 1
            else:
                k += 1
            i += 1

        return k
        