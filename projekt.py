import datetime
from datetime import timedelta

monety = {"1gr": 1, "2gr": 2, "5gr": 5, "10gr": 10, "20gr": 20, "50gr": 50, "1zl": 100, "2zl": 200, "5zl": 500,
          "10zl": 1000, "20zl": 2000, "50zl": 5000}
kasa = 0

teraz = datetime.datetime.now()
teraz_dzien = teraz.weekday()  # zwraca dzien tygodnia 0-poniedzialek 1-wtorek itd
teraz_nr_dnia = teraz.day

teraz = datetime.datetime.now()
terazstring = (str(teraz)).split(" ")
terazstring = terazstring[1].split(".")
terazstring = terazstring[0].split(":")  # tablica stringow godzina,minuta,sekunda


def dodajMonete(ile, iloraz=1):
    """Funcja dodająca monety do ogólnej ilosci pieniedzy"""
    global kasa
    for i in range(iloraz):
        kasa += monety[ile]


def CzasUserFriendly(data):
    """zamienia format datatime na string wsywietlajacy date zgodnie z zaleceniami"""
    tmp = (str(data)).split(" ")
    wynik = tmp[0]
    tmp = tmp[1].split(":")
    wynik = wynik + " " + tmp[0] + ":" + tmp[1]
    return wynik


print(CzasUserFriendly(teraz))


def przelicz_czas(sekundy):
    """Funkcja otrzymuje ilosc sekund i zamienia to na zbior: dni godziny minuty i sekundy"""
    wykupiony_czas = {"d": 0, "h": 0, "m": 0, "s": 0}
    if sekundy < 0:
        exit(1)
    if sekundy < 60:
        wykupiony_czas["s"] += sekundy
    elif sekundy < 3600:
        wykupiony_czas["s"] += sekundy % 60
        sekundy -= sekundy % 60
        wykupiony_czas["m"] += sekundy / 60
    elif sekundy < 86400:
        wykupiony_czas["s"] += sekundy % 60
        sekundy -= sekundy % 60
        wykupiony_czas["m"] += (sekundy % 3600) / 60
        sekundy -= sekundy % 3600
        wykupiony_czas["h"] += (sekundy / 3600)
    else:
        wykupiony_czas["s"] += sekundy % 60
        sekundy -= sekundy % 60
        wykupiony_czas["m"] += (sekundy % 3600) / 60
        sekundy -= sekundy % 3600
        wykupiony_czas["h"] += (sekundy / 3600) % 24
        sekundy -= (sekundy / 3600) % 24
        wykupiony_czas["d"] += (sekundy / 86400)
    return wykupiony_czas


# datetime.now() + timedelta(days=1)
def aktualizujCzas(sekundy):
    # wyjazd = datetime.datetime.now()
    # platnyHMin = datetime.time(8, 0, 0)
    # platnyHMax = datetime.time(20, 0, 0)
    # Ddzisiaj = teraz.weekday()
    # platnyDMin = 0
    # platnyDMax = 4
    # while(sekundy>0):
    #     if Ddzisiaj > 4:
    #         pass
    pass


def zwroc_czas(kasa):
    """Funkcja otrzymuje kwote w groszach i zwraca ilosc wykupionego czasu w sekundach"""
    if (kasa <= 200):
        return kasa * 18
    elif (kasa <= 600):
        return 3600 + (kasa - 200) * 9
    else:
        return 7200 + (kasa - 600) * 7.2

# czas = zwroc_czas(601)
# print(czas)
# wykupiony = przelicz_czas(czas)
# print(wykupiony)
# print(uaktualnij_czas(wykupiony))
# dodajMonete("1zl")
# print(kasa)
