# PARKOMAT - raport
## Założenia projektowe kodu
Moim zadaniem było napisanie programu imitującego parkomat,
Projekt został wykonany w programie PyCharm, do rysowania okienek użyłem biblioteki tkinter,
 którą poznałem na lab6 z języków symbolicznych
## Ogólny opis kodu
Projekt składa się z 3 modułów, projektMain.py, projekt.py, exceptions.py.
- w pliku projektMain.py znajduje sie interfejs programu
- w pliku projekt.py znajduje sie logika programu
- exceptions.py znajdują się wyjątki 
- testy.py w którym znajduja sie wszystkie testy które udało mi się przeprowadzić bez użycia interfejsu
- pliku raport.md oraz README.md
## Co udało się zrobić
Udało mi się zrealizować wszystkie założenia projektu
## z czym były problemy
Największy problem sprawił mi github, ponieważ dodawałem commity poprzez interfejs tortoise git
oraz przez strone github doszło do utraty 3 commitów których nie potrafie odzyskać. Dużo czasu również 
spędziłem pisząc funkcje aktualizuj_czas w module projekt.py i aktualizowanie czasu w przedziale 
od 8 do 20 godziny i od poniedziałku do piątku sprawiło mi problemy
## zauważone problemy z testami
- nie mogę przeprowadzić pierwszego testu ponieważ godzina jest obliczana przez program
- gdy o godzinie 20:00 (do tej godziny jest liczony parking) dodam pare groszy powstaje błąd,

[Repository](https://github.com/MarcinosP/Parkomat_js_Marcin_Poreba)

[lambda](https://github.com/MarcinosP/Parkomat_js_Marcin_Poreba/blob/ff61f583571ea183d5e10cd6327ee6cf71fbd0bb/projektMain.py#L76)

[lambda](https://github.com/MarcinosP/Parkomat_js_Marcin_Poreba/blob/ff61f583571ea183d5e10cd6327ee6cf71fbd0bb/projektMain.py#L81)

[lambda](https://github.com/MarcinosP/Parkomat_js_Marcin_Poreba/blob/ff61f583571ea183d5e10cd6327ee6cf71fbd0bb/projektMain.py#L84)

[dictionary comprehension](https://github.com/MarcinosP/Parkomat_js_Marcin_Poreba/blob/ff61f583571ea183d5e10cd6327ee6cf71fbd0bb/projekt.py#L29)

[class Monety](https://github.com/MarcinosP/Parkomat_js_Marcin_Poreba/blob/105987151de0ef5e83c1890734d47f51ddce484c/projekt.py#L7-L56)

[class Skarbonka](https://github.com/MarcinosP/Parkomat_js_Marcin_Poreba/blob/105987151de0ef5e83c1890734d47f51ddce484c/projekt.py#L59-L122)

[class Czas](https://github.com/MarcinosP/Parkomat_js_Marcin_Poreba/blob/105987151de0ef5e83c1890734d47f51ddce484c/projekt.py#L138-L207)

[class interfejs](https://github.com/MarcinosP/Parkomat_js_Marcin_Poreba/blob/105987151de0ef5e83c1890734d47f51ddce484c/projektMain.py#L8-L102)

[logic module](https://github.com/MarcinosP/Parkomat_js_Marcin_Poreba/blob/master/projekt.py)

[interface module](https://github.com/MarcinosP/Parkomat_js_Marcin_Poreba/blob/master/projektMain.py)

[exception module](https://github.com/MarcinosP/Parkomat_js_Marcin_Poreba/blob/master/exceptions.py)

[test module](https://github.com/MarcinosP/Parkomat_js_Marcin_Poreba/blob/master/testy.py)
