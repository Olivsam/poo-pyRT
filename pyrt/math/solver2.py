"""résolution d'équation du second degré"""

import math
from .constants import *

def solve2(a, b, c):
    """Résolution de l'équation a*x^2 + b*x + c = 0
       Cette fonction retourne :
         - None si l'équation n'a pas de solution ou un nombre infini de solutions réelles ;
         - l'unique solution réelle lorsqu'elle existe ;
         - la paire ordonnée des deux solution réelles sinon.
    """
    if abs(a)<G_EPSILON:
        if abs(b)<G_EPSILON:
            return None
        else:
            return -c/b
    d=b*b-4*a*c
    if d<-G_EPSILON:
        return None
    elif d<G_EPSILON:
        return -0.5*b/a
    else:
        q=-0.5*(b+math.copysign(math.sqrt(d), b))
        x0=q/a
        x1=c/q
        return (min(x0, x1), max(x0, x1))
