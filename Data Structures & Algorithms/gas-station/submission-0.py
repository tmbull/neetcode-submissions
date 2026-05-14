class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # brute force
        # start at each gas station and go until we make it around the loop
        # or run out of fuel
        # we can memoize how far we make it at each station which may help
        # greedy?
        # sum(gas) >= sum(cost)
        efficiency = []
        total_gas = 0
        total_cost = 0
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            efficiency.append(gas[i] - cost[i])

        if total_cost > total_gas:
            return -1

        total = 0
        i = 0
        start = 0
        for i in range(len(efficiency)):
            total += efficiency[i]
            if total < 0:
                start = i + 1
                total = 0
        
        return start
                


        


        
        