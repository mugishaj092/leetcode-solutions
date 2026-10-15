class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        total_area = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                
                h = grid[i][j]
                total_area += 4 * h + 2

                if i+1 < n:
                    total_area -= 2 * min(h, grid[i + 1][j]) 
                
                if j+1 < n:
                    total_area -= 2 * min(h, grid[i] [j + 1]) 
        
        return total_area