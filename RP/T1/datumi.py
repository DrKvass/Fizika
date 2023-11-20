# =============================================================================
# Datumi
# =====================================================================@021409=
# 1. podnaloga
# Sestavite funkcijo `je_prestopno(leto)`, ki vrne `True`, kadar je `leto`
# prestopno, in `False`, kadar ni.
# =============================================================================
1
def je_prestopno(leto):
    True if (leto % 4) == 0 and  ((leto % 400 == 0) or (leto % 100 != 0)) else False

# =====================================================================@021410=
# 2. podnaloga
# Sestavite funkcijo `stevilo_dni(mesec, leto)`, ki vrne število dni danega
# meseca (podanega s številom med 1 in 12) v danem letu.
# =============================================================================
def stevilo_dni(mesec, leto):
 31 if mesec in {1,3,5,7,8,10,12} else (30 if mesec in {4,6,9,11} else (29 if je_prestopno(leto) else 28))
    if mesec in {1,3,5,7,8,10,12}:
        return 31
    elif mesec in {4,6,9,11}:
        return 30
    elif je_prestopno(leto) == True:
        return 29
    else:
        return 28

# =====================================================================@021411=
# 3. podnaloga
# Sestavite funkcijo `je_veljaven_datum(dan, mesec, leto)`, ki vrne `True`
# natanko tedaj, kadar `dan`, `mesec` in `leto` določajo veljaven datum
# (torej `mesec` mora biti število med 1 in 12, `dan` pa mora ustrezati dnevu
# v tem mesecu).
# =============================================================================

def je_veljaven_datum(dan, mesec, leto):
    if je_prestopno(leto) == True and (dan <= stevilo_dni(mesec, leto)) and 1 <= mesec <= 12:
        return True
    elif dan <= stevilo_dni(mesec, leto) and 1 <= mesec <= 12:
        return True
    else:
        return False