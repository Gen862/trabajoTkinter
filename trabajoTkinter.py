'''Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se
compone de los siguientes porcentajes:
55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final.
15% de la calificación de un trabajo final'''
from tkinter import Tk, Label, Button, Entry

def calcular():
    n1 = c1.get()
    n2 = c2.get()
    n3 = c3.get()
    n4 = cE.get()
    n5 = ctf.get()
    r = float(n1) + float(n2) + float(n3) / 3
    prom= float(r * 0.55)
    pef = float(n4 * 0.30)
    ptf = float(n5 * 0.15)
    ct = float(prom) + float(pef) + float(ptf)
    res.insert(0,ct)




ventana = Tk()
ventana.geometry("750x900")
ventana.title("Ejercicio")


etiqueta = Label(ventana, text="Bienvenido, evaluaremos la materia de Algoritmos", bg="pink")
etiqueta.place(x=10, y=10, width=100, height=30)


notac1 = Label(ventana, text="Digite la primera calificación: ")
notac1.place(x=10, y=10, width=100, height=30)
c1 = Entry(ventana)
c1.place(x=120, y=10, width=100, height=30)

notac2 = Label(ventana, text="Digite la segunda calificación: ")
notac2.place(x=10, y=50, width=100, height=30)
c2 = Entry(ventana)
c2.place(x=120, y=50, width=100, height=30)

notac3 = Label(ventana, text="Digite la tercera calificación: ")
notac3.place(x=10, y=90, width=100, height=30)
c3 = Entry(ventana)
c3.place(x=120, y=90, width=100, height=30)

notaEF = Label(ventana, text="Digite la nota del examen final: ")
notaEF.place(x=10, y=130, width=100, height=30)
cE = Entry(ventana)
cE.place(x=120, y=130, width=100, height=30)

notaTF = Label(ventana, text="Digite la nota del trabajo final:")
notaTF.place(x=10, y=170, width=100, height=30)
ctf = Entry(ventana)
ctf.place(x=120, y=170, width=100, height=30)

botonM = Button(ventana, text="Calcular", fg="blue", command=calcular)
botonM.place(x=150, y=250, width=100, height=30)

res = Entry(ventana, bg="plum", x=10, y=220, width=100, height=30)
res.place(x=120, y=220, width=100, height=30)






ventana.mainloop()