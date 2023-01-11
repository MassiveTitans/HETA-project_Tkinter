from tkinter import *




class Aplication:
    def __init__(self, display):
        self.wind = display


    def display_1(self):

        def btn_clicked():
            try:
                if entry0.get() == "heta123":
                    print("Button Clicked"  , entry0.get())
                    self.wind.destroy()
                else:
                     print('Code eror')
                     canvas.create_text(
                        205.0, 380.0,
                        text="code eror",
                        fill="red",
                        font=("TiroTelugu-Regular", int(10.0)))
            except:
                print("EROR")


        canvas = Canvas(
                    self.wind,
                    bg = "#ffffff",
                    height = 600,
                    width = 1024,
                    bd = 0,
                    highlightthickness = 0,
                    relief = "ridge")


        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(master = canvas , file ="source/win1/background.png")
        background = canvas.create_image(
            512.0, 300.0,
            image=background_img)

        img0 = PhotoImage( master = canvas ,file ="source/win1/img0.png")
        b0 = Button(
            master= canvas ,
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            relief = "flat")

        b0.place(
            x = 99, y = 416,
            width = 208,
            height = 50)

        canvas.create_text(
            205.0, 320.0,
            text = "Authentication code",
            fill = "#ffffff",
            font = ("TiroTelugu-Regular", int(15.0)))

        entry0_img = PhotoImage(master = canvas, file ="source/win1/img_textBox0.png")

        entry0_bg = canvas.create_image(
            203.5, 352.5,
            image = entry0_img)

        entry0 = Entry(
            self.wind,
            bd = 0,
            bg = "#a6a6a6",
            highlightthickness = 0)

        entry0.place(
            x = 122.0, y = 339,
            width = 163.0,
            height = 25)



        self.wind.resizable(False, False)
        self.wind.mainloop()