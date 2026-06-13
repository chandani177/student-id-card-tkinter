import tkinter as tk
from tkinter import ttk,messagebox

def display():
     x1 = inputbox0.get()
     x2 = inputbox1.get()
     x3 = inputbox2.get()
     x4 = inputbox3.get()
     x5 = inputbox4.get()
     x6 = inputbox5.get()

    # Validation
     if x1 == "" or x2 == "" or x3 == "" or x4 == "" or x5 == "" or x6 == "":
         messagebox.showerror("Error", "Please fill all fields")
         return
     
     if not x2.isdigit():
         messagebox.showerror("Error", "Roll no number must contain only digits")
         return

     if not x6.isdigit():
         messagebox.showerror("Error", "Phone number must contain only digits")
         return

     messagebox.showinfo("Success", "ID Card Generated Successfully")

     # Display values
     label00.grid(row=8,column=0,sticky="ewns")
     label11.grid(row=9,column=0,sticky="ewns")
     label22.grid(row=10,column=0,sticky="ewns")
     label33.grid(row=11,column=0,sticky="ewns")
     label44.grid(row=12,column=0,sticky="ewns")
     label55.grid(row=13,column=0,sticky="ewns")

     ouputvar1.set(x1)
     ouputvar2.set(x2)
     ouputvar3.set(x3)
     ouputvar4.set(x4)
     ouputvar5.set(x5)
     ouputvar6.set(x6)

     output1.grid(row=8,column=1,sticky="ewns")
     output2.grid(row=9,column=1,sticky="ewns")
     output3.grid(row=10,column=1,sticky="ewns")
     output4.grid(row=11,column=1,sticky="ewns")
     output5.grid(row=12,column=1,sticky="ewns")
     output6.grid(row=13,column=1,sticky="ewns")
    

# window Create
window = tk.Tk()
window.title("ID Card")
window.geometry("1200x1200")
window.configure(bg="#5D8F62")

# row and column create
window.columnconfigure((0,1),weight=1)
window.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14),weight=1)

#heading create
heading = tk.Label(window,text="Student ID Card Information",bg="darkgreen",fg="white",font=("Calibri 24 bold"))
heading.grid(row=0,column=0,sticky="ewns")

#photo 
photo = tk.PhotoImage(file="photo1.png")

photo = photo.subsample(10,10)   # Make image 4 times smaller

photoLabel = tk.Label(window, image=photo)
photoLabel.image = photo
photoLabel.grid(row=0, column=1, rowspan=7, sticky="n")


# label created
label0 = ttk.Label(window,text="Name",font=("Arial",12,"bold"))
label1 = ttk.Label(window,text="Roll no",font=("Arial",12,"bold"))
label2 = ttk.Label(window,text="Branch",font=("Arial",12,"bold"))
label3 = ttk.Label(window,text="Year",font=("Arial",12,"bold"))
label4 = ttk.Label(window,text="Collage Name",font=("Arial",12,"bold"))
label5 = ttk.Label(window,text="Phone no.",font=("Arial",12,"bold"))

label00 = ttk.Label(window,text="Name")
label11 = ttk.Label(window,text="Roll no")
label22 = ttk.Label(window,text="Branch")
label33 = ttk.Label(window,text="Year")
label44 = ttk.Label(window,text="Collage Name")
label55 = ttk.Label(window,text="Phone no.")

# input boxes created
name = tk.StringVar()
rollno = tk.StringVar()
branch = tk.StringVar()
year = tk.StringVar()
collage_name = tk.StringVar()
phone_no = tk.StringVar()
inputbox0 = ttk.Entry(window,textvariable=name)
inputbox1 = ttk.Entry(window,textvariable=rollno)
inputbox2 = ttk.Entry(window,textvariable=branch)
inputbox3 = ttk.Entry(window,textvariable=year)
inputbox4 = ttk.Entry(window,textvariable=collage_name)
inputbox5 = ttk.Entry(window,textvariable=phone_no)



# filling value of row and column

label0.grid(row=1,column=0,sticky="ewns")
label1.grid(row=2,column=0,sticky="ewns")
label2.grid(row=3,column=0,sticky="ewns")
label3.grid(row=4,column=0,stick="ewns")
label4.grid(row=5,column=0,sticky="ewns")
label5.grid(row=6,column=0,sticky="ewns")

inputbox0.grid(row=1,column=1,sticky="ewns")
inputbox1.grid(row=2,column=1,sticky="ewns")
inputbox2.grid(row=3,column=1,sticky="ewns")
inputbox3.grid(row=4,column=1,stick="ewns")
inputbox4.grid(row=5,column=1,sticky="ewns")
inputbox5.grid(row=6,column=1,sticky="ewns")

b1 = tk.Button(window,text="Submit Me",command=display,bg="orange",fg="white",font=("Calibri",14,"bold"))
b1.grid(row=7,column=0,stick="ewns",columnspan=2)

# display information 
ouputvar1 = tk.StringVar()
ouputvar2 = tk.StringVar()
ouputvar3 = tk.StringVar()
ouputvar4 = tk.StringVar()
ouputvar5 = tk.StringVar()
ouputvar6 = tk.StringVar()
output1 = ttk.Label(window,text="check the age",textvariable=ouputvar1,relief="solid",borderwidth=1)
output2 = ttk.Label(window,text="check the age",textvariable=ouputvar2,relief="solid",borderwidth=1)
output3 = ttk.Label(window,text="check the age",textvariable=ouputvar3,relief="solid",borderwidth=1)
output4 = ttk.Label(window,text="check the age",textvariable=ouputvar4,relief="solid",borderwidth=1)
output5 = ttk.Label(window,text="check the age",textvariable=ouputvar5,relief="solid",borderwidth=1)
output6 = ttk.Label(window,text="check the age",textvariable=ouputvar6,relief="solid",borderwidth=1)

footer = tk.Label(window,text="Valid Student Identity",bg="navy",fg="white")
footer.grid(row=14,column=0,stick="ewns",columnspan=2)



window.mainloop()
