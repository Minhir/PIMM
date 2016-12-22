from math import log


def Bethe(element, matt, x=None):
    A = matt.A
    z_0 = matt.z
    rho = matt.rho
    z = element.z
    m = element.m
    beta = element.beta
    gamma = element.gamma
    I = 16 * z_0 ** 0.9
    m_e = 511 * 10**3
    if x is None:
        t = 1
    else:
        t = rho * x
    print(log(2 * m * beta**2 * gamma**2 / I))
    E = 0.3 * z_0 / A * z**2 / (beta**2) * (log(2 * m_e * beta**2 * gamma**2 / I) - beta**2) * t
    if E >= element.T:
        print("E > T !!!!")
    print("E = {0} [MeV/[g/cm^2]]".format(E))
    return E
