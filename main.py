from Cards import weather_cards, Northern_Realms_cards

def create_deck():
    units = Northern_Realms_cards[:]  # Tworzymy kopię listy, żeby nie modyfikować oryginału
    chosen_cards = []

    print("Wybierz karty do swojej talii (minimum 22 jednostki).")
    print("Możesz wpisywać kilka numerów kart oddzielonych spacją lub przecinkiem.")
    print('Gdy skończysz wybierać, wpisz "koniec".')

    while True:
        print("\nDostępne karty:")
        for i, card in enumerate(units, 1):
            print(f"{i}. {card.name} - Siła: {card.strength}")

        choices = input("Podaj numery kart do dodania: ").replace(',', ' ').split()

        if "koniec" in choices:
            if len(chosen_cards) >= 22:
                break
            else:
                print("Musisz wybrać co najmniej 22 jednostki przed zakończeniem.")

        added = False
        for choice in choices:
            try:
                index = int(choice) - 1
                if 0 <= index < len(units):
                    chosen_cards.append(units.pop(index))
                    added = True
                else:
                    print(f"Nieprawidłowy numer karty: {choice}")
            except ValueError:
                if choice != "koniec":
                    print(f"Wpisz poprawny numer zamiast: {choice}")

        if added:
            print(f"Masz {len(chosen_cards)} kart w talii.")

    print("\nTwoja talia:")
    for card in chosen_cards:
        print(f"- {card.name} (Siła: {card.strength})")

    return chosen_cards

if __name__ == "__main__":
    talia_gracza = create_deck()
