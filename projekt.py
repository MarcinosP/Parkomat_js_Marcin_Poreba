import datetime

miesiace_MAX = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
monety = {"1gr": 1, "2gr": 2, "5gr": 5, "10gr": 10, "20gr": 20, "50gr": 50, "1zl": 100, "2zl": 200, "5zl": 500,
          "10zl": 1000, "20zl": 2000, "50zl": 5000}
dni_tygodnia_nazwy = {0: "poniedzialek", 1: "wtorek", 2: "sroda", 3: "czwartek", 4: "piatek", 5: "sobota",
                      6: "niedziela"}

teraz = datetime.datetime.now()
teraz_dzien = teraz.weekday()  # zwraca dzien tygodnia 0-poniedzialek 1-wtorek itd
teraz_nr_dnia = teraz.day

print((str(teraz)))
print(dni_tygodnia_nazwy[teraz_dzien])
print(teraz_nr_dnia)


def przelicz_czas(sekundy):
    # dostaje liczbe sekund zwraca liste wykupiony czas
    wykupiony_czas = {"d": 0, "h": 0, "m": 0, "s": 0}
    if sekundy < 0:
        exit(1)
    if sekundy < 60:
        wykupiony_czas["s"] += sekundy
        return wykupiony_czas
    elif sekundy < 3600:
        wykupiony_czas["s"] += sekundy % 60
        sekundy -= sekundy % 60
        wykupiony_czas["m"] += sekundy / 60
        return wykupiony_czas
    else:
        wykupiony_czas["s"] += sekundy % 60
        sekundy -= sekundy % 60
        wykupiony_czas["m"] += (sekundy % 3600) / 60
        sekundy -= sekundy % 3600
        wykupiony_czas["h"] += (sekundy / 3600)
        return wykupiony_czas


def uaktualnij_czas(wykupiony_czas):

    teraz = datetime.datetime.now()
    terazstring = (str(teraz)).split(" ")
    terazstring = terazstring[1].split(".")
    terazstring = terazstring[0].split(":")  # tablica stringow godzina,minuta,sekunda
    teraz_i = [int(i) for i in terazstring]

    wykupiony_czas["s"] += teraz_i[2]
    if wykupiony_czas["s"] > 59:
        wykupiony_czas["m"] += 1
        wykupiony_czas["s"] = wykupiony_czas["s"] % 59
    wykupiony_czas["m"] += teraz_i[1]


def zwroc_czas(kasa):
    # zwraca ilos czasu w sekundach w zaleznosci od podanej kwoty
    if (kasa <= 200):
        return kasa * 18
    elif (kasa <= 600):
        return 3600 + (kasa - 200) * 9
    else:
        return 7200 + (kasa - 600) * 7.2


def kup_bilet():
    numer_rejestracyjny = input("podaj numer rejestracyjny samochodu: ")
    while (1):
        wrzuc = input("wrzuć monetę")
        if wrzuc == 0:
            exit()
        czas = zwroc_czas(monety[wrzuc])
        print(czas / 60)

# kup_bilet()
