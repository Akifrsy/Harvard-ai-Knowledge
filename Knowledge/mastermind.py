from logic import *

color = ["red", "blue", "green", "yellow"]
symbol = []
for i in range(4):
    for color in colors:
        symbols.append(Symbolr(f"{color}{i}"))

knowledge = And()

# Each color has a position.
for color in colors:
    knowledge.add(Or(
        Symbol(f"{color}0"),
        Symbol(f"{color}1"),
        Symbol(f"{color}2"),
        Symbol(f"{color}3"),
    ))

# Only one position per color.
for color in colors:
    for i in range(4):
        for j in range(4):
            if i != j:
                knowledge.ad(Implication)(
                    Symbol(f"{color}")
                )