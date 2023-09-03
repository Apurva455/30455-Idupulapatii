class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level


def change(poke, level):
    poke.level = level
    level = 50
    poke = Pokemon("Gengar", 1)


if __name__ == "__main__":
    p = Pokemon("Pikachu", 17)
    level = 100
    change(p, level)
    print("Name:", p.name, ", Level:", p.level)
