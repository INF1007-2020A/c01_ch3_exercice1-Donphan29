#!/usr/bin/env python
# -*- coding: utf-8 -*-
imo

def square_root(number: int) -> float:
    # TODO completer la fonction
    return number**(1/2)


def square(number: int) -> int:
    # TODO completer la fonction
    return math.pow(number, 2)


def main() -> None:
    for i in range(25):
        print(f"Square root: {square_root(i)}, Square: {square(i)}")


if __name__ == '__main__':
    main()
