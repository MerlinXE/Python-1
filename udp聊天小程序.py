import socket
from tkinter import *
import threading as td
import time

msg = "de"


class MyCon:

    def __init__(self):
        self.con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.r_add = ("192.168.1.104", 7890)
        self.s_add = ("192.168.1.104", 8090)
        self.con.bind(self.r_add)

    def send_data(self):
        while True:
            global msg
            self.con.sendto("msg".encode("utf-8"), self.s_add)
            # print("msg")
            time.sleep(1)

    def recv_data(self):
        while True:
            info = self.con.recvfrom(1024)
            print(info)
            # time.sleep(1)



class MyWindow:
    def __init__(self):
        w = Tk()
        self.ent = Entry(text="输入：")
        btn = Button(command=self.click, text="点击")
        txt = Text()

        self.ent.pack()
        btn.pack()
        txt.pack()
        # self.con = con
        w.mainloop()

    def click(self):
        global msg
        msg = self.ent.get()
        print(msg)
        self.con.send_data()

def main():
    con = MyCon()
    # con.recv_data()

    t2 = td.Thread(target=con.send_data, args=())
    t2.start()

    t1 = td.Thread(target=con.recv_data, args=())
    t1.start()

    win = MyWindow()
    # t3 = td.Thread(target=, args=(con,))
    # t3.start()


if __name__ == "__main__":
    main()

