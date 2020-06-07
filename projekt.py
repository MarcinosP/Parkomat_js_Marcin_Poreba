import datetime
from datetime import timedelta
import exceptions as e
from tkinter import messagebox


class Monety:
    """
    klasa reprezentujaca monety

    Atrybuty
    __monety: dictionary
        slownik zawierajacy wszystkie dostepne monety{str:int}
    __drobne: dictionary
        slownik zwierajacy monety zaliczano jako drobne

    Metody
    getwartosc():
        zwraca prywatna zmienna __wartosc

    getmonety():
        zwraca prywatny slownik __monety

    getdrobne():
        zwraca prywatny slownik __drobne
    """
    __monety = {"1gr": 1, "2gr": 2, "5gr": 5, "10gr": 10, "20gr": 20, "50gr": 50, "1zl": 100, "2zl": 200, "5zl": 500,
                "10zl": 1000, "20zl": 2000, "50zl": 5000}
    __drobne = {x for x in __monety.values() if x <= 500}

    def __init__(self, __wartosc):
        """
        :param __wartosc: wartosc monety
        """

        self.__wartosc = self.__monety[__wartosc]

    def getwartosc(self):
        """
        :return: prywatna zmienna __wartosc
        """

        return self.__wartosc

    def getmonety(self):
        """
        :return: prywatna zmienna __monety
        """

        return self.__monety

    def getdrobne(self):
        """
        :return: prywatna zmienna __drobne
        """
        return self.__drobne


class Skarbonka(Monety):
    """
    klasa reprezentujaca zbior monet ktore wrzucil uzytkownik programu do parkomatu

    Metody
    dodajMonete(m, ile=1)
        Funkcja dodajaca monete do skarbonki

    warotsc_w_skarbonce()
        Funkcja zwraca warotsc wszystkich monet w skarbonce

    zwroc_czas()
        Funkcja sprawdza ile jest monet w skarbonce i zwraca ilosc wykupionego czasu w sekundach
        zgodnie z okreslonym przelicznikiem
    """

    def __init__(self, __wartosc):
        """
        :param __wartosc: wartosc monety
        """
        super().__init__(__wartosc)
        self.__lista = []
        self.__licznikmonet = []

    def dodajMonete(self, m, ile=1):
        """
        :param m: obiekt monety jaką chcesz dodać
        :param ile: ilość monet jaką chcesz dodać
        """
        try:
            if len(self.__licznikmonet) > 199:
                raise e.PrzepelnienieDrobnych
            if isinstance(m, Monety):
                for i in range(ile):
                    if len(self.__licznikmonet) > 199:
                        raise e.PrzepelnienieDrobnych
                    self.__lista.append(m)
                    if (m.getwartosc() in self.getdrobne()):
                        self.__licznikmonet.append(m)
            else:
                print("Przesłany obiekt nie jest monetą")
        except (e.PrzepelnienieDrobnych):
            messagebox.showwarning("Przepełnienie", e.PrzepelnienieDrobnych.message)

    def warotsc_w_skarbonce(self):
        """
        :return: zwraca wartosc monet w skarbonce
        """

        val = 0
        for i in self.__lista:
            val += i.getwartosc()
        return val

    def zwroc_czas(self):
        """
        :return: zwraca czas w sekundach w zaleznosci od wartosci monet w skarbonce
        """
        if (self.warotsc_w_skarbonce() <= 200):
            return self.warotsc_w_skarbonce() * 18
        elif (self.warotsc_w_skarbonce() <= 600):
            return 3600 + (self.warotsc_w_skarbonce() - 200) * 9
        else:
            return 7200 + (self.warotsc_w_skarbonce() - 600) * 7.2


def CzasUserFriendly(data):
    """
    zamienia format datatime na string wsywietlajacy date zgodnie z zaleceniami
    :param data: dostaje datatime
    :return: zwraca string
    """
    tmp = (str(data)).split(" ")
    wynik = tmp[0]
    tmp = tmp[1].split(":")
    wynik = wynik + " " + tmp[0] + ":" + tmp[1]
    return wynik


class Czas(Skarbonka):
    """
    klasa pozwalajaca na przeprowadzenie operacji na czasie

    Metody
    ustawRano(data)
        funkcja dostaje date ktora nie jest w okresie platnym(godzina wieksza od 20 lub mniejsza od 8)
        i zamienia ta godzine na 8 rano

    ustawPon(data)
        funkcja dostaje date ktora nie jest w okresie platnym(dzien wiekszy od piatku)
        i zamienia ten dzien na poniedzialek

    aktualizujCzas()
        Funkcja otrzymuje wykupiony czas w sekundach i dodaje go zgodnie z zaleceniami
        godziny platne od 8 do 20
        dni platne od poniedzialku do piatku

    """

    def __init__(self, __wartosc):
        super().__init__(__wartosc)
        self.__wyjazd = datetime.datetime.now()
        self.__teraz = datetime.datetime.now()

    def ustawRano(self, data):
        """
        :param data: datatime
        :return:datatime ustawiony na rano
        """
        while True:
            data = data + timedelta(seconds=1)
            if data.hour == 8:
                return data

    def ustawPon(self, data):
        """
        :param data: datatime
        :return: datatime ustwaiony na poniedzialek
        """

        while True:
            data = data + timedelta(days=1)
            if data.weekday() == 0:
                return data

    def aktualizujCzas(self):
        """
        :return: zwraca format datatime zaktualizowany o ilosc wykupionego czasu
        """

        i = 0
        tmpwyjazd = self.__wyjazd
        while True:
            if i == self.zwroc_czas():
                break
            if (tmpwyjazd.hour < 8 or tmpwyjazd.hour >= 20):
                tmpwyjazd = self.ustawRano(tmpwyjazd)
            if (tmpwyjazd.weekday() > 4):  # sprawdzam czy jest pomiedzy pon a piatkiem
                tmpwyjazd = self.ustawRano(tmpwyjazd)
                if (tmpwyjazd.weekday() > 4):
                    tmpwyjazd = self.ustawPon(tmpwyjazd)
                    tmpwyjazd = tmpwyjazd + timedelta(seconds=1)
                else:
                    tmpwyjazd = tmpwyjazd + timedelta(seconds=1)
                    i += 1
            else:
                tmpwyjazd = tmpwyjazd + timedelta(seconds=1)
                i += 1
        return tmpwyjazd
timer = Czas("1zl")

