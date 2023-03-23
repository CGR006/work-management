import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime, timedelta

class TaskManager(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.attributes('-fullscreen', True)
        self.master.configure(background='black')
        self.pack()
        self.create_widgets()

        # Create task list
        self.task_list = []

    def create_widgets(self):
        # Create categories
        category_frame = tk.Frame(self, bg='black')
        category_label = tk.Label(category_frame, text="Categories", font=("Helvetica", 20), fg="white", bg="black")
        category_label.pack(pady=20)
        category_frame.pack(side="left", fill="y")

        # Create goals
        goal_frame = tk.Frame(self, bg='black')
        goal_label = tk.Label(goal_frame, text="Goals", font=("Helvetica", 20), fg="white", bg="black")
        goal_label.pack(pady=20)
        goal_frame.pack(side="left", fill="y")

        # Create progress tracker
        progress_frame = tk.Frame(self, bg='black')
        progress_label = tk.Label(progress_frame, text="Progress Tracker", font=("Helvetica", 20), fg="white", bg="black")
        progress_label.pack(pady=20)
        progress_frame.pack(side="left", fill="y")

        # Create search bar
        search_frame = tk.Frame(self, bg='black')
        search_label = tk.Label(search_frame, text="Search", font=("Helvetica", 20), fg="white", bg="black")
        search_label.pack(pady=20)
        search_frame.pack(side="left", fill="y")

        # Create import tasks button
        import_frame = tk.Frame(self, bg='black')
        import_button = tk.Button(import_frame, text="Import Tasks", font=("Helvetica", 20), bg="white", fg="black", command=self.import_tasks)
        import_button.pack(pady=20)
        import_frame.pack(side="left", fill="y")

        # Create add task button
        add_frame = tk.Frame(self, bg='black')
        add_button = tk.Button(add_frame, text="Add Task", font=("Helvetica", 20), bg="white", fg="black", command=self.add_task)
        add_button.pack(pady=20)
        add_frame.pack(side="left", fill="y")

    def import_tasks(self):
        # Open file dialog to select task file
        file_path = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            try:
                # Read task file and add tasks to task list
                with open(file_path, 'r') as f:
                    tasks = f.readlines()
                    for task in tasks:
                        task = task.strip()
                        if task:
                            self.task_list.append(task)
                messagebox.showinfo("Import Tasks", "Tasks imported successfully.")
            except Exception as e:
                messagebox.showerror("Import Tasks", "Error importing tasks: {}".format(e))

    def add_task(self):
        # Open dialog to enter new task
        task = simpledialog.askstring("Add Task", "Enter task:")
        if task:
            self.task_list.append(task)
            messagebox.showinfo("Add Task", "Task added successfully.")

   def edit_task(self, index):
    # Open dialog to edit task
    task = simpledialog.askstring("Edit Task", "Enter task:", initialvalue=self.task_list[index])
    if task:
        self.task_list[index] = task
        messagebox.showinfo("Edit Task", "Task edited successfully.")

def delete_task(self, index):
    # Confirm task deletion
    confirmed = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
    if confirmed:
        del self.task_list[index]
        messagebox.showinfo("Delete Task", "Task deleted successfully.")

def set_reminder(self, index):
    # Open dialog to set reminder time
    reminder = simpledialog.askinteger("Set Reminder", "Enter number of minutes before task due date to set reminder:")
    if reminder:
        # Calculate reminder time
        due_date = datetime.now() + timedelta(minutes=reminder)
        reminder_time = due_date.strftime("%Y-%m-%d %H:%M:%S")
        # Add reminder to task list
        self.task_list[index] += " (Reminder: {})".format(reminder_time)
        messagebox.showinfo("Set Reminder", "Reminder set successfully.")

def save_tasks(self):
    # Open file dialog to select save location
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path:
        try:
            # Save task list to file
            with open(file_path, 'w') as f:
                f.write('\n'.join(self.task_list))
            messagebox.showinfo("Save Tasks", "Tasks saved successfully.")
        except Exception as e:
            messagebox.showerror("Save Tasks", "Error saving tasks: {}".format(e))

def create_task_list(self):
    # Create task list frame
    task_frame = tk.Frame(self.master, bg='black')
    task_frame.pack(expand=True, fill="both")

    # Create task list scrollbar
    scrollbar = tk.Scrollbar(task_frame)
    scrollbar.pack(side="right", fill="y")

    # Create task list
    task_listbox = tk.Listbox(task_frame, font=("Helvetica", 16), bg="black", fg="white", yscrollcommand=scrollbar.set)
    for index, task in enumerate(self.task_list):
        task_listbox.insert(index, task)
    task_listbox.pack(expand=True, fill="both")
    scrollbar.config(command=task_listbox.yview)

    # Add task list right-click menu
    menu = tk.Menu(task_listbox, tearoff=0)
    menu.add_command(label="Edit", command=lambda: self.edit_task(task_listbox.curselection()[0]))
    menu.add_command(label="Delete", command=lambda: self.delete_task(task_listbox.curselection()[0]))
    menu.add_command(label="Set Reminder", command=lambda: self.set_reminder(task_listbox.curselection()[0]))
    task_listbox.bind("<Button-3>", lambda event: menu.post(event.x_root, event.y_root))

def update_task_list(self):
    # Clear and update task list
    task_listbox = self.master.children["!frame"].children["listbox"]
    task_listbox.delete(0, tk.END)
    for index, task in enumerate(self.task_list):
        task_listbox.insert(index, task)

def mainloop(self):
    # Create task list
    self.create_task_list()

    # Add save tasks button
    save_frame = tk.Frame(self.master, bg='black')
    save_button = tk.Button(save_frame, text="Save Tasks", font=("Helvetica", 20), bg="white", fg"black", command=self.save_tasks)
save_button.pack(padx=20, pady=20)
save_frame.pack(side="bottom", fill="x")
        search_frame = tk.Frame(self.master, bg='black')
        search_label = tk.Label(search_frame, text="Search Tasks:", font=("Helvetica", 20), bg="black", fg="white")
        search_label.pack(side="left", padx=20, pady=20)
        search_entry = tk.Entry(search_frame, font=("Helvetica", 20), bg="white", fg="black")
        search_entry.pack(side="left", expand=True, fill="x", padx=20, pady=20)
        search_button = tk.Button(search_frame, text="Search", font=("Helvetica", 20), bg="white", fg="black", command=self.search_tasks)
        search_button.pack(side="left", padx=20, pady=20)
        search_frame.pack(side="bottom", fill="x")

    # Add import tasks button
    import_frame = tk.Frame(self.master, bg='black')
    import_button = tk.Button(import_frame, text="Import Tasks", font=("Helvetica", 20), bg="white", fg="black", command=self.import_tasks)
    import_button.pack(padx=20, pady=20)
    import_frame.pack(side="bottom", fill="x")

    # Update task list periodically
    self.master.after(1000, self.update_task_list)

    # Start main loop
    self.master.mainloop()
    app = TaskManagerApp()
    app.mainloop():
