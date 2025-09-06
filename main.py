import tkinter as tk
import random

window = tk.Tk()
window.geometry("300x200")
window.title("Random number Generator")

secret = random.randint(1, 100)
attempts_left = 7

def guess():
    global attempts_left
    guess = entry.get()

    if not guess.isdigit():
        result.config(text="Please enter a valid number.")
        return
    
    guess = int(guess)
    if guess == secret:
        result.config(text="Угадал!")
        button.config(state="disabled")
    else:
        attempts_left -= 1
        if attempts_left == 0:
            result.config(text=f"Игра окончена! Загаданное число: {secret}")
            button.config(state="disabled")
        elif guess < secret:
            result.config(text=f"Загаданное число больше. Попыток осталось: {attempts_left}")
        else:
            result.config(text=f"Загаданное число меньше. Попыток осталось: {attempts_left}")

entry = tk.Entry(window)
entry.pack(pady=10)

result = tk.Label(window, text="")
result.pack(pady=10)

button = tk.Button(window, text="Нажми сюда", command=guess)
button.pack(pady = 10)

window.mainloop()