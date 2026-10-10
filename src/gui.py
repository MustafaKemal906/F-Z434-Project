import tkinter as tk
from tkinter import messagebox
import math
from .variables import SimulatorVariables
from .pipline import PendulumSimulator
from .graph import plot_results

class PendulumGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sarkaç Simülatörü - RK2 ve RK4")
        self.root.geometry("450x650") # Sarkaç çizimi için pencereyi uzattık
        self.root.eval('tk::PlaceWindow . center')

        # Varsayılan değişkenleri yükle
        self.var = SimulatorVariables()
        self.entries = {}

        self.setup_ui()

    def setup_ui(self):
        # --- Formül Gösterimi ---
        formula_frame = tk.Frame(self.root, bg="#f0f0f0", bd=2, relief="groove")
        formula_frame.grid(row=0, column=0, columnspan=2, pady=5, padx=20, sticky="ew")

        tk.Label(formula_frame, text="Sarkaç (SHM) Diferansiyel Denklemi:", 
                 font=("Arial", 10, "bold"), bg="#f0f0f0").pack(pady=2)
        
        equation = "d²θ/dt² = -(g / L) * θ"
        tk.Label(formula_frame, text=equation, 
                 font=("Courier New", 14, "bold"), fg="#d32f2f", bg="#f0f0f0").pack(pady=2)

        # --- Görsel Sarkaç (Canvas) ---
        self.canvas = tk.Canvas(self.root, width=200, height=150, bg="white", highlightthickness=1, highlightbackground="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=5)


        # --- Parametre Giriş Alanları ---
        self.create_input_row(2, "Yerçekimi İvmesi (g):", self.var.g, 'g')
        self.create_input_row(3, "Sarkaç Boyu (L):", self.var.L, 'L')
        self.create_input_row(4, "Zaman Adımı (h):", self.var.h, 'h')
        self.create_input_row(5, "Maks. Zaman (t_max):", self.var.t_max, 't_max')
        self.create_input_row(6, "Başlangıç Açısı (theta_0):", self.var.theta_0, 'theta_0')
        self.create_input_row(7, "Başlangıç Hızı (omega_0):", self.var.omega_0, 'omega_0')

        # Çöz ve Çiz Butonu
        solve_btn = tk.Button(
            self.root, 
            text="🚀 Çöz ve Çiz", 
            command=self.on_solve, 
            bg="#4CAF50", 
            fg="white", 
            font=("Arial", 12, "bold"), 
            width=15
        )
        solve_btn.grid(row=8, column=0, columnspan=2, pady=10)

        # İlk çizimi yap
        self.draw_pendulum()

    def create_input_row(self, row, label_text, default_val, key):
        tk.Label(self.root, text=label_text, font=("Arial", 10)).grid(row=row, column=0, padx=20, pady=5, sticky="w")
        entry = tk.Entry(self.root, font=("Arial", 10), width=15)
        entry.insert(0, str(default_val))
        entry.grid(row=row, column=1, padx=20, pady=5)
        self.entries[key] = entry
        
        # Eğer 'L' veya 'theta_0' değişirse çizimi anında güncelle
        if key in ['L', 'theta_0']:
            entry.bind("<KeyRelease>", lambda event: self.draw_pendulum())

    def draw_pendulum(self):
        self.canvas.delete("all") # Önceki çizimi temizle
        
        try:
            L_val = float(self.entries['L'].get())
            theta_val = float(self.entries['theta_0'].get())
        except ValueError:
            return # Eğer kutu boşsa veya harf varsa çizim yapma

        origin_x = 100
        origin_y = 20

        scale = 80 
        drawn_L = min(L_val * scale, 120) 
        
        x = origin_x + drawn_L * math.sin(theta_val)
        y = origin_y + drawn_L * math.cos(theta_val)

        self.canvas.create_line(origin_x - 30, origin_y, origin_x + 30, origin_y, width=3, fill="black")
        
        self.canvas.create_line(origin_x, origin_y, x, y, width=2, fill="gray")
        
        r = 10 # top yarıçapı
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="red")

        self.canvas.create_line(origin_x, origin_y, origin_x, origin_y + drawn_L + 10, dash=(4, 4), fill="lightgray")

    def on_solve(self):
        try:
            self.var.g = float(self.entries['g'].get())
            self.var.L = float(self.entries['L'].get())
            self.var.h = float(self.entries['h'].get())
            self.var.t_max = float(self.entries['t_max'].get())
            self.var.theta_0 = float(self.entries['theta_0'].get())
            self.var.omega_0 = float(self.entries['omega_0'].get())

            sim = PendulumSimulator(self.var)

            t, theta_rk2, omega_rk2 = sim.method_rk2()
            
            try:
                t, theta_rk4, omega_rk4 = sim.method_rk4(self.var) 
            except TypeError:
                t, theta_rk4, omega_rk4 = sim.method_rk4()

            plot_results(t, theta_rk2, theta_rk4)
            
        except ValueError:
            messagebox.showerror("Hatalı Giriş", "Lütfen tüm değerleri geçerli birer sayı olarak giriniz (Örn: 9.81).")
        except Exception as e:
            messagebox.showerror("Hata", f"Beklenmeyen bir hata oluştu:\n{e}")

    def run(self):
        self.root.mainloop()

def run_gui():
    app = PendulumGUI()
    app.run()