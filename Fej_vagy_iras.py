#Varda Dávid 2021.02.10.
 
"""A "Dobj" gomb egyszeri megnyomására a program generál egy random 1-est vagy 0-át, melyeket külön listákban tárol. (Továbbiakban: 0=Fej, 1=Írás)
Minden dobás után összesen 2 db eredményt tárol: fej vagy írás közül az egyiket (aszerint,hogy melyik elágazás futott végig) és a dobás(ok) számát.
Az összegzés gomb megnyomására figyelembe veszi a listák hosszát, ezek alapján képes megállapítani, hogy hány db dobásból hány db fej és írás keletkezett és -csak a nyertes eredményt- %-osan, kerekítve megadni.
A "Dobásod száma:" és a "Jelenlegi dobásod:" nevű mezők minden "Dobj!" gombnyomás után ujraíródnak.
A kiürít gomb megynomására a listák tartalma és a mezők is törlődnek, új játék kezdődhet.
Kilépésre kilép."""

from random import randint

l=[]
fej=[]
iras=[]

def rand():

    for i in range(1):
        result=randint(0,1)       

    if result==0:
        dobasod.delete(0,END)
        dobasod.insert(0,'Fej')
        l.append(1)
        fej.append(1)

    else:
        dobasod.delete(0,END)
        dobasod.insert(0,'Írás')
        l.append(1)
        iras.append(1)

    dobasszam=len(l)
    dobszam.delete(0,END)
    dobszam.insert(0,dobasszam)

def osszegzes():
    
    dobasszam=len(l)
    print(dobasszam, "érmefeldobásból:" ,len(fej), "fej és" ,len(iras),"írás.")
    a=len(fej)
    b=len(iras)
    c=(100*a//dobasszam)
    d=(100*b//dobasszam)

    if c>d:
        print("Az írás nyert:",c,"%-al.")

    elif c==d:
        print("Döntetlen!")
    
    else:
        d>c
        print("A fej nyert:",d,"%-al.")

def nullaz():
    l.clear()
    fej.clear()
    iras.clear()
    dobszam.delete(0,END)
    dobasod.delete(0,END)
    

from tkinter import *
ablak1=Tk()
ablak1.title("Fej vagy írás?")
ablak1.geometry("245x130")
felirat1=Label(ablak1,text="Dobásod száma:")
felirat1.grid(row=1,column=1)
felirat2=Label(ablak1,text="Jelenlegi dobásod:")
felirat2.grid(row=1,column=2)
dobj = Button(ablak1, text='Dobj!', width=5, command=rand)
dobj.grid(row=2,column=3)
dobasod = Entry(ablak1,width=5)
dobasod.grid(row=2,column=2)
dobszam = Entry(ablak1,width=5)
dobszam.grid(row=2,column=1)
geredmeny = Button(ablak1, text='Összegzés', width=10, command =  osszegzes)
geredmeny.grid(row=3,columnspan=2,column=1)
gnullaz=Button(ablak1, text='Kiürít', width=10, command =  nullaz)
gnullaz.grid(row=5,columnspan=2,column=1)
gexit = Button(ablak1, text='Kilépés', width=10, command = ablak1.destroy)
gexit.grid(row=6,columnspan=2,column=1)
ablak1.mainloop()
