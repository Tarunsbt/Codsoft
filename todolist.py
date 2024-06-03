import tkinter
from tkinter import messagebox, Tk
task_row=3
def task():
    global task_frame
    global task_row
    task_name = task_entry.get()
    if task_name != "":
        task_frame = tkinter.Frame(task_frame)
        task_frame.grid(row=task_row,column=0,columnspan=3, sticky="w")

        task_label = tkinter.Label(task_frame, text=task_name, font=("TimesNewRoman", 10))
        task_label.grid(row=3,column=0,padx=5,pady=5)

        edit_button = tkinter.Button(task_frame, text="Edit", bg="green", fg="white",
                                command=lambda tf=task_frame, tl=task_label: edit_task(tf, tl))
        edit_button.grid(row=3,column=1,padx=5)

        delete_button = tkinter.Button(task_frame, text="Delete", bg="red", fg="white",
                                  command=lambda tf=task_frame: delete_task(tf))
        delete_button.grid(row=3,column=2,padx=5)

        task_entry.delete(0, tkinter.END)
        task_row += 1
    else:
        messagebox.showwarning("Warning", "You must enter a task.")
def edit_task(task_frame, task_label):
    new_task_name = task_entry.get()
    if new_task_name != "":
        task_label.config(text=new_task_name)
        task_entry.delete(0, tkinter.END)
    else:
        messagebox.showwarning("Warning", "You must enter a new task name.")



def delete_task(self, task_frame):
        task_frame.destroy()



window=Tk()
window.title("To-do List")
window.config(padx=10,pady=5,bg="white")

heading=tkinter.Label(text="To-Do List",fg="white",bg="green",font="Courier")
heading.grid(row=0,column=1)
entry_frame = tkinter.Frame()
entry_frame.grid(row=1,column=0,columnspan=3,pady=5)


task_entry = tkinter.Entry(entry_frame, font=("Courier", 10))
task_entry.grid(row=1,column=0,pady=5)


add_button = tkinter.Button(entry_frame, text="Submit", width=20,command=task)
add_button.grid(row=1,column=1,pady=5)
task_frame=tkinter.Frame()
task_frame.grid(row=3,column=0,columnspan=3)

title = tkinter.Label( text="Tasks", font=("TimesNewRoman", 16))
title.grid(row=2,column=1,pady=5)

        # Create a frame for the tasks




window.mainloop()
