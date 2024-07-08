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

def alphabeta(board, depth, white):
    start = time()
    def order_moves(moves, board):
        return moves

    def abmax(board, depth, alpha, beta):
        if depth == 0: return evaluate(board)

        tb = board.copy()

        for move in tb.legal_moves:
            tb.push(move)
            val = abmin(board, depth-1, alpha, beta)
            if val >= beta: return beta 
            if val > alpha: alpha = val
            tb.pop()
        return alpha 
    
    def abmin(board, depth, alpha, beta):
        if depth == 0: return evaluate(board)

        tb = board.copy()

        for move in tb.legal_moves:
            tb.push(move)
            val = abmax(board, depth-1, alpha, beta)
            if val <= alpha: return alpha
            if val < beta:
                beta = val
            tb.pop()

        return beta


    end = time()

    if white:
        return abmax(board, depth, float('-inf'), float('inf'))
    else:
        return abmin(board, depth, float('-inf'), float('inf'))

def evaluate_move(move, board):
    tb = board.copy()
    tb.push(move)

    score = alphabeta(tb, 3, True if tb.turn == chess.WHITE else False)
    return [score, move]

def find_best_move(board):
    white = True if board.turn == chess.WHITE else False

    evals = []
    for move in board.legal_moves:
        evals.append(evaluate_move(move, board))

    if white:
        return max(evals, key=lambda m : m[0])[1]
    else:
        return min(evals, key=lambda m : m[0])[1]

