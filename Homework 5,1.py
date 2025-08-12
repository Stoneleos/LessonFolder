# Задание 5.1

import tkinter as tk

def on_entry_click(event):
    if entry1.get() == "Введите имя...":
        entry1.delete(0, "end")
        entry1.config(fg="black")

def on_focusout(event):
    if entry1.get() == "":
        entry1.insert(0, "Введите имя...")
        entry1.config(fg="grey")


root = tk.Tk()
root.title("ФИО")

# Текстовая инструкция сверху по центру
instruction = tk.Label(root, text="Укажите ФИО", font=("Arial", 12))
instruction.grid(row=0, column=0, columnspan=3, pady=(10, 15))

# Панель ввода
tk.Label(root, text="Имя:").grid(row=1, column=0, padx=5, pady=2, sticky="e")



entry1 = tk.Entry(root, fg="grey")
entry1.insert(0, "Введите имя...")
entry1.bind("<FocusIn>", on_entry_click)
entry1.bind("<FocusOut>", on_focusout)
entry1.grid(row=1, column=1, padx=5, pady=2)

tk.Label(root, text="Фамилия:").grid(row=2, column=0, padx=5, pady=2, sticky="e")
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1, padx=5, pady=2)

tk.Label(root, text="Отчество:").grid(row=3, column=0, padx=5, pady=2, sticky="e")
entry3 = tk.Entry(root)
entry3.grid(row=3, column=1, padx=5, pady=2)

# Кнопки сбоку от панелей ввода
tk.Button(root, text="Ввод", width=12).grid(row=1, column=2, padx=10, pady=2, sticky="ns")
tk.Button(root, text="Ввод", width=12).grid(row=2, column=2, padx=10, pady=2, sticky="ns")
tk.Button(root, text="Ввод", width=12).grid(row=3, column=2, padx=10, pady=2, sticky="ns")

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var).grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()