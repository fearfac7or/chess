from exceptions import InvalidMove
from exceptions import NotYourTurn
from exceptions import InvalidFigure
from position import Position
import copy


class Validator:
    def validate_move(last_move, board, a, b, c, d, ui_mode):
        position = board[a][b]
        if position.figure.figure_type is None:
            raise InvalidMove(ui_mode)
        elif position.figure.player == last_move:
            raise NotYourTurn(ui_mode)
        elif c < 0 or c > 7 or d < 0 or d > 7:
            raise InvalidMove(ui_mode)
        elif board[c][d].figure is not None and board[c][d].figure.player == position.figure.player:
            raise InvalidMove(ui_mode)
        elif not Validator.validate_figure_move(last_move, board, a, b, c, d, ui_mode):
            raise InvalidMove(ui_mode)
        return True

    def validate_figure_move(last_move, board, a, b, c, d, ui_mode):
        figure = board[a][b].figure.figure_type
        if figure == "rock":
            return Validator.square(last_move, board, a, b, c, d, ui_mode)
        elif figure == "knight":
            return Validator.horse(last_move, board, a, b, c, d, ui_mode)
        elif figure == "king":
            return Validator.king(last_move, board, a, b, c, d, ui_mode)
        elif figure == "queen":
            return Validator.diagonal(last_move, board, a, b, c, d, ui_mode) or Validator.square(last_move, board, a, b, c, d, ui_mode)
        elif figure == "bishop":
            return Validator.diagonal(last_move, board, a, b, c, d, ui_mode)
        elif figure == "pawn":
            return Validator.pawn(last_move, board, a, b, c, d, ui_mode)
        else:
            raise InvalidFigure(ui_mode)
        return True

    def check_chess_and_mate(last_move, board, a, b, ui_mode):
        if(not Validator.check_chess_status(last_move, board, ui_mode)):
            return False
        possible_moves = [[a, b-1], [a, b+1], [a-1, b-1], [a-1, b],
                                    [a-1, b+1], [a+1, b-1], [a+1, b], [a+1, b+1]]
        for move in possible_moves:
            if(Validator.validate_skip_king_move(last_move, board, a, b, move[0], move[1], ui_mode)
                    and not Validator.path_chess_check(last_move, board, a, b, move[0], move[1]), ui_mode):
                return False
        if(last_move == "white"):
            next = "black"
        else:
            next = "white"
        figures = Validator.found_opponent_figures(board, next)
        for figure in figures:
            for x in range(0, 8):
                for y in range(0, 8):
                    if(Validator.validate_figure_move(last_move, board, figure[0], figure[1], x, y, ui_mode)):
                        return False
        return True

    def check_chess(current_last_move, current_board, a, b, c, d, ui_mode):
        last_move = copy.deepcopy(current_last_move)
        board = copy.deepcopy(current_board)
        board[c][d].add_figure(board[a][b].figure)
        board[a][b] = Position(a, b)
        return Validator.check_chess_status(last_move, board, ui_mode)

    def path_chess_check(last_move, board, a, b, c, d, ui_mode):
        if(Validator.check_chess(copy.deepcopy(last_move), copy.deepcopy(board), a, b, c, d, ui_mode)):
            return True
        return False

    def check_chess_status(current_last_move, current_board, ui_mode):
        last_move = copy.deepcopy(current_last_move)
        board = copy.deepcopy(current_board)
        king = Validator.found_king_coordinates(board, last_move)
        opponent_figures = Validator.found_opponent_figures(board, last_move)
        for opponents in opponent_figures:
            figure = board[opponents[0]][opponents[1]].figure.figure_type
            if figure == "rock":
                if(Validator.square_path(last_move, board, opponents[0], opponents[1], king[0], king[1], ui_mode)):
                    return True
            elif figure == "knight":
                if(Validator.validate_skip_horse_move(last_move, board, opponents[0], opponents[1], king[0], king[1], ui_mode)):
                    return True
            elif figure == "king":
                if(Validator.king_path(last_move, board, opponents[0], opponents[1], king[0], king[1], ui_mode)):
                    return True
            elif figure == "queen":
                if(Validator.diagonal_path(last_move, board, opponents[0], opponents[1], king[0], king[1], ui_mode)
                        or Validator.square_path(last_move, board, opponents[0], opponents[1], king[0], king[1], ui_mode)):
                    return True
            elif figure == "bishop":
                if(Validator.diagonal_path(last_move, board, opponents[0], opponents[1], king[0], king[1], ui_mode)):
                    return True
            elif figure == "pawn":
                if(Validator.pawn_path(last_move, board, opponents[0], opponents[1], king[0], king[1], ui_mode)):
                    return True
        return False

    def found_king_coordinates(board, last_move):
        king = []
        for x in range(0, 8):
            for y in range(0, 8):
                if(board[x][y].figure is not None and board[x][y].figure.figure_type == "king"
                        and board[x][y].figure.player != last_move):
                    king.append(x)
                    king.append(y)
        return king

    def found_opponent_figures(board, last_move):
        opponents = []
        for x in range(0, 8):
            for y in range(0, 8):
                if(board[x][y].figure is not None and board[x][y].figure.player == last_move):
                    figure = []
                    figure.append(x)
                    figure.append(y)
                    opponents.append(figure)
        return opponents

    def final_check(last_move, board, c, d):
        if(board[c][d].figure is None or (board[c][d].figure is not None and board[c][d].figure.player != last_move)):
            return True
        else:
            return False

    def square(last_move, board, a, b, c, d, ui_mode):
        if(last_move == "white"):
            next = "black"
        else:
            next = "white"
        return Validator.square_path(next, board, a, b, c, d, ui_mode) and not Validator.path_chess_check(last_move, board, a, b, c, d, ui_mode)

    def square_path(last_move, board, a, b, c, d, ui_mode):
        if (a == c and b == d) or (a != c and b != d):
            return False
        if c-a > 0:
            for i in range(a+1, c):
                if board[i][b].figure is not None:
                    return False
            return Validator.final_check(last_move, board, c, d)
        elif c-a < 0:
            for i in range(a-1, c):
                if board[i][b].figure is not None:
                    return False
            return Validator.final_check(last_move, board, c, d)
        elif d-b > 0:
            for i in range(b+1, d):
                if board[i][b].figure is not None:
                    return False
            return Validator.final_check(last_move, board, c, d)
        elif d-b < 0:
            for i in range(b-1, d):
                if board[i][b].figure is not None:
                    return False
            return Validator.final_check(last_move, board, c, d)

    def diagonal(last_move, board, a, b, c, d, ui_mode):
        if(last_move == "white"):
            next = "black"
        else:
            next = "white"
        return Validator.diagonal_path(next, board, a, b, c, d, ui_mode) and not Validator.path_chess_check(last_move, board, a, b, c, d, ui_mode)

    def diagonal_path(last_move, board, a, b, c, d, ui_mode):
        if(abs(c - a) != abs(b - d)):
            return False
        if(c > a and b < d):
            k = a + 1
            l = b + 1
            while(l < d and k < c):
                if(board[k][l].figure is not None):
                    return False
                k += 1
                l += 1
            return Validator.final_check(last_move, board, k, l)
        elif(c > a and b > d):
            k = a + 1
            l = b - 1
            while(l > d and k < c):
                if(board[k][l].figure is not None):
                    return False
                k += 1
                l -= 1
            return Validator.final_check(last_move, board, k, l)
        elif(c < a and b > d):
            k = a - 1
            l = b - 1
            while(l > d and k > c):
                if(board[k][l].figure is not None):
                    return False
                k -= 1
                l -= 1
            return Validator.final_check(last_move, board, k, l)
        elif(c < a and b < d):
            k = a - 1
            l = b + 1
            while(l < d and k > c):
                if(board[k][l].figure is not None):
                    return False
                k -= 1
                l += 1
            return Validator.final_check(last_move, board, k, l)

    def horse(last_move, board, a, b, c, d, ui_mode):
        return Validator.horse_path(last_move, board, a, b, c, d, ui_mode) and not Validator.path_chess_check(last_move, board, a, b, c, d, ui_mode)

    def horse_path(last_move, board, a, b, c, d, ui_mode):
        possible_moves = [[a-2, b-1], [a-1, b-2], [a+1, b+2], [a+2, b+1], [a+2, b-1], [a+1, b-2], [a-1, b+2], [a-2, b+1]]

        for move in possible_moves:
            if Validator.validate_skip_horse_move(last_move, board, move[0], move[1], c, d, ui_mode):
                return True
        return False

    def king(last_move, board, a, b, c, d, ui_mode):
        return Validator.king_path(last_move, board, a, b, c, d, ui_mode) and not Validator.path_chess_check(last_move, board, a, b, c, d, ui_mode)

    def king_path(last_move, board, a, b, c, d, ui_mode):
        possible_moves = [[a, b-1], [a, b+1], [a-1, b-1], [a-1, b],
                                    [a-1, b+1], [a+1, b-1], [a+1, b], [a+1, b+1]]
        for move in possible_moves:
            if(move[0] == c and move[1] == d
                    and Validator.validate_skip_king_move(last_move, board, a, b, c, d, ui_mode)):
                return True
        return False

    def pawn(last_move, board, a, b, c, d, ui_mode):
        return Validator.pawn_path(last_move, board, a, b, c, d, ui_mode) and not Validator.path_chess_check(last_move, board, a, b, c, d, ui_mode)

    def pawn_path(last_move, board, a, b, c, d, ui_mode):

        if(last_move == "black" and c > a):
            if(c - a == 1 and b == d and board[c][d].figure is None):
                return True
            if(c - a == 2 and b == d and a == 1 and board[c][d].figure is None):
                return True
            if(c - a == 1 and (b - d == 1 or b - d == -1) and board[c][d].figure is not None
                    and board[c][d].figure.player == last_move):
                    return True
            return False
        if(last_move == "white" and c < a):
            if(c - a == -1 and b == d and board[c][d].figure is None):
                return True
            if(c - a == -2 and b == d and a == 6 and board[c][d].figure is None):
                return True
            if(c - a == -1 and (b - d == 1 or b - d == -1) and board[c][d].figure is not None
                    and board[c][d].figure.player == last_move):
                return True
            return False

    def validate_skip_horse_move(last_move, board, a, b, c, d, ui_mode):
        if(a == c and b == d and (board[c][d].figure is None or board[c][d].figure.player == last_move)):
            return True

    def validate_skip_king_move(last_move, board, a, b, c, d, ui_mode):
        if(c < 0 or c > 7 or d < 0 or d > 7):
            return False
        if(board[c][d].figure is None or board[c][d].figure.player == last_move):
            possible_moves = [[c, d-1], [c, d+1], [c-1, d-1], [c-1, d], [c-1, d+1], [c+1, d-1], [c+1, d], [c+1, d+1]]
            for move in possible_moves:
                if((move[0] < 0 or move[1] > 7) or (move[1] < 0 or move[1] > 7)):
                    pass
                if(board[move[0]][move[1]].figure is not None and
                    board[move[0]][move[1]].figure.figure_type == "king"
                        and (move[0] != a and move[1] != b)):
                        return False
            return True
