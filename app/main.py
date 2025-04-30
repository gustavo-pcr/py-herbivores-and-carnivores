class Animal:
    alive = []

    def __init__(self, health: int, name: str, hidden: bool) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden

    def alive_animals(self) -> None:
        if self in Animal.alive:
            if self.health <= 0:
                Animal.alive.remove(self)
        elif self.health > 0:
            Animal.alive.append(self)

    @classmethod
    def show_alive(cls) -> None:
        for animal in cls.alive:
            output = {
                "Name": {animal.name},
                "Health": {animal.health},
                "Hidden": {animal.hidden}
            }
            print(output)


class Herbivore(Animal):
    def hide(self) -> bool:
        return self.hidden


class Carnivore(Animal):
    def bite(self, herbivore: Animal) -> int:
        if not herbivore.hidden:
            herbivore.health -= 50
        return herbivore.health
