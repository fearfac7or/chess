import tkinter as tk
from layout import Layout
from game import GameBoard

if __name__ == "__main__":
    root = tk.Tk()
    board = GameBoard(root)
    layout = Layout()
    layout.load(root, board)
