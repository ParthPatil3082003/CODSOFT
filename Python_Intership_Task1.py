#Author Parth Patil
import tkinter as tk
from tkinter import ttk, messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do App By Parth Patil")

        # Style configuration
        self.style = ttk.Style()
        self.style.configure('Green.TButton', font=('Broadway', 14), padding=5, background = 'green', foreground='green')
        self.style.configure('Red.TButton', font=('Broadway', 14), padding=5,background='red', foreground='red')
        self.style.configure('Blue.TButton', font=('Broadway', 14), padding=5,background='blue', foreground='blue')
        self.style.configure('TEntry', font=('Agency FB', 14), padding=5)
        self.style.configure('TListbox', font=('Agency FB', 14), padding=5)

        # Create widgets
        self.task_entry = ttk.Entry(self.master, style='TEntry', width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.add_button = ttk.Button(self.master, text="Add Task", command=self.add_task, style='Green.TButton' )
        self.add_button.grid(row=0, column=2, padx=10, pady=10)
        #can use shortcut enter
        self.task_entry.bind('<Return>', lambda event=None: self.add_task())


        self.task_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, font=('Agency FB', 16), width=30, height=10)
        self.task_listbox.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

        self.delete_button = ttk.Button(self.master, text="Delete Task", command=self.delete_task, style='Red.TButton')
        self.delete_button.grid(row=2, column=0, padx=10, pady=10)
        #can use shortcut ctrl+enter
        self.master.bind('<Control-Return>', lambda event=None: self.delete_task())



        self.update_button = ttk.Button(self.master, text="Update Task", command=self.update_task, style='Blue.TButton')
        self.update_button.grid(row=2, column=1, padx=10, pady=10)
        #can use shortcut shift+enter
        self.master.bind('<Shift-Return>', lambda event=None: self.update_task())


        # Populate the listbox with existing tasks
        self.tasks = []  # Example tasks
        self.refresh_task_list()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.refresh_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.refresh_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.task_entry.get()
            if task:
                self.tasks[selected_index[0]] = task
                self.refresh_task_list()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter a task.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()