import chess
import chess.svg

from bot import sevaluate_board
from bot import find_best_move
from time import time

board = chess.Board("rnbqkbnr/1pp1p1pp/8/p4p2/2pP1B2/5N2/PP2PPPP/RN1QKB1R w KQkq - 0 5")

print(board)
print("Score: "+str(sevaluate_board(board)))
start = time()
print("Best Move: "+str(find_best_move(board)))
end = time()
print("Found best move in "+str(end - start) + " seconds")