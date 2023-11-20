# =============================================================================
# Ljubezen nam je vsem v pogubo
#
# Socialno omrežje zaljubljenosti podamo s slovarjem, ki ime osebe preslika v
# množico vseh, v katere je oseba zaljubljena (ena oseba je lahko zaljubljena v
# več oseb). Na primer, slovar
# 
#     {
#         'Ana': {'Bine', 'Cene'},
#         'Bine': set(),
#         'Cene': {'Bine'},
#         'Davorka': {'Davorka'},
#         'Eva': {'Bine'}
#     }
# 
# nam pove, da je Ana zaljubljena v Bineta in Ceneta, Bine ni zaljubljen, Cene
# ljubi Bineta, Davorka samo sebe in Eva Bineta.
# =====================================================================@021515=
# 1. podnaloga
# Sestavite funkcijo `narcisoidi`, ki sprejme slovar zaljubljenih in vrne
# _množico_ tistih, ki ljubijo same sebe.
# =============================================================================
def narcisoidi(zaljub):
    a = set()
    for i, b in zaljub.items():
        if i in b:
            a.add(i)
    return a
# =====================================================================@021516=
# 2. podnaloga
# Sestavite funkcijo `ljubljeni`, ki sprejme slovar zaljubljenih in vrne
# _množico_ tistih, ki so ljubljeni.
# =============================================================================
def ljubljeni(sez):
    n = set()
    for i in sez.values():
        n.update(i)
    return n
# =====================================================================@021517=
# 3. podnaloga
# Sestavite funkcijo `pari`, ki sprejme slovar zaljubljenih in vrne _množico_
# vseh parov, ki so srečno zaljubljeni. Vsak par naj se pojavi samo enkrat in
# sicer tako, da sta zaljubljenca našteta po abecedi. Na primer, če sta Ana in
# Bine zaljubljena, dodamo par `('Ana', 'Bine')`.
# =============================================================================
def pari(sez):
    s = set()
    for per, ljub in sez.items():
        for per2 in ljub:
            if per in sez[per2]:
                s.add((min(per, per2), max(per, per2)))
    return s
# =====================================================================@021518=
# 4. podnaloga
# Sestavite funkcijo `ustrezljivi(oseba, zaljubljeni)`, ki sprejme ime osebe
# ter slovar zaljubljenih, vrne pa _množico_ vseh ljudi, ki so do dane osebe še
# posebej ustrežljivi. Posebej ustrežljivi so seveda zato, ker so bodisi
# zaljubljeni v dano osebo, bodisi so zaljubljeni v osebo, ki je posebej
# ustrežljiva do nje, in tako naprej.
# 
# Na primer, če imamo slovar
# 
#     {
#         'Ana': {'Bine', 'Cene'},
#         'Bine': {'Ana'},
#         'Cene': {'Bine'},
#         'Davorka': {'Davorka'},
#         'Eva': {'Bine'}
#     }
# 
# so do Ceneta posebej ustrežljivi Ana (ki je zaljubljena vanj), Bine (ki je
# zaljubljen v Ano) ter Cene in Eva (ki sta zaljubljena v Bineta).
# =============================================================================
"""def ustrezljivi(oseba, zaljubljeni):
    pot = [oseba]
    preverjeni = set()
    mn = set() # ustrezljivi
    while len(pot) > 0:
        oseba1 = pot.pop()
        preverjeni.add(oseba1)
        for oseba2, koga_ljubi in zaljubljeni.items():
            if oseba1 in koga_ljubi: 
                if oseba2 not in preverjeni:
                    pot.append(oseba2)
                mn.add(oseba2)
    return mn"""


"""def ustrezljivi(interes_og, zaljubljeni):
    iteration = 0
    s = set()
    interes = interes_og
    while iteration < 2:
        
        for ustr1, zalj in zaljubljeni.items():
                if interes in zalj:
                    zaljubljeni[ustr1] = interes
                    interes = ustr1
                    s.add(interes)

        for ustr2, zalj2 in zaljubljeni.items():
            if (interes_og in zalj2):
                for ustr3, zalj3 in zaljubljeni.items():
                    if ustr2 in zalj3:
                        pass
                    iteration += 1
    return s"""