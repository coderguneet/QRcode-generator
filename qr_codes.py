from tkinter import *
import qrcode
import os
from PIL import ImageTk,Image
root=Tk()
resultimage=1
def qrdisplay():
    global resultimage
    mysite=site.get()
    handle=qrcode.make(mysite)
    handle.save("sampleimage.png")
    resultimage=ImageTk.PhotoImage(Image.open("sampleimage.png"))
    l=Label(image=resultimage)
    l.grid(row=3,column=0)
site=Entry(root,width=32)
site.grid(row=0,column=0,padx=10)
site.insert(0,"enter website")
mybutton=Button(root,text="enter",command=qrdisplay)
mybutton.grid(row=1,column=0)
root.mainloop()
os.remove("sampleimage.png")

