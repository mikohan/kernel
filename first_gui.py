# import tkinter as tk
#
# class SampleApp(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         def_var = 'dom --dfsdf'
#         self.entry = tk.Entry(self,text = def_var)
#         self.button = tk.Button(self, text="Get", command=self.on_button)
#         self.button.pack(padx=20,pady=20)
#         self.entry.pack()
#         self.geometry("300x200")
#
#     def on_button(self):
#         print(self.entry.get())
#
# app = SampleApp()
# app.mainloop()


from tkinter import *

def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
   e1.delete(0,END)
   e2.delete(0,END)
   master.destroy()

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)
e1.insert(10,"Miller")
e2.insert(10,"Jill")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )