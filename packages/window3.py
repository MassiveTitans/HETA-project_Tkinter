from tkinter import *
import tkintermapview as tk_m
from PIL import ImageTk
from PIL import  Image as imee
import time as t


timer = 0



data = [
        [41.379832756018494, 69.21988242366837] ,
        [41.38027534334367 , 69.22077291706131] ,
        [41.38077395239715  , 69.2219960043721] ,
        [41.3810315582568  , 69.22332638004349] ,
        [41.381933170729766 , 69.22332638004349] ,
        [41.38281867081267  , 69.22341221073196] ,
        [41.38331776554601 , 69.22349804142044]
        ]







def btn_clicked(window):
    print("Button Clicked")
    window.destroy()


def display_2(window):

    def time():
        for x in data:
            for _ in widget.canvas_marker_list[1:]:
                _.delete()
            t.sleep(2)
            image_1 = ImageTk.PhotoImage(imee.open("source/track_35x35.png"))
            ad = widget.set_marker(x[0], x[1], icon=image_1)
            entry1.delete(0 , END)
            entry1.insert(0, "Tashkent, Узбекистан")

    canvas = Canvas(
            window,
            bg = "#ffffff",
            height = 600,
            width = 1024,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file ="source/win2/background.png")
    background = canvas.create_image(
            512.0, 300.0,
            image=background_img)

    img0 = PhotoImage(file ="source/win2/img0.png")
    b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            relief = "flat")

    b0.place(
            x = 102, y = 432,
            width = 136,
            height = 44)

    entry0_img = PhotoImage(file ="source/win2/img_textBox0.png")
    entry0_bg = canvas.create_image(
            170.0, 359.0,
            image = entry0_img)



    entry0 = Entry(

            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0 )

    entry0.place(

            x = 54, y = 340,
            width = 232,
            height = 36)




    entry1_img = PhotoImage(file ="source/win2/img_textBox1.png")
    entry1_bg = canvas.create_image(
            170.0, 245.0,
            image = entry1_img)

    entry1 = Entry(
            bd = 0,
            bg = "#d9d9d9",
            highlightthickness = 0)

    entry1.place(
            x = 54, y = 226,
            width = 232,
            height = 36)

    label = LabelFrame(window)
    label.pack(pady = 0 , side =  RIGHT)
    widget = tk_m.TkinterMapView(label, width=675, height=600)
    widget.set_position(41.379832756018494 , 69.21988242366837)
    widget.set_zoom(16)
    widget.pack()




    entry0.insert( 0 ,  "lat:41.38331776554601  long:69.22349804142044")
    new_marker = widget.set_marker(41.38331776554601, 69.22349804142044, text="Keyingi manzil")


    window.after(1000 , time)









    window.resizable(False, False)
    window.mainloop()