"""
Kth Smallest Element in a Sorted Matrix
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
"""
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix: return 0
        n = len(matrix)
        heap = []
        j = 0
        for i in matrix:
            heapq.heappush(heap, (i[0], j, 0))
            j += 1
        for _ in range(k):
            element, i, idx = heapq.heappop(heap)
            if idx+1 < n:
                heapq.heappush(heap, (matrix[i][idx+1], i, idx+1))
        return element

"""
Spiral Matrix
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
"""
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        u, d, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        re = []
        while u < d and l < r:
            re.extend(matrix[u][i] for i in range(l, r+1))
            re.extend(matrix[j][r] for j in range(u+1, d+1))
            re.extend(matrix[d][i] for i in range(r-1, l-1, -1))
            re.extend(matrix[j][l] for j in range(d-1, u, -1))
            u, d, l, r = u+1, d-1, l+1, r-1
        if u != d and l == r:
            re.extend(matrix[j][r] for j in range(u, d+1))
        elif l != r and u == d:
            re.extend(matrix[u][i] for i in range(l, r+1))
        elif u == d and l == r:
            re.append(matrix[u][l])
        return re

"""
Set Matrix Zeroes
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
"""
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        one = two = False
                
        for i in range(len(matrix)):
            if matrix[i][0] == 0: one = True
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0: two = True
                    matrix[0][j] = matrix[i][0] = 0
                    
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
                    
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(1, len(matrix)):
                    matrix[j][i] = 0
                    
        if one == True:
            for i in range(len(matrix)):
                matrix[i][0] = 0
                
        if two == True:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0