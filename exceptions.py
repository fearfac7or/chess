from tkinter import messagebox


class NotYourTurn(Exception):
    def __init__(self, ui_mode):
        if ui_mode:
            messagebox.showerror("Error", "It is not your turn")


class InvalidMove(Exception):
    def __init__(self, ui_mode):
        if ui_mode:
            messagebox.showerror("Error", "Invalid Move")


class InvalidFigure(Exception):
    def __init__(self, ui_mode):
        if ui_mode:
            messagebox.showerror("Error", "Wrong figure")
