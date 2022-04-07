import time
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import pyqrcode 
from pyqrcode import QRCode 

linkT = ""
def dataREAD():
    global linkT
    linkT = str(e1_var.get())
    window.destroy()
window = Tk()

window.title("QR Code Generator App - Elshan Naghizade")

window.resizable(False, False)
window.geometry('600x160+10+10')

lbl1 = Label(window, text="Enter data to be processed (e.g. links, phone numbers, addresses): ", font=("Arial", 12))
lbl1.grid(column=0, row=0, columnspan = 1, pady=(20, 1))

e1_var=StringVar()
e1 = Entry(window ,textvariable = e1_var, width=95)
e1.insert(END, '')
e1.grid(column=0, row=1, columnspan = 1, pady=(2, 10), padx=(10, 10))

B = Button(window, text ="Generate QR code + Save it", command = dataREAD, width = 30, height=2, font=("Arial", 11))
B.grid(column=0, row=2, columnspan = 1,pady=5)


window.mainloop()

saytimiz = pyqrcode.create(linkT) 
  
saytimiz.png("QRshekil.png", scale = 5)

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.resizable(False, False)
root.geometry('600x450+10+10')
root.title("QR Code Generator App - Elshan Naghizade")

lbl = Label(root, text="The generated QR code: ", font=("Arial", 16))
lbl.pack(pady=(15,15))

image1 = Image.open("QRshekil.png")
test = ImageTk.PhotoImage(image1)

label1 = Label(image=test)
label1.image = test

label1.pack()
root.mainloop()