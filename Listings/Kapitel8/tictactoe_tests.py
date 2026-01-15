# tictactoe_tests.py
# Aus "Algorithmen in Python" Kapitel 8
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
from typing import List
from minimax import find_best_move
from tictactoe import TTTPiece, TTTBoard
from board import Move


class TTTMinimaxTestCase(unittest.TestCase):
    def test_easy_position(self):
        # In 1 Zug gewinnen
        to_win_easy_position: List[TTTPiece] = [TTTPiece.X, TTTPiece.O, TTTPiece.X,
                                                TTTPiece.X, TTTPiece.E, TTTPiece.O,
                                                TTTPiece.E, TTTPiece.E, TTTPiece.O]
        test_board1: TTTBoard = TTTBoard(to_win_easy_position, TTTPiece.X)
        answer1: Move = find_best_move(test_board1)
        self.assertEqual(answer1, 6)

    def test_block_position(self):
        # Muss den Sieg von O blockieren
        to_block_position: List[TTTPiece] = [TTTPiece.X, TTTPiece.E, TTTPiece.E,
                                             TTTPiece.E, TTTPiece.E, TTTPiece.O,
                                             TTTPiece.E, TTTPiece.X, TTTPiece.O]
        test_board2: TTTBoard = TTTBoard(to_block_position, TTTPiece.X)
        answer2: Move = find_best_move(test_board2)
        self.assertEqual(answer2, 2)

    def test_hard_position(self):
        # Den besten Zug finden, um in 2 Zügen zu gewinnen
        to_win_hard_position: List[TTTPiece] = [TTTPiece.X, TTTPiece.E, TTTPiece.E,
                                                TTTPiece.E, TTTPiece.E, TTTPiece.O,
                                                TTTPiece.O, TTTPiece.X, TTTPiece.E]
        test_board3: TTTBoard = TTTBoard(to_win_hard_position, TTTPiece.X)
        answer3: Move = find_best_move(test_board3)
        self.assertEqual(answer3, 1)


if __name__ == '__main__':
    unittest.main()


