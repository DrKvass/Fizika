# =============================================================================
# Logične operacije
#
# Logični operator *konjunkcija* ima naslednjo resničnostno tabelo, kjer
# `F` predstavlja neresnično (`False`), `T` pa resnično (`True`) vrednost:
# 
#     A  B | A /\ B
#     -----+-------
#     F  F |   F
#     F  T |   F
#     T  F |   F
#     T  T |   T
# 
# S pomočjo vgrajenega operatorja `and` enostavno sestavimo funkcijo
# `konjunkcija(a, b)`, ki sprejme logični vrednosti `a` in `b` ter vrne logično
# vrednost konjunkcije `a /\ b`:
# 
#     def konjunkcija(a, b):
#         return a and b
# =====================================================================@021412=
# 1. podnaloga
# Logični operator *disjunkcija* ima naslednjo resničnostno tabelo:
# 
#     A  B | A \/ B
#     -----+-------
#     F  F |   F
#     F  T |   T
#     T  F |   T
#     T  T |   T
# 
# Sestavite funkcijo `disjunkcija(a, b)`, ki sprejme logični vrednosti
# `a` in `b` ter vrne logično vrednost disjunkcije `a \/ b`. Pri tem si
# pomagajte z vgrajenim operatorjem `or`.
# =============================================================================

from cmath import nan
from operator import xor


a = False
b= False

def disjunkcija(a, b):
    c = (bool(a) or bool(b))
    return c

print(disjunkcija(a, b))
# =====================================================================@021413=
# 2. podnaloga
# Logični operator *negacija* ima naslednjo resničnostno tabelo:
# 
#     A | ~A
#     --+----
#     F | T
#     T | F
# 
# Sestavite funkcijo `negacija(a)`, ki vrne logično vrednost negacije `~a`.
# =============================================================================
def negacija(a):
    b = not(a)
    return b
# =====================================================================@021414=
# 3. podnaloga
# Logični operator *implikacija* ima naslednjo resničnostno tabelo:
# 
#     A  B | A => B
#     -----+-------
#     F  F |   T
#     F  T |   T
#     T  F |   F
#     T  T |   T
# 
# Sestavite funkcijo `implikacija(a, b)`, ki vrne logično vrednost
# implikacije `a => b`.
# =============================================================================
def implikacija(a, b):
    return not a or b
# =====================================================================@021415=
# 4. podnaloga
# Logični operator *ekvivalenca* ima naslednjo resničnostno tabelo:
# 
#     A  B | A <=> B
#     -----+--------
#     F  F |    T
#     F  T |    F
#     T  F |    F
#     T  T |    T
# 
# Sestavite funkcijo `ekvivalenca(a, b)`, ki vrne logično vrednost implikacije
# `a <=> b`.
# 
# Namig: Pomagajte si lahko s funkcijo `implikacija`.
# =============================================================================
def ekvivalenca(a,b):
    if a == b: 
        return True 
    else: 
        return False
# =====================================================================@021416=
# 5. podnaloga
# Logični operator *ekskluzivni ali* (*exclusive or* ali XOR) ima naslednjo
# resničnostno tabelo:
# 
#     A  B | A XOR B
#     -----+--------
#     F  F |    F
#     F  T |    T
#     T  F |    T
#     T  T |    F
# 
# Sestavite funkcijo `xor(a, b)`, ki vrne logično vrednost `a XOR b`.
# =============================================================================
def xor(a,b):
    return a^b
# =====================================================================@021417=
# 6. podnaloga
# Logični operator *NAND* (*not and*) ima naslednjo
# resničnostno tabelo:
# 
#     A  B | A NAND B
#     -----+---------
#     F  F |    T
#     F  T |    T
#     T  F |    T
#     T  T |    F
# 
# Sestavite funkcijo `nand(a, b)`, ki vrne logično vrednost `a NAND b`.
# =============================================================================
def nand(a,b):
    return not(a and b)
# =====================================================================@021418=
# 7. podnaloga
# Operator NAND je prav poseben, saj z njim lahko izrazimo vse osnovne logične
# operatorje (in s tem tudi vse operatorje).
# 
# Sestavite še funkcije `negacija_nand`, `disjunkcija_nand` in
# `konjunkcija_nand`, ki vrnejo logične vrednosti negacije, disjunkcije in
# konjunkcije svojih argumentov, vendar pri njihovih definicijah ne smete
# uporabiti vgrajenih logičnih operacij ali funkcij iz prejšnjih podnalog.
# Namesto tega uporabite funkcijo `nand`.
# =============================================================================

def negacija_nand(a):
    return nand(a,a)

def disjunkcija_nand(a, b):
    return nand(nand(a,a),nand(b,b))
    #return not( (not(a and a))  and  (not(b and b)) )

def konjunkcija_nand(a, b):
    return nand(nand(a,b),nand(a,b))
    #return not( (not(a and b))  and  (not(a and b)) )