import random
from tkinter import*

#BOTONES
def crear():
    m=int(x.get())
    n=int(y.get())
    M = []
    for i in range(m):
        M.append([])
        for j in range(n):
            M[i].append(random.randint(1,9))
    for k in range(m):
        filas= print()
    for j in range(n):
         columnas =print(M[k][j], end="\t")
    t_resultados = filas
    

ventana_principal = Tk()
ventana_principal.title("Graficas 2D - Texto")
ventana_principal.resizable(False,False)
ventana_principal.geometry("800x500")
ventana_principal.config(bg = "blue")

x = StringVar()
y = StringVar()


frame_graficacion= Frame(ventana_principal)
frame_graficacion.config(bg= "red", width=480, height=480)
frame_graficacion.pack(fill=BOTH, padx=10, pady=10)

#CANVA
c= Canvas(frame_graficacion, width=760, height=310)
c.place(x=10, y=160)

rect1=c.create_rectangle(60,80,50, 90, outline="green")

#LABEL
titulo = Label(frame_graficacion, text = "Filas = ")
titulo.config(bg = "red", fg = "black", font = ("Arial",16))
titulo.place(x = 20, y = 10)

titulo = Label(frame_graficacion, text = "Columnas = ")
titulo.config(bg = "red", fg = "black", font = ("Arial",16))
titulo.place(x = 20, y = 50)

#BOTONES

bt_matriz = Button(frame_graficacion, text="Crear matriz.",command=crear)
bt_matriz.place(x=20, y=90, width=100, height=30)

# ENTRYS

entry_x = Entry(frame_graficacion, textvariable=x)
entry_x.config(font=("Arial",20), justify=LEFT,fg="black")
entry_x.focus_set()
entry_x.place(x=100, y=10, width=115, height=30)

entry_y = Entry(frame_graficacion, textvariable=y)
entry_y.config(font=("Arial",20), justify=LEFT,fg="black")
entry_y.focus_set()
entry_y.place(x=150, y=50, width=115, height=30)

#RESULTADOS


ventana_principal.mainloop()

