import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

class massive_geodesics:
    def __init__(self, b, v, M):
        """
        b : impact parameter
        v : velocity (when c=1)
        M : blackhole Mass
        E : energy
        L : angular momentum
        r_crtical : critical distance

        """
        if v >= 1:
            raise ValueError("The speed of a particle should not exceed the speed of light")

        self.gamma = 1 / np.sqrt(1 - v ** 2)
        self.E = self.gamma
        self.L = -self.gamma * b * v

        self.central_mass = M

        self.ingoing = True

        self.r = 500
        self.phi = np.pi - np.arcsin(b / self.r)

        self.r_critical = self._critical_radius(M)

        self.x_positions = [] 
        self.y_positions = []

        self._run_trajectory()

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

    def arrive_critical(self):
        return abs(self.r - self.r_critical) > 1e-4
    
    def _run_trajectory(self, step = 0.01):
        while self.r <= 500:
            dr = np.sqrt(self.E ** 2 - (1 - 2 * self.central_mass / self.r) * (1 + self.L ** 2 / self.r ** 2)) * step

            dphi = self.L / self.r ** 2 * step

            if self.ingoing: 
                self.r -= dr
                self.ingoing = self.arrive_critical()

            else:
                self.r += dr

            self.phi += dphi

            self.phi = (self.phi + np.pi) % (2 * np.pi) - np.pi 

            x, y = self.get_cartesian()

            self.x_positions.append(x)
            self.y_positions.append(y)

# you can uncomment the following lines to test if everything works good

# fig, ax = plt.subplots(figsize = (6, 6))

# ax.set_xlim(-10, 10)
# ax.set_ylim(-10, 10)

# M = 1
# r = 2 * M
# circle = Circle((0, 0), r, color = "black")

# test = massive_geodesics(7, 0.9, M)

# ax.add_patch(circle)
# ax.plot(test.x_positions, test.y_positions)

# plt.savefig("test.png")
