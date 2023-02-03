#Arya Venkat
#01/24/2023
#Period 3 331
# The goal of this project is to create a pop up which shows a logo and also has a button which leads to a pdf reader. 
# When the file is chosen there will be an output that shows the pdf text.

#imports
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from tkinter import ttk



root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open('logo.png') #giving the logo a name where it can be easily recovered from any computer not just local
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(root, text="Select a PDF file on your computer to extract all its text", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

def open_file():
    global logo_label
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfReader(file)
        page = read_pdf.pages[0]
        
        page_content = page.extract_text()

        #text box
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)
        browse_text.set("Search another file")

        #displays image to indicate the process worked
        logo1 = Image.open('logo1.png')
        newsize1 = (200, 200)
        logo1 = logo1.resize(newsize1)
        logo1 = ImageTk.PhotoImage(logo1)
        logo1_label = tk.Label(image=logo1)
        logo1_label.image = logo1
        logo1_label.grid(column=1, row=0)
        logo_label.destroy()

        #pdf converted sucessfully message
        instructions.destroy()
        success = tk.Label(root, text="Successfully Converted PDF to Text", font="Raleway")
        success.grid(columnspan=3, column=0, row=1)

#time
my_w = root  
from time import strftime
def my_time():
    time_string = strftime('%H:%M:%S %p') # time format 
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
	
my_font=('times',52,'bold') # display size and style

l1=tk.Label(my_w,font=my_font,bg='black')
l1.grid(row=3,column=1,padx=5,pady=25)


my_time() 

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=1000, height=250)
canvas.grid(columnspan=3)




root.mainloop()
