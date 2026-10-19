class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = collections.deque([0])
        visited = {0}
        coins_used = 0
        if amount == 0:
            return 0
        while queue:
            coins_used += 1
            for i in range(len(queue)):
                cur = queue.popleft()
                for coin in coins:
                    if coin + cur == amount:
                        return coins_used
                    if coin + cur < amount and coin + cur not in visited:
                        queue.append(coin + cur)
                        visited.add(coin + cur)
        return -1

            