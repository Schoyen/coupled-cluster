import collections
from sympy.physics.secondquant import AntiSymmetricTensor, NO, Fd, F
from sympy import symbols, Dummy, Rational


def get_clusters(cc_functions, *args, **kwargs):
    if not isinstance(cc_functions, collections.Iterable):
        cc_functions = [cc_functions]

    return sum([func(*args, **kwargs) for func in cc_functions])


def get_t_1_operator(ast_symb="t"):
    i = symbols("i", below_fermi=True, cls=Dummy)
    a = symbols("a", above_fermi=True, cls=Dummy)

    t_ai = AntiSymmetricTensor(ast_symb, (a,), (i,))
    c_ai = NO(Fd(a) * F(i))

    T_1 = t_ai * c_ai

    return T_1


def get_t_2_operator(ast_symb="t"):
    i, j = symbols("i, j", below_fermi=True, cls=Dummy)
    a, b = symbols("a, b", above_fermi=True, cls=Dummy)

    t_abij = AntiSymmetricTensor(ast_symb, (a, b), (i, j))
    c_abij = NO(Fd(a) * Fd(b) * F(j) * F(i))

    T_2 = Rational(1, 4) * t_abij * c_abij

    return T_2


def get_t_3_operator(ast_symb="t"):
    i, j, k = symbols("i, j, k", below_fermi=True, cls=Dummy)
    a, b, c = symbols("a, b, c", above_fermi=True, cls=Dummy)

    t_abcijk = AntiSymmetricTensor(ast_symb, (a, b, c), (i, j, k))
    c_abcijk = NO(Fd(a) * Fd(b) * Fd(c) * F(k) * F(j) * F(i))

    T_3 = Rational(1, 36) * t_abcijk * c_abcijk

    return T_3


def get_l_1_operator(ast_symb="l"):
    i = symbols("i", below_fermi=True, cls=Dummy)
    a = symbols("a", above_fermi=True, cls=Dummy)

    l_ia = AntiSymmetricTensor(ast_symb, (i,), (a,))
    c_ia = NO(Fd(i) * F(a))

    L_1 = l_ia * c_ia

    return L_1


def get_l_2_operator(ast_symb="l"):
    i, j = symbols("i, j", below_fermi=True, cls=Dummy)
    a, b = symbols("a, b", above_fermi=True, cls=Dummy)

    l_ijab = AntiSymmetricTensor(ast_symb, (i, j), (a, b))
    c_ijab = NO(Fd(i) * Fd(j) * F(b) * F(a))

    L_2 = Rational(1, 4) * l_ijab * c_ijab

    return L_2


def get_l_3_operator(ast_symb="l"):
    i, j, k = symbols("i, j, k", below_fermi=True, cls=Dummy)
    a, b, c = symbols("a, b, c", above_fermi=True, cls=Dummy)

    l_ijkabc = AntiSymmetricTensor(ast_symb, (i, j, k), (a, b, c))
    c_ijkabc = NO(Fd(i) * Fd(j) * Fd(k) * F(c) * F(b) * F(a))

    L_3 = Rational(1, 36) * l_ijkabc * c_ijkabc

    return L_3
