class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        best_k = 1000000001
        p1 = 1
        p2 = max(piles)

        def is_ok(rate,hours) -> bool:
            ans = 0
            for size in piles:
                if size % rate == 0:
                    ans += size // rate
                else:
                    ans += size // rate + 1
                if ans > hours:
                    return False
            return ans <= hours

        while(p1 <= p2):
            mid = p1 + (p2 - p1) // 2
            if is_ok(mid,h): 
                best_k = mid
                p2 = mid - 1
            else:
                p1 = mid + 1

        return best_k


        