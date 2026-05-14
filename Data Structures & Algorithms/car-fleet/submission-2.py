class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # calculate position at each step, and find overtaking positions
        # the speed of a fleet is always min([speeds])
        # sort by position, then speed
        # if pos_x > pos_y and speed_x >= speed_y 
            # y will never catch up to x
        # else if time_x < time_y where time_x = (target - pos_x) // speed_x
            # y will never catch up
        # for x, y, z
            # increment fleets if x won't catch up to y
        fleets = 0
        sorted_pairs = reversed(sorted(zip(position, speed)))

        prev_time = 0
        for pos, sp in sorted_pairs:
            time = (target - pos) / sp 
            if time > prev_time:
                fleets += 1
                prev_time = time

        
        return fleets
