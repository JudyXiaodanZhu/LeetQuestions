"""
Partition to K Equal Sum Subsets
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
"""
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k==1: return True
        self.n=len(nums)
        if k>self.n: return False

        total=sum(nums)
        if total%k: return False

        self.target=total/k
        visit=[0]*self.n

        nums.sort(reverse=True)
        def dfs(k,ind,sum,cnt):
            if k==1: return True
            if sum==self.target and cnt>0:
                return dfs(k-1,0,0,0)
            for i in range(ind,self.n):
                if not visit[i] and sum+nums[i]<=self.target:
                    visit[i]=1
                    if dfs(k,i+1,sum+nums[i],cnt+1): 
                        return True
                    visit[i]=0
            return False

        return dfs(k,0,0,0)

"""
Course Schedule
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
"""
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites: return True
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        def dfs(i):
            if visited[i] == -1: return False
            if visited[i] == 1: return True
            visited[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            return True
        for j in range(numCourses):
            if not dfs(j): 
                return False
        return True

"""
Find Iteinerary
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = {}
        for x, y in tickets:
            targets[x] = targets.get(x,[]) + [y]
        for j in targets:
            j = targets[j].sort(reverse=True)
        route = []
        def visit(airport):
            if airport in targets:
                while targets[airport]:
                    visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]

