from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import serial
import time

def program(*args):
    try:
        value = str(id.get())
        value = value + "#"
        ser = serial.Serial('com8', 9600)
        time.sleep(3)
        ser.write(bytes(value, 'UTF-8'))
        print("Written")
        meters.set(("Success!"))
        Success()
        
    except ValueError:
        pass

def Success():
    MsgBox = messagebox.askquestion ('Success!','Success! Would you like to program another?',icon = 'info')
    if MsgBox == 'no':
       root.destroy()


root = Tk()
root.title("ID Card Programmer")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

id = StringVar()
id_entry = ttk.Entry(mainframe, width=7, textvariable=id)
id_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Program", command=program).grid(column=3, row=1, sticky=W)

ttk.Label(mainframe, text="ID Number").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Hold The Card On The Reader").grid(column=1, row=0, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

id_entry.focus()
root.bind("<Return>", program)


root.mainloop()