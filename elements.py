class Element:

    def __init__(self, name, T):
        self.T = T
        if name == "e-":
            self.z = 1  # ??
            self.m = 511 * 10**3
        elif name == "proton":
            self.z = 1  # ??
            self.m = 938 * 10**6
        elif name == "alpha":
            self.z = 2
            self.m = 3.72 * 10**9
        else:
            raise NameError("Wrong name!")
        self.gamma = (self.m + self.T) / self.m
        self.beta = (1 - 1 / self.gamma**2)**0.5


class Matt:

    def __init__(self, name):
        if name == "Pb":
            self.z = 82
            self.A = 207
            self.rho = 11.3
        elif name == "Al":
            self.z = 13
            self.A = 27
            self.rho = 2.6989
        else:
            raise NameError("Wrong name!")
