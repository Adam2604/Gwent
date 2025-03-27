
class Player:
    def __init__(self, name):
        self.name = name
        self.cards_in_the_deck = []
        self.cards_in_the_game = []

    def use_card(self, card):
        self.cards_in_the_deck.append(card)
        print(f"{self.name} used {card.name} (Strength: {card.strength})")

class Fraction:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Fraction: {self.name}"

class Unit:
    def __init__(self, name, strength, fraction, type,  effect = None):
        self.name = name
        self.strength = strength
        self.fraction = fraction
        self.type = type
        self.effect = effect

    def __str__(self):
        return f"{self.name} {self.strength} {self.fraction} {self.effect}"

class Close_combat(Unit):
    def __init__(self, name, strength, fraction, effect = None):
        super().__init__(name, strength, fraction, "Close_combat", effect)


class Ranged_combat(Unit):
    def __init__(self, name, strength, fraction, effect = None):
        super().__init__(name, strength, fraction, "Ranged_combat", effect)


class Siege_combat(Unit):
    def __init__(self, name, strength, fraction, effect = None):
        super().__init__(name, strength, fraction, "Siege_combat", effect)


class Special_card(Unit):
    def __init__(self, name, effect):
        super().__init__(name, None, None, "Special_card", effect)


