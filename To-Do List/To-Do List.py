import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.tasks = []

        self.label = tk.Label(master, text="Task:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Add Task", command=self.add_task)
        self.button.pack()

        self.listbox = tk.Listbox(master)
        self.listbox.pack()

        self.master.mainloop()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Please enter a task.")


def main():
    root = tk.Tk()
    root.title("To-Do List")
    app = ToDoListApp(root)


if __name__ == "__main__":
    main()