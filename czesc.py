# pytanie = "Ile złotych kosztuje 1 kg jabłek w "
# biedr = float(input(pytanie + "Bierdronce?"))
# lidl = float(input(pytanie + "Lidlu?"))
# zabka = float(input(pytanie + "Żabce?"))
#
# najtansze = min(biedr, lidl, zabka)
#
# print("Najtańsze jabłka kosztują", najtansze, "PLN za kilogram")
#
# kapital = float(input("Podaj kapitał początkowy w złotych:"))
# odsetki = float(input("Podaj jaka jest przewidywane oprocentowanie: (%)"))
# czas = float(input("Podaj czas trwania inwestycji w latach:"))
#
# zwrot = kapital * (1 + odsetki / 100) ** czas
#
# print(f"Na końcu inwestycji otrzymasz kwotę brutto w wysokości {zwrot: .2f} złotych")
#
# pytanie = input("Podaj proszę swoje imię: ")
# liter = int(len(pytanie))
#
# print("Twoje imię zaweiera", liter, "liter")
#
# pytanie = input("Podaj miasto w jakim mieszkasz ")
# liter = int(len(pytanie))
#
# print("Jak miło, że Twoje miasto to", pytanie.title())
#
# ford = "ab100100"
# audi = "EEE 123123"
# citroen = "Zk-300300"
# honda = "AB210210"
#
# ford = ford.upper()
# audi = audi.replace(" ", "")
# citroen = citroen.upper().replace("-", "")
#
# print(f"Ford: {ford}")
# print(f"Audi: {audi}")
# print(f"Citroen: {citroen}")
# print(f"Honda: {honda}")
#
# favourite_sports = ["koszykówka", "tenis", "ping-pong", "siatkówka"]
# print("Najlepszym sportem dla mnie jest ", favourite_sports[0])
# print("Ostatnim na liście ulubionych sportów jest ", favourite_sports[-1])
#
# favourite_sports[1] = "kalestenika"
#
# print(favourite_sports)
#
# lista_dan = input("Wymień ulubione potrawy oddzielając je przecinkiem: ")
# lista_dan = lista_dan.split(",")
# print(lista_dan)
#
# indeks_dan = 0
# while indeks_dan < len(lista_dan):
#     print(f"{indeks_dan} -> {lista_dan[indeks_dan]}")
#     indeks_dan += 1
#
# nr_telefonu = input("Podaj swój numer telefonu: ")
# nr_telefonu = nr_telefonu.replace(" ", "")
# nr_telefonu = nr_telefonu.replace("-", "")
# # nr_publiczne = nr_telefonu[:6]
# # liczba_prywatnych_liczb = len(nr_telefonu) - 6
# # prywatne_liczby = "-" * liczba_prywatnych_liczb
# # nr_anonim = f"{nr_publiczne}{prywatne_liczby}"
# #
# # print(nr_anonim)
# # if "0" in nr_telefonu:
# #     print("Twój numer zawiera cyfrę 0")
#
# # sformatowany_nr_telefonu = ""
# # indeks_liter = 0
# # while indeks_liter < len(nr_telefonu):
# #     if indeks_liter % 3 == 0 and indeks_liter != 0:
# #         sformatowany_nr_telefonu += "-"
# #     sformatowany_nr_telefonu += nr_telefonu[indeks_liter]
# #     indeks_liter += 1
# # print(sformatowany_nr_telefonu)
#
# for cyfra in range(10):
#     ile_razy_cyfra = nr_telefonu.count(str(cyfra))
#     if ile_razy_cyfra != 0:
#         print(f"{cyfra} występuje {ile_razy_cyfra} razy.")
#
# Słownik_pol_ang = {"amnezja": "amnesia", "aktywista": "activist", "burza": "storm"}
# # print(f" Po polsku ‘burza’ to po angielsku '{Słownik_pol_ang['burza']}'")
# empty = {}
# Slownik_z_lista = {"Wydatki": [1, 3, 5.35, 63], "Prezenty": [50]}
# print(Słownik_pol_ang.keys())
# keys = list(Słownik_pol_ang.keys())
# values = list(Słownik_pol_ang.values())
# print(keys)
#
# liczba_kluczy = len(keys)
# print("Liczba kluczy w słowniku wynosi: ", liczba_kluczy)
#
# przedmioty_szkolne = {"polski": 5, "matematyka": 4, "angielski": 3, "biologia": 1, "fizyka": 5}
# keys = list(przedmioty_szkolne.keys())
# values = list(przedmioty_szkolne.values())
# numer = 0
#
# while numer < len(keys):
#     przedmiot = keys[numer]
#     ocena = values[numer]
#     print("Ocena z przedmiotu", przedmiot, "to: ", ocena)
#     numer = numer + 1
# print()
# print(przedmioty_szkolne)
#
# jedzenie = float(input("Ile miesięcznie wydajesz pieniędzy w PLN na jedzenie?: "))
# rozrywka = float(input("Ile miesięcznie wydajesz pieniędzy w PLN na rozrywkę?: "))
# opłaty = float(input("Ile miesięcznie wydajesz pieniędzy w PLN na opłaty?: "))
# inne = float(input("Ile miesięcznie wydajesz pieniędzy w PLN na inne wydatki?: "))
#
# wydatki = jedzenie + rozrywka + opłaty + inne
#
# wydatki_procentowo = {
#     "jedzenie": jedzenie * 100 / wydatki,
#     "rozrywka": rozrywka * 100 / wydatki,
#     "opłaty": opłaty * 100 / wydatki,
#     "inne": inne * 100 / wydatki,
# }
# Wybrana_kategoria = input(
#     "Wybierz jedną z tych kategorii aby poznać procentowy udział w wydatkach: jedzenie, rozrywka, opłaty, inne: ")
# print(f"Na {Wybrana_kategoria} wydajesz {wydatki_procentowo[Wybrana_kategoria]:.2f}% wszystkich wydatków")
#
# cena_cebuli = float(input("Proszę podaj cenę cebuli w zł: "))
# cena_pomidora = float(input("Proszę podaj cenę pomidora w zł: "))
# cena_banana = float(input("Proszę podaj cenę banana w zł: "))
#
# print()
# print(f"Czy cebula jest droższa od pomidora? {cena_cebuli > cena_pomidora}")
# print(f"Czy pomidor jest droższy od banana? {cena_pomidora > cena_banana}")
# print(f"Czy banan jest droższy od cebuli? {cena_banana > cena_cebuli}")
#
# zakupy = input("Wprowadź listę zakupów rozdzielając je przecinkiem: ")
# lista_zakupów = zakupy.split(", ")
#
# czy_lista_zakupów_długa = len(lista_zakupów) > 4
# print(f"Czy uważam, że Twoja lista zakupów jest długa? {czy_lista_zakupów_długa}")
#
# wiek = int(input("Podaj swój wiek: "))
#
# if wiek >= 18:
#     if wiek >= 21:
#         if wiek >= 30:
#             if wiek >= 35:
#                 print("Możesz kandydować na prezydenta, senatora, posła i głosować w wyborach.")
#             else:
#                 print("Możesz kandydować na senatora, posła i głosować w wyborach.")
#         else:
#             print("Możesz kandydować na posła i głosować w wyborach.")
#     else:
#         print("Możesz głosować w wyborach.")
# else:
#     print("Jesteś za młody, żeby głosować")
#
# name = input("Jak masz na imię?")
#
# if name[-1] == "a":
#     print("Jesteś kobitą")
# else:
#     print("Jesteś chłopem")
#
# dochod = 5000
# liczba_pracownikow = 7
# lat_na_rynku = 3
#
# if dochod < 5000:
#     print("Przyznano Ci główne wsparcie")
# elif 5 <= liczba_pracownikow <= 10:
#     print("Przyznano Ci wsparcie z funduszu pracowników")
# elif lat_na_rynku < 3:
#     print("Przyznano Ci wsparcie dla nowych firm")
# else:
#     print("Przyznano Ci wsparcie na pocieszenie")
#
# kalkulator = input("Jaki kalkulator potrzebujesz: do lokat - napisz literę 'l', lub kredytów - napisz literę 'k': ")
# if kalkulator == "l":
#     print("Wybrałeś kalkulator wartości lokaty z roczną kapitalizacją")
#
#     wartość_początkowa = int(input("Jaką kwotą wpłaciłeś/wpłaciłaś? "))
#     oprocentowanie = int(input("Jakie jest oprocentowanie (%)? "))
#     lat = int(input("Ile lat trwa inwestycja? "))
#
#     wartość_końcowa = wartość_początkowa * (1 + oprocentowanie / 100) ** lat
#     zysk = wartość_końcowa - wartość_początkowa
#     ROI = zysk / wartość_początkowa * 100
#
#     print(f"Po {lat} latach otrzymasz {wartość_końcowa: .2f} złotych. ROI wyniesie {ROI: .2f} procent.")
#     print(f"Czy wartość Twojej inwestycji wzrośnie o 10% lub więcej? {ROI >= 10}")
#
# elif kalkulator == "k":
#     print("Wybrałeś kalkulator kredytowy.")
#     kwota_kredytu = int(input("Podaj jaką chcesz kwotę kredytu: "))
#     oprocentowanie = float(input("Podaj oprocentowanie kredytu: "))
#     wklad_wlasny = float(input("Jaki jest Twój wkład własny: "))
#     lat = float(input("Na ile lat chcesz zaciągnąć kredyt: "))
#     przychod = float(input("Jakie masz miesięcznie przychody: "))
#     wydatki = float(input("Ile wynosi suma Twoich wydatków miesięcznych: "))
#
#     rata = kwota_kredytu * oprocentowanie / 100 / 12 + kwota_kredytu / (lat * 12)
#     dostepne_srodki = przychod - wydatki
#     wartosc_nieruchomosci = wklad_wlasny + kwota_kredytu
#     maks_kwota_kredytu = dostepne_srodki / (oprocentowanie / 100 / 12 + 1 / (lat * 12))
#
#     if wklad_wlasny >= wartosc_nieruchomosci * 0.2 and dostepne_srodki >= rata + 1000:
#         print("Stać Cię na taki kredyt.")
#     else:
#         if wklad_wlasny >= wartosc_nieruchomosci * 0.1 and dostepne_srodki >= rata + 2000:
#             print("Stać Cię na taki kredyt.")
#         else:
#             print("Nie stać się na taki kredyt.")
# else:
#     kalkulator = input("Wprowadziłeś niepoperawną wartość. Napisz tylko jedną literę: l albo k.")
#
# print("Analiza wyników testu biegowego Coopera.")
#
# sportowiec = input("Czy jesteś profesjonalnym sportowcem?(tak, nie?): ")
# plec = input("Czy jesteś kobietą? (tak, nie?): ")
# wiek = int(input("Podaj swój wiek: "))
# wynik = float(input("Podaj wynik testu: "))
#
# if sportowiec == "tak":
#     if plec == "tak":
#         if wynik >= 3000:
#             print("Bardzo dobrze")
#         elif wynik >= 2700:
#             print("Dobrze")
#         elif wynik >= 2400:
#             print("Średnio")
#         elif wynik >= 2100:
#             print("Źle")
#         else:
#             print("Bardzo źle")
#     elif plec == "nie":
#         if wynik >= 3700:
#             print("Bardzo dobrze")
#         elif wynik >= 3400:
#             print("Dobrze")
#         elif wynik >= 3100:
#             print("Średnio")
#         elif wynik >= 2800:
#             print("Źle")
#         else:
#             print("Bardzo źle")
# elif plec == "tak":
#     if
#
# zakupy = input("Wprowadź listę zakupów rozdzielając je przecinkiem: ")
# lista_zakupów = zakupy.split(", ")
#
# czy_lista_zakupów_długa = len(lista_zakupów) > 4
# print(f"Czy uważam, że Twoja lista zakupów jest długa? {czy_lista_zakupów_długa}")
#
# if 'chleb' in lista_zakupów:
#     if 'bułki' in lista_zakupów:
#         print("Na liścią znajdują się chleb i bułki.")
#     else:
#         print("Na liście znajduje się chleb, ale nie ma bułek.")
# elif 'bułki' in lista_zakupów:
#     print("Na liście są bułki, ale nie ma chleba.")
# else:
#     print("Na liście ni ma ani chleba, ani bułek.")
#
# zmienna = input("Podaj zmienną: ")
# if zmienna == "True":
#     zmienna = bool(True)
# if zmienna == "False":
#     zmienna = bool(False)
#
# if zmienna == True:
#     print("zmienna równa się True")
# else:
#     print("zmienna równa się False")
#
# if zmienna == None:
#     print("zmienna równa się None")
# else:
#     print("zmienna nie równa się None")
#
# if zmienna is True:
#     print("zmienna jest True")
# elif zmienna is False:
#     print("zmienna jest False")
# else:
#     print("zmienna nie jest typem bool")
#
# licznik = 0
#
# liczba = int(input(f"Podaj parzystą liczbę. Masz {10 - licznik} prób:"))
#
# while licznik < 9:
#     if liczba % 2 == 1 and liczba != 0:
#         liczba = int(input(f"Ta liczba jest nieparzysta. Pozostało {9 - licznik} prób. Spróbuj jeszcze raz: "))
#     else:
#         liczba = int(input(f"Brawo! Ta liczba jest parzysta. Pozostało {9 - licznik} prób. Spróbuj jeszcze raz: "))
#     licznik += 1
#
# if liczba % 2 == 1 and liczba != 0:
#     print(f"Wykorzystałeś 10 prób. Ostatnia liczba jest nieparzysta.")
# else:
#     print(f"Wykorzystałeś 10 prób. Ostatnia liczba jest parzysta.")
#
# oceny = []
# ocena_wpisana = input("Podaj kolejną ocenę albo zakończ wpisując 'X': ")
# while ocena_wpisana != 'x':
#     ocena = int(ocena_wpisana)
#     oceny.append(ocena)
#     ocena_wpisana = input("Podaj kolejną ocenę, albo zakończ wpisując 'X': ")
#
# suma_ocen = 0
# for ocena in oceny:
#     suma_ocen += ocena
#
# średnia = suma_ocen / len(oceny)
# print(f"Twoja średnia wynosi: {średnia: .2f}")
#
# grades = []
# while True:
#     grade_input = input("Podaj ocenę na koniec roku albo napisz X: ")
#     if grade_input == 'X':
#         break
#     grade = int(grade_input)
#     grades.append(grade)
#     if grade == 1:
#         print("Nie zdałeś do kolejnej klasy :( .")
#         break
#
# average = sum(grades) / len(grades)
# print(f"Twoja średnia wynosi {average:.2f}")
#
# print("Kalkulaor miesięcznych wydatków")
# wydatki = {}
#
# nazwa_kategorii = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")
# while nazwa_kategorii != 'X':
#     wydatki[nazwa_kategorii] = []
#     wydatek = input(f"Podaj wartość następnego wydatku w kategorii {nazwa_kategorii} albo zakończ wpisując 'X': ")
#     while wydatek != 'X':
#         wartosc_wydatku = float(wydatek)
#         wydatki[nazwa_kategorii].append(wartosc_wydatku)
#         wydatek = input(f"Podaj wartość następnego wydatku w kategorii {nazwa_kategorii} albo zakończ wpisując 'X': ")
#     nazwa_kategorii = input("Podaj kolejną kategorię wydatków albo zakończ wpisując 'X': ")
#
# suma_wydatkow = 0
# for wydatki_kategorii in wydatki.values():
#     for wartosc_wydatku in wydatki_kategorii:
#         suma_wydatkow += wartosc_wydatku
#
# procent_wydatkow = {}
# for nazwa_kategorii, wydatki_kategorii in wydatki.items():
#     suma_wydatkow_kategorii = sum(wydatki_kategorii)
#     procent_wydatkow[nazwa_kategorii] = suma_wydatkow_kategorii * 100 / suma_wydatkow
#
# najwazniejsza_kategoria = None
# procent_najwazniejszej_kategorii = 0
# for kategoria, procent in procent_wydatkow.items():
#     if procent > procent_najwazniejszej_kategorii:
#         procent_najwazniejszej_kategorii = procent
#         najwazniejsza_kategoria = kategoria
#
# if najwazniejsza_kategoria is not None:
#     print(
#         f"Najwięcej wydajesz na {najwazniejsza_kategoria} - {procent_najwazniejszej_kategorii:.2f}% miesięcznych wydatków.")
#
# for kategoria, procent in procent_wydatkow.items():
#     print(f"Na {kategoria} wydajesz {procent:.0f}% miesięcznych wydatków.")
#
# capital = int(input("Na jaką kwotę jest kredyt: "))
# interest_rate = float(input("Jakie jest oprocentowanie (%): "))
# years = int(input("Na ile lat jest kredyt: "))
# initial_fees = int(input("Jakie są koszty początkowe:"))
#
# credit_time_in_months = years * 12
# monthly_paid_capital = capital / credit_time_in_months
# total_paid = initial_fees
# for month_number in range(1, credit_time_in_months + 1):
#     capital_to_be_paid = capital - (month_number - 1) * monthly_paid_capital
#     installment = (capital_to_be_paid * interest_rate / 100) / 12 + monthly_paid_capital
#     total_paid += installment
#     print(f"Rata w miesiącu {month_number} wyniesie {installment:.2f}")
#
# print(f"Zaciągając {capital} na tych warunkach spłacisz z odsetkami {total_paid:.2f}")
#
# expenditures = [120, 300, 250.45, 1300, 50, 75]
# for expenditure in expenditures:
#     print(expenditure)
#     if expenditure > 1000:
#         print("Drogi wydatek znaleziony.")
#         break
#
# favourite_sports = ["bieganie", "koszykówka", "tenis", "ping-pong", "pływanie", "rower", "żeglowanie"]
# for index, sport in enumerate(favourite_sports):
#     if index % 2 != 0:
#         continue
#     print(sport)
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# for number in numbers:
#     if number % 2 == 0:
#         continue
#     print(number)
#
#
# def pole_prostokata():
#     dlugi_bok = int(input("Napisz długość długiego boku prostokąta: "))
#     krotki_bok = int(input("Napisz długość długość krótkiego boku: "))
#     return dlugi_bok * krotki_bok
#
#
# print(f"Pole prostokąta wynosi {pole_prostokata()}.")
#
#
def predkosc_srednia():
    dystans = float(input("Podaj dystans w kilometrach: "))
    czas = int(input("Podaj czas w minutach: "))
    return dystans / czas * 60


print(f"Średnia prędkość wynosi {predkosc_srednia():.2f} kilometrów na godzinę.")
