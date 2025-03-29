from Cards import special_cards, Northern_Realms_cards
from database import initialize_db, add_player, save_player_deck, load_player_deck
from Classes import Unit


def wybierz_talie(player_name):
    saved_deck = load_player_deck(player_name)

    if saved_deck:
        print(f"\nZnaleziono zapisaną talię dla {player_name}:")
        for card in saved_deck:
            print(f"- {card[0]} (Siła: {card[1]})")
        choice = input("Czy chcesz załadować tę talię? (tak/nie): ").lower()
        if choice == "tak":
            return [Unit(*card) for card in saved_deck], []

    units = Northern_Realms_cards[:]
    special = special_cards[:]
    chosen_cards = []
    chosen_special_cards = []

    print(f"\n{player_name}, wybierz karty do swojej talii (minimum 22 jednostki).")
    print("Możesz wpisywać kilka numerów kart oddzielonych spacją lub przecinkiem.")
    print('Gdy skończysz wybierać jednostki, wpisz "koniec".')

    # Wybór kart jednostek
    while True:
        print("\nDostępne karty jednostek:")
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

    # Wyświetlenie kart wybranych przez gracza
    print("\nTwoja talia jednostek:")
    for card in chosen_cards:
        print(f"- {card.name} (Siła: {card.strength})")

    # Wybór kart specjalnych
    print("\nTeraz możesz wybrać karty specjalne (opcjonalnie).")
    print("Możesz wpisać numery kart specjalnych oddzielone spacją lub przecinkiem.")
    print('Jeśli nie chcesz wybrać żadnej, wpisz "koniec".')

    while True:
        print("\nDostępne karty specjalne:")
        for i, card in enumerate(special, 1):
            print(f"{i}. {card.name} - Efekt: {card.effect}")

        choices = input("Podaj numery kart specjalnych do dodania: ").replace(',', ' ').split()
        if "koniec" in choices:
            break

        added = False
        for choice in choices:
            try:
                index = int(choice) - 1
                if 0 <= index < len(special):
                    chosen_special_cards.append(special.pop(index))
                    added = True
                else:
                    print(f"Nieprawidłowy numer karty: {choice}")
            except ValueError:
                if choice != "koniec":
                    print(f"Wpisz poprawny numer zamiast: {choice}")

        if added:
            print(f"Masz {len(chosen_special_cards)} kart specjalnych w talii.")

    # Wyświetlenie kart specjalnych wybranych przez gracza
    print("\nTwoje karty specjalne:")
    for card in chosen_special_cards:
        print(f"- {card.name} (Efekt: {card.effect})")

    # Zapytanie gracza, czy chce zapisać talię
    save_choice = input("\nCzy chcesz zapisać tę talię w bazie danych? (tak/nie): ").lower()

    if save_choice == "tak":
        add_player(player_name)
        save_player_deck(player_name, chosen_cards + chosen_special_cards)
        print("Talia została zapisana w bazie danych.")
    else:
        print("Talia nie została zapisana.")

    return chosen_cards, chosen_special_cards



if __name__ == "__main__":
    initialize_db()

    # Pobieranie nazw graczy
    player1_name = input("Podaj nazwę dla Gracza 1: ").strip()
    player2_name = input("Podaj nazwę dla Gracza 2: ").strip()

    # Wybór talii dla graczy z podanymi nazwami
    talia_gracza1_jednostki, talia_gracza1_specjalne = wybierz_talie(player1_name)
    talia_gracza2_jednostki, talia_gracza2_specjalne = wybierz_talie(player2_name)

    # Wyświetlenie talii graczy
    print(f"\n{player1_name} - Talia:")
    for card in talia_gracza1_jednostki:
        print(f"{card.name} - Siła: {card.strength}")
    for card in talia_gracza1_specjalne:
        print(f"{card.name} - Efekt: {card.effect}")

    print(f"\n{player2_name} - Talia:")
    for card in talia_gracza2_jednostki:
        print(f"{card.name} - Siła: {card.strength}")
    for card in talia_gracza2_specjalne:
        print(f"{card.name} - Efekt: {card.effect}")

