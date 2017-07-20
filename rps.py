#!/usr/bin/env python3.6

from enum import Enum
from random import choice

from getch import getch  # pip install getch


class PPrintEnum(Enum):
    def __str__(self):
        return self.name.replace('_', ' ')

class Weapon(PPrintEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

def randweapon(WEAPONS=tuple(Weapon)):
    return choice(WEAPONS)

class ShootResult(PPrintEnum):
    Tie = 0
    Player_1_Won = 1
    Player_2_Won = 2

def shoot(p1weapon, p2weapon):
    return ShootResult((p1weapon.value - p2weapon.value) % 3)

def main(NROUNDS=float('inf'), p1move=randweapon, p2move=randweapon):
    print('Press any character to play another round, Ctrl+C to quit...\n')

    print('  Round  │  Player 1  │  Player 2  │  Result        │  P1 Win %  │  P2 Win %\n' \
          '─────────┼────────────┼────────────┼────────────────┼────────────┼────────────')
    i = 0
    p1wins = p2wins = 0
    while i < NROUNDS:
        p1weapon = p1move()
        p2weapon = p2move()
        result = shoot(p1weapon, p2weapon)
        p1wins += result == ShootResult.Player_1_Won
        p2wins += result == ShootResult.Player_2_Won
        p1percent = p1wins / (p1wins + p2wins) if p1wins or p2wins else 0
        p2percent = p2wins / (p1wins + p2wins) if p1wins or p2wins else 0
        i += 1
        print(f'{i:8} │  {p1weapon:8}  │  {p2weapon:8}  │  {result:12}  │  {p1percent:8.2f}  │  {p2percent:8.2f}')
        getch()

if __name__ == '__main__':
    main()
