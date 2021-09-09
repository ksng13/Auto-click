def callback(input):
    if input.isdigit():
        return True

    elif input == "":
        return True

    else:
        return False

def checkBoxT(entry,location):
    reg = location.register(callback)
    entry.config(validate="key",
             validatecommand=(reg, '%P'))


from tkinter import *
def test():
    root = Tk()
    root.title('Auto Clicker ver 1.0')
    root.geometry('460x325')
    root.resizable(width=FALSE, height=FALSE)
    root.grid_columnconfigure(1, weight=0,minsize=265)
    root.grid_rowconfigure(1, weight=0,minsize=100)

    e = Entry(root)
    e.place(x = 50, y = 50)

    checkBoxT(e,root)

    root.mainloop()