class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # priority queue? 
        # we want a task at the top of the queue with no (or minimal) waiting required
        # processing a task increases waiting by 'n'
        # if all wait times are equal, we want task with most instances
        counts = Counter(tasks)

        heap = [-n for n in counts.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0

        while heap or q:
            time += 1

            # if not heap:
            #     time = q[0][1]
            # else:
            if heap:
                count = 1 + heapq.heappop(heap)
                if count:
                    q.append((count, time + n))
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time

