# =============================================================================
# Razdalje med točkami
# =====================================================================@021949=
# 1. podnaloga
# Sestavite funkcijo `ravninska_razdalja(x1, y1, x2, y2)`, ki vrne
# razdaljo med točkama (`x1`, `y1`) in (`x2`, `y2`).
# 
#     >>> ravninska_razdalja(1, 2, 3, 4)
#     2.82842712475
# =============================================================================
import math
from math import cos, pi, sqrt
def ravninska_razdalja(x1, y1, x2, y2):
    A = sqrt( ( (x2-x1)**2 + (y2-y1)**2) )
    print(A)
    return A
# =====================================================================@021950=
# 2. podnaloga
# Sestavite funkcijo `polarna_razdalja(r1, fi1, r2, fi2)`, ki vrne
# razdaljo med točkama (`r1`, `fi1`) in (`r2`, `fi2`) v ravnini, pri
# čemer so koordinate v polarnem zapisu, koti pa so izraženi v stopinjah.
# 
#     >>> polarna_razdalja(1, 30, 4, 90)
#     3.60555127546
# =============================================================================

def polarna_razdalja(r1, fi1, r2, fi2):
    return (r1**2 + r2**2 - 2 * r1 * r2 * cos((fi1*pi/180)-(fi2*pi/180)))**(1/2)
