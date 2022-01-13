import socket
from tkinter import *
import threading as td
import time

rev_msg = ""


class nini:
    def df(self):
        print("jicheng")


class MyWindow(nini):

    def __init__(self):

        self.msg = "de"

        self.w = Tk()
        self.w.title("windows")
        self.ent = Entry(text="输入：")
        btn = Button(command=self.click, text="点击")
        self.txt = Text()

        self.ent.pack()
        btn.pack()
        self.txt.pack()
        # self.con = con

        self.con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.r_add = ("192.168.1.104", 7890)
        self.s_add = ("192.168.1.104", 8090)
        self.con.bind(self.r_add)

    def showwind(self):
        super().df()
        self.w.mainloop()


    def click(self):
        self.msg = self.ent.get()
        # print(msg)



def main():
    con = MyWindow()
    con.showwind()


if __name__ == "__main__":
    main()
