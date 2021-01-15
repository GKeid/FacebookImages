
from tkinter import *
from funcs import *

initFBFiles()

app = Tk()
app.title("Facebook Photos getter")
app.geometry("720x80")

url_entry = Entry(app, width = 720,font=("Century Gothic",15))
url_entry.pack(side=TOP, ipady=10)

url_button = Button(app, text= "Get Photos",width = 720,font=("Century Gothic",15),command = lambda : getAllFBPhotos(url_entry.get()))
url_button.pack(side=TOP, ipady=3)

app.mainloop()


