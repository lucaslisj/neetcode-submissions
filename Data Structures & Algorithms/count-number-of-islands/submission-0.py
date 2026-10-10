class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ans = 0
        def dfs(row, col) -> None:
            if (row,col) in visited:
                return
            visited.add((row,col))
            # check left right top bottom

            if row > 0 and grid[row - 1][col] == "1":
                dfs(row - 1, col)
            if row < len(grid) - 1 and grid[row + 1][col] == "1":
                dfs(row + 1, col)
            if col > 0 and grid[row][col - 1] == "1":
                dfs(row, col - 1)
            if col < len(grid[0]) - 1 and grid[row][col + 1] == "1":
                dfs(row, col + 1)
            return

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) in visited:
                    continue
                elif grid[row][col] == "1":
                    ans += 1
                    dfs(row,col)
        return ans


        