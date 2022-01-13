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
        self.w.mainloop()

    super.df()

    def click(self):
        self.msg = self.ent.get()
        # print(msg)
        self.send_data()

    def send_data(self):
        # global msg
        self.con.sendto(self.msg.encode("utf-8"), self.s_add)
        # print(msg)
        # time.sleep(1)

    def recv_data(self):
        while True:
            info = self.con.recvfrom(1024)
            # print(info)
            # time.sleep(1)
            self.txt.insert(END, info)


def main():
    con = MyWindow()
    con.df()
    # # con.recv_data()
    #
    # t2 = td.Thread(target=con.send_data, args=())
    # t2.start()
    #
    # t1 = td.Thread(target=con.recv_data, args=())
    # t1.start()
    #
    # t3 = td.Thread(target=con.showwind(), args=(con,))
    # t3.start()


if __name__ == "__main__":
    main()
