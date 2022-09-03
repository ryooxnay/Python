# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 01:26:50 2022

@author: USER
"""
from tkinter import *
from tkinter import ttk
from database import *

class App:
    def __init__(self, master):
        self.ventana = master
        self.DibujarLabel()
        self.DibujarEntry()
        self.DibujarBoton()
        self.DibujarLista()
    
    def DibujarLabel(self):
        self.lbl_name = Label(self.ventana, foreground="white", background="#314252", text="Nombre", font=(8)).place(x = 60, y = 110)
        self.lbl_edad = Label(self.ventana, foreground="white", background="#314252", text="Edad", font=(8)).place(x = 60, y = 160)
        self.lbl_carrera = Label(self.ventana, foreground="white", background="#314252", text="Carrera", font=(8)).place(x = 60, y = 210)
    
    def DibujarEntry(self):
        self.nombre = StringVar()
        self.edad = StringVar()
        self.carrera = StringVar()
        self.txt_nombre = Entry(self.ventana, font=("Arial",12), textvariable=self.nombre).place(x=140, y=110)
        self.txt_edad = Entry(self.ventana, font=("Arial",12), textvariable=self.edad).place(x=140, y=160)
        self.txt_carrera = Entry(self.ventana, font=("Arial",12), textvariable=self.carrera).place(x=140, y=210)
    def DibujarBoton(self):
        self.btn_guardar = Button(self.ventana, text="Guardar", relief="flat", background = "#0051C8",cursor="hand1", foreground="White", COMMAND = lambda: self.guardar()).place(x=750,y=440, width=90)
        self.btn_borrar = Button(self.ventana, text="Borrar", relief="flat", background = "red",cursor="hand1", foreground="White", COMMAND = lambda: self.borrar()).place(x=850,y=440, width=90)
    #def guardar(self):
        
    #def borrar(self):
        
    
    def DibujarLista(self):
        self.lista = ttk.Treeview(self.ventana, column=(1,2,3), show="headings", height="8")
        #Estilo
        estilo = ttk.Style()
        estilo.theme_use("clam")
        
        estilo.configure("Treeview.Headings", background="blak", relief="flat", foreground="write")
        self.lista.heading(1, text="Nombre")
        self.lista.heading(2, text="Edad")
        self.lista.heading(3, text="Carrera")
        self.lista.column(2, anchor=CENTER)
        #fill list
        d=Data()
        element= d.returnAllElements()
        for i in element:
            self.lista.insert("", "end", values = i)
            
        self.lista.place(   x=350, y=90)
        
        
root = Tk()
root.title("CRUD_SQL")
root.geometry("1000x500")
root.config(background="#314252")
aplication=App(root)








root.mainloop()

