import tkinter as tk
from tkinter import messagebox
from validator import Validator
from position import Position
from figure import Figure
import copy


class GameBoard(tk.Frame):
    def __init__(self, parent=None, rows=8, columns=8, size=64, color1="white", color2="gray"):
        # BUSSINES LOGIC
        self.load_board(rows, columns, size, color1, color2)
        self.ui_mode = False
        if parent is not None:
            self.ui_mode = True
            canvas_width = columns * size
            canvas_height = rows * size
            tk.Frame.__init__(self, parent)
            self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                    width=canvas_width, height=canvas_height, background="gray")
            self.canvas.pack(side="top", fill="both", expand=False, padx=15, pady=15)
            self.canvas.bind("<Configure>", self.refresh)
            self.canvas.bind("<ButtonPress-1>", self.press)
            self.canvas.bind("<ButtonRelease-1>", self.release)

    def load_board(self, rows, columns, size, color1, color2):
        self.board = []
        for x in range(0, 8):
            row = []
            for y in range(0, 8):
                row.append(Position(x, y))
            self.board.append(row)
        self.load_figures(0, 1, "white")
        self.load_figures(7, 6, "black")
        self.last_move = "black"
        self.displayed_figures = {}
        self.images = {}
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.figures = {}

    def press(self, event):
        self.x1 = int(event.y / self.size)
        self.y1 = int(event.x / self.size)

    def release(self, event):
        self.x2 = int(event.y / self.size)
        self.y2 = int(event.x / self.size)
        self.move(self.x1, self.y1, self.x2, self.y2)

    def load_figures(self, x, y, color):
        rock = Figure("rock", color)
        knight = Figure("knight", color)
        bishop = Figure("bishop", color)
        queen = Figure("queen", color)
        king = Figure("king", color)
        pawn = Figure("pawn", color)
        self.board[x][0].add_figure(rock)
        self.board[x][1].add_figure(knight)
        self.board[x][2].add_figure(bishop)
        self.board[x][3].add_figure(queen)
        self.board[x][4].add_figure(king)
        self.board[x][5].add_figure(bishop)
        self.board[x][6].add_figure(knight)
        self.board[x][7].add_figure(rock)
        for pawn_y in range(0, 8):
            self.board[y][pawn_y].add_figure(pawn)

    def move_current_figure(self, a, b, c, d):
        if Validator.validate_move(copy.deepcopy(self.last_move), copy.deepcopy(self.board), a, b, c, d, self.ui_mode):
            self.move_figure(a, b, c, d)

    def move(self, a, b, c, d):
        if Validator.validate_move(copy.deepcopy(self.last_move), copy.deepcopy(self.board), a, b, c, d, self.ui_mode):
            self.move_figure(a, b, c, d)
            #remove current figure on (c,d) position
            if (c, d) in self.displayed_figures:
                self.remove_figure(self.displayed_figures[(c, d)])
            self.displayed_figures[(c, d)] = self.displayed_figures[(a, b)]
            self.displayed_figures[(a, b)] = None
            self.images[(c, d)] = self.images[(a, b)]
            self.images[(a, b)] = None
            self.remove_figure(self.displayed_figures[(c, d)])
            self.add_figure(self.displayed_figures[(c, d)], self.images[(c, d)], c, d)

    def move_figure(self, a, b, c, d):
        figure = self.board[a][b].figure
        self.board[a][b] = Position(a, b)
        self.board[c][d].add_figure(figure)
        self.last_move = figure.player
        king = Validator.found_king_coordinates(copy.deepcopy(self.board), copy.deepcopy(self.last_move))
        self.check_game_status(king[0], king[1])

    def check_game_status(self, a, b):
        if Validator.check_chess_and_mate(copy.copy(self.last_move), copy.copy(self.board), a, b, self.ui_mode):
            if self.ui_mode:
                messagebox.showinfo("Information", "Chess and mate")
            self.status = "Chess and mate"
        elif Validator.check_chess_status(self.last_move, self.board, self.ui_mode):
            if self.ui_mode:
                messagebox.showinfo("Information", "Chess")
            self.status = "Chess"
        else:
            self.status = "Next turn"

    def get_status(self):
        return self.status

    def add_figure(self, name, image, row=0, column=0):
        self.canvas.create_image(0, 0, image=image, tags=(name, "piece"), anchor="c")
        self.place_figure(name, row, column)

    def remove_figure(self, name):
        self.canvas.delete(name)

    def place_figure(self, name, row, column):
        self.figures[name] = (row, column)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)

    def refresh(self, event):
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.figures:
            self.place_figure(name, self.figures[name][0], self.figures[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")
