# =============================================================================
# Sprehod
# =====================================================================@021965=
# 1. podnaloga
# Sestavite funkcijo `celostevilski`, ki sprejme niz, ki
# predstavlja sprehod po celih številih, in vrne število, v katerem se
# sprehod konča.
# 
# Sprehod po celih številih se začne v številu 0, predstavimo pa ga z
# nizem, sestavljenim iz znakov `+` in `-`. Na ostale znake v nizu se
# ne oziramo.
# =============================================================================
def celostevilski(n):
    p = 0
    m = 0
    for i in range(len(n)):
        if n[i] == "+":
            p += 1
        elif n[i] == "-":
            m += 1
    return p - m
# =====================================================================@021966=
# 2. podnaloga
# Napišite število, v katerem se konča sprehod, podan z:
# 
#     ++++-+--++---+-+--+++-++-+++---+++--+-+---+-+++--++-+++-++-++-++----+-
#     ++++-+--++---+-+--+++-++-+++---+++--+-+---+-+++--++-+++-++-++-++----+-
#     +++-+++++++-+++--+--+++--+++---+--+--+++--+-+-+++--++--+++-----+----+-
#     +++-+++++++-+++--+--+++--+++---+--+--+++--+-+-+++--++--+++-----+----+-
#     +++--++++++--+--+-++++++++-+++++-+++-----+-+-+++-+-++-----+--+-+++--++
#     +++--++++++--+--+-++++++++-+++++-+++-----+-+-+++-+-++-----+--+-+++--++
#     +++--+--+-+-+-+--+-++-+---++++-+--++-+--++-+-++---++-------+++++++--+-
#     +++--+--+-+-+-+--+-++-+---++++-+--++-+--++-+-++---++-------+++++++--+-
#     ++-++-+-----++----+++++-+-+++++-++-+--+-++-++++-----++-+--++---++++++-
#     ++-++-+-----++----+++++-+-+++++-++-+--+-++-++++-----++-+--++---++++++-
#     ++-+-++----+-++--++++++-++--+-+++-+-+--+++-++--+---++++-+--++-+++--+-+
#     ++-+-++----+-++--++++++-++--+-+++-+-+--+++-++--+---++++-+--++-+++--+-+
#     ++-+---+--+-+++--+++--+++-+--+-++++++--++++---+--+-----++-++-+-++-+--+
#     ++-+---+--+-+++--+++--+++-+--+-++++++--++++---+--+-----++-++-+-++-+--+
#     ++--+-+--+--+-----+-+-++-++-+++-+++-+-++---++--++-+-++++++-+++-++-+++-
#     ++--+-+--+--+-----+-+-++-++-+++-+++-+-++---++--++-+-++++++-+++-++-+++-
#     ++------+--++---+-+-+-----++++-++---++-+--+-++------+-+--++++-+-++----
#     ++------+--++---+-+-+-----++++-++---++-+--+-++------+-+--++++-+-++----
#     +-++++++---++--------+++-----++----+----+-+++---+-+-+---+++-+---++-+-+
#     +-++++++---++--------+++-----++----+----+-+++---+-+-+---+++-+---++-+-+
#     +-+-+--+-+++++----++---++--++++-+++-++--+-+-+-+++--+-+-+--+++---+-+-+-
#     +-+-+--+-+++++----++---++--++++-+++-++--+-+-+-+++--+-+-+--+++---+-+-+-
#     +--------+-+--+--++--+--+++-+--++++-----+---+++++++++++++-++-+-+-+-+--
#     +--------+-+--+--++--+--+++-+--++++-----+---+++++++++++++-++-+-+-+-+--
#     -++-+++---+-+--+-+--++++----+-+--+-+-+++++-+++-+--+---+-+--+++-++-++++
#     -++-+++---+-+--+-+--++++----+-+--+-+-+++++-+++-+--+---+-+--+++-++-++++
#     -+--++--+++++-++-+--++-+---+--++---+----+++-+-++++-+---+++-+++---++-+-
#     -+--++--+++++-++-+--++-+---+--++---+----+++-+-++++-+---+++-+++---++-+-
#     -+---+------+++-+++----+----+++-+-+-+-+++------++-+-++----+---++++++++
#     -+---+------+++-+++----+----+++-+-+-+-+++------++-+-++----+---++++++++
#     --++-++--+-+++++-+--+---++-+--++---+-++-+----++-+--++++------+--+---+-
#     --++-++--+-+++++-+--+---++-+--++---+-++-+----++-+--++++------+--+---+-
#     --++--+----+--+---+-+++-+--++++-+--++-+-+-+-++-+---+-+-++++++---+-+--+
#     --++--+----+--+---+-+++-+--++++-+--++-+-+-+-++-+---+-+-++++++---+-+---
#     --+-++++-+-++----++++-+++-++--+-++-+++++-+-+-++--++++++++--+++--+++++-
#     --+-++++-+-++----++++-+++-++--+-++-+++++-+-+-++--++++++++--+++--+++++-
#     --+--+++-+-++-+--++---+--+-++-----+--+++--+++--------+-+++---++++-+-+-
#     --+--+++-+-++-+--++---+--+-++-----+--+++--+++--------+-+++---++++-+-+-
#     -----++--------++++-+++-+-++---+++---+++-++--++++--++-++-----++----+--
#     -----++--------++++-+++-+-++---+++---+++-++--++++--++-++-----++----+--
#     -----+------+++--++----+----+++--+++--+---+-+--+--+++-++--+--+--++--+-
#     -----+------+++--++----+----+++--+++--+---+-+--+--+++-++--+--+--++--+-
#     ------+--+-+--+-++-+++-+-++-+++++--+--+++++-+-++-+-++-++-+---++-++--+-
#     ------+--+-+--+-++-+++-+-++-+++++--+--+++++-+-++-+-++-++-+---++-++--+-
# =============================================================================
42
# =====================================================================@021967=
# 3. podnaloga
# Sestavite funkcijo `ravninski`, ki sprejme niz, ki
# predstavlja zaporedje korakov v ravnini, in vrne točko, v kateri se
# sprehod konča.
# 
# Sprehod po ravnini se začne v izhodišču, predstavimo pa ga z nizem,
# sestavljenim iz črk `S`, `J`, `V` ali `Z`, odvisno od smeri
# (sever, jug, vzhod, zahod). Na ostale znake v nizu se ne oziramo.
# =============================================================================
def ravninski(n):
    s = 0
    v = 0
    for i in range(len(n)):
        if n[i] == "S":
            s += 1
        elif n[i] == "J":
            s += -1
        elif n[i] == "V":
            v += 1
        elif n[i] == "Z":
            v += -1
    return (v, s)
# =====================================================================@021968=
# 4. podnaloga
# Sestavite funkcijo `hitri(tek)`, ki sprejme niz, ki predstavlja
# zaporedje korakov in skokov v ravnini, in vrne točko, v kateri se
# tek konča.
# 
# Tek po ravnini se začne v izhodišču, predstavimo pa ga, tako kot
# sprehod, z nizem, sestavljenim iz črk `S`, `J`, `V` ali `Z`, odvisno
# od smeri (sever, jug, vzhod, zahod).
# 
# Poleg tega lahko tek vsebuje tudi števke od `1` do `9`, ki povedo,
# koliko dolg naj bo naslednji korak. Tako niz `5S` pomeni skok
# na sever, dolg 5 korakov. Privzamete lahko, da zaporednih števk v
# nizu ni, ter da se na ostale znake v nizu ne oziramo.
# =============================================================================
def hitri(n):
    x = y = 0
    dolzina = 1
    for korak in n:
        if korak == 'S':
            y += dolzina
        elif korak == 'J':
            y -= dolzina
        elif korak == 'V':
            x += dolzina
        elif korak == 'Z':
            x -= dolzina
        if korak in '123456789':
            dolzina = int(korak)
        elif korak in 'SJVZ':
            dolzina = 1
    return (x, y)
