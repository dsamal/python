


class Solution:
    def twosum(self, nums, target):
        i = -1
        j = 0
        nlist = []
        while i < len(nums):
            i = i + 1
            j = i + 1
            while j < len(nums):
                sum1 = nums[i] + nums[j]
                if sum1 == target:
                    print("The two indexes are", i, j)
                    nlist.append((i, j))
                    break
                j = j + 1
        return nlist


nums1 = [2, 7, 11, 15, 1, 8]
target1 = 9
obj1 = Solution()
opt = obj1.twosum(nums1, 9)
print(opt)
