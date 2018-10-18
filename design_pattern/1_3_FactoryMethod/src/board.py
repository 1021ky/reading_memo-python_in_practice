# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# Copyright © 2012-13 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version. It is provided for
# educational purposes and is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import io
import itertools
import os
import sys
import tempfile
import unicodedata

# チェスの駒の種類
DRAUGHT, PAWN, ROOK, KNIGHT, BISHOP, KING, QUEEN = ("DRAUGHT", "PAWN",
        "ROOK", "KNIGHT", "BISHOP", "KING", "QUEEN")
# 駒の色
BLACK, WHITE = ("BLACK", "WHITE")


def main():
    checkers = CheckersBoard()
    print(checkers)

    chess = ChessBoard()
    print(chess)

    # windows向けの処理
    if sys.platform.startswith("win"):
        filename = os.path.join(tempfile.gettempdir(), "gameboard.txt")
        with open(filename, "w", encoding="utf-8") as file:
            file.write(sys.stdout.getvalue())
        print("wrote '{}'".format(filename), file=sys.__stdout__)

# windows向けの処理
if sys.platform.startswith("win"):
    def console(char, background):
        return char or " "
    sys.stdout = io.StringIO()
else:
    def console(char, background):
        return "\x1B[{}m{}\x1B[0m".format(
                43 if background == BLACK else 47, char or " ")


class AbstractBoard:
    """ボードの基底抽象クラス"""
    def __init__(self, rows, columns):
        self.board = [[None for _ in range(columns)] for _ in range(rows)]
        self.populate_board()


    def populate_board(self):
        """ボードに駒を置く"""
        raise NotImplementedError()


    def __str__(self):
        squares = []
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                square = console(piece, BLACK if (y + x) % 2 else WHITE)
                squares.append(square)
            squares.append("\n")
        return "".join(squares)


class CheckersBoard(AbstractBoard):
    """チェッカーボードクラス"""

    def __init__(self):
        self.populate_board()


    def populate_board(self): # Thanks to Doug Hellmann for the idea!
        """盤に駒を置く"""
        def black():
            """黒駒インスタンスを生成する"""
            return create_piece(DRAUGHT, BLACK)
        def white():
            """白駒インスタンスを生成する"""
            return create_piece(DRAUGHT, WHITE)
        # 各行の左から2マス分の組み合わせを定義
        rows = ((None, black()), (black(), None), (None, black()),
                (black(), None),            # 4 black rows -> 黒側
                (None, None), (None, None), # 2 blank rows -> 真ん中の空き
                (None, white()), (white(), None), (None, white()),
                (white(), None))            # 4 white rows -> 白側
        # cycleで左から2マスのもので長い1行を作る。その後、ボードに必要な個数のインスタンスをisliceで取得する。
        # それを全行分繰り返す。
        self.board = [list(itertools.islice(
            itertools.cycle(squares), 0, len(rows))) for squares in rows]


class ChessBoard(AbstractBoard):
    """チェスボードクラス"""

    def __init__(self):
        super().__init__(8, 8)


    def populate_board(self):
        """盤に駒を置く"""
        for row, color in ((0, BLACK), (7, WHITE)):
            for columns, kind in (((0, 7), ROOK), ((1, 6), KNIGHT),
                    ((2, 5), BISHOP), ((3,), QUEEN), ((4,), KING)):
                for column in columns:
                    self.board[row][column] = create_piece(kind, color)
        for column in range(8):
            for row, color in ((1, BLACK), (6, WHITE)):
                self.board[row][column] = create_piece(PAWN, color)


def create_piece(kind, color):
    """指定された色と種類の名前のPieceクラスの子クラスのインスタンスを生成する"""
    color = "White" if color == WHITE else "Black"
    name = {DRAUGHT: "Draught", PAWN: "ChessPawn", ROOK: "ChessRook",
            KNIGHT: "ChessKnight", BISHOP: "ChessBishop",
            KING: "ChessKing", QUEEN: "ChessQueen"}[kind]
    return globals()[color + name]()


class Piece(str):

    __slots__ = ()


# Unicodeに駒の文字が定義されている。そのコードの名前のクラスを定義する
for code in itertools.chain((0x26C0, 0x26C2), range(0x2654, 0x2660)):
    char = chr(code)
    print(f'char:{char}')
    name = unicodedata.name(char).title().replace(" ", "")
    if name.endswith("sMan"):
        name = name[:-4]
    # 定義するメソッドのコンストラクタの引数として駒の文字が渡るようにする
    new = (lambda c: lambda Class: Piece.__new__(Class, c))(char)
    new.__name__ = "__new__"
    # Pieceクラスを継承して属性なしのクラスを定義してglobalで使えるようにする
    Class = type(name, (Piece,), dict(__slots__=(), __new__=new))
    globals()[name] = Class


if __name__ == "__main__":
    main()
