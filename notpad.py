from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

root = Tk()
root.title("Untitled - Notepad")

def menu(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()

def copy_t():
    text_box.event_generate("<<Copy>>")

def past_t():
    text_box.event_generate("<<Paste>>")
def cut_t():
    text_box.event_generate("<<Cut>>")
def change_title(x):
    global status_title
    status_title = True
    root.title(x + " - Notpade")

def check_t_box():
    global status_title
    if status_title is False:
        if len(text_box.get(1.0 , END)) != 1:
            root.title("*Untitled - Notepad")
        else:
            root.title("Untitled - Notepad")
    else:
        pass
    root.after(100, check_t_box)

def text_rm_all():
    text_box.delete(1.0, END)

def open_file():
    try:
        global status_title
        status_title = True
        path_open = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        file = open(path_open, "r")
        text_rm_all()
        text_box.insert(1.0, file.read())
        file_name = path_open.split("/")[-1]
        change_title(file_name)
        file.close()
    except:
        pass

def new_file():
    global status_title
    status_title = False
    text_rm_all()
    root.title("Untitled - Notepad")

def save_file():
    path_file = asksaveasfilename(initialfile="Untitled.txt", filetypes=[("Text Documents", ".txt")])
    file = open(path_file, "w")
    file.write(text_box.get(1.0, END))
    file.close()

def app_dst():
    if len(text_box.get(1.0, END)) != 1:
        save_file()
    else:
        root.quit()

# ===========================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=app_dst)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=cut_t)
editmenu.add_command(label="Copy", command=copy_t)
editmenu.add_command(label="Past", command=past_t)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About")
menubar.add_cascade(label="Help", menu=helpmenu)
# ==============================================
scroll_y = Scrollbar(root, orient=VERTICAL)
scroll_x = Scrollbar(root, orient=HORIZONTAL)

text_box = Text(root, wrap=NONE, undo=True, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.configure(command=text_box.xview)
scroll_y.configure(command=text_box.yview)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

text_box.pack(expand=True, fill=BOTH)


# ===================================================
m = Menu(root, tearoff=0)
m.add_command(label="Cut", command=cut_t)
m.add_command(label="Copy", command=copy_t)
m.add_command(label="Paste", command=past_t)

# ==============================================

status_title = False
root.bind("<Button-3>", menu)
root.config(menu=menubar)
check_t_box()
root.mainloop()


