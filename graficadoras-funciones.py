# importamos la libreria matplotlib y numpy y le asignamos un alias
import numpy as np
import matplotlib.pyplot as plt

def funcion_lineal(m,x,b):
  return m*x+b

def funcion_cuadratica(a,b,x,c):
  return a*x**2+b+c

N=100
print("---------------------------")
print("-----Calculadora-de-funciones---")
print("----------------------------")

print("1. Funcion lineal")
print("2. Funcion cuadratica")
print("3. Funcion cubica")
print("4. Funcion exponencial")
print("5. Funcion logaritmica")
print("6. Funcion trigonometrica")
print("7. Funcion valor absoluto")
print("8. Funcion racional de primer grado")

función= int(input("Ingresa la funcion que quieres realizar: "))

if función==1:
  m = int(input("Digite el valor de la pendiente: "))
  b = int(input("Digite el valor del punto de corte con el eje y: "))
  x=np.linspace(-10,10,num=N)
  y= funcion_lineal(m,b,x)
  plt.plot(x,y, color = 'r')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title('Función lineal: y = mx + b')
  plt.grid()
  plt.axhline(y=0, color= 'b')
  plt.axvline(x=0, color= 'b')
  plt.show()
elif función==2:

  N=100
  def funcion_cuadratica(a,b,x,c):

    return a*x**2+b+c
  a = int(input("Digite el valor de a : "))
  b = int(input("Digite el valor de b: "))
  c = int(input("Digite el valor de c: "))


 
  x = np.linspace(-10,10,num=N)
  y = funcion_cuadratica(a,b,x,c)

  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion cuadratica: y = ax^2 + bx + c")
  plt.grid()
  plt.axhline(y=0, color="b")
  plt.axvline(x=0, color="b")
  plt.show()
elif función==3:
  N=100
  def funcion_cubica(a,b,c,x,d):
    return a*x**3+b*x**2+c*x+d
  a = int(input("Digite el valor de a : "))
  b = int(input("Digite el valor de b: "))
  c = int(input("Digite el valor de c: "))
  d= int(input("Digite el valor de d: "))


 
  x = np.linspace(-10,10,num=N)
  y = funcion_cubica(a,b,c,x,d)

  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion cubica: y = ax^3 + bx^2 + cx+d")
  plt.grid()
  plt.axhline(y=0, color="b")
  plt.axvline(x=0, color="b")
  plt.show()
elif función==4:
  N=100
  def funcion_exponencial(a,x):
    return a**x
  a= int(input("Digite el valor de la base: "))
  x = np.linspace(-10,10,num=N)
  y = funcion_exponencial(a,x)

  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion exponencial: y = a^x")
  plt.grid()
  plt.axhline(y=0, color="b")
  plt.axvline(x=0, color="b")
  plt.show()
elif función ==5:
  N=100
  def funcion_logaritmica(a,x):
    return np.log(x)/np.log(a)
  a=int(input("Digite el valor de la base: " ))
  x = np.linspace(-10,10,num=N)
  y = funcion_logaritmica(a,x)

  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion Logaritmica: y = log(a)/log(x)")
  plt.grid()
  plt.axhline(y=0, color="b")
  plt.axvline(x=0, color="b")
  plt.show()
elif función ==6:
  N=100
  def funcion_seno(x):
    return np.sin(x)
  def funcion_coseno(x):
    return np.cos(x)
  def funcion_tangente(x):
    return np.tan(x)
  print("1. Función Seno")
  print("2. Función Coseno")
  print("3. Función Tangente")
  n=int(input("Ingresa la función trigonometrica que deseas realizar: "))
  if n==1:
    #a= int(input("Ingresa el valor al cual deseas calcular el seno: "))
    x = np.linspace(-10,10,num=N)
    y = funcion_seno(x)
    plt.plot(x,y,color="r")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Funcion seno: y = sen(a)")
    plt.grid()
    plt.axhline(y=0, color="b")
    plt.axvline(x=0, color="b")
    plt.show()
  if n==2:
    x = np.linspace(-10,10,num=N)
    y = funcion_coseno(x)
    plt.plot(x,y,color="r")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Funcion coseno: y = cos(x)")
    plt.grid()
    plt.axhline(y=0, color="b")
    plt.axvline(x=0, color="b")
    plt.show()
  if n==3:
    x = np.linspace(-10,10,num=N)
    y = funcion_tangente(x)
    plt.plot(x,y,color="r")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Funcion tagente: y = tan(x)")
    plt.grid()
    plt.axhline(y=0, color="b")
    plt.axvline(x=0, color="b")
    plt.show()
elif función ==7:
  N=100
  def funcion_valorabsoluto(x):
    return abs(x)
  a=int(input("Digite el valor de la base: " ))
  x = np.linspace(-10,10,num=N)
  y = funcion_valorabsoluto(x)

  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion valor absoluto: y = /x/")
  plt.grid()
  plt.axhline(y=0, color="b")
  plt.axvline(x=0, color="b")
  plt.show()
elif función==8:
  N=100
  def funcion_racional(x):
    return 1/x
  
  x = np.linspace(-10,10,num=N)
  y = funcion_racional(x)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion Racional: y = 1/x")
  plt.grid()
  plt.axhline(y=0, color="b")
  plt.axvline(x=0, color="b")
  plt.show()

