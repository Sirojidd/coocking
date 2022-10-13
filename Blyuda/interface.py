import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()


    def MainMenu(self):
    # configure the root window
        self.title('Главное меню')
        self.geometry('800x450')

        # label
        x = 800
        y = 450
        self.label = ttk.Label(self, text='Главное меню', font=25)
        self.label.grid(padx=x/2.5, pady=y/10)
        # button
        ypad = y / 35 # средняя ширина отступов для размеров

        xpad = x/7.5  # средняя высота отступов для размеров

        btnname = []
        mname = ["Национальные блюда", "Просмотреть Супы", "Поиск блюд по продуктам"]
        mcommand = [self.National_food, self.Soupe, self.poisk]
        lenm = len(mname)

        for i in range(lenm):
            count = 1
            btnname.append(f'btn{count + 1}')
            btnname[i] = tk.Button(self, text=mname[i] ,width=50, height=5, command=mcommand[i]).grid(padx= xpad, pady= ypad)

        #
        # self.btn1 = tk.Button(self, text="Национальные блюда", width=50, height=5, command=self.button_clicked)
        # self.btn1.grid(padx=xpad, pady=ypad)
        # # self.btn1.geo
        # self.btn2 = tk.Button(self, text="Просмотреть Супы",width=50, height=5, command=self.button_clicked)
        # self.btn2.grid(padx=xpad, pady=ypad)
        # self.btn3 = tk.Button(self, text="Поиск блюд по продуктам", width=50,height=5, command=self.poisk)
        # self.btn3.grid(padx=xpad, pady=ypad)

    def National_food(self):
        print('nigger')
    def Soupe(self):
        print('Soupe')
    def poisk(self):
        print('poisk')

    def button_clicked(self):
        showinfo(title='Книга рецептов', message='Приветствую!')

if __name__ == "__main__":
  app = App()
  app.MainMenu()
  app.mainloop()





# import tkinter
# from tkinter import *
# from tkinter import Button, Label, Frame, Menubutton, PhotoImage
# from PIL import  ImageTk, Image
# from nationals import Nat
# from poisk import poisk
 #
 # ap = Tk()
 # ap.geometry('500x300')
 # ap.title('Книга рецептов')

 #
 # canv = Canvas(ap, width='1500', height='1300', bg='white')
 # canv.grid(row=0, column=0)
 #
 # img = ImageTk.PhotoImage(Image.open("J:\kursovaya\coocking-main/Blyuda/cook.jpg"))  # PIL solution
 # canv.create_image(20, 20, anchor=NW, image=img)




# class App():
    # def __init__(self):
    #     self.root = tkinter.Tk()
    #
    #     # создаем рабочую область
    #     self.frame = tkinter.Frame(self.root)
    #     self.frame.grid(    )

    # nationals_food = []
    # street_food = []
    # first_meal = []
    # second_courses = []
    # soups = []
    # salads = []
    # search= []


        # menu.btn3 = Button(self.Frame, text='Поиск блюд по продуктам', command=poisk)
        # menu.btn3.pack



#
#
# if __name__ == '__main__':
#     # App()MainMenu()
#     App().root.mainloop()

# import tkinter
# from tkinter import Tk
# from PIL import Image, ImageTk


#
# class App():
#
#     def __init__(self):
#         self.root = tkinter.Tk()
#
#         # создаем рабочую область
#         self.frame = tkinter.Frame(self.root)
#         self.frame.grid(column=75,
#                         row=75)
#
#         # Добавим метку
#         self.label = tkinter.Label(self.frame, text="Hello, World!").grid(row=1, column=1)
#
#         # self.image = Image.open("J:\kursovaya\coocking-main/Blyuda/cook.jpg")
#         # self.photo = ImageTk.PhotoImage(self.image)
#
#         # вставляем кнопку
#         self.but = tkinter.Button(self.frame, text="Кнопка", command='').grid(row=15, column=20)
#
#         # # Добавим изображение
#         # self.canvas = tkinter.Canvas(self.root, height=600, width=700)
#         # self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
#         # self.canvas.grid(row=2, column=1)
#         self.root.mainloop()
#
#     # def my_event_handler(self):
#     #     print("my_event_handler")
#     #     self.image = Image.open("J:\kursovaya\coocking-main/Blyuda/cook.jpg")
#     #     self.photo = ImageTk.PhotoImage(self.image)
#     #     self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
#     #     self.canvas.grid(row=2, column=1)
# if __name__ == '__main__':
#     app = App()
#     tk.mainloop()
