from Cards import *

#zbiór kart pogodowych
weather_cards = [
    Special_card("Czyste niebo", clear)
    Special_card("Czyste niebo", clear)
    Special_card("Ulewny deszcz", one_point)
    Special_card("Ulewny deszcz", one_point)
    Special_card("Gęsta mgła", one_point)
    Special_card("Gęsta mgła", one_point)
    Special_card("Gęsta mgła", one_point)
    Special_card("Trzaskający mróz", one_point)
    Special_card("Trzaskający mróz", one_point)
    Special_card("Trzaskający mróz", one_point)
]

#zbiór kart Królestwa Północy
Northern_Realms_cards = [
    Siege_combat("Mistrz Oblężeń z Kaedwen", 1, "Królestwo Północy"),  # efekt +1 dla wszystkich
    Siege_combat("Mistrz Oblężeń z Kaedwen", 1, "Królestwo Północy"),  # efekt +1 dla wszystkich
    Siege_combat("Mistrz Oblężeń z Kaedwen", 1, "Królestwo Północy"),  # efekt +1 dla wszystkich
    Close_combat("Redański Piechur", 1, "Królestwo Północy"),
    Close_combat("Redański Piechur", 1, "Królestwo Północy"),
    Close_combat("Biedna Pierdolona Piechota", 1, "Królestwo Północy"),  # efekt - połączone podwajają punkty swoje
    Close_combat("Biedna Pierdolona Piechota", 1, "Królestwo Północy"),
    Close_combat("Biedna Pierdolona Piechota", 1, "Królestwo Północy"),
    Close_combat("Talar", 1, "Królestwo Północy"),  # szpieg
    Close_combat("Yarpen Zirgin", 2, "Królestwo Północy"),
    Close_combat("Komandos Niebieskich Pasów", 4, "Królestwo Północy"),  # połączone podwajają punkty swoje
    Close_combat("Komandos Niebieskich Pasów", 4, "Królestwo Północy"),
    Close_combat("Komandos Niebieskich Pasów", 4, "Królestwo Północy"),
    Ranged_combat("Sheldon Skaggs", 4, "Królestwo Północy"),
    Ranged_combat("Sabrina Glevissig", 4, "Królestwo Północy"),
    Close_combat("Sigismund Dijkstra", 4, "Królestwo Północy"),  # szpieg
    Siege_combat("Medyczka Burej Chorągwi", 5, "Królestwo Północy"),  # przywraca kartę ze stosu odrzuconych
    Ranged_combat("Rębacze z Crifrid", 5, "Królestwo Północy"),  # połączone podwajają punkty swoje
    Ranged_combat("Rębacze z Crifrid", 5, "Królestwo Północy"),
    Ranged_combat("Rębacze z Crifrid", 5, "Królestwo Północy"),
    Close_combat("Książe Stannis", 5, "Królestwo Północy"),  # szpieg
    Ranged_combat("Sheala the Tancarville", 5, "Królestwo Północy"),
    Ranged_combat("Keira Metz", 5, "Królestwo Północy"),
    Close_combat("Zygfryd z Denesle", 5, "Królestwo Północy"),
    Close_combat("Ves", 5, "Królestwo Północy"),
    Siege_combat("Wieża oblężnicza", 6, "Królestwo Północy"),
    Siege_combat("Balista", 6, "Królestwo Północy"),
    Siege_combat("Trebusz", 6, "Królestwo Północy"),
    Siege_combat("Trebusz", 6, "Królestwo Północy"),
    Ranged_combat("Detmold", 6, "Królestwo Północy"),
    Siege_combat("Katapulta", 8, "Królestwo Północy"),  # połączone podwajają punkty swoje
    Siege_combat("Katapulta", 8, "Królestwo Północy"),
    Ranged_combat("Philippa Eilhart", 10, "Królestwo Północy"),  # bohater
    Close_combat("Esterad Thyssen", 10, "Królestwo Północy"),  # bohater
    Close_combat("Jan Natalis", 10, "Królestwo Północy"),  # bohater
    Close_combat("Vernon Roche", 10, "Królestwo Północy")  # bohater
]


