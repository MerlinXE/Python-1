import socket
from tkinter import *
import threading as td
import time

msg = "default"


class MyCon:

    def __init__(self):
        self.con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.add = ("192.168.1.104", 8080)

    def send_data(self):
        global msg
        self.con.sendto(msg.encode("utf-8"), self.add)
        time.sleep(1)


class MyWindow:
    def __init__(self):
        w = Tk()
        self.ent = Entry(text="输入：")
        btn = Button(command=self.click, text="点击")
        self.ent.pack()
        btn.pack()

        w.mainloop()

    def click(self):
        global msg
        msg = self.ent.get()
        print(msg)
        con.send_data()


def main():
    con = MyCon()
    win = MyWindow()
    # t1 = td.Thread(target=MyWindow, args=())
    # t1.start()

    # t2 = td.Thread(target=MyCon, args=())
    # t2.start()

    # newcon.send_data()

    #print(newcon.con)
    #print(newcon.add)


if __name__ == "__main__":
    main()

