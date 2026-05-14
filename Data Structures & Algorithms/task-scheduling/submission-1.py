class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # goal - interleave tasks if possible, insert idle if not
        # other observations - count # of each task type
        # # cycles = # of tasks + max difference ? 
        # tasks with highest count first
        # keep track of last n tasks,
        # pop things off the counter heap and push them onto the queue
        # pop them off the queue and decrement them before putting them back on the heap
        # if count == 0, don't put it on the queue
        counts = Counter(tasks)
        heap = [-count for count in counts.values()]
        heapq.heapify(heap)

        time = 0
        q = deque()

        while heap or q:
            time += 1
            if heap:
                count = 1 + heapq.heappop(heap)
                if count != 0:
                    q.append((count, time + n))
            if q and q[0][1] == time:
                c, _ = q.popleft()
                heapq.heappush(heap, c)
        return time

