from sympy import fourier_series, pi, Abs
from sympy.plotting import plot
from sympy.abc import x
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application


def function(func):
    transformations = (standard_transformations + (implicit_multiplication_application,))
    f = parse_expr(str(func), transformations=transformations)
    return f


def ploting(f, f_series, l_bound, r_bound):
    p = plot(f, f_series, (x, l_bound, r_bound), show=False, legend=False)
    p.show()


def fourier(f, l_bound, r_bound, n):
    s = fourier_series(f, (x, l_bound, r_bound))
    return s.truncate(n)
