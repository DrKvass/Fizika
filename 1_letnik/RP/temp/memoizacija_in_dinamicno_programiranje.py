# =============================================================================
# Memoizacija in dinamično programiranje
#
# Pri pristopu, imenovanem *dinamično programiranje*, do rešitve danega
# problema pridemo tako, da rešitev sestavimo iz rešitev nekoliko manjših
# različic problema. Slednje lahko dobimo na enak način, dokler ne rešujemo
# tako majhnega problema, da ga lahko rešujemo neposredno.
# 
# Uberemo lahko dva pristopa. Prvi je od spodaj gor – najprej rešujemo
# najmanjše probleme, dokler ne pridemo do tistega, ki nas zanima. Pri tem
# lahko vmesne rešitve shranjujemo v slovar, iz katerega beremo rešitve pri
# reševanju večjih problemov.
# 
# Drugi način je od zgoraj dol, torej rekurzivno. Vendar to pomeni, da bomo
# morda isti problem reševali večkrat. Zato si pomagamo z *memoizacijo* - vsak
# problem prvič rešimo, nato pa njegovo rešitev spravimo v slovar, od koder
# preberemo rešitev, ko jo naslednjič potrebujemo.
# =====================================================================@021519=
# 1. podnaloga
# Zanima nas problem *najlažje poti po matriki*. Dana je matrika `A` (kot
# seznam seznamov števil), iščemo pa pot od zgornjega levega polja (`A[0][0]`)
# do spodnjega desnega polja, tako da je vsota števil v obiskanih poljih čim
# manjša. V vsakem koraku se lahko premikamo le za eno polje v desno ali dol
# (tj., v vsakem koraku se bo ena od koordinat povečala za 1). V testnih
# primerih bomo uporabili naslednjo matriko:
# 
#     A = [[5, 7, 3, 6],
#          [2, 7, 3, 4],
#          [1, 3, 9, 2],
#          [6, 6, 4, 2]]
# 
# Definirajte funkcijo `najlazja_pot_do(A, i, j, resitve)`, ki naj vrne dolžino
# najlažje poti v matriki `A` od `A[0][0]` do `A[i][j]`. Predpostavite, da ima
# slovar `resitve` že ključa `(i - 1, j)` oziroma `(i, j - 1)` z vrednostima,
# ki predstavljata vsoti najlažjih poti od `A[0][0]` do `A[i - 1][j]` oziroma
# `A[i][j - 1]` (ali pa upoštevajte ustrezne robne pogoje). Funkcija naj ne
# uporablja rekurzije ali zank, prav tako naj ne spreminja slovarja `resitve`.
# =============================================================================
def najlazja_pot_do(A, i, j, resitve):
    if i == j == 0:
        return A[0][0]
    elif i == 0: return A[i][j] + resitve[(0, j - 1)]
    elif j == 0: return A[i][j] + resitve[(i - 1, 0)]
    else: return A[i][j] + min(resitve[(i - 1, j)],resitve[(i, j - 1)])
# =====================================================================@021520=
# 2. podnaloga
# Sestavite funkcijo `najlazja_pot_slovar(A)`, ki naj vrne vsoto polj v
# najlažji poti v matriki `A`. Pri tem naj si pomaga s funkcijo
# `najlazja_pot_do` in ustrezno polni slovar, ki ji ga poda kot argument.
# =============================================================================
def najlazja_pot_slovar(A):
    resitve = {}
    for i in range(len(A)):
        for j in range(len(A[0])):
            resitve[(i, j)] = najlazja_pot_do(A, i, j, resitve)
    return resitve[(len(A) - 1, len(A) - 1)]
# =====================================================================@021521=
# 3. podnaloga
# V Pythonu lahko definiramo *dekoratorje*. Dekorator je funkcija, ki kot
# argument sprejme funkcijo in vrne novo funkcijo. Slednjo lahko definiramo kar
# znotraj telesa dekoratorja. Dekorator uporabimo tako, da ga z `@` napišemo
# pred definicijo dekorirane funkcije:
# 
#     @dekorator
#     def funkcija(x, y=1):
#         ...
# 
# `funkcija` se tako nadomesti z vrednostjo `dekorator(funkcija)`.
# 
# Definirajte dekorator `memo(fun)`, ki opravlja memoizacijo za funkcije z
# dvema argumentom. Tako slovar kot vrnjena funkcija naj bosta definirana v
# telesu dekoratorja.
# 
# Na primer, če definiramo:
# 
#     sesteti_pari = []
# 
#     @memo
#     def dodaj_in_sestej(x, y):
#          sesteti_pari.append((x, y))
#          return x + y
# 
# Bi morali dobiti sledeče rezultate
# 
#     >>> dodaj_in_sestej(42, 23)
#     65
#     >>> dodaj_in_sestej(23, 42)
#     65
#     >>> dodaj_in_sestej(42, 23)
#     65
#     >>> sesteti_pari
#     [(42, 23), (23, 42)]
# =============================================================================

# =====================================================================@021522=
# 4. podnaloga
# Sestavite funkcijo `najlazja_pot_memo(A)`, ki naj vrne vsoto polj
# v najlažji poti v matriki `A`. Pri tem naj si pomaga z dekoratorjem `memo`
# in gnezdeno rekurzivno pomožno funkcijo, ki jo pokliče samo enkrat.
# =============================================================================
