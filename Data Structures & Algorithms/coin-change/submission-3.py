class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hashtable = {} # key is the amount of coins allowed, value is the set of values we can get to in exactly that many coins
        hashtable[0] = {0}
        if amount == 0:
            return 0
        for i in range(1,amount + 1):
            cur = set()
            for num in hashtable[i - 1]:
                for coin in coins:
                    if num + coin == amount:
                        return i
                    if num + coin < amount:
                        cur.add(num + coin)
            hashtable[i] = cur
        return -1
            

