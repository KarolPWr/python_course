from collections import defaultdict
from enum import Enum
from random import randint, choice
from typing import List, Dict


class Color(Enum):
    red = 'RED'
    green = 'GREEN'


class WeightCategory(Enum):
    light = 'LIGHT'
    heavy = 'HEAVY'


class Apple:
    def __init__(self, color: Color, weight: int):
        self.color = color
        self.weight = weight

    def __str__(self):
        return f'Apple(color={self.color.value}, weight={self.weight})'

    @staticmethod
    def generate_random_apple():
        return Apple(color=choice(list(Color)), weight=randint(50, 150))

    def get_weight_category(self) -> WeightCategory:
        """Return WeightCategory.light if weight is below 100"""
        if self.weight < 100:
            return WeightCategory.light
        else:
            return WeightCategory.heavy


def group_apples_by_color(apples: List[Apple]) -> Dict[Color, List[Apple]]:
    apples_by_color = defaultdict(lambda: list())
    for apple in apples:
        apples_by_color[apple.color].append(apple)

    return apples_by_color


def group_apples_by_color_then_weight(apples: List[Apple]) -> Dict[Color, Dict[WeightCategory, List[Apple]]]:
    # a.color == Color.red and a.weight < 100
    color_weight = defaultdict(lambda: defaultdict(lambda: list()))
    for apple in apples:
        color_weight[apple.color][apple.get_weight_category()].append(apple)

    return color_weight


if __name__ == '__main__':
    light_apple = Apple(color=Color.red, weight=55)
    assert light_apple.get_weight_category() == WeightCategory.light

    random_apple = Apple.generate_random_apple()
    print(random_apple)

    # Exercise1: generate 100 random apples
    apples = list()
    for _ in range(100):
        apples.append(Apple.generate_random_apple())
    assert apples

    # Exercise2: group apples by color
    apples_by_color = group_apples_by_color(apples)

    assert apples_by_color[Color.red]
    assert all(a.color == Color.red for a in apples_by_color[Color.red])

    # Exercise3: group apples by color, then by WeightCategory
    apples_by_color_and_weight = group_apples_by_color_then_weight(apples)
    assert apples_by_color_and_weight[Color.red][WeightCategory.light]
    assert all(
        a.color == Color.red and a.weight < 100
        for a in apples_by_color_and_weight[Color.red][WeightCategory.light]
    )
