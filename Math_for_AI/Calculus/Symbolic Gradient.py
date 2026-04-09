from sympy import symbols, diff

x, y = symbols('x y')
f = x**2 + y**3

# Partial derivatives (the gradient components)
grad_x = diff(f, x) # 2*x
grad_y = diff(f, y) # 3*y**2
