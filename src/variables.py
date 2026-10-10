from dataclasses import dataclass


@dataclass
class SimulatorVariables:
    method_name: str = "Improved Euler (Heun)"
    method_name_2: str = "Ralston's 4th Order Method"

    g: float = 9.81
    L: float = 1.0

    h: float = 0.05
    t_max: float = 10.0

    theta_0: float = 0.2
    omega_0: float = 0.0

    