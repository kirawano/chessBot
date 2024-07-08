import chess
import chess.svg

from bot import sevaluate_board
from bot import find_best_move
from time import time
from time import sleep

board = chess.Board(
    "r1bqkb1r/1pp2ppp/p1Np1n2/8/4pP2/2N1P3/PPPPQ1PP/R1B1KB1R b KQkq - 0 7"
)

print(board)
print("Score: " + str(sevaluate_board(board)))
start = time()

best_move = find_best_move(board)
print("Best Move: " + str(best_move))
end = time()
print("Found best move in " + str(end - start) + " seconds")

sleep(1)
print("================")
board.push(best_move)
print(board)
