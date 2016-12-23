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
    print("Log = ", log(2 * m * beta**2 * gamma**2 / I))
    E = 0.3 * z_0 / A * z**2 / (beta**2) * (log(2 * m_e * beta**2 * gamma**2 / I) - beta**2) * t
    if E >= element.T:
        print("E > T !!!!")
    print("E = {0} [MeV/[g/cm^2]]".format(E))
    return E


def ksi(element, matt, t):
    """Обозначение Ландау"""
    # TODO: переменная либо t, либо x. Х скорее всего в материале хранить.
    z_0 = matt.z
    A = matt.A
    z = element.z
    beta = element.beta
    # t = x * matt.rho
    KSI = 0.15 * z_0 / A * z**2 / beta**2 * t
    print("ksi = {0} [MeV]".format(KSI))
    return KSI


def T_max(element):
    if 0.95 < element.gamma < 1.05:
        print("Gamma = {0}, не релятивистский случай!".format(element.gamma))
        m = 511 * 10**3
        M = element.m
        T = element.T
        t_max = 4 * m * M / (m + M)**2 * T
    else:
        print("Gamma = {0}, околорелятивистский случай!".format(element.gamma))
        gamma = element.gamma
        t_max = gamma**2
    return t_max
