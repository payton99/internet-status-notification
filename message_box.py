import tkinter as tk
from typing import Text

window = tk.Tk()
window.title("Display Message")

# canvas = tk.Canvas(window, width = 650, height = 300)

window.geometry("400x100+60+50")


label1 = tk.Label(window, text = "Looks like you're disconnected from the internet.\nTry to get back online.")
label1.pack(pady = 20)

button = tk.Button(window, text = "Close", command = window.destroy).pack()

tk.mainloop()
