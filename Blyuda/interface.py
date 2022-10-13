import tkinter
from tkinter import *
from tkinter import Button, Label, Frame, Menubutton, PhotoImage
import tkinter.ttk as ttk


ap=Tk()
ap.geometry('1500x1300')
ap.title('Книга рецептов')


# our_image = PhotoImage(file = "/home/siroj/Загрузки/cook.jpg")
# our_image = our_image.subsample(5, 5)
# our_label = Label(Tk)
# our_label.image = our_image
# our_label.image = our_label.image



class App(Tk):
    nationals_food = []
    street_food = []
    first_meal = []
    second_courses = []
    soups = []
    salads = []



    def menu(self):
        menu = self.menu
        menu.lbl = LabelFrame(text='Меню')
        menu.lbl.pack
        menu.btn = Button(text='Национальные блюда', command=self.nationals_food)
        menu.btn.pack
        menu.btn2 = Button(text='', command='')
        menu.btn2.pack
        menu.btn3 = Button(text='', command='')
        menu.btn3.pack


    def nationals_food(self):
        nat_food = self.menu
        nat_food.lbl = LabelFrame(text='Меню национальных блюд')
        nat_food.lbl.pack
        nat_food.btn = Button(text='', command='')
        nat_food.btn.pack
        nat_food.btn2 = Button(text='', command='')
        nat_food.btn2.pack
        nat_food.btn3 = Button(text='', command='')
        nat_food.btn3.pack




ap.mainloop()
