from tkinter import *

window = Tk()

photo1 = PhotoImage(file="C:\\Users\\TaeHyun\\Desktop\\새 폴더\\WindowPrograming\\다운로드.gif")
photo2 = PhotoImage(file="C:\\Users\\TaeHyun\\Desktop\\새 폴더\\WindowPrograming\\고양이.gif")

label1 = Label(window, image=photo1)
label2 = Label(window, image=photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop()
