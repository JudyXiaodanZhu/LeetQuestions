"""
Permutation
Example:
Input: [1,2,3]
Output:
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.re = []
        def dfs(nums, path):
            if len(nums) == 1:
                self.re.append(path+[nums[0]])
                return
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path+[nums[i]])
        dfs(nums,[])
        return self.re

"""
Combination
Input: n = 4, k = 2
Output:
[[2,4],[3,4],[2,3],[1,2],[1,3],[1,4],]
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = []
        for i in range(1, n+1):
            nums.append(i)
        self.re = []
        def dfs(nums, path, k, idx):
            if k == 0:
                self.re.append(path)
                return
            for i in range(idx, len(nums)):
                dfs(nums, path+[nums[i]], k-1, i+1)
        dfs(nums,[], k, 0)
        return self.re

"""
Subset
Input: nums = [1,2,3]
Output:
[[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]
"""
class Solution(object):
    def subsets(self, nums):
        self.re = []
        def dfs(nums, path, k, idx):
            if k == 0:
                self.re.append(path)
                return
            for i in range(idx, len(nums)):
                dfs(nums, path+[nums[i]], k-1, i+1)
        for i in range(len(nums)+1):
            dfs(nums,[], i, 0)
        return self.re

"""
Combination Sum
Input: candidates = [2,3,5], target = 8,
A solution set is:
[[2,2,2,2],[2,3,3],[3,5]]
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.re = []
        def dfs(candidates, path, target, idx):
            if target == 0:
                self.re.append(path)
                return
            if target < 0:
                return
            for i in range(idx, len(candidates)):
                dfs(candidates, path+[candidates[i]], target-candidates[i], i)
        dfs(candidates,[], target, 0)
        return self.re

"""
Generalized Abbreviation
Input: "word"
Output:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def helper(word, pos, cur, count, result):
            if len(word) == pos:
                # Once we reach the end, append current to the result
                result.append(cur + str(count) if count > 0 else cur)
            else:
                # Skip current position, and increment count
                helper(word, pos + 1, cur, count + 1, result)
                # Include current position, and zero-out count
                helper(word, pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0, result)

        result = []
        helper(word, 0, '', 0, result)
        return result

"""
Decode Ways
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def dfs(s, memo, k):
            if k == len(s): return 1
            if s[k] == '0': return 0
            if memo[k] != 0: return memo[k]
            result = dfs(s,memo, k+1)
            if k < len(s) - 1 and 10 <= int(s[k:k+2]) <= 26:
                result += dfs(s, memo, k+2)
            memo[k] = result
            return result
        memo = [0 for _ in range(len(s))]
        return dfs(s, memo, 0)