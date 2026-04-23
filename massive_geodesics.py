import numpy as np
import matplotlib.pyplot as plt

class massive_geodesics:
    def __init__(self, b, v, M):
        if v >= 1:
            raise ValueError("The speed of a particle should not exceed the speed of light")

        self.gamma = 1 / np.sqrt(1 - v ** 2)
        self.E = self.gamma
        self.L = self.gamma * b * v

        self.central_mass = M

        self.ingoing = True

        self.r = 50
        self.phi = np.pi

        self.r_critical = self._critical_radius(M)

    def get_cartesian(self):
        x = self.r * np.cos(self.phi)
        y = self.r * np.sin(self.phi)

        return x, y
    
    def _critical_radius(self, M):
        a = 2 * M * self.L ** 2
        b = - self.L ** 2
        c = 2 * M
        d = self.E ** 2 - 1
    
        coeffs = [d, c, b, a]

        roots = np.roots(coeffs)
        real_roots = roots[np.isreal(roots)]

        return np.max(np.real(real_roots)).item()

    def check_in_or_out(self):
        return abs(self.r - self.r_critical) < 1e4
    
    def trajectory(self, step = 0.01):
        while (self.phi < 0) and (self.r < 50):
            self.ingoing = self.check_in_or_out()

            dr = np.sqrt(self.E ** 2 - (1 - 2 * self.central_mass) / self.r)
    
    