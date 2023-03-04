from tkinter import *

root = Tk()
root.title("Python GUI")
# root.geometry("640x480") # 가로x세로 창 크기
root.geometry("640x480+100+200") # 가로x세로 창 크기 + 창 위치

root.resizable(False, False) # x 크기 변경 가능 여부, y 크기 변경 가능 여부

root.mainloop()