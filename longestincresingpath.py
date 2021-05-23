directions = [[1,0], [0, 1], [-1, 0], [0,-1]]

def longestIncreasingPath(matrix) :
        if len(matrix) == 0 or matrix == None :
            return 0
        n, m = len(matrix) , len(matrix[0])
        cache = [[0]*m]*n
        ans = 0
        for i in range(n):
            for j in range(m):
                longest = longestPath(matrix, cache, n, m, i, j)
                
                ans = max(longest, ans)
        print(cache)
        return ans

def longestPath(matrix, cache, n, m, i, j):
        print(i,j, cache)
        if cache[i][j] > 0:
            return cache[i][j]
        max1 = 0
        for direction in directions:
            x, y = i + direction[0], j + direction[1]
            if  x > -1 and y > -1 and x < n and y < m and matrix[x][y] > matrix[i][j]:
                
                longest = longestPath(matrix, cache, n, m, x, y)
                max1 = max(max1, longest)
        cache[i][j] = max1 + 1
        return cache[i][j]

mat = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(mat))