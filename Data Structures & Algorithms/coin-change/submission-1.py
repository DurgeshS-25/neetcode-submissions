class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()

        memo = {0:0}

        def min_coins(a):
            if a in memo:
                return memo[a]
            
            minn = float('inf')

            for coin in coins:
                diff = a - coin
                if diff < 0:
                    break
                minn = min(minn,1+min_coins(diff))
            
            memo[a] = minn
            return minn
        
        result = min_coins(amount)
        if result < float('inf'):
            return result
        else:
            return -1