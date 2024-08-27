import turtle


arkaplan=turtle.Screen()
cizgi=turtle.Turtle()

arkaplan.bgcolor("black")
cizgi.color("white","white")
cizgi.setposition(0,0)
hiz=10
cizgi.speed(hiz)

def ciz(uzunluk=50):
    cizgi.left(65)
    cizgi.forward(uzunluk)
    cizgi.right(195)
    cizgi.left(58)
    cizgi.forward(uzunluk)

def yıldızciz(t=50):
    for c in range(0,5):
        c+=1
        ciz(t)

def yap(hiz):
    cizgi.setposition(0,0)
    kalinlik=10
    cizgi.pensize(kalinlik)
    for u in range(1,20):
        yıldızciz(u*50)
        if kalinlik>0:
            kalinlik-=1
        hiz*=2
        cizgi.pensize(kalinlik)
        cizgi.speed(hiz)
        cizgi.penup()
        cizgi.left(180)
        cizgi.forward(15)
        cizgi.right(90)
        cizgi.forward(25)
        cizgi.right(90)
        cizgi.pendown()

yap(10)

cizgi.color("black","black")

yap(10)

arkaplan.bgcolor("white")
cizgi.color("white","white")

yap(10)


cizgi.getscreen()._root.mainloop()