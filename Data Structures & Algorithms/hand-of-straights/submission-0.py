class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # sort, then iterate through the results to find groups?
        # add numbers to dict (number -> count)
            # the problem here is that the keys are not sorted
        # sort then add to dict - rely on isertion order
        hand.sort()
        lookup = defaultdict(int)
        for c in hand:
            lookup[c] += 1

        while lookup:
            first = list(lookup.keys())[0]
            print(first)
            lookup[first] -= 1
            if lookup[first] == 0:
                del(lookup[first])
            for i in range(first + 1, first + groupSize):
                if i not in lookup or lookup[i] == 0:
                    return False
                lookup[i] -= 1
                if lookup[i] == 0:
                    del(lookup[i])

        return True

                