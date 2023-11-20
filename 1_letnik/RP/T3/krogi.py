# =============================================================================
# Krogi
# =====================================================================@021449=
# 1. podnaloga
# Krog predstavimo s trojico `(x, y, r)`, kjer je `(x, y)` središče kroga in
# `r` njegov radij.
# 
# Sestavite funkcijo `v_uniji(x0, y0, krogi)`, ki vrne `True`, če točka
# `(x0, y0)` leži v vsaj enem krogu v seznamu `krogi`, in `False`
# sicer.
# =============================================================================
def v_uniji(x, y, n):
    for i in n:
        if (x - i[0])**2 + (y - i[1])**2 <= (i[2])**2:
            return True
    return False

# =====================================================================@021450=
# 2. podnaloga
# Sestavite funkcijo `v_preseku(x, y, krogi)`, ki vrne `True`, če točka
# `(x, y)` leži v vseh krogih v danem seznamu `krogi`, in `False`
# sicer.
# =============================================================================
def v_preseku(x,y, n):
    for i in n:
        if not ((x - i[0])**2 + (y - i[1])**2 <= (i[2])**2):
            return False
    return True
# =====================================================================@021451=
# 3. podnaloga
# Sestavite funkcijo `pravokotnik(krogi)`, ki poišče najmanjši pravokotnik,
# ki vsebuje unijo vseh krogov iz danega seznama `krogi`. Pravokotnik
# naj vrne kot nabor `(x_min, y_min, x_max, y_max)`, torej najprej
# koordinati oglišča spodaj levo, nato pa koordinati oglišča zgoraj desno.
# 
# Predpostavite, da seznam vsebuje vsaj en krog.
# 
#     >>> pravokotnik([(0, 0, 1)]
#     (-1, -1, 1, 1)
# =============================================================================
def pravokotnik(n):
    (x, y, r) = n[0]
    xmin = x - r
    ymin = y - r
    xmax = x + r
    ymax = y + r
    for (x, y, r) in n:
        xmin = min(xmin, x - r)
        ymin = min(ymin, y - r)
        xmax = max(xmax, x + r)
        ymax = max(ymax, y + r)
    return xmin, ymin, xmax, ymax
