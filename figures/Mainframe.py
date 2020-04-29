# coding=UTF-8

import tkinter as tk
import tkinter.font as tkFont
import tkinter.filedialog
from PIL import Image, ImageTk
import time
#f0 = tk.StringVar()

window = tk.Tk()
window.title('图片-文本互译系统')
window.geometry('800x800')  #窗口尺寸
 
function_choice = tk.IntVar()

color1 = 'lemonchiffon'
file_path = ''

f1 = tkFont.Font(font=('Arial', '30', tkFont.NORMAL), size=40)

l1 = tk.Label(window, text = '文本输入栏',
    width = 10, height = 2, bg=color1)
l2 = tk.Label(window, text = '图片输入栏',
    width = 10, height = 2, bg=color1)
l0 = tk.Label(window, text = '',
    width = 40, height = 4, bg='lightyellow',
    font = f1, wraplength = 700,
justify = 'left')

b1 = tk.Radiobutton(window, 
    text='图片翻译文本',      # 显示按钮上的文字
    width=12, height=2, 
    value=1, variable = function_choice)
b2=  tk.Radiobutton(window, 
    text='文本翻译图片',      # 显示按钮上的文字
    width=12, height=2, 
    value=2, variable = function_choice)

lfile = tk.Label(text = '', bg = '#666FFF', width = 33, height = 2)
lfile.place(x = 420, y = 90)

def openimage():
    file_path = tk.filedialog.askopenfilename(title=u'选择文件')
    lfile['text'] = file_path

bb = tk.Button(window, text = '选择文件', width = 6, height = 2, command = openimage)
bb.place(x = 360, y = 90)

e = tk.Entry(window, width = 40)

cvsBanner = tk.Canvas(window, bg='#DDDDDD', width = 750, height = 450)
cvsBanner.place(x = 25, y=320)

def txt2img(name):
    l0['text'] = e.get()
    #time.sleep(1)
    #photo = Image.open('/Users/LeiBohan/Desktop/学习文件/毕业设计/whu-thesis/figures/whulogo.gif')
    icon = tk.PhotoImage(file = '/Users/LeiBohan/Downloads/test_upload/0.gif')
    window.a=icon
    print(icon)
    cvsBanner.create_image(375,225,image=icon)
    #a sheep by another sheep standing on the grass with sky above and a boat in the ocean by a tree behind the sheep

def img2txt(name):
    #photo = Image.open(file_path)
    print(file_path)
    icon = tk.PhotoImage(file = lfile['text'])
    window.a = icon
    time.sleep(1)
    l0['text'] = 'a group of people standing arround a table'
    cvsBanner.create_image(375, 225, image=icon)


def deal():
    if function_choice.get() == 1:
        l0['text'] = e.get()
        img2txt('')
    elif function_choice.get() == 2:
        txt2img('')
    else:
        l0['text'] = '请选择功能' #'a man is talking with a woman beside a table'


b1.place(x=50,y=50)
b2.place(x=50,y=90)

b = tk.Button(window, text='确认', width=8, height = 4,
    command = deal)
b.place(x=160, y=50)

l1.place(x=260, y=50)
l2.place(x=260, y=90)

e.place(x = 360, y = 50)

l0.place(x = 50, y = 150)

window.mainloop()     