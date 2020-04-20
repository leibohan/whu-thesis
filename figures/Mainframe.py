import tkinter as tk

def txt2img(filename):
    pass

def img2txt(filename):
    pass

window = tk.Tk()
window.title("图片-语义互译系统")
window.geometry('800x600')  #窗口尺寸
 
b = tk.Button(window, 
    text='图片生成语义',      # 显示按钮上的文字
    width=15, height=2, 
    command=hit_me)
b.pack()


window.mainloop()     