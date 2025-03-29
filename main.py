from Cards import special_cards, Northern_Realms_cards


def wybierz_talie(gracz_num):
    units = Northern_Realms_cards[:]  # Tworzymy kopię listy kart jednostek
    special = special_cards[:]  # Tworzymy kopię listy kart specjalnych
    chosen_cards = []  # Lista, w której będą przechowywane wybrane karty
    chosen_special_cards = []  # Lista wybranych kart specjalnych

    print(f"\nGracz {gracz_num}, wybierz karty do swojej talii (minimum 22 jednostki).")
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

    # Po zakończeniu wyboru zwrócimy pełną talię
    return chosen_cards, chosen_special_cards


if __name__ == "__main__":
    talia_gracza1_jednostki, talia_gracza1_specjalne = wybierz_talie(1)

    talia_gracza2_jednostki, talia_gracza2_specjalne = wybierz_talie(2)

    print("\nGracz 1 - Talia:")
    for card in talia_gracza1_jednostki:
        print(f"{card.name} - Siła: {card.strength}")
    for card in talia_gracza1_specjalne:
        print(f"{card.name} - Efekt: {card.effect}")

    print("\nGracz 2 - Talia:")
    for card in talia_gracza2_jednostki:
        print(f"{card.name} - Siła: {card.strength}")
    for card in talia_gracza2_specjalne:
        print(f"{card.name} - Efekt: {card.effect}")
