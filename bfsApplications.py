"""
Word Ladder
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
"""
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    check = word[:i] + c + word[i+1:]
                    if check in wordList:
                        wordList.remove(check)
                        queue.append([check, length + 1])
        return 0

"""
Number of Islands
Input:
11000
11000
00100
00011

Output: 3
"""
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]: 
            return False
        
        if grid[0][0] == '9': return True
        
        queue = [(0,0)]
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            x, y = queue.pop()
            visited.add((x, y))
            for d in directions:
                i, j = x+d[0], y+d[1]
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                    if grid[x][y] == '9':
                        return True
                    if grid[i][j] == '1' and (i, j) not in visited:
                        queue.append((i, j))
        return False

"""
01 Matrix
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
Input:
0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
"""
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        visited = set()
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    visited.add((i, j))
                    queue.append((i, j))
                    
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            item = queue.popleft()
            for d in directions:
                o, p = item[0] + d[0], item[1]+ d[1]
                if 0 <= o < m and 0 <= p < n and (o, p) not in visited:
                    matrix[o][p] = matrix[item[0]][item[1]] + 1
                    queue.append((o, p))
                    visited.add((o, p))
        return matrix

"""
Network Delay Time
There are N network nodes, labelled 1 to N.
Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
"""
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        if not times: return 0
        dic = collections.defaultdict(dict)
        for u, v, w in times:
            dic[u-1][v-1] = w
        Q = set(range(N))
        dist = [float('Inf') for _ in range(N)]
        dist[K-1] = 0
        while Q:
            u = None
            for node in Q:
                if u == None or dist[node] < dist[u]:
                    u = node
            Q.remove(u)
            for edge in dic[u]:
                if dist[u] + dic[u][edge] < dist[edge]:
                    dist[edge] = dist[u] + dic[u][edge]
        re = max(dist)
        return -1 if re == float('Inf') else re