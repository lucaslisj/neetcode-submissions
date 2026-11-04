class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        length = len(heights[0])
        width = len(heights)

        pacific = set()
        atlantic = set()

        # start backtracking the areas that can be reach the pacific ocean
        visited = set()
        queue = deque()
        for i in range(0,length):
            cur = (0,i)
            if cur not in visited:
                pacific.add(cur)
                visited.add(cur)
                queue.append(cur)
            while queue:
                cur = queue.popleft()
                visited.add(cur)
                pacific.add(cur)
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for direction in directions:
                    x = cur[0] + direction[0]
                    y = cur[1] + direction[1]
                    if 0 <= y < length and 0 <= x < width and heights[x][y] >= heights[cur[0]][cur[1]] and (x,y) not in visited:
                        queue.append((x,y))
        
        for i in range(0,width):
            cur = (i,0)
            if cur not in visited:
                pacific.add(cur)
                visited.add(cur)
                queue.append(cur)
            while queue:
                cur = queue.popleft()
                visited.add(cur)
                pacific.add(cur)
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for direction in directions:
                    x = cur[0] + direction[0]
                    y = cur[1] + direction[1]
                    if 0 <= y < length and 0 <= x < width and heights[x][y] >= heights[cur[0]][cur[1]] and (x,y) not in visited:
                        queue.append((x,y))
        
        # backtrack for atlantic now
        visited = set()
        for i in range(0,length):
            cur = (width - 1,i)
            if cur not in visited:
                atlantic.add(cur)
                visited.add(cur)
                queue.append(cur)
            while queue:
                cur = queue.popleft()
                visited.add(cur)
                atlantic.add(cur)
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for direction in directions:
                    x = cur[0] + direction[0]
                    y = cur[1] + direction[1]
                    if 0 <= y < length and 0 <= x < width and heights[x][y] >= heights[cur[0]][cur[1]] and (x,y) not in visited:
                        queue.append((x,y))
        
        for i in range(0,width):
            cur = (i, length - 1)
            if cur not in visited:
                atlantic.add(cur)
                visited.add(cur)
                queue.append(cur)
            while queue:
                cur = queue.popleft()
                visited.add(cur)
                atlantic.add(cur)
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for direction in directions:
                    x = cur[0] + direction[0]
                    y = cur[1] + direction[1]
                    if 0 <= y < length and 0 <= x < width and heights[x][y] >= heights[cur[0]][cur[1]] and (x,y) not in visited:
                        queue.append((x,y))
        ans = []
        for y in range(width):
            for x in range(length):
                if (y,x) in atlantic and (y,x) in pacific:
                    ans.append([y,x])
        return ans
        

                


        