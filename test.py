import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# Główna konfiguracja kolumn i wierszy
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)  # wiersz z listą ToDOs może rosnąć

# Nagłówki
tk.Label(root, text="Remainder", font=("Arial", 25), anchor="w").grid(row=0, column=0, padx=5, pady=5, sticky="ew")
tk.Label(root, text="To do", font=("Arial", 20), anchor="w").grid(row=1, column=0, padx=5, pady=5, sticky="ew")

# Frame na listę ToDOs
todo_frame = tk.Frame(root, bg="gray")
todo_frame.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

# Label wewnątrz frame
todo_label = tk.Label(todo_frame, text="ToDOs", bg="gray", anchor="nw", justify="left")
todo_label.pack(fill="both", expand=True)  # wypełnia cały frame w pionie i poziomie

# Guzik w osobnym wierszu/kolumnie
tk.Button(root, text="Add", font=("Arial", 15)).grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

root.mainloop()
