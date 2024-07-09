import chess
from time import time
from multiprocessing import Pool

val_map = {1: 1, 2: 3, 3: 3, 4: 5, 5: 8, 6: 1000}


def sevaluate_board(board):

    # creates a BaseBoard from our current board, then makes a dictionary of all of the pieces on said board
    B = chess.BaseBoard(board.board_fen())
    pieces = B.piece_map()
    total = 0
    for piece in pieces.values():
        # for some reason piece.color returns a boolean
        c = 1 if piece.color else -1
        total += c * val_map[piece.piece_type]

    return total


evaluate = sevaluate_board


def alphabeta(board, depth):
    start = time()

    def order_moves(moves, board):
        start = time()
        B = chess.BaseBoard(board.board_fen())
        omoves = []
        for move in moves:
            mg = 0
            if board.is_capture(move):
                P = B.piece_type_at(move.from_square)
                C = B.piece_type_at(move.to_square)

                pv = val_map[P]
                cv = val_map[C]
                mg += 10 * cv - pv
            omoves.append([move, mg])

        smoves = sorted(omoves, key=lambda x: x[1])

        ret = []
        for move in smoves:
            ret.append(move[0])
        return ret

    def abmax(board, depth, alpha, beta):
        if depth == 1:
            return evaluate(board)

        tb = board.copy()

        moves = order_moves(tb.legal_moves, tb)
        #moves = tb.legal_moves

        for move in moves:
            tb.push(move)
            val = abmin(board, depth - 1, alpha, beta)
            if val >= beta:
                break
            if val > alpha:
                alpha = val
            tb.pop()
        return alpha

    def abmin(board, depth, alpha, beta):
        if depth == 1:
            return evaluate(board)

        tb = board.copy()

        moves = order_moves(tb.legal_moves, tb)
        #moves = tb.legal_moves

        for move in moves:
            tb.push(move)
            val = abmax(board, depth - 1, alpha, beta)
            if val <= alpha:
                break
            if val < beta:
                beta = val
            tb.pop()
        return beta

    end = time()

    if board.turn == chess.WHITE:
        return abmax(board, depth, float("-inf"), float("inf"))
    else:
        return abmin(board, depth, float("-inf"), float("inf"))


def evaluate_move(move, board, depth):
    tb = board.copy()
    tb.push(move)

    score = alphabeta(tb, depth)
    return [score, move]


def find_best_move(board, depth):
    white = True if board.turn == chess.WHITE else False

    evals = []
    for move in board.legal_moves:
        evals.append(evaluate_move(move, board, depth))

    if white:
        return max(evals, key=lambda m: m[0])[1]
    else:
        return min(evals, key=lambda m: m[0])[1]
