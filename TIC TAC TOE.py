class TicTacToeCSP:
    def __init__(self):
        # Initialize the grid (3x3)
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # 'X' starts first
    
    def print_board(self):
        # Prints the Tic-Tac-Toe board
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def is_winner(self, player):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):  # row
                return True
            if all(self.board[j][i] == player for j in range(3)):  # column
                return True
        if all(self.board[i][i] == player for i in range(3)):  # main diagonal
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):  # anti diagonal
            return True
        return False

    def is_full(self):
        # Check if the board is full
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def is_consistent(self, row, col, player):
        # Check if the current move is valid (doesn't overwrite another player's mark)
        if self.board[row][col] != ' ':
            return False
        return True

    def backtrack(self):
        # If the board is full or someone wins, return the solution
        if self.is_full() or self.is_winner('X') or self.is_winner('O'):
            return self.board
        
        # Try to fill each cell with X or O
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    if self.is_consistent(row, col, self.current_player):
                        # Try this move
                        self.board[row][col] = self.current_player
                        
                        # Switch players
                        self.current_player = 'O' if self.current_player == 'X' else 'X'
                        
                        result = self.backtrack()  # Recursively try to solve the board
                        if result:
                            return result
                        
                        # Backtrack (undo the move)
                        self.board[row][col] = ' '
                        
                        # Switch players back
                        self.current_player = 'O' if self.current_player == 'X' else 'X'
        
        return None

    def solve(self):
        # Start the backtracking search for a solution
        solution = self.backtrack()
        return solution

# Initialize the Tic-Tac-Toe CSP problem
tic_tac_toe = TicTacToeCSP()

# Solve the Tic-Tac-Toe problem using backtracking
solution = tic_tac_toe.solve()

# Print the solution
if solution:
    print("Solution found:")
    tic_tac_toe.print_board()
else:
    print("No solution found.")
