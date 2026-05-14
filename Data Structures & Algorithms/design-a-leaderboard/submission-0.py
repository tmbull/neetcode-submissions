class Leaderboard:
    # need to maintain a map of playId -> score
    # we also care about sorting, so need to be able to sort playerIds by score
    # reset - sets playerId to 0
    # two data structures: map for O(1) playerId lookups, heap for sorting
    # heap element should be a tuple (score, playerId) so that we can 
    def __init__(self):
        self.board = {}
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.board:
            self.board[playerId] = 0;

        self.board[playerId] += score;
        

    def top(self, K: int) -> int:
        return sum(heapq.nlargest(K, self.board.values()));
        

    def reset(self, playerId: int) -> None:
        self.board[playerId] = 0;
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
