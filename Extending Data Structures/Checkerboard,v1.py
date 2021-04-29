# Pass this function a list of lists, and it will
# print it such that it looks like the grids in
# the exercise instructions.
def print_board(board):
    for i in range(len(board)):
        # This line uses some Python you haven't
        # learned yet. You'll learn about this
        # part in a future lesson:
        #
        # [str(x) for x in board[i]]
        print " ".join([str(x) for x in board[i]])

# Your code here...
board=[]
for i in range(3):
    board.append([1]*8)
for i in range(2):
    board.append([0]*8)
for i in range(3):
    board.append([1]*8)
print_board(board)