#Se importa libreria tkinter con todas sus funciones

from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(-5,5,100)
def graficar_funciones():
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Calculadora graficadora")
    plt.grid()
    plt.axhline(y=0, color="b")
    plt.axvline(x=0, color="b")
    plt.show()
def funcion_lineal():
    y= float(lineal_a.get())*x + float(lineal_b.get())
    plt.plot(x,y, color="y")
    graficar_funciones()
def funcion_cuadratica():
    y= float(cuadratica_a.get())*x**2+ float(cuadratica_b.get())*x+float(cuadratica_c.get())
    plt.plot(x,y, color="y")
    graficar_funciones()
def funcion_cubica():
    y = float(cubica_a.get()) * x**3 + float(cubica_b.get()) * x**2 + float(cubica_c.get()) * x + float(cubica_d.get())
    plt.plot(x,y, color="y")
    graficar_funciones()
def funcion_exponencial():
    y= float(exponencial_a.get())**x
    plt.plot(x,y, color="y")
    graficar_funciones()
def funcion_logaritmica():
    y= np.log(x)/np.log(float(logaritmica_a.get()))
    plt.plot(x,y, color="y")
    graficar_funciones()
inicio= Tk()


# a, b,c,d
atexto= Label(inicio,text="a")
atexto.grid(row=0, column=1)

btext = Label(inicio, text="b")
btext.grid(row=0, column=2)

ctexto = Label(inicio, text="c")
ctexto.grid(row=0, column=3)
ctexto = Label(inicio, text="d")
ctexto.grid(row=0, column=4)
# Funcion lineal
label_lineal= Label(inicio, text="y = ax + b")
label_lineal.grid(row=0, column=0)
graficar_lineal = Button(inicio, text="Graficar", command=funcion_lineal)
graficar_lineal.grid(row=1, column=0)

lineal_a = Entry(inicio, width=7)
lineal_a.grid(row=1, column=1, padx=7)

lineal_b = Entry(inicio, width=7)
lineal_b.grid(row=1, column=2, padx=7)

# Funcion cuadratica

label_cuadratica = Label(inicio, text="y = ax² + bx + c")
label_cuadratica.grid(row=2, column=0)
graficar_cuadratica = Button(inicio, text="Graficar", command=funcion_cuadratica)
graficar_cuadratica.grid(row=3, column=0)

cuadratica_a = Entry(inicio, width=7)
cuadratica_a.grid(row=3, column=1, padx=7)

cuadratica_b = Entry(inicio, width=7)
cuadratica_b.grid(row=3, column=2, padx=7)

cuadratica_c = Entry(inicio, width=7)
cuadratica_c.grid(row=3, column=3, padx=7)

label_cubica = Label(inicio, text="y = ax³ + bx² + c")
label_cubica.grid(row=4, column=0)
graficar_cubica = Button(inicio, text="Graficar", command=funcion_cubica)
graficar_cubica.grid(row=5, column=0)

cubica_a = Entry(inicio, width=7)
cubica_a.grid(row=5, column=1, padx=7)

cubica_b = Entry(inicio, width=7)
cubica_b.grid(row=5, column=2, padx=7)

cubica_c = Entry(inicio, width=7)
cubica_c.grid(row=5, column=3, padx=7)

cubica_d = Entry(inicio, width=7)
cubica_d.grid(row=5, column=4, padx=7)

label_exponencial = Label(inicio, text="y = a^x")
label_exponencial.grid(row=6, column=0)
graficar_exponencial  = Button(inicio, text="Graficar", command=funcion_exponencial)
graficar_exponencial.grid(row=7, column=0)

exponencial_a = Entry(inicio, width=7)
exponencial_a.grid(row=7, column=1, padx=7)

label_logaritmica = Label(inicio, text="y = logₐ(x)")
label_logaritmica.grid(row=8, column=0)
graficar_logaritmica= Button(inicio, text="Graficar", command=funcion_logaritmica)
graficar_logaritmica.grid(row=9, column=0)

logaritmo_a = Entry(inicio, width=7)
logaritmo_a.grid(row=9, column=1, padx=7)






inicio.mainloop()