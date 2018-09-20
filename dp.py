"""
Subarray Sum Equal K
Input:nums = [1,1,1], k = 2
Output: 2
"""
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = {0:1}
        res = s = 0
        for n in nums:
            s += n
            res += sum.get(s-k, 0)
            sum[s] = sum.get(s, 0) + 1
        return res

"""
Maximum Subarray
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        maxSum = currSum = nums[0]
        for i in range(1, len(nums)):
            currSum = max(currSum+nums[i], nums[i])
            maxSum = max(currSum, maxSum)
        return maxSum

"""
Target Sum
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
"""
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if sum(nums) < S: return 0
        if (sum(nums) + S) % 2 != 0: return 0
        
        target = (sum(nums) + S) / 2
        
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(len(nums)):
            for val in range(target, nums[i]-1, -1):
                if dp[val-nums[i]]:
                    dp[val] += dp[val-nums[i]]
        return dp[-1]

"""
Longest Increasing Subsequence
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
"""
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1]*len(nums)
        for i in range (1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


"""
Maximum Length of Repeated Subarray
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
"""
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        return max(max(row) for row in dp)

"""
Super Ugly Number
Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
"""
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1] * n
        i_list = [-1] * len(primes)
        v_list = [1] * len(primes)
        
        for i in range(n):
            num = min(v_list)
            ugly[i] = num
            for j in range(len(v_list)):
                if num == v_list[j]:
                    i_list[j] += 1
                    v_list[j] = ugly[i_list[j]] * primes[j]
        return ugly[-1]