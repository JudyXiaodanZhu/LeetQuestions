"""
3Sum
a + b + c = 0
"""
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        re = []
        for i in range(len(nums)-2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue
            target = -nums[i]
            j = i+1
            k = len(nums) -1
            while j < k:
                if nums[j] + nums[k] == target:
                    re.append((nums[i], nums[j], nums[k]))
                    while j < k and nums[j] == nums[j+1]: j += 1
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else: j += 1
        return re

"""
Find Duplicate
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res

"""
Find first and last occurance of val
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1, -1]
        if len(nums) == 1 and nums[0] == target: return [0,0]
        check = [False, False]
        re = [0,0]
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (high + low) / 2
            if nums[mid] == target:
                if mid-1 >= 0 and nums[mid-1] < nums[mid] and mid nums[mid+1] > nums[mid]:
                    return [mid, mid]
                elif nums[mid-1] < nums[mid]:
                    re[0] = mid
                    check[0] = True
                    if check[1] == True:
                        return re
                    else:
                        low = mid + 1
                        continue
                elif nums[mid+1] > nums[mid]:
                    check[1] = True
                    re[1] = mid
                    if check[0] == True:
                        return re
                    else:
                        high = mid - 1
                        continue
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return [-1, -1]

"""
Search in Rotated Sorted Array
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1