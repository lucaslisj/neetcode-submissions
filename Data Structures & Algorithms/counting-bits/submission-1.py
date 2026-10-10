class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            x = i
            counter = 0
            while x > 0:
                counter += x % 2
                x >>= 1
            ans.append(counter)
        return ans