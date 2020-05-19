from tkinter import *
from tkinter import ttk
import projekt as p
import datetime

root = Tk()
root.configure(bg="#404040")
root.title("Parkomat")

def pom(i):
    if i < 4:
        return 3
    elif i < 8:
        return 2
    else:
        return 1


def gui():
    """Funkcja wyswietlajaca interfejs graficzny dla uzytkownika

    pokazuje przyciski reprezentujace moenty z mozliwoscia "wrzucania" ich aktualizuje czas oraz pokazuje date wjazdu"""

    global nrR
    nrR = Entry(root, width=50,bg="#404040",foreground="#FFFFFF")
    nrR.grid(row=0, column=0, columnspan=4, pady=10)
    nrR.insert(0, "podaj numer rejstracyjny")


    i=0
    for m in p.monety.keys():
        b = Button(root, text=m, height=5, width=10, activebackground="#8CB4DD", bg="#ACD6FF",
                   command=lambda m=m: p.dodajMonete(m, int(iloraze.get())))
        b.grid(row=pom(i), column=i % 4)
        i += 1

    p1 = Button(root,text="Potwierdź nr rejestracyjny",height=3,width=21,bg="#99FF99")
    p1.grid(row=4,column=0,columnspan=2)
    p2 = Button(root,text="Zatwierdź ",height=3,width=21,bg="#99FF99")
    p2.grid(row=4,column=2,columnspan=2)

    iloraz = Label(root, text="liczba monet(dodatni int):",bg="#404040",foreground="#FFFFFF")
    iloraz.grid(row=5, column=0, columnspan=2, pady=10)
    iloraze = Entry(root, width=25,bg="#404040",foreground="#FFFFFF")
    iloraze.insert(0,1)
    iloraze.grid(row=5, column=2, columnspan=2, pady=10)

    d1 = Label(root, text="Aktualna data: ",bg="#404040",foreground="#FFFFFF")
    d1.grid(row=6, column=0, columnspan=2, pady=10)
    d2 = Label(root, text=p.CzasUserFriendly(datetime.datetime.now()),bg="#404040",foreground="#FFFFFF")
    d2.grid(row=6, column=2, columnspan=2, pady=10)

    d3 = Label(root, text="Przewidziany wyjazd",bg="#404040",foreground="#FFFFFF")
    d3.grid(row=7, column=0, columnspan=2, pady=10)
    d4 = Label(root, text="czas wyjazdu",bg="#404040",foreground="#FFFFFF")
    d4.grid(row=7, column=2, columnspan=2, pady=10)


gui()
root.mainloop()
print(p.kasa)

