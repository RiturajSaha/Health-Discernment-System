# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 22:40:22 2020

@author: R2J
"""
from tkinter import *
import os



def malaria():
    print("malaria")
    os.system('cmd /c "python application_ml"')

def pneumonia():
    print("pneumonia")
    os.system('cmd /c "python application_pn"')

def breast_cancer():
    print("breast_cancer")
    os.system('cmd /c "python application_bc"')
    
def skin_cancer():
    print("skin_cancer")
    os.system('cmd /c "python application_sc"')    


 
root = Tk()

root.attributes('-fullscreen',True)
root.title("Health Discernment System")

background = PhotoImage(file = "images/cover_main.png")
Label(root,image = background).place(x=0, y=0)

button_ml = PhotoImage(file = r"images/button_ml.png")  
Button(root, text="MALARIA",image=button_ml,bd=0,highlightthickness=0, command=malaria).place(x=200,y=400)

button_pn = PhotoImage(file = r"images/button_pn.png") 
Button(root, text="PNEUMPONIA",image=button_pn,bd=0,highlightthickness=0,command=pneumonia).place(x=200,y=600)

button_bc = PhotoImage(file = r"images/button_bc.png") 
Button(root, text="BREAST CANCER",image=button_bc,bd=0,highlightthickness=0, command=breast_cancer).place(x=500,y=400)

button_sc = PhotoImage(file = r"images/button_sc.png") 
Button(root, text="SKIN CANCER",image=button_sc,bd=0,highlightthickness=0, command=skin_cancer).place(x=500,y=600)

close = PhotoImage(file = r"images/close.png")
Button(root, text = "close",image = close,highlightthickness = 0,
                            command = root.destroy).place(x=0,y=0) 
mainloop()