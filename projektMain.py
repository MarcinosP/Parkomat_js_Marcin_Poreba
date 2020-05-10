from tkinter import *
from tkinter import ttk
import projekt as p
window = Tk()
window.title("Skarbonka")
# Tworzenie siatki na przyciski
mainframe = ttk.Frame(window)
# Umieszczenie siatki w oknie
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# Dodanie przycisków do wrzucania monet
i = 0
for c in p.monety:
    ttk.Button(mainframe, text="Wrzuć " + str(c) + "zł",
               command=lambda c=c: p.dodajMonete(c)).grid(column=2, row=i)
    i += 1
# Dodanie przycisku sprawdzenia wartości zawartości
ttk.Button(mainframe, text="Przerwij",command=print("hello"))
print(p.kasa)