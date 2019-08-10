import tkinter
from tkinter import filedialog
from tkinter import ttk

win = tkinter.Tk()
win.geometry("500x400")
win.title("Convert2Read 格式转换器")
Label1 = tkinter.Label(win, text="请输入网址")
Label1.pack(side=tkinter.LEFT)

enter1 = tkinter.Entry(win, bd= 5)
enter1.pack(side=tkinter.LEFT)


def upload_file(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

def showEnd(event):
    tkinter.text.see(tkinter.END)
    tkinter.text.edit_modified(0)

file_button = tkinter.Button(win, text='打开', command=upload_file)
file_button.pack()

def conver2pdf():
    print("转换成功")

convert_button = tkinter.Button(win, text='转换')

convert_button.pack()
convert_button.config(command=conver2pdf)
win.mainloop()