from math import ceil

def ewakuacja(lista_osob, liczba_klatek_schodowych, liczba_osob_w_rzedzie, tempo_schodzenia):
    rzad_razy_klatki = liczba_klatek_schodowych * liczba_osob_w_rzedzie
    result = [0]
    for osoby in reversed(lista_osob):
        liczba_rzedow = ceil(osoby/rzad_razy_klatki)
        czas = liczba_rzedow + tempo_schodzenia
        result.append(result[len(result) - 1] + czas)
    return [x for x in reversed(result) if x != result[len(result)-1]]

lista_osob = [5, 10, 15]
liczba_klatek_schodowych = 2
liczba_osob_w_rzedzie = 1
tempo_schodzenia = 30

assert [73, 38, 0] == ewakuacja(
    lista_osob=lista_osob,
    liczba_klatek_schodowych=liczba_klatek_schodowych,
    liczba_osob_w_rzedzie=liczba_osob_w_rzedzie,
    tempo_schodzenia=tempo_schodzenia
    )