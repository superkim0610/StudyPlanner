from tkinter import *

root = Tk()
root.title("Python GUI")

btn1 = Button(root, text="버튼1")
btn1.pack() # pack을 해야 생성됨

btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼2")
btn3.pack()

btn4 = Button(root, fg="red", bg="yellow", text="알록달록한 버튼")
btn4.pack

def btncmd():
    print("button5 was clicked!")

check_img = PhotoImage(file="gui_practice\check_img.png")
btn5 = Button(root, image=check_img, command=btncmd)
btn5.pack()

root.mainloop()