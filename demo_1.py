__author__ = 'Administrator'
# print('hello,world')
# print('The quick brown fox','jumps over','the lazy dog')
#
# name = input('please enter your name:')
# print('name:',name)
# print('1024 * 768 = ',1024*768)
# a = 100
# if a >= 0:
#     print(a)
# else:
#     print(-a)

# print('I\'m \"OK\"!') #I'm "OK"!
# print(r'I\'m \"OK\"!') #I\'m \"OK\"!

# print(True and True)
# print(True and False)
# print(False and False)
# print(5 > 3 and 3 > 1)

# print(True or True)
# print(True or False)
# print(False or False)
# print(5 > 3 or 1 > 3)

# print(not True)
# print(not False)
# print(not 1 > 2)

# print(10//3)

# print('n = ',123)
# print('f = ',456.789)
# print('s1 = ','Hello,world')
# print('s2 = ','Hello,\\\'Adm\'\'')

# print('Hello, %s' %'world')
# print('Hi,%s,you have $%d'%('Ajax',10000000))
# print('%.2f' % 3.1415926)
# print('Age: %s. Gender: %s' %(20,True))
# print('growth rate: %d %% ' %7)

classmates = ['Micheal', 'Bob', 'Tracy']
num = input('please input num:')
num1 = int(num)
if abs(num1) >= len(classmates):
    print('out of range')
else:
    print(classmates[num1])

# str = input('please input name:')
# classmates.append(str)
# classmates.insert(1, str)
# classmates.pop(0)
# classmates[1] = 'Sarah'
# print(classmates)

# TCP客户端
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn',80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# s.close()
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)

# from tkinter import *
# import tkinter.messagebox as messagebox
#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello, %s' % name)
#
# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()