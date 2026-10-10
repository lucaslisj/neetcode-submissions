class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ans = 0
        def bfs(row, col) -> None:
            queue = []
            queue.append((row,col))

            while queue:
                cur = queue.pop(0)
                visited.add((cur[0],cur[1]))
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for direction in directions:
                    r = cur[0] + direction[0]
                    c = cur[1] + direction[1]
                    if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == "1" and (r,c) not in visited:
                        queue.append((r,c))
                        visited.add((r,c))
            return

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in visited and grid[row][col] == "1":
                    ans += 1
                    bfs(row,col)
        return ans


        