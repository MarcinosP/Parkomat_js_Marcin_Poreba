import projekt
import projektMain

# nalezy zakomentowac 110 linijke w module projektMain czyli root.mainloop()

###### test2
print("test 2:")
test1 = projekt.Czas("1zl")
test1.dodajMonete(projekt.Monety("2zl"))
print(projekt.CzasUserFriendly(test1.aktualizujCzas()))
test1.dodajMonete(projekt.Monety("2zl"))
test1.dodajMonete(projekt.Monety("2zl"))
print(projekt.CzasUserFriendly(test1.aktualizujCzas()))
test1.dodajMonete(projekt.Monety("5zl"))

###### test5
print("\ntest 5:")
test5 = projekt.Czas("1zl")
test5.dodajMonete(projekt.Monety("1zl"))
print(projekt.CzasUserFriendly(test5.aktualizujCzas()))


###### test6
print("\ntest 6:")
test6 = projekt.Czas("1zl")
test6.dodajMonete(projekt.Monety("1gr"),200)
print(projekt.CzasUserFriendly(test6.aktualizujCzas()))

###### test7
print("\ntest 7:")
test7 = projekt.Czas("1zl")
test7.dodajMonete(projekt.Monety("1gr"),201)
print(projekt.CzasUserFriendly(test7.aktualizujCzas()))


###### test8 i test9
print("\ntest 9 i 8:")
test8 = projektMain.interfejs()
test8.ZatwierdzFun()
