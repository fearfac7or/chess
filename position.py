class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.figure = None

    def add_figure(self, figure):
        self.figure = figure
