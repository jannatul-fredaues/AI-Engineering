# Symbolic Differentiation (Exact Formula)

import sympy as sp
x = sp.Symbol('x')
f = x**2 + 3*x + 1
df_dx = sp.diff(f, x)  # Returns 2*x + 3
