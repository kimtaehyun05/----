from tkinter import *
from tkinter import messagebox

def keyEvent1(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 왼쪽 화살표")

def keyEvent2(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 위쪽 화살표")

def keyEvent3(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 오른쪽 화살표")

def keyEvent4(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 아래쪽 화살표")

window = Tk()

window.bind("<Shift-Left>", keyEvent1)
window.bind("<Shift-Up>", keyEvent2)
window.bind("<Shift-Down>", keyEvent4)
window.bind("<Shift-Right>", keyEvent3)

window.mainloop()
