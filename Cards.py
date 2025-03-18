
class Fraction:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Fraction: {self.name}"

class Unit:
    def __init__(self, name, strength, fraction):
        self.name = name
        self.strength = strength
        self.fraction = fraction

    def __str__(self):
        return f"{self.name} {self.strength} {self.fraction}"

class Close_combat(Unit):
    def __init__(self, name, strength, fraction):
        super().__init__(name, strength, fraction)


class Ranged_combat(Unit):
    def __init__(self, name, strength, fraction):
        super().__init__(name, strength, fraction)


class Siege_combat(Unit):
    def __init__(self, name, strength, fraction):
        super().__init__(name, strength, fraction)


class Special_card(Unit):
    def __init__(self, name, action):
        super.__init__(name, action)