from Classes import *
from Cards import *

def plus_one_point(player, played_card):
    # zwiększa siłę każdej karty w grze tego samego typu o 1 punkt

    for card in player.cards_in_the_game:
        if card.type == played_card.type:
            card.strenght += 1


def double_points(player, played_card):
    #podwaja siłę tych samych kart

    for card in player.cards_in_the_game:
        if card.name == played_card.name:
            card.strength *= 2
    played_card.strenght *= 2