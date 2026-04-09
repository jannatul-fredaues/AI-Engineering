import autograd.numpy as anp
from autograd import grad
def f(x): return anp.sin(x)
grad_f = grad(f)
print(grad_f(1.0)) # Exact numerical gradient at x=1.0
