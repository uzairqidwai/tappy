from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import serial
import serial.tools.list_ports

#Function to program an ID Card
def program(*args):
    try:
        value = str(id.get())                               # Get entered value
        value = value + "#"                                 # Append a # as EOL char
        ser = serial.Serial(arduino_port, 9600)             # Connect to serial
        ser.write(bytes("W", 'UTF-8'))                      # Push 'W' over serial to indicate write mode
        ser.write(bytes(value, 'UTF-8'))                    # Push value to be written over serial
        print(value, " Written")                            # Print to console
        written()                                           # Call Message Box function
        
    except ValueError:
        pass

#Funtion to pop out a message box once written
def written():
    MsgBox = messagebox.askquestion ('Written!','Written! Please use the read function to ensure data was written correctly. Would you like to continue?',icon = 'info')
    if MsgBox == 'no':                                      
       root.destroy()                                       # Close program
    if MsgBox == 'yes':
        id_entry.delete(0, END)                             # Clear previous entered value from box


#Function to read an ID Card
def read():
    ser = serial.Serial(arduino_port, 9600)                 # Connect to serial
    ser.write(bytes("R", 'UTF-8'))                          # Push 'R' over serial to indicate read mode
    rr = str(ser.readline())                                # Read Value from serial till \n EOL
    id_number = rr [2:][:-5]                                # Remove surrounding characters & save
    print("ID Number: ", id_number)                         # Print to console
    id_message = ("ID Number: " + id_number)                # Message + Value to be printed
    messagebox.showinfo("Card Read!", id_message)           # Message Box showing value on card


#Function to find the COM port of the arduino
def find_port():
    ports = list(serial.tools.list_ports.comports())        # List all COM ports
    for p in ports:
        print (p)
    if "Arduino Leonardo" in p.description:                 
        return p.device                                     # Returns the COM port number


arduino_port = find_port()                                  # Saves the COM port value in a var

#---------------------------------------------------------------------------------------------------------------------------------

# GUI Design 

import pyi_splash
pyi_splash.close()


root = Tk()
root.title("tappy")
#root.iconbitmap("C:/Users/Uzair Qidwai/Documents/GitHub/tappy/tappy_programming_app/tappy_icon.ico")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

id_number = str()
id = StringVar()
id_entry = ttk.Entry(mainframe, width=7, textvariable=id)
id_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

#ttk.Label(mainframe, text="Hold The Card On The Reader").grid(column=1, row=0, sticky=E)

ttk.Label(mainframe, text="Enter ID Number:").grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text="Program", command=program).grid(column=3, row=1, sticky=W)

ttk.Separator(mainframe, orient='horizontal').grid(column=1, row=2, columnspan=3, sticky=W+E)

ttk.Button(mainframe, text="Read ID", command=read).grid(column=1, row=3, columnspan=3, sticky=W+E)


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

id_entry.focus()
root.bind("<Return>", program)


root.mainloop()