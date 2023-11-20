# =============================================================================
# Evklidov algoritem
# =====================================================================@021970=
# 1. podnaloga
# Implementirajte [Evklidov algoritem](https://sl.wikipedia.org/wiki/Evklidov_algoritem)
# za iskanje največjega skupnega delitelja s pomočjo zanke `while`.
# 
#     >>> evklidov_algoritem(144, 40)
#     8
#     >>> evklidov_algoritem(81, 36)
#     9
# =============================================================================
def evklidov_algoritem(a,b):
    r=a%b
    while r:
        a=b
        b=r
        r=a%b
    return b
