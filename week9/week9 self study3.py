from tkinter import *
from time import *

fnameList = ["1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif", "7.gif", "8.gif", "9.gif"]
photoList = [None] * 9
num = 0

def updateImage():
    photo = PhotoImage(file = "C:\\Users\\TaeHyun\\Desktop\\새 폴더\\WindowPrograming\\" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image = photo
    nameLabel.config(text=fnameList[num])

def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    updateImage()

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    updateImage()

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text = "<<이전", command = clickPrev)
btnNext = Button(window, text = "다음>>", command = clickNext)

photo = PhotoImage(file = "C:\\Users\\TaeHyun\\Desktop\\새 폴더\\WindowPrograming\\" + fnameList[0])
pLabel = Label(window, image = photo)
nameLabel = Label(window, text=fnameList[0], font=("Arial", 12))


btnPrev.place(x = 200, y = 10)
nameLabel.place(x = 320, y = 15)
btnNext.place(x = 440, y = 10)
pLabel.place(x = 15, y = 50)

window.mainloop()
