import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario con Tkinter")
root.geometry("400x500")

# Etiquetas y campos de texto
labels = ["Nombre del Pokémon", "Edad", "Domicilio", "Tipo", "Entrenador", "Nivel", "Región", "Altura", "Peso", "Habilidad"]
entries = []

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(root, width=30)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Radio Buttons (Sexo)
tk.Label(root, text="Sexo:").grid(row=len(labels), column=0, padx=10, pady=5, sticky="w")
sexo_frame = tk.Frame(root)
sexo_frame.grid(row=len(labels), column=1, padx=10, pady=5, sticky="w")
sexo_var = tk.StringVar(value="Masculino")
tk.Radiobutton(sexo_frame, text="Masculino", variable=sexo_var, value="Masculino").pack(side="left")
tk.Radiobutton(sexo_frame, text="Femenino", variable=sexo_var, value="Femenino").pack(side="left")

# Combobox (Escolaridad)
tk.Label(root, text="Escolaridad:").grid(row=len(labels) + 1, column=0, padx=10, pady=5, sticky="w")
escolaridad = ttk.Combobox(root, values=["Primaria", "Secundaria", "Preparatoria", "Universidad"])
escolaridad.grid(row=len(labels) + 1, column=1, padx=10, pady=5)

# Checkbox (Disponible para batallas)
checkbox_var = tk.BooleanVar()
tk.Checkbutton(root, text="Disponible para batallas", variable=checkbox_var).grid(row=len(labels) + 2, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Progress Bar
tk.Label(root, text="Progreso de entrenamiento:").grid(row=len(labels) + 3, column=0, padx=10, pady=5, sticky="w")
progress = ttk.Progressbar(root, length=200, mode="determinate")
progress.grid(row=len(labels) + 3, column=1, padx=10, pady=5)
progress["value"] = 50  # Simular progreso al 50%

# Botón de salida
tk.Button(root, text="Cerrar", command=root.quit).grid(row=len(labels) + 4, column=0, columnspan=2, pady=20)

# Ejecutar la aplicación
root.mainloop()
