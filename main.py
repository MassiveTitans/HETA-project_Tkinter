from tkinter import *
from packages import window1 , window2  , window3


# display
def make_display():
    window = Tk()
    window.title("HETA")
    photo = PhotoImage("source/ico1.ico")
    window.iconbitmap(photo)
    window.geometry("1024x600")
    window.configure(bg="#ffffff")
    return window





window = make_display()
app =window1.Aplication(window)
app.display_1()



window = make_display()
app2 = window2.Aplication2(window)
app2.display_2()



window = make_display()
window3.display_2(window)