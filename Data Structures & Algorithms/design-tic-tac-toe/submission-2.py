class TicTacToe:

    def __init__(self, n: int):
        # We need an n x n matrix to store game state
        self.state = [[0 for i in range(n)] for j in range(n)]
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        # steps:
        # 1. update game state
        # 2. check if there are any wins
        # 2a. we only need ot check possible wins involving the current space
        # we don't need to check if the move is valid or if th game has inded
        self.state[row][col] = player
        # posible win conditions: all state[i][player] state[player][i] or state[i][i] if row == col
        win = True
        for i in range(self.n):
            if self.state[i][col] != player:
                win = False
                break

        if win:
            return player

        win = True
        for i in range(self.n):
            if self.state[row][i] != player:
                win = False
                break
        if win:
            return player

        if row == col:
            win = True
            for i in range(self.n):
                if self.state[i][i] != player:
                    win = False
                    break
            if win:
                return player

        if row + col == self.n - 1:
            win = True
            for i in range(self.n):
                if self.state[i][0-1-i] != player:
                    win = False
                    break
            if win:
                return player

        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
