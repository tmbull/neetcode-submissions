class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        # need to represent the food and the snake on the board
        # empty = 0, food = 1, snake = 2
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.food = food
        self.food_i = 0
        self.score = 0

        # We could store the snake on the board, but It would be easier to keep track if we just store it's coordinates separately
        self.snake = deque([(0,0)])
        self.movements = {
            "U": (-1,0),
            "D": (1,0),
            "L": (0,-1),
            "R": (0,1)
        }

        print(self.board)

        self.width = width
        self.height = height

    def get_head(self):
        return self.snake[-1]

    def get_tail(self):
        return self.snake[0]

    def del_tail(self):
        self.snake.popleft()

    def move(self, direction: str) -> int:
        # moving...
        # tail: self.snake[0]
        # head: self.snake[-1]
        r,c = self.get_head()
        add_r, add_c = self.movements[direction]
        next_r, next_c = r + add_r, c + add_c

        print(f"{direction} - {next_r},{next_c}")

        # if snake moves into an invalid space, return -1
        if next_r < 0 or next_r >= self.height or next_c < 0 or next_c >= self.width:
            return -1
        # if snake moves into itself, return -1
        if (next_r, next_c) in self.snake:
            return -1
        # if snake moves into food, add the new space
        if self.food_i < len(self.food):
            food_r, food_c = self.food[self.food_i]
            if next_r == food_r and next_c == food_c:
                self.food_i += 1
                self.score += 1
        
        self.snake.popleft()
        
        # otherwise, add the new space, and remove the tail space
        self.snake.append((next_r, next_c))
        
        return self.score
        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
