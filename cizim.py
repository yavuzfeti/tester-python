import turtle

arkaplan = turtle.Screen()
cizgi = turtle.Turtle()

arka_renk = "white"
renk = "black"
hiz = 1
kalinlik = 50
sekil = "square"
sekil_boyutu = 2

arkaplan.bgcolor(arka_renk)
cizgi.color(renk)
cizgi.speed(hiz)
cizgi.pensize(kalinlik)
cizgi.shape(sekil)

def ciz():
    cizgi.setposition(250,250)

ciz()


cizgi.getscreen()._root.mainloop()