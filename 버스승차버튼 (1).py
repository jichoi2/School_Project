from tkinter import*
from PIL import Image, ImageTk
#---------------------창 시작------------------
a = Tk()
photo = ImageTk.PhotoImage(Image.open("5.png"))
photo1 = ImageTk.PhotoImage(Image.open("814.png"))
photo2 = ImageTk.PhotoImage(Image.open("840.png"))

img = Image.open("5.png")
img1 = Image.open("814.png")
img2 = Image.open("840.png")

def b():
    print(type(img))
    img.show()

def c():
    print(type(img1))
    img1.show()

def d():
    print(type(img2))
    img2.show()

def e():
    L4.configure(text="급행5 예약되었습니다.")

def f():
    L4.configure(text="814 예약되었습니다.")

def g():
    L4.configure(text="840 예약되었습니다.")

def h():
    L4.configure(text="급행5 예약취소되었습니다.")

def i():
    L4.configure(text="814 예약취소되었습니다.")

def j():
    L4.configure(text="840 예약취소되었습니다.")

    
a.title("버스 승차버튼")
a.geometry("660x250")
L1 = Label(a,text = "버스 노선표\n버스 승차예약버튼", font = "Time 15")
L1.grid(row=0,column=2)

L2 = Label(a,text = "버스 노선", font = "Time 10")
L2.grid(row=1,column=1)

L3 = Label(a,text = "승차 예약/예약취소", font = "Time 10")
L3.grid(row=1,column=3)

L4 = Label(a, text = ":", font = "Time 13")
L4.grid(row = 300, column = 500)

#---------------------버튼 만들기-------------------

bt1 = Button(a, text="급행5",width=10, height=2, command=b)
bt1.grid(row=2,column=1)

bt2 = Button(a, text="814",width=10, height=2, command=c)
bt2.grid(row=4,column=1)

bt3 = Button(a, text="840",width=10, height=2, command=d)
bt3.grid(row=6,column=1)

bt4 = Button(a, text="예약",width=10, height=1, command=e)
bt4.grid(row=2,column=3)

bt5 = Button(a, text="예약",width=10, height=1, command=f)
bt5.grid(row=4,column=3)

bt6 = Button(a, text="예약",width=10, height=1, command=g)
bt6.grid(row=6,column=3)

bt7 = Button(a, text="예약취소",width=10, height=1, command=h)
bt7.grid(row=2,column=5)

bt8 = Button(a, text="예약취소",width=10, height=1, command=i)
bt8.grid(row=4,column=5)

bt9 = Button(a, text="예약취소",width=10, height=1, command=j)
bt9.grid(row=6,column=5)

a.mainloop()



