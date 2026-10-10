import matplotlib.pyplot as plt

def plot_results(t, theta_rk2, theta_rk4):
    plt.figure(figsize=(10, 5))

    # RK2 (Improved Euler) Çizimi
    plt.plot(
        t,
        theta_rk2,
        label="RK2 Angle (θ)",
        color="blue",
        linestyle="--"
    )

    # RK4 (Ralston 4th Order) Çizimi
   # RK4 (Ralston 4th Order) Çizimi
    plt.plot(
        t,
        theta_rk4,
        label="RK4 Angle (θ)",
        color="red",
        linewidth=3, # Biraz kalınlaştırdık
        alpha=0.4    # %60 saydam yaptık
    )

    plt.title("SHM Pendulum - RK2 vs RK4")
    plt.xlabel("Time (s)")
    plt.ylabel("Angle (rad)")

    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()