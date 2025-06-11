from tkinter import *
import random

btnList = [None] * 9
fnameList = ["1.gif", "2.gif", "3.gif", "4.gif",
             "5.gif", "6.gif", "7.gif", "8.gif", "9.gif"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

random.shuffle(fnameList)

window = Tk()
window.geometry("210x210")

for i in range(0, 9):
    photoList[i] = PhotoImage(file="C:\\Users\\TaeHyun\\Desktop\\새 폴더\\WindowPrograming\\"+ fnameList[i])
    btnList[i] = Button(window, image=photoList[i])

for i in range(3):
    for k in range(3):
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()
