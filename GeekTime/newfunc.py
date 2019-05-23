"""
    Pathlib(3.4+)
    Type hinting(3.5+)
    Enumerations(3.4+)
"""
from pathlib import Path
from enum import Enum, auto


def show_path(path: str):
    current_path = Path(path)
    print(current_path.absolute())


def sentence_has_animal(sentence: str) -> bool:
    return "animal" in sentence


class Monster(Enum):
    ZOMBIE = auto()
    WARRIOR = auto()
    BEAR = auto


if __name__ == "__main__":
    show_path('hdd')
    print(sentence_has_animal("Donald had a farm without animals"))
    for monster in Monster:
        print(monster)
