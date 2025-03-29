from Effects import plus_one_point, double_points, weather_one_point

class Player:
    def __init__(self, name):
        self.name = name
        self.cards_in_the_deck = [] #kart w talii
        self.cards_in_the_game = [] #karty wyłożone na stół
        self.points = 0

    def use_card(self, card):
        if card in self.cards_in_the_deck:
            self.cards_in_the_deck.remove(card)
            self.cards_in_the_deck.append(card)
            self.points += card.strength
            print(f"{self.name} used {card.name} (Strength: {card.strength})")

            if card.effect == "plus_one_point":
                plus_one_point(self, card)

            if card.effect == "double_points":
                double_points(self, card)

            if card.effect == "weather_one_point":
                weather_one_point(self, card)

class Fraction:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Fraction: {self.name}"

class Unit:
    def __init__(self, name, strength, fraction, unit_type="Unknown", effect = None):
        self.name = name
        self.strength = strength
        self.fraction = fraction
        self.type = unit_type
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

class Hero(Unit):
    def __init__(self, name, fraction, effect = None):
        super().__init__(name, 10, fraction, "Hero", effect)
        self.is_hero = True #flaga zaznaczająca że to bohater