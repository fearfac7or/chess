import tkinter as tk


class Layout:
    def load(self, root, board):
        board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
        b_rock = tk.PhotoImage(file="images/b_rock.gif")
        b_knight = tk.PhotoImage(file="images/b_knight.gif")
        b_bishop = tk.PhotoImage(file="images/b_bishop.gif")
        b_queen = tk.PhotoImage(file="images/b_queen.gif")
        b_king = tk.PhotoImage(file="images/b_king.gif")
        b_pawn = tk.PhotoImage(file="images/b_pawn.gif")
        w_rock = tk.PhotoImage(file="images/w_rock.gif")
        w_knight = tk.PhotoImage(file="images/w_knight.gif")
        w_bishop = tk.PhotoImage(file="images/w_bishop.gif")
        w_queen = tk.PhotoImage(file="images/w_queen.gif")
        w_king = tk.PhotoImage(file="images/w_king.gif")
        w_pawn = tk.PhotoImage(file="images/w_pawn.gif")

        board.add_figure("b_rock1", b_rock, 7, 0)
        board.displayed_figures[(7, 0)] = "b_rock1"
        board.images[(7, 0)] = b_rock
        board.add_figure("b_knight1", b_knight, 7, 1)
        board.displayed_figures[(7, 1)] = "b_knight1"
        board.images[(7, 1)] = b_knight
        board.add_figure("b_bishop1", b_bishop, 7, 2)
        board.displayed_figures[(7, 2)] = "b_bishop1"
        board.images[(7, 2)] = b_bishop
        board.add_figure("b_queen", b_queen, 7, 3)
        board.displayed_figures[(7, 3)] = "b_queen"
        board.images[(7, 3)] = b_queen
        board.add_figure("b_king", b_king, 7, 4)
        board.displayed_figures[(7, 4)] = "b_king"
        board.images[(7, 4)] = b_king
        board.add_figure("b_bishop2", b_bishop, 7, 5)
        board.displayed_figures[(7, 5)] = "b_bishop2"
        board.images[(7, 5)] = b_bishop
        board.add_figure("b_kinght2", b_knight, 7, 6)
        board.displayed_figures[(7, 6)] = "b_knight2"
        board.images[(7, 6)] = b_knight
        board.add_figure("b_rock2", b_rock, 7, 7)
        board.displayed_figures[(7, 7)] = "b_rock2"
        board.images[(7, 7)] = b_rock
        board.add_figure("b_pawn1", b_pawn, 6, 0)
        board.displayed_figures[(6, 0)] = "b_pawn1"
        board.images[(6, 0)] = b_pawn
        board.add_figure("b_pawn2", b_pawn, 6, 1)
        board.displayed_figures[(6, 1)] = "b_pawn2"
        board.images[(6, 1)] = b_pawn
        board.add_figure("b_pawn3", b_pawn, 6, 2)
        board.displayed_figures[(6, 2)] = "b_pawn3"
        board.images[(6, 2)] = b_pawn
        board.add_figure("b_pawn4", b_pawn, 6, 3)
        board.displayed_figures[(6, 3)] = "b_pawn4"
        board.images[(6, 3)] = b_pawn
        board.add_figure("b_pawn5", b_pawn, 6, 4)
        board.displayed_figures[(6, 4)] = "b_pawn5"
        board.images[(6, 4)] = b_pawn
        board.add_figure("b_pawn6", b_pawn, 6, 5)
        board.displayed_figures[(6, 5)] = "b_pawn6"
        board.images[(6, 5)] = b_pawn
        board.add_figure("b_pawn7", b_pawn, 6, 6)
        board.displayed_figures[(6, 6)] = "b_pawn7"
        board.images[(6, 6)] = b_pawn
        board.add_figure("b_pawn8", b_pawn, 6, 7)
        board.displayed_figures[(6, 7)] = "b_pawn8"
        board.images[(6, 7)] = b_pawn
        board.add_figure("w_rock1", w_rock, 0, 0)
        board.displayed_figures[(0, 0)] = "w_rock1"
        board.images[(0, 0)] = w_rock
        board.add_figure("w_knight1", w_knight, 0, 1)
        board.displayed_figures[(0, 1)] = "w_knight1"
        board.images[(0, 1)] = w_knight
        board.add_figure("w_bishop1", w_bishop, 0, 2)
        board.displayed_figures[(0, 2)] = "w_bishop1"
        board.images[(0, 2)] = w_bishop
        board.add_figure("w_queen", w_queen, 0, 3)
        board.displayed_figures[(0, 3)] = "w_queen"
        board.images[(0, 3)] = w_queen
        board.add_figure("w_king", w_king, 0, 4)
        board.displayed_figures[(0, 4)] = "w_king"
        board.images[(0, 4)] = w_king
        board.add_figure("w_bishop2", w_bishop, 0, 5)
        board.displayed_figures[(0, 5)] = "w_bishop2"
        board.images[(0, 5)] = w_bishop
        board.add_figure("w_kinght2", w_knight, 0, 6)
        board.displayed_figures[(0, 6)] = "w_knight2"
        board.images[(0, 6)] = w_knight
        board.add_figure("w_rock2", w_rock, 0, 7)
        board.displayed_figures[(0, 7)] = "w_rock2"
        board.images[(0, 7)] = w_rock
        board.add_figure("w_pawn1", w_pawn, 1, 0)
        board.displayed_figures[(1, 0)] = "w_pawn1"
        board.images[(1, 0)] = w_pawn
        board.add_figure("w_pawn2", w_pawn, 1, 1)
        board.displayed_figures[(1, 1)] = "w_pawn2"
        board.images[(1, 1)] = w_pawn
        board.add_figure("w_pawn3", w_pawn, 1, 2)
        board.displayed_figures[(1, 2)] = "w_pawn3"
        board.images[(1, 2)] = w_pawn
        board.add_figure("w_pawn4", w_pawn, 1, 3)
        board.displayed_figures[(1, 3)] = "w_pawn4"
        board.images[(1, 3)] = w_pawn
        board.add_figure("w_pawn5", w_pawn, 1, 4)
        board.displayed_figures[(1, 4)] = "w_pawn5"
        board.images[(1, 4)] = w_pawn
        board.add_figure("w_pawn6", w_pawn, 1, 5)
        board.displayed_figures[(1, 5)] = "w_pawn6"
        board.images[(1, 5)] = w_pawn
        board.add_figure("w_pawn7", w_pawn, 1, 6)
        board.displayed_figures[(1, 6)] = "w_pawn7"
        board.images[(1, 6)] = w_pawn
        board.add_figure("w_pawn8", w_pawn, 1, 7)
        board.displayed_figures[(1, 7)] = "w_pawn8"
        board.images[(1, 7)] = w_pawn
        root.mainloop()