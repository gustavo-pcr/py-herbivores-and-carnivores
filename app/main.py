class Animal:
    alive = []

    def __init__(self, health: int, name: str, hidden: bool) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden

    def alive_animals(self) -> None:
        if self.health > 0:
            Animal.alive.append({
                "Name": self.name,
                "Health": self.health,
                "Hidden": self.hidden
            })


class Herbivore(Animal):
    def hide(self) -> bool:
        hidden_bool = self.hidden
        return not hidden_bool


class Carnivore(Animal):
    def bite(self, herbivore: Animal) -> int:
        if herbivore.hidden is True:
            herbivore.health -= 50
        return herbivore.health
