from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import serial
import serial.tools.list_ports
import os
from PIL import ImageTk, Image
import requests

__author__ = 'Uzair Qidwai'
__copyright__ = 'Copyright (C) 2022, Uzair Qidwai'
__license__ = 'The MIT License (MIT)'
__version__ = 'v1.0.0-beta'
__AppName__ = 'tappy'
__client__ = 'MY Project USA'


#Function to program an ID Card
def program(*args):
    try:
        value = str(id.get())                               # Get entered value
        value = value + "#"                                 # Append a # as EOL char
        ser = serial.Serial(arduino_port,baudrate = 9600, timeout=1)  # Connect to serial
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
    ser = serial.Serial(arduino_port,baudrate = 9600, timeout=1)  # Connect to serial
    ser.write(bytes("R", 'UTF-8'))                          # Push 'R' over serial to indicate read mode
    rr = str(ser.readline())                                # Read Value from serial till \n EOL
    id_number = rr [2:][:-5]                                # Remove surrounding characters & save
    print("ID Number: ", id_number)                         # Print to console
    id_message = ("ID Number: " + id_number)                # Message + Value to be printed
    messagebox.showinfo("Card Read!", id_message)           # Message Box showing value on card

# Function to get ports
def get_ports():
    ports = serial.tools.list_ports.comports()
    return ports

#Function to find the COM port of the arduino
def findArduino(portsFound):
    commPort = 'None'
    numConnection = len(portsFound)
    
    for i in range(0,numConnection):
        port = foundPorts[i]
        strPort = str(port)
        
        if 'Arduino' in strPort: 
            splitPort = strPort.split(' ')
            commPort = (splitPort[0])

    if commPort == 'None':
        messagebox.showerror ('Error','Connection Error! Please disconnect reader, restart the program, and then reconnect the reader.',icon = 'error')
        root.destroy()

    return commPort  

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def aboutScreen():
    aboutWindow = Toplevel(root)
    aboutWindow.iconbitmap(resource_path("tappy_icon.ico"))
    img = ImageTk.PhotoImage(Image.open(resource_path("tappy_logo_small.png")))
    panel = Label(aboutWindow, image = img)
    panel.grid(column=10, row=0, sticky=(W, E))
    #ttk.Label(aboutWindow, text="version 1.0").grid(column=10, row=1)
    ttk.Label(aboutWindow, text=__AppName__ + " " + str(__version__)).grid(column=10, row=1)
    ttk.Label(aboutWindow, text="Developed by " + __author__).grid(column=10, row=2)
    ttk.Label(aboutWindow, text= __client__).grid(column=10, row=3)
    ttk.Label(aboutWindow, text= " ").grid(column=10, row=4)
    aboutWindow.mainloop()


def versionCheck():
    response = requests.get("https://api.github.com/repos/uzairqidwai/tappy/releases/latest")
    release = (response.json()["name"])
    URL = "https://github.com/uzairqidwai/tappy/blob/" + release + "/tappy_app/tappy_app_windows/tappy_app.exe"
    print(release)
    if (release != __version__ and "beta" not in release):
        MsgBox = messagebox.askquestion ('New Version!','tappy '+release+' is available now. Would you like to update?',icon = 'info')
        if MsgBox == 'no':                                      
            root.destroy()                                      
        if MsgBox == 'yes':
            response = requests.get(URL)
            root.destroy()
            



import pyi_splash
pyi_splash.close()

foundPorts = get_ports()        
arduino_port = findArduino(foundPorts)   
versionCheck()           

#---------------------------------------------------------------------------------------------------------------------------------

# GUI Design 

root = Tk()
root.title("tappy")
root.iconbitmap(resource_path("tappy_icon.ico"))

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

# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label='About', command=aboutScreen)
file_menu.add_separator()

# add Exit menu item
file_menu.add_command(
    label='Exit',
    command=root.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu
)

root.mainloop()