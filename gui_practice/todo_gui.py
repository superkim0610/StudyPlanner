from tkinter import *

def askTodoName():
    global todoNameEntry, todoNameBtn

    todoNameEntry = Entry(root, width=30)
    todoNameEntry.pack()
    todoNameEntry.focus()
    todoNameBtn = Button(root, text="submit", command=addTodo)
    todoNameBtn.pack()

def addTodo():
    todoName = todoNameEntry.get()

    todoListValue.append(IntVar())

    todoList.append(Checkbutton(root, text=todoName, variable=todoListValue[-1], command=todoCheckboxCmd))
    todoList[-1].pack()

    todoNameEntry.destroy()
    todoNameBtn.destroy()

def todoCheckboxCmd():
    global destroyMode

    print(list(map(lambda l: l.get(), todoListValue)))

    for c in todoList:
            c.config(fg="black")

    if destroyMode: destroyMode = False

def destroyBtnCmd():
    global destroyMode
    destroyMode = not destroyMode
    
    if destroyMode == True:
        for c in todoList:
            c.config(fg="red")
    else:
        for c in todoList:
            c.config(fg="black")
         

root = Tk()
root.title("pyTodo")
root.geometry("640x480+300+300")

destroyMode = False

addBtnImg = PhotoImage(file="gui_practice/add_btn_img.png")
addBtn = Button(root, image=addBtnImg, command=askTodoName)
addBtn.pack()

destroyBtnImg = PhotoImage(file="gui_practice\destroy_btn_img.png")
destroyBtn = Button(root, image=destroyBtnImg, command=destroyBtnCmd)
destroyBtn.pack()

todoList = []
todoListValue = []

root.mainloop()