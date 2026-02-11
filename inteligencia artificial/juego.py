import tkinter as tk
from tkinter import messagebox
import random

# --- CONFIGURACIÓN ESTÉTICA ---
COLOR_BG = "#F5F5F5"      
COLOR_CARD = "#FFFFFF"    
COLOR_TEXT = "#333333"    
COLOR_ACCENT = "#9E9E9E"  
FONT_MAIN = ("Segoe UI", 12)
FONT_TITLE = ("Segoe UI", 18, "bold")

class GameHubApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Minimalist Game Hub")
        self.geometry("600x700")
        self.configure(bg=COLOR_BG)
        self.container = tk.Frame(self, bg=COLOR_BG)
        self.container.pack(fill="both", expand=True)
        self.current_frame = None
        self.after_id = None
        self.show_frame(MainMenu)

    def show_frame(self, container_class, game_data=None):
        # Cancelar cualquier animación pendiente
        if self.after_id:
            self.after_cancel(self.after_id)
            self.after_id = None
        
        # Destruir frame actual
        if self.current_frame:
            self.current_frame.destroy()
        
        # Crear nuevo frame
        frame = container_class(parent=self.container, controller=self, data=game_data)
        frame.pack(fill="both", expand=True)
        self.current_frame = frame

# --- NAVEGACIÓN PRINCIPAL ---
class MainMenu(tk.Frame):
    def __init__(self, parent, controller, data=None):
        super().__init__(parent, bg=COLOR_BG)
        tk.Label(self, text="GAME HUB", font=FONT_TITLE, bg=COLOR_BG, fg=COLOR_TEXT).pack(pady=40)
        
        games = [
            ("SNAKE", SnakeGame),
            ("AHORCADO", HangmanGame),
            ("ADIVINANZA", GuessNumberGame),
            ("PPT", RPSGame)
        ]

        for name, cls in games:
            btn = tk.Button(self, text=name, font=FONT_MAIN, bg=COLOR_CARD, fg=COLOR_TEXT,
                           relief="flat", width=20, height=2, 
                           command=lambda c=cls: controller.show_frame(LevelSelector, c))
            btn.pack(pady=10)

class LevelSelector(tk.Frame):
    def __init__(self, parent, controller, data):
        super().__init__(parent, bg=COLOR_BG)
        tk.Label(self, text="SELECCIONAR NIVEL", font=FONT_TITLE, bg=COLOR_BG, fg=COLOR_TEXT).pack(pady=30)
        grid_frame = tk.Frame(self, bg=COLOR_BG)
        grid_frame.pack(pady=10)

        for i in range(1, 11):
            row, col = divmod(i-1, 2)
            btn = tk.Button(grid_frame, text=f"Nivel {i}", font=FONT_MAIN, bg=COLOR_CARD,
                           width=10, command=lambda l=i: controller.show_frame(data, l))
            btn.grid(row=row, column=col, padx=10, pady=5)
        
        tk.Button(self, text="← Volver", font=FONT_MAIN, bg=COLOR_BG, borderwidth=0,
                  command=lambda: controller.show_frame(MainMenu)).pack(pady=30)

# --- LÓGICA DE VIDEOJUEGOS ---

class GuessNumberGame(tk.Frame):
    def __init__(self, parent, controller, level):
        super().__init__(parent, bg=COLOR_BG)
        self.controller, self.level = controller, level
        self.limit = level * 10 # Dificultad: el rango aumenta
        self.secret = random.randint(1, self.limit)
        
        tk.Label(self, text=f"Adivina el número (1-{self.limit})", font=FONT_TITLE, bg=COLOR_BG).pack(pady=20)
        self.entry = tk.Entry(self, font=FONT_MAIN)
        self.entry.pack(pady=10)
        tk.Button(self, text="Probar", command=self.check, bg=COLOR_CARD).pack(pady=5)
        tk.Button(self, text="Volver", command=lambda: controller.show_frame(LevelSelector, GuessNumberGame)).pack(pady=20)

    def check(self):
        try:
            val = int(self.entry.get())
            if val == self.secret:
                messagebox.showinfo("¡Ganaste!", f"Nivel {self.level} superado.")
                self.controller.show_frame(LevelSelector, GuessNumberGame)
            else:
                hint = "Más alto" if val < self.secret else "Más bajo"
                messagebox.showinfo("Pista", hint)
        except: pass

class HangmanGame(tk.Frame):
    def __init__(self, parent, controller, level):
        super().__init__(parent, bg=COLOR_BG)
        self.controller, self.level = controller, level
        # Dificultad: Palabras más técnicas y largas según nivel
        pool = ["SOL", "CASA", "PYTHON", "TECLADO", "SISTEMA", "INTERFAZ", "ALGORITMO", "ESCALABILIDAD", "ABSTRACCION", "MICROPROCESADOR"]
        self.word = pool[level-1]
        self.guesses = []
        self.tries = 6
        
        self.lbl_word = tk.Label(self, text=self.get_display(), font=("Courier", 24), bg=COLOR_BG)
        self.lbl_word.pack(pady=40)
        self.entry = tk.Entry(self, font=FONT_MAIN, width=5)
        self.entry.pack()
        tk.Button(self, text="Intentar Letra", command=self.play).pack(pady=10)
        tk.Button(self, text="Volver", command=lambda: controller.show_frame(LevelSelector, HangmanGame)).pack()

    def get_display(self):
        return " ".join([c if c in self.guesses else "_" for c in self.word])

    def play(self):
        char = self.entry.get().upper()
        self.entry.delete(0, tk.END)
        if char and char not in self.guesses:
            self.guesses.append(char)
            if char not in self.word: self.tries -= 1
            self.lbl_word.config(text=self.get_display())
            
            if "_" not in self.get_display():
                messagebox.showinfo("Victoria", "¡Nivel Completado!")
                self.controller.show_frame(LevelSelector, HangmanGame)
            elif self.tries <= 0:
                messagebox.showerror("Game Over", f"La palabra era {self.word}")
                self.controller.show_frame(LevelSelector, HangmanGame)

class RPSGame(tk.Frame):
    def __init__(self, parent, controller, level):
        super().__init__(parent, bg=COLOR_BG)
        self.controller, self.level = controller, level
        # Dificultad: En niveles altos, necesitas ganar más veces seguidas
        self.wins_needed = 1 + (level // 3)
        self.current_wins = 0
        
        tk.Label(self, text=f"Gana {self.wins_needed} veces para pasar", font=FONT_MAIN, bg=COLOR_BG).pack(pady=20)
        self.lbl_score = tk.Label(self, text=f"Victorias: {self.current_wins}", bg=COLOR_BG)
        self.lbl_score.pack()

        for opt in ["Piedra", "Papel", "Tijera"]:
            tk.Button(self, text=opt, width=15, command=lambda o=opt: self.play(o)).pack(pady=5)
        tk.Button(self, text="Volver", command=lambda: controller.show_frame(LevelSelector, RPSGame)).pack(pady=20)

    def play(self, user):
        cpu = random.choice(["Piedra", "Papel", "Tijera"])
        if (user == "Piedra" and cpu == "Tijera") or (user == "Papel" and cpu == "Piedra") or (user == "Tijera" and cpu == "Papel"):
            self.current_wins += 1
            res = "¡Ganaste esta ronda!"
        elif user == cpu: res = "Empate"
        else:
            self.current_wins = 0
            res = "Perdiste. Racha reiniciada."
        
        self.lbl_score.config(text=f"Victorias: {self.current_wins}")
        if self.current_wins >= self.wins_needed:
            messagebox.showinfo("Nivel Superado", f"Has dominado el nivel {self.level}")
            self.controller.show_frame(LevelSelector, RPSGame)
        else:
            messagebox.showinfo("Resultado", f"CPU eligió: {cpu}\n{res}")

class SnakeGame(tk.Frame):
    def __init__(self, parent, controller, level):
        super().__init__(parent, bg=COLOR_BG)
        self.controller = controller
        self.level = level
        self.speed = max(150 - (level * 12), 40)
        self.food_needed = 3 + level
        self.game_over = False
        self.after_id = None
        
        tk.Label(self, text=f"NIVEL {level} - SNAKE", font=FONT_TITLE, bg=COLOR_BG, fg=COLOR_TEXT).pack(pady=10)
        self.lbl_score = tk.Label(self, text=f"Puntuación: 0 | Meta: {self.food_needed}", font=FONT_MAIN, bg=COLOR_BG, fg=COLOR_TEXT)
        self.lbl_score.pack()
        
        self.canvas = tk.Canvas(self, width=400, height=400, bg="black")
        self.canvas.pack(pady=20)
        
        self.snake = [(100, 100), (100, 120)]
        self.direction = "Up"
        self.next_direction = "Up"
        self.food = (150, 150)
        self.score = 0
        
        # Bind local de teclas
        self.focus_set()
        self.bind("<KeyPress-Up>", lambda e: self.set_direction("Up"))
        self.bind("<KeyPress-Down>", lambda e: self.set_direction("Down"))
        self.bind("<KeyPress-Left>", lambda e: self.set_direction("Left"))
        self.bind("<KeyPress-Right>", lambda e: self.set_direction("Right"))
        
        button_frame = tk.Frame(self, bg=COLOR_BG)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="← Volver", font=FONT_MAIN, bg=COLOR_CARD, 
                  command=self.go_back).pack(side=tk.LEFT, padx=10)
        
        self.run_game()

    def set_direction(self, new_dir):
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_dir != opposites.get(self.direction):
            self.next_direction = new_dir

    def run_game(self):
        if self.game_over:
            return
        
        self.direction = self.next_direction
        head_x, head_y = self.snake[-1]
        
        if self.direction == "Up": head_y -= 20
        elif self.direction == "Down": head_y += 20
        elif self.direction == "Left": head_x -= 20
        elif self.direction == "Right": head_x += 20
        
        new_head = (head_x, head_y)
        
        if head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400 or new_head in self.snake:
            self.game_over = True
            messagebox.showinfo("Game Over", f"¡Colisión! Puntuación: {self.score}\nMeta era: {self.food_needed}")
            self.go_back()
            return

        self.snake.append(new_head)
        
        if new_head == self.food:
            self.score += 1
            self.lbl_score.config(text=f"Puntuación: {self.score} | Meta: {self.food_needed}")
            self.food = (random.randint(0, 19) * 20, random.randint(0, 19) * 20)
            
            if self.score >= self.food_needed:
                self.game_over = True
                messagebox.showinfo("¡Nivel Superado!", f"¡Ganaste el Nivel {self.level}!")
                self.go_back()
                return
        else:
            self.snake.pop(0)

        self.canvas.delete("all")
        self.canvas.create_oval(self.food[0], self.food[1], self.food[0]+20, self.food[1]+20, fill="red")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+20, y+20, fill=COLOR_ACCENT)
        
        self.after_id = self.after(self.speed, self.run_game)

    def go_back(self):
        self.game_over = True
        if self.after_id:
            self.after_cancel(self.after_id)
        self.controller.show_frame(LevelSelector, SnakeGame)

if __name__ == "__main__":
    app = GameHubApp()
    app.mainloop()