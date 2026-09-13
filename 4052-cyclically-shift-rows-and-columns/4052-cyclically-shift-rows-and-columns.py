class Solution(object):
    def cyclicShift(self, n, grid, rowShift, colShift):
        result = [[0] * n for j in range(n)]
        for i in range(n):
            for j in range(n):
                j2 = (j - rowShift[i]) % n
                i2 = (i - colShift[j2]) % n
                result[i2][j2] = grid[i][j]
        return result
        