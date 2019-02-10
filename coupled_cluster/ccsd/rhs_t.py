# Labelling of the different terms comes from the book "Many-Body Methods in
# Chemistry and Physics" by I. Shavitt and R. J. Bartlett.


# Diagrams for CCSD T_1 amplitude equations


def compute_t_1_amplitudes(f, u, t_1, t_2, o, v, np, out=None):
    if out is None:
        out = np.zeros_like(t_1)

    return out


def compute_t_2_amplitudes(f, u, t_1, t_2, o, v, np, out=None):
    if out is None:
        out = np.zeros_like(t_2)

    return out


def add_s1_t(f, o, v, out, np):
    """Function adding the S1 diagram

        g(f, u, t) <- f^{a}_{i}

    Number of FLOPS required: O(m n).
    """
    out += f[v, o]


def add_s2a_t(f, t_2, o, v, out, np):
    """Function adding the S2a diagram

        g(f, u, t) <- f^{k}_{c} t^{ac}_{ik}

    Numer of FLOPS required: O(m^2 n^2).
    """
    out += np.tensordot(f[o, v], t_2, axes=((0, 1), (3, 1)))


def add_s2b_t(u, t_2, o, v, out, np):
    """Function adding the S2b diagram

        g(f, u, t) <- 0.5 u^{ak}_{cd} t^{cd}_{ik}

    Number of FLOPS required: O(m^3 n^2).
    """
    out += 0.5 * np.tensordot(u[v, o, v, v], t_2, axes=((1, 2, 3), (3, 0, 1)))


def add_s2c_t(u, t_2, o, v, out, np):
    """Function adding the S2b diagram

        g(f, u, t) <- -0.5 u^{kl}_{ic} t^{ac}_{kl}

    Number of FLOPS required: O(m^2 n^3)
    """
    term = np.tensordot(u[o, o, o, v], t_2, axes=((0, 1), (2, 3)))
    out -= 0.5 * np.trace(term, axis1=1, axis2=3).swapaxes(0, 1)


def add_s3a_t(f, t_1, o, v, out, np):
    """Function adding the S3a diagram

        g(f, u, t) <- f^{a}_{c} t^{c}_{i}

    Number of FLOPS required: O(m^2 n)
    """
    out += np.tensordot(f[v, v], t_1, axes=((1), (0)))


def add_s3b_t(f, t_1, o, v, out, np):
    """Function adding the S3b diagram

        g(f, u, t) <- -f^{k}_{i} t^{a}_{k}

    Number of FLOPS required: O(m, n^2)
    """
    out += -np.tensordot(f[o, o], t_1, axes=((0), (1))).transpose(1, 0)


def add_s3c_t(u, t_1, o, v, out, np):
    """Function adding the S3c diagram

        g(f, u, t) <- u^{ak}_{ic} t^{c}_{k}

    Number of FLOPS required: O(m^2, n^2)
    """
    out += np.tensordot(u[v, o, o, v], t_1, axes=((1, 3), (1, 0)))


def add_s4a_t(u, t_1, t_2, o, v, out, np):
    """Function for adding the S4a diagram

        g(f, u, t) <- -0.5 * u^{kl}_{cd} t^{c}_{i} t^{ad}_{kl}

    Number of FLOPS required: O(m^3 n^3)
    """
    W_kldi = -0.5 * np.tensordot(u[o, o, v, v], t_1, axes=((2), (0)))
    out += np.tensordot(W_kldi, t_2, axes=((0, 1, 2), (2, 3, 1))).swapaxes(0, 1)


def add_s4b_t(u, t_1, t_2, o, v, out, np):
    """Function for adding the S4b diagram

        g(f, u, t) <- -0.5 * u^{kl}_{cd} t^{a}_{k} t^{cd}_{il}

    Number of FLOPS required: O(m^3 n^3)
    """
    W_lcda = -0.5 * np.tensordot(u[o, o, v, v], t_1, axes=((0), (1)))
    out += np.tensordot(W_lcda, t_2, axes=((1, 2, 0), (0, 1, 3)))


def add_s4c_t(u, t_1, t_2, o, v, out, np):
    """Function for adding the S4c diagram

        g(f, u, t) <- u^{kl}_{cd} t^{c}_{k} t^{da}_{li}

    Number of FLOPS required: O(m^3 n^3)
    """
    temp_ld = np.tensordot(u[o, o, v, v], t_1, axes=((0, 2), (1, 0)))
    out += np.tensordot(temp_ld, t_2, axes=((0, 1), (2, 0)))


def add_s5a_t(f, t_1, o, v, out, np):
    """Function for adding the S5a diagram

        g(f, u, t) <- f^{k}_{c} t^{c}_{i} t^{a}_{k}

    Number of FLOPS required: O(m^2, n^2)
    """
    temp_ki = -np.tensordot(f[o, v], t_1, axes=((1), (0)))
    out += np.tensordot(temp_ki, t_1, axes=((0), (1))).swapaxes(0, 1)


def add_s5b_t(u, t_1, o, v, out, np):
    """Function for adding the S5b diagram

        g(f, u, t) <- u^{ak}_{cd} t^{c}_{i} t^{d}_{k}

    Number of FLOPS required: O(m^2 n^3)
    """
    W_akdi = np.tensordot(u[v, o, v, v], t_1, axes=((2), (0)))
    out += np.tensordot(W_akdi, t_1, axes=((1, 2), (1, 0)))


def add_s5c_t(u, t_1, o, v, out, np):
    """Function for adding the S5c diagram

        g(f, u, t) <- - u^{kl}_{ic} t^{a}_{k} t^{c}_{l}

    Number of FLOPS required: O(m^2, n^3)
    """
    W_lica = -np.tensordot(u[o, o, o, v], t_1, axes=((0), (1)))
    out += np.tensordot(W_lica, t_1, axes=((0, 2), (1, 0))).swapaxes(0, 1)


def add_s6_t(u, t_1, o, v, out, np):
    """Function for adding the S6 diagram

        g(f, u, t) <- (-1) * u ^{kl}_{cd} t^{c}_{i} t^{a}_{k} t^{d}_{l}

    Number of FLOPS required: O(m^3 n^3)
    """
    W_kldi = -np.tensordot(u[o, o, v, v], t_1, axes=((2), (0)))
    W_ldia = np.tensordot(W_kldi, t_1, axes=((0), (1)))
    out += np.tensordot(W_ldia, t_1, axes=((0, 1), (1, 0))).swapaxes(0, 1)


# Diagrams for T_1 contributions to CCSD T_2 equations.


def add_d4a_t(u, t_1, o, v, out, np):
    """Function for adding the D4a diagram

        g(f, u, t) <- u^{ab}_{cj} t^{c}_{i} P(ij)

    Number of FLOPS required: O(m^3, n^2)
    """
    
    # Get abji want abij
    term = np.tensordot(u[v, v, v, o], t_1, axes=((2), (0))).transpose(
        0, 1, 3, 2
    )
    term -= term.swapaxes(2, 3)
    out += term


def add_d4b_t(u, t_1, o, v, out, np):
    """Function for adding the D4b diagram

        g(f, u, t) <-  (-1) * u^{kb}_{ij} t^{a}_{k} P(ab)

    Number of FLOPS required: O(m^2 n^3)
    """
    term = np.tensordot(u[o, v, o, o], t_1, axes=((0), (1))).transpose(
        3, 0, 1, 2
    )
    term -= term.swapaxes(0, 1)
    out -= term

def add_d5a_t(f, t_1, t_2, o, v, out, np):
    """Function for adding the D5a diagram

        g(f, u, t) <- (-1) * f^{k}_{c} t^{c}_{i} t^{ab}_{kj} P(ij)

    Number of FLOPS required: O(m^3 n^3)
    """

    term_ki = np.tensordot(f[o, v], t_1, axes=((1), (0)))
    # Get iabj want abij
    term = np.tensordot(term_ki, t_2, axes=((0), (2))).transpose(1, 2, 0, 3)
    term -= term.swapaxes(2, 3)
    out -= term
