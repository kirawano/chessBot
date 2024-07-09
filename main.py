import chess
import chess.svg

from bot import sevaluate_board
from bot import find_best_move
from time import time
from time import sleep

depth = 4

# test positions: 
    # "r1bqkb1r/1pp2ppp/p1Np1n2/8/4pP2/2N1P3/PPPPQ1PP/R1B1KB1R b KQkq - 0 7"
    # "rnbqkbnr/pppp1ppp/8/4p3/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 0 2"
    # "rnb1kbnr/ppp1Ppp1/7p/8/8/8/PPP1PPPP/RNBQKBNR w KQkq - 0 5"
board = chess.Board(
    
)

print(board)
print("Score: " + str(sevaluate_board(board)))
start = time()

best_move = find_best_move(board, depth)
print("Best Move: " + str(best_move))
end = time()
print("Found best move in " + str(end - start) + " seconds at "+str(depth+1) + " ply")

sleep(1)
print("================")
board.push(best_move)
print(board)
