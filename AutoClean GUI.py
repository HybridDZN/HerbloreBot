#AutoClean v3 GUI
from tkinter import *

class AutoCleanV3:
    def __init__(self, master):
        self.master = master
        master.title('Auto Clean v3')
        self.welcome_label = Label(master, text="Welcome to Auto-Clean by xero")
        self.welcome_label.pack()
    
        self.time_entry = Entry(master, width=50)
        self.time_entry.pack()


root = Tk()
my_gui = AutoCleanV3(root)
root.mainloop()