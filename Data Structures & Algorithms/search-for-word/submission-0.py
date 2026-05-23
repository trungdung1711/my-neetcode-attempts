class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # input
        # m x n board of characters
        # string word

        # output
        # true if word exists in grid

        # constraints
        # m = row
        # n = col
        # m, n >= 1 <= 6
        # lowercase and uppercase English letters
        # adjacent == horizontally + vertially neibouring

        # edge cases
        # [1, 1] -> only one word

        # current cell
        self.result = False
        self.explored = set()

        for i, row in enumerate(board):
            for j, col in enumerate(board[i]):

                self.dfs(i, j, self.explored, board, 0, word)

        return self.result



    def dfs(self, i, j, explored, board, index, s):
        if index == len(s):
            # match sucessfull
            self.result = self.result or True
            return
        
        if board[i][j] == s[index]:
            
            if index == len(s) - 1:
                # match sucessful
                self.result = self.result or True
                return

            # current match
            explored.add((i,j))

            for cell_i, cell_j in self.possible_cells(board, (i, j), explored):
                self.dfs(cell_i, cell_j, explored, board, index + 1, s)

            explored.remove((i, j))

        else:
            self.result = self.result or False

        

    def possible_cells(self, board : List[List[str]], current, explored : set):
        # row
        m = len(board)
        # col
        n = len(board[0])

        i, j = current

        first_possibles = [
            (i + 1, j),
            (i, j + 1),
            (i - 1, j),
            (i, j - 1)
        ]

        second_possibles = [

        ]

        for i, j in first_possibles:
            if i < 0 or j < 0 or i >= m or j >= n:
                continue

            elif (i, j) in explored:
                continue

            else:
                second_possibles.append((i, j))

        return second_possibles