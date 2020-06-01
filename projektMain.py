from tkinter import *
from tkinter import messagebox
import projekt as p
import datetime
import exceptions as e


class interfejs:
    """
    Główna klasa interfejsu programu

    Metody:
    pom(i)
        Funkcja pomagajaca rozmiescic przyciski w gui

    wyswietlCzas(tekst, przycisk)
        Funkcja pomocnicza do gui

    ZatwierdzFun():
        Funkcja wypisujaca na koncu numer rejestracyjny pojazdu, date wjazdu i planowaną date wyjazdu
        jezeli nie ma zadnego bledu funkcja ta zakonczy dzialanie programu
        mozliwe bledy: brak podania rejestracji pojzadu, male litery w rejestracji podjazdu,brak podania monet

    def gui():
        Funkcja wyswietlajaca interfejs graficzny dla uzytkownika
        pokazuje przyciski reprezentujace moenty z mozliwoscia "wrzucania" ich aktualizuje czas oraz pokazuje date wjazdu
        zawiera przyciski zatwierdz i aktualizuj czas
    """

    def pom(i):
        """
        :return: int z zakresu od 1 do 3
        """
        if i < 4:
            return 3
        elif i < 8:
            return 2
        else:
            return 1

    def wyswietlCzas(tekst, przycisk):
        """
        :param przycisk: tkinter.Button
        """
        przycisk.config(text=tekst)

    def ZatwierdzFun(self):
        try:
            if p.timer.warotsc_w_skarbonce() == 0:
                raise e.NieWrzuconoMonet
            if nrR.get() == "PODAJ NR REJESTRACYJNY POJAZDU":
                raise e.NieWprowadzonoNrR
            if not nrR.get().isupper():
                raise e.RejestracjaMaleLitery
            messagebox.showinfo("Potwierdzenie Zakupu",
                                "numer rejestracyjny: " + nrR.get() + "\naktualna data: " + p.CzasUserFriendly(
                                    datetime.datetime.now()) + "\ndata planowanego wyjazdu: " + p.CzasUserFriendly(
                                    p.timer.aktualizujCzas()))
            exit(1)
        except(e.RejestracjaMaleLitery):
            messagebox.showerror("Rejestracja blad", e.RejestracjaMaleLitery.message)
        except(e.NieWprowadzonoNrR):
            messagebox.showerror("Rejetracja blad", e.NieWprowadzonoNrR.message)
        except(e.NieWrzuconoMonet):
            messagebox.showerror("Monety blad", e.NieWrzuconoMonet.message)

    def gui(self):
        global nrR
        nrR = Entry(root, width=50, bg="#404040", foreground="#FFFFFF")
        nrR.grid(row=0, column=0, columnspan=4, pady=10)
        nrR.insert(0, "PODAJ NR REJESTRACYJNY POJAZDU")

        i = 0
        for m in p.timer.getmonety():
            b = Button(root, text=m, height=5, width=10, activebackground="#8CB4DD", bg="#ACD6FF",
                       command=lambda m=m: p.timer.dodajMonete(p.Monety(m), int(iloraze.get())))
            b.grid(row=self.pom(i), column=i % 4)
            i += 1

        p1 = Button(root, text="Aktualizuj czas", height=3, width=21, bg="#99FF99",
                    command=lambda: self.wyswietlCzas(p.CzasUserFriendly(p.timer.aktualizujCzas()), d4))
        p1.grid(row=4, column=0, columnspan=2)
        p2 = Button(root, text="Zatwierdź ", height=3, width=21, bg="#99FF99",
                    command=lambda: self.ZatwierdzFun(self))
        p2.grid(row=4, column=2, columnspan=2)

        iloraz = Label(root, text="liczba monet(dodatni int):", bg="#404040", foreground="#FFFFFF")
        iloraz.grid(row=5, column=0, columnspan=2, pady=10)
        iloraze = Entry(root, width=25, bg="#404040", foreground="#FFFFFF")
        iloraze.insert(0, 1)
        iloraze.grid(row=5, column=2, columnspan=2, pady=10)

        d1 = Label(root, text="Aktualna data: ", bg="#404040", foreground="#FFFFFF")
        d1.grid(row=6, column=0, columnspan=2, pady=10)
        d2 = Label(root, text=p.CzasUserFriendly(datetime.datetime.now()), bg="#404040", foreground="#FFFFFF")
        d2.grid(row=6, column=2, columnspan=2, pady=10)

        d3 = Label(root, text="Przewidziany wyjazd", bg="#404040", foreground="#FFFFFF")
        d3.grid(row=7, column=0, columnspan=2, pady=10)
        d4 = Label(root, text=p.CzasUserFriendly(p.timer.aktualizujCzas()), bg="#404040",
                   foreground="#FFFFFF")
        d4.grid(row=7, column=2, columnspan=2, pady=10)


root = Tk()
root.configure(bg="#404040")
root.title("Parkomat")
projekt = interfejs
projekt.gui(interfejs)
root.mainloop()

messagebox.showinfo("Rejestracja blad", e.RejestracjaMaleLitery.message)
