import random
from abc import abstractmethod
from enum import Enum
from typing import Union

# result
# -1 = opponent win
# 0 = draw
# 1 = i win

matrix = [
    [0, -1, 1],
    [1, 0, -1],
    [-1, 1, 0]
]


class Figure(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    def result(self, other: 'Figure') -> int:
        return matrix[self.value][other.value]


class AlgoBase:
    @abstractmethod
    def bet(self) -> Figure:
        raise NotImplementedError()

    @abstractmethod
    def opponents_result(self, figure: Figure, result: int):
        raise NotImplementedError()


class AlgoRandom(AlgoBase):
    def bet(self) -> Figure:
        return random.choice(list(Figure))

    def opponents_result(self, figure: Figure, result: int):
        pass


class AlgoRock(AlgoBase):
    def bet(self) -> Figure:
        return Figure.ROCK

    def opponents_result(self, figure: Figure, result: int):
        pass


class AlgoFirst(AlgoBase):
    bets = [
        Figure.SCISSORS,
        Figure.ROCK,
        Figure.PAPER
    ]

    def __init__(self):
        self.prev_opponent_bet: Union[Figure, None] = None

    def bet(self) -> Figure:
        if self.prev_opponent_bet is None:
            return random.choice(list(Figure))
        else:
            fig = self.bets[self.prev_opponent_bet.value]
            return fig

    def opponents_result(self, figure: Figure, result: int):
        self.prev_opponent_bet = figure


class AlgoSecond(AlgoFirst):
    def __init__(self):
        super().__init__()
        self.double_fig: Union[Figure, None] = None

    def bet(self) -> Figure:
        if self.double_fig is None:
            return random.choice(list(Figure))
        else:
            return self.bets[self.double_fig.value]

    def opponents_result(self, figure: Figure, result: int):
        if figure == self.prev_opponent_bet:
            self.double_fig = figure
        else:
            self.double_fig = None

        self.prev_opponent_bet = figure


def test(algo1: AlgoBase, algo2: AlgoBase, count: int) -> (int, int, int):
    win_algo1 = 0
    win_algo2 = 0
    for i in range(0, count):
        algo1_bet = algo1.bet()
        algo2_bet = algo2.bet()

        result = algo1_bet.result(algo2_bet)
        algo1.opponents_result(algo2_bet, result)
        algo2.opponents_result(algo1_bet, result * -1)

        win_algo1 += (result == 1)
        win_algo2 += (result == -1)

    return win_algo1, win_algo2, count - win_algo1 - win_algo2


def check_results(algo1: AlgoBase, algo2: AlgoBase, n: int):
    win_1, win_2, draw = test(algo1, algo2, n)
    print(
        f'{algo1.__class__.__name__} advantage over {algo2.__class__.__name__} with {n} iterations = {win_1 / (n - draw)}, draw = {draw} ({draw / n}%)')


n = 1000000
check_results(AlgoRandom(), AlgoRandom(), n)
check_results(AlgoFirst(), AlgoRandom(), n)
check_results(AlgoSecond(), AlgoRandom(), n)
check_results(AlgoRock(), AlgoRandom(), n)
# check_results(AlgoSecond(), AlgoFirst(), n)
# check_results(AlgoSecond(), AlgoRock(), n)
# check_results(AlgoFirst(), AlgoRock(), n)
