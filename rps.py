#!/usr/bin/env python3

from enum import Enum
from math import inf
from random import choice


class Penum(Enum):  # you know, like a pretty enum
    def __str__(self):
        # Note the f"{self.__class__.__name__}." prefix is omitted here too
        return self.name.replace("_", " ")


class Weapon(Penum):
    Rock = 0
    Paper = 1
    Scissors = 2


class ShootResult(Penum):
    Tie = 0
    Player_1_Won = 1
    Player_2_Won = 2


def shoot(p1weapon, p2weapon):
    return ShootResult((p1weapon.value - p2weapon.value) % 3)


def randweapon(WEAPONS=tuple(Weapon)):
    return choice(WEAPONS)


def main(NROUNDS=inf):
    print("  Round  │  Player 1  │  Player 2  │  Result        │  P1 Win %  │  P2 Win %\n" \
          "─────────┼────────────┼────────────┼────────────────┼────────────┼────────────")
    i = 0
    p1wins = p2wins = 0
    while i < NROUNDS:
        p1weapon = randweapon()
        p2weapon = randweapon()
        result = shoot(p1weapon, p2weapon)
        p1wins += result == ShootResult.Player_1_Won
        p2wins += result == ShootResult.Player_2_Won
        p1percent = p1wins / (p1wins + p2wins) if p1wins or p2wins else 0
        p2percent = p2wins / (p1wins + p2wins) if p1wins or p2wins else 0
        i += 1
        print(f"{i:8} │  {p1weapon:8}  │  {p2weapon:8}  │  {result:12}  │  {p1percent:8.2f}  │  {p2percent:8.2f}")
        try:
            input("\n  << Enter for another round, Ctrl+C to quit... >>\n")
        except KeyboardInterrupt:
            return


if __name__ == "__main__":
    main()
