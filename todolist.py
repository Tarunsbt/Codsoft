import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # Create a frame for the header
        header_frame = tk.Frame(self.root, bg="green", padx=10, pady=10)
        header_frame.pack(fill=tk.X, pady=10)

        # Create a header label
        header = tk.Label(header_frame, text="To-Do List", font=("Helvetica", 24), bg="green", fg="white")
        header.pack()

        # Create a frame for the entry and submit button
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=10, padx=20, fill=tk.X)

        # Create an Entry widget to enter tasks
        self.task_entry = tk.Entry(entry_frame, font=("Helvetica", 12))
        self.task_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        # Create a Button to add tasks
        add_task_button = tk.Button(entry_frame, text="Submit", width=20, command=self.add_task)
        add_task_button.pack(side=tk.LEFT, padx=5)

        # Create a title label
        title = tk.Label(self.root, text="Tasks", font=("Helvetica", 18))
        title.pack(pady=5)

        # Create a frame for the tasks
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(pady=10, padx=20)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            task_frame = tk.Frame(self.task_frame)
            task_frame.pack(fill=tk.X, pady=2)

            task_label = tk.Label(task_frame, text=task, font=("Helvetica", 12), anchor="w")
            task_label.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))

            edit_button = tk.Button(task_frame, text="Edit", bg="green", fg="white", command=lambda tf=task_frame, tl=task_label: self.edit_task(tf, tl))
            edit_button.pack(side=tk.LEFT, padx=(0, 5))

            delete_button = tk.Button(task_frame, text="Delete", bg="red", fg="white", command=lambda tf=task_frame: self.delete_task(tf))
            delete_button.pack(side=tk.LEFT)

            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def edit_task(self, task_frame, task_label):
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Task")

        edit_entry = tk.Entry(edit_window, font=("Helvetica", 12))
        edit_entry.pack(pady=10, padx=10)
        edit_entry.insert(0, task_label.cget("text"))

        def save_edit():
            new_task = edit_entry.get()
            if new_task != "":
                task_label.config(text=new_task)
                edit_window.destroy()
            else:
                messagebox.showwarning("Warning", "You must enter a task.")

        save_button = tk.Button(edit_window, text="Save", command=save_edit)
        save_button.pack(pady=5)

    def delete_task(self, task_frame):
        task_frame.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
