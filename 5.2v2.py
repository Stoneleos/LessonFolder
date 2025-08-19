import tkinter as tk
import tkinter.messagebox as messagebox
import math

def only_numbers(char):
    try:
        float(char) if char else 0
        return True
    except ValueError:
        return False

def on_entry_click(event):
    widget = event.widget
    if widget.get() in [f"Введите число {i}" for i in range(1, 4)]:
        widget.delete(0, tk.END)
        widget.config(fg="black")

def on_focusout(event):
    widget = event.widget
    if not widget.get():
        widget.insert(0, f"Введите число {1 + [entry1, entry2, entry3].index(widget)}")
        widget.config(fg="grey")

def calculate(op):
    try:
        nums = [float(e.get()) if e.get() not in [f"Введите число {i}" for i in range(1, 4)] else (0 if op == "add" else 1) for e in [entry1, entry2, entry3]]
        result = sum(nums) if op == "add" else math.prod(nums)
        result_label.config(text=f"Результат: {result}", fg="black")
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

root = tk.Tk()
root.title("Калькулятор")
root.geometry(f"400x300+{(root.winfo_screenwidth()//2-200)}+{(root.winfo_screenheight()//2-150)}")
root.grid_columnconfigure(0, weight=1)

tk.Label(root, text="Введите цифры", font=("Arial", 15)).grid(row=0, column=0, sticky="nsew")

vcmd = (root.register(only_numbers), "%P")

for i, entry in enumerate([entry1 := tk.Entry(root, fg="grey", validate="key", validatecommand=vcmd),
                          entry2 := tk.Entry(root, fg="grey", validate="key", validatecommand=vcmd),
                          entry3 := tk.Entry(root, fg="grey", validate="key", validatecommand=vcmd)]):
    entry.insert(0, f"Введите число {i+1}")
    entry.bind("<FocusIn>", on_entry_click)
    entry.bind("<FocusOut>", on_focusout)
    entry.grid(row=i+1, column=0, padx=10, pady=5)

tk.Label(root, text="").grid(row=5, column=0, pady=3)

tk.Button(root, text="Сложение", command=lambda: calculate("add"), width=12).grid(row=6, column=0, sticky="ns")
tk.Button(root, text="Умножение", command=lambda: calculate("multiply"), width=12).grid(row=7, column=0, sticky="ns")

result_label = tk.Label(root, text="Результат: ", font=("Arial", 12))
result_label.grid(row=8, column=0, pady=10)

root.mainloop()