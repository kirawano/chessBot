import chess
from time import time

val_map = {
    1 : 1,
    2 : 3,
    3 : 3,
    4 : 5,
    5 : 8,
    6 : 1000
}

def sevaluate_board(board):

    # creates a BaseBoard from our current board, then makes a dictionary of all of the pieces on said board 
    B = chess.BaseBoard(board.board_fen())
    pieces = B.piece_map()
    total = 0
    for piece in pieces.values():
        # for some reason piece.color returns a boolean
        c = 1 if piece.color else -1
        total+=(c*val_map[piece.piece_type])

    return total

evaluate = sevaluate_board 

def ab(board, depth, white):
    start = time()
    def order_moves(moves, board):
        return moves
    
    def alphabeta(board,depth,alpha,beta,white):
        tb = board.copy()
        if depth == 1: return evaluate(tb)

        if white:
            moves = tb.legal_moves
            val = float('-inf')
            for move in moves:
                tb.push(move)
                val = max(val, alphabeta(tb, depth-1, alpha, beta, False))

                if val > beta: break
                alpha = max(alpha,val)

                tb.pop()
            return val
        else:
            moves = tb.legal_moves
            val = float('inf')
            for move in moves:
                tb.push(move)
                val = min(val, alphabeta(tb, depth-1, alpha, beta, True))

                if val < alpha: break 
                beta = min(beta, val)

                tb.pop()
            return val

    end = time()
    return alphabeta(board, depth, float('-inf'), float('inf'), white)
    
def evaluate_move(move, board):
    tb = board.copy()
    tb.push(move)

    return [ab(tb, 3, True if tb.turn == chess.WHITE else False), move]

def find_best_move(board):
    white = True if board.turn == chess.WHITE else False

    if white:
        return max(board.legal_moves, key=lambda m : evaluate_move(m, board)[0])
    else:
        return min(board.legal_moves, key=lambda m : evaluate_move(m, board)[0])

