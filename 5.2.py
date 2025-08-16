import tkinter as tk
import tkinter.messagebox as messagebox

def only_numbers(char):
    if char == "":
        return True
    try:
        float(char)
        return True
    except ValueError:
        return False

def on_entry_click(event):
    if event.widget.get() in [f"Введите цифру {i}" for i in range(1, 4)]:
        event.widget.delete(0, tk.END)
        event.widget.config(fg="black")

def on_focusout(event):
    if not event.widget.get():
        for i, e in enumerate([entry1, entry2, entry3], 1):
            if event.widget == e:
                event.widget.insert(0, f"Введите цифру {i}")
                event.widget.config(fg="darkgrey")

def add():
    try:
        # Check if all entries are empty or contain placeholder text
        if (not entry1.get() or entry1.get() == "Введите цифру 1") and \
           (not entry2.get() or entry2.get() == "Введите цифру 2") and \
           (not entry3.get() or entry3.get() == "Введите цифру 3"):
            messagebox.showerror("Ошибка", "Все поля пустые. Введите хотя бы одно число")
            return
            
        num1 = float(entry1.get()) if entry1.get() and entry1.get() != "Введите цифру 1" else 0
        num2 = float(entry2.get()) if entry2.get() and entry2.get() != "Введите цифру 2" else 0
        num3 = float(entry3.get()) if entry3.get() and entry3.get() != "Введите цифру 3" else 0
        result_label.config(text=f"Результат: {num1 + num2 + num3}", fg="black")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные цифры")

def multiply():
    try:
        # Check if all entries are empty or contain placeholder text
        if (not entry1.get() or entry1.get() == "Введите цифру 1") and \
           (not entry2.get() or entry2.get() == "Введите цифру 2") and \
           (not entry3.get() or entry3.get() == "Введите цифру 3"):
            messagebox.showerror("Ошибка", "Все поля пустые. Введите хотя бы одно число")
            return
            
        num1 = float(entry1.get()) if entry1.get() and entry1.get() != "Введите цифру 1" else 1
        num2 = float(entry2.get()) if entry2.get() and entry2.get() != "Введите цифру 2" else 1
        num3 = float(entry3.get()) if entry3.get() and entry3.get() != "Введите цифру 3" else 1
        result_label.config(text=f"Результат: {num1 * num2 * num3}", fg="black")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные цифры")

root = tk.Tk()
root.title("Калькулятор")
root.geometry(f"400x300+{(root.winfo_screenwidth()//2-200)}+{(root.winfo_screenheight()//2-150)}")
root.grid_columnconfigure(0, weight=1)

tk.Label(root, text="Введите цифры", font=("Arial", 15)).grid(row=0, column=0, sticky='nsew')

vcmd = (root.register(only_numbers), "%P")

entry1 = tk.Entry(root, fg="darkgrey", validate="key", validatecommand=vcmd)
entry1.insert(0, "Введите цифру 1")
entry1.bind("<FocusIn>", on_entry_click)
entry1.bind("<FocusOut>", on_focusout)
entry1.grid(row=1, column=0, padx=10, pady=5)

entry2 = tk.Entry(root, fg="darkgrey", validate="key", validatecommand=vcmd)
entry2.insert(0, "Введите цифру 2")
entry2.bind("<FocusIn>", on_entry_click)
entry2.bind("<FocusOut>", on_focusout)
entry2.grid(row=2, column=0, padx=10, pady=5)

entry3 = tk.Entry(root, fg="darkgrey", validate="key", validatecommand=vcmd)
entry3.insert(0, "Введите цифру 3")
entry3.bind("<FocusIn>", on_entry_click)
entry3.bind("<FocusOut>", on_focusout)
entry3.grid(row=3, column=0, padx=10, pady=5)

tk.Label(root, text="").grid(row=5, column=0, pady=3)

tk.Button(root, text="Сложение", command=add, width=12).grid(row=6, column=0, sticky="ns")
tk.Button(root, text="Умножение", command=multiply, width=12).grid(row=7, column=0, sticky="ns")

result_label = tk.Label(root, text="Результат: ", font=("Arial", 12))
result_label.grid(row=8, column=0, pady=10)

root.mainloop()