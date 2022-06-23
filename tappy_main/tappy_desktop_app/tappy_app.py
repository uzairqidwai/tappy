from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import serial
import time
import serial.tools.list_ports

def program(*args):
    try:
        value = str(id.get())
        value = value + "#"
        ser = serial.Serial(arduino_port, 9600)
        time.sleep(3)
        ser.write(bytes(value, 'UTF-8'))
        print("Written")
        success()
        
    except ValueError:
        pass

def success():
    MsgBox = messagebox.askquestion ('Success!','Success! Would you like to program another?',icon = 'info')
    if MsgBox == 'no':
       root.destroy()
    if MsgBox == 'yes':
        id_entry.delete(0, END)

def find_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print (p)
    if "Arduino Leonardo" in p.description:
        return p.device


arduino_port = find_port()

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