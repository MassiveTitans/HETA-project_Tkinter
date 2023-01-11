from tkinter import *
import tkintermapview as tk_m
from PIL import ImageTk
from PIL import  Image as imee
from packages import window3







class Aplication2:
    def __init__(self, wnd):
        self.window = wnd





    def btn_clicked(self):
        print("Button Clicked")
        self.window.destroy()


    def display_2(self):



        canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 600,
            width = 1024,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(master = canvas ,file ="source/win2/background.png")
        background = canvas.create_image(
            512.0, 300.0,
            image=background_img)

        img0 = PhotoImage(master = canvas , file ="source/win2/img0.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            relief = "flat")

        b0.place(
            x = 102, y = 432,
            width = 136,
            height = 44)

        entry0_img = PhotoImage(master = canvas , file ="source/win2/img_textBox0.png")
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
        aa = 23.46383
        bb = 54.85734



        entry1_img = PhotoImage(master = canvas , file ="source/win2/img_textBox1.png")
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

        label = LabelFrame(self.window)
        label.pack(pady = 0 , side =  RIGHT)
        widget = tk_m.TkinterMapView(label, width=675, height=600)
        widget.set_position(41.379832756018494 , 69.21988242366837)
        widget.set_zoom(16)
        widget.pack()


        def add_marker_event(coords):
            print("Add marker:", coords)
            entry0.delete(0 , END)
            for _ in widget.canvas_marker_list[1:]:
                _.delete()

            entry0.insert( 0 ,  f"lat:{coords[0]} long:{coords[1]}")
            new_marker = widget.set_marker(coords[0], coords[1], text="Keyingi manzil")

        widget.add_left_click_map_command(add_marker_event)




        image_1 = ImageTk.PhotoImage(imee.open("source/track_35x35.png"))
        ad = widget.set_marker(41.379832756018494, 69.21988242366837, text="Bizning joylashuv", icon = image_1)
        entry1.insert(0, "Tashkent, Узбекистан")







        self.window.resizable(False, False)
        self.window.mainloop()