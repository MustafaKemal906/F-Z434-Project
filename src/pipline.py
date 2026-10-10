import numpy as np
from .variables import SimulatorVariables


class PendulumSimulator:
    def __init__(self, var):
        self.var = var
        self.n_steps = round(var.t_max / var.h) + 1

        self.t = np.linspace(0, var.t_max, self.n_steps) # x-base

        self.theta = np.zeros(self.n_steps) # set 0 initial angle for each step
        self.omega = np.zeros(self.n_steps) 

        self.theta[0] = var.theta_0 # Initial conditions
        self.omega[0] = var.omega_0

    def method_rk2(self):
            g_L = -(self.var.g / self.var.L)
            h = self.var.h
            
            for i in range(self.n_steps - 1):
                # Tüm bu blok 4 boşluk (1 tab) sağa kaydırıldı
                # Define slopes for Improved Euler (Heun) Method
                k1_theta = self.omega[i]
                k1_omega = g_L * self.theta[i]

                theta_2 = self.theta[i] + h * k1_theta
                omega_2 = self.omega[i] + h * k1_omega

                k2_theta = omega_2
                k2_omega = g_L * theta_2

                # Corrector: 0.5'ten sonra eksik olan '*' eklendi
                self.theta[i + 1] = self.theta[i] + (
                    0.5 * (k1_theta + k2_theta) * h
                )

                self.omega[i + 1] = self.omega[i] + (
                    0.5 * (k1_omega + k2_omega) * h
                )

            return self.t, self.theta, self.omega

    def method_rk4(self, var):
        g_L = -(self.var.g / self.var.L)
        h = self.var.h

        for i in range(self.n_steps - 1):
            th_i = self.theta[i]
            om_i = self.omega[i]

            # Step 1: k1
            k1_theta = om_i
            k1_omega = g_L * th_i

            # Step 2: k2
            th_temp2 = th_i + (2/5) * h * k1_theta
            om_temp2 = om_i + (2/5) * h * k1_omega
            k2_theta = om_temp2
            k2_omega = g_L * th_temp2

            # Step 3: k3
            th_temp3 = th_i - (3/20) * h * k1_theta + (3/4) * h * k2_theta
            om_temp3 = om_i - (3/20) * h * k1_omega + (3/4) * h * k2_omega
            k3_theta = om_temp3
            k3_omega = g_L * th_temp3

            # Step 4: k4
            th_temp4 = th_i + (1/44) * h * (19*k1_theta - 15*k2_theta + 40*k3_theta)
            om_temp4 = om_i + (1/44) * h * (19*k1_omega - 15*k2_omega + 40*k3_omega)
            k4_theta = om_temp4
            k4_omega = g_L * th_temp4

            # Step 5: Update
            self.theta[i + 1] = th_i + (1/72) * h * (11*k1_theta + 25*k2_theta + 25*k3_theta + 11*k4_theta)
            self.omega[i + 1] = om_i + (1/72) * h * (11*k1_omega + 25*k2_omega + 25*k3_omega + 11*k4_omega)

        return self.t, self.theta, self.omega

