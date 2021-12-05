#!/usr/bin/env python3


class BingoBoard:
    def __init__(self, board):
        self.board = board
        self.marks = []
        for row in self.board:
            row_entry = [False] * len(row)
            self.marks.append(row_entry)

    def _is_entire_column_marked(self, column_index):
        for row in self.marks:
            if row[column_index] is False:
                return False
        return True

    def _is_entire_row_marked(self, row_index):
        row_length = len(self.marks[row_index])
        return self.marks[row_index] == [True] * row_length

    def _sum_marked_values(self):
        values_sum = 0
        for row_index, row in enumerate(self.board):
            for col_index, board_value in enumerate(row):
                if self.marks[row_index][col_index] is True:
                    values_sum += board_value
        return values_sum

    def _sum_unmarked_values(self):
        values_sum = 0
        for row_index, row in enumerate(self.board):
            for col_index, board_value in enumerate(row):
                if self.marks[row_index][col_index] is False:
                    values_sum += board_value
        return values_sum

    def is_winner(self):
        for row_index in range(len(self.marks)):
            if self._is_entire_row_marked(row_index):
                return True
        for column_index in range(len(self.marks[0])):
            if self._is_entire_column_marked(column_index):
                return True
        return False

    def mark(self, number):
        for row_index, row in enumerate(self.board):
            if number in row:
                col_index = row.index(number)
                self.marks[row_index][col_index] = True
        return

    def get_score(self, last_number_drawn):
        def calculate_score():
            unmarked_values_sum = self._sum_unmarked_values()
            return unmarked_values_sum * last_number_drawn

        for row_index in range(len(self.marks)):
            if self._is_entire_row_marked(row_index):
                return calculate_score()

        for column_index in range(len(self.marks[0])):
            if self._is_entire_column_marked(column_index):
                return calculate_score()

        return None


class Bingo:
    def __init__(self, all_drawn_numbers, boards):
        self.all_drawn_numbers = all_drawn_numbers
        self.boards = [BingoBoard(board) for board in boards]
        self.drawn_number_index = None
        self.drawn_number = None
        self.winners = []

    def draw(self):
        if self.drawn_number_index is None:
            self.drawn_number_index = 0
        else:
            self.drawn_number_index += 1
        self.drawn_number = self.all_drawn_numbers[self.drawn_number_index]

    def mark_boards(self):
        for board in self.boards:
            board.mark(self.drawn_number)
            if board not in self.winners and board.is_winner():
                self.winners.append(board)

    def get_winner_score(self, winner_index):
        return self.winners[winner_index].get_score(self.drawn_number)


def parse_file(input_file):
    with open(input_file, "r", encoding="utf-8") as fp:
        file_lines = [line.strip() for line in fp.readlines()]
    drawn_nums = list(map(int, file_lines[0].split(",")))
    boards = []
    for i in range(1, len(file_lines)):
        if file_lines[i] == "":
            boards.append([])
            continue
        board_row = file_lines[i].split(" ")
        board_row = list(filter(None, board_row))
        board_row = list(map(int, board_row))
        boards[-1].append(board_row)
    return (drawn_nums, boards)


def solution_1(input_file):
    drawn_nums, boards = parse_file(input_file)
    bingo = Bingo(drawn_nums, boards)

    while not bingo.winners:
        bingo.draw()
        bingo.mark_boards()

    winner_score = bingo.get_winner_score(0)

    return winner_score


def solution_2(input_file):
    drawn_nums, boards = parse_file(input_file)
    bingo = Bingo(drawn_nums, boards)

    while len(bingo.winners) < len(boards):
        bingo.draw()
        bingo.mark_boards()

    winner_score = bingo.get_winner_score(-1)

    return winner_score
