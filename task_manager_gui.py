import tkinter as tk
from tkinter import messagebox

class ShoaibTaskTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Shoaib's Task Tracker")
        self.root.geometry("420x520")
        self.root.config(bg="#1e272e")
        self.tasks = []

        title = tk.Label(
            root,
            text="📋 Task Management App",
            font=("Poppins", 18, "bold"),
            bg="#1e272e",
            fg="#34ace0"
        )
        title.pack(pady=10)

        subtitle = tk.Label(
            root,
            text="Stay organized every day!",
            font=("Poppins", 10),
            bg="#1e272e",
            fg="#d2dae2"
        )
        subtitle.pack()

        input_frame = tk.Frame(root, bg="#1e272e")
        input_frame.pack(pady=10)

        self.task_entry = tk.Entry(
            input_frame,
            font=("Poppins", 12),
            width=25,
            bd=2,
            relief="solid"
        )
        self.task_entry.grid(row=0, column=0, padx=5)

        add_btn = tk.Button(
            input_frame,
            text="➕ Add New",
            bg="#34ace0",
            fg="white",
            font=("Poppins", 10, "bold"),
            width=10,
            command=self.add_task
        )
        add_btn.grid(row=0, column=1, padx=5)

        self.task_listbox = tk.Listbox(
            root,
            width=45,
            height=15,
            font=("Poppins", 11),
            selectmode=tk.SINGLE,
            bd=2,
            relief="solid"
        )
        self.task_listbox.pack(pady=10)

        self.counter_label = tk.Label(
            root,
            text="Total Tasks: 0",
            font=("Poppins", 10, "bold"),
            bg="#1e272e",
            fg="#f1f2f6"
        )
        self.counter_label.pack()

        btn_frame = tk.Frame(root, bg="#1e272e")
        btn_frame.pack(pady=15)

        complete_btn = tk.Button(
            btn_frame,
            text="✅ Done",
            bg="#2ecc71",
            fg="white",
            font=("Poppins", 10, "bold"),
            width=10,
            command=self.mark_completed
        )
        complete_btn.grid(row=0, column=0, padx=5)

        delete_btn = tk.Button(
            btn_frame,
            text="🗑️ Remove",
            bg="#e74c3c",
            fg="white",
            font=("Poppins", 10, "bold"),
            width=10,
            command=self.delete_task
        )
        delete_btn.grid(row=0, column=1, padx=5)

        clear_btn = tk.Button(
            btn_frame,
            text="♻️ Reset",
            bg="#f39c12",
            fg="white",
            font=("Poppins", 10, "bold"),
            width=10,
            command=self.clear_all
        )
        clear_btn.grid(row=0, column=2, padx=5)

        footer = tk.Label(
            root,
            text="Developed by Shoaib Ali. 💻",
            bg="#1e272e",
            fg="#808e9b",
            font=("Poppins", 9)
        )
        footer.pack(side="bottom", pady=8)

    def add_task(self):
        task = self.task_entry.get().strip()
        if not task:
            messagebox.showwarning("Warning", "Please enter a task!")
            return
        self.tasks.append({"task": task, "completed": False})
        self.update_task_list()
        self.task_entry.delete(0, tk.END)

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = f"{task['task']} {'✅' if task['completed'] else '❌'}"
            self.task_listbox.insert(tk.END, display_text)
        self.counter_label.config(text=f"Total Tasks: {len(self.tasks)}")

    def mark_completed(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showinfo("Info", "Please select a task to mark as done.")
            return
        index = selected[0]
        self.tasks[index]["completed"] = True
        self.update_task_list()

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showinfo("Info", "Please select a task to remove.")
            return
        index = selected[0]
        del self.tasks[index]
        self.update_task_list()

    def clear_all(self):
        confirm = messagebox.askyesno("Confirm", "Delete all tasks?")
        if confirm:
            self.tasks.clear()
            self.update_task_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoaibTaskTracker(root)
    root.mainloop()
