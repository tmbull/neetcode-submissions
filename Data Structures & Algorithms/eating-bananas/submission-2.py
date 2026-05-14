class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # need to visit each pile at least once
        # for each pile, time is size // k
        # want to maximize time up to 'h', but minimize k
        # min(k) = h / max(pile), max(k) = max(pile)

        # reverse sort piles
            # binary search through values of k

        piles.sort(reverse=True)

        min_k = 1
        max_k = piles[0]
        result = max_k

        while min_k <= max_k:
            time = 0
            k = min_k + ((max_k - min_k) // 2)
            for pile in piles:
                pile_time = math.ceil(pile / k)
                time += pile_time
                if time > h:
                    break
            print(f"res: {result} | time: {time} | {min_k} < {k} < {max_k}")
            if time <= h:
                result = k
                max_k = k - 1
            else:
                min_k = k + 1
        
        return result
            