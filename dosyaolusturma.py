for i in range (1,10,1):
    dosya=open("sayılar.txt","a")
    veri=str(i)+"\n"
    dosya.write(veri)
    dosya.close