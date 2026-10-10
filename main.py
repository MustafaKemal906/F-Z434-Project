from src.variables import SimulatorVariables
from src.pipline import PendulumSimulator
from src.graph import plot_results
from src.gui import run_gui

def main():
    
    var = SimulatorVariables()
    
    print(f"Çalıştırılan Modeller: RK2 ve RK4 (Ralston)")
    print(f"Yerçekimi (g): {var.g} m/s^2, Sarkaç Boyu (L): {var.L} m")

    # 2. Simülatör nesnesini başlat
    sim = PendulumSimulator(var)

    # 3. RK2 (Improved Euler) yöntemini çalıştır
    t, theta_rk2, omega_rk2 = sim.method_rk2()

    # 4. RK4 (Ralston 4th Order) yöntemini çalıştır
    try:
        t, theta_rk4, omega_rk4 = sim.method_rk4(var)
    except TypeError:
        t, theta_rk4, omega_rk4 = sim.method_rk4()

    plot_results(t, theta_rk2, theta_rk4)

if __name__ == "__main__":
    run_gui()