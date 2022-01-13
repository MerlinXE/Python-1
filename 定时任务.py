import pyfirmata
import socket
import tkinter as tk
import time
import threading as td
from schedule import *
import schedule
import winsound






class ScaleWin():
    def __init__(self):
        self.Win = tk.Tk()
        self.Win.title("滚动条")

        self.data = tk.IntVar()
        self.lbl2 = tk.Label(text="时间", relief=tk.SUNKEN)
        self.lbl2.pack(anchor=tk.NW)

        self.data = tk.DoubleVar()
        self.lbl = tk.Label(relief=tk.SUNKEN, text="\N{DEGREE FAHRENHEIT}")
        self.lbl.pack(anchor=tk.NW)

        self.scale = tk.Scale(variable=self.data, command=self.change,
                              from_=0, to=100, length=500, orient=tk.HORIZONTAL,
                              resolution=1)
        self.scale.pack()

        self.scl = tk.Scrollbar(master=self.Win)
        self.scl.pack(side="right", fill="y")

        self.txt = tk.Text(yscrollcommand=self.scl.set)
        self.txt.pack()

        self.scl.config(command=self.txt.yview)

        t1 = td.Thread(target=self.update_time)
        t1.start()

        self.Win.mainloop()

    def change(self, value):
        self.lbl["text"] = self.data.get()

    def update_time(self):

        def set_minute():
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.txt.insert(tk.END, t)
            self.txt.insert(tk.END, "\n")

        def set_second():
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.lbl2["text"] = t

        self.i = 1

        def alarm():
            while True:
                if self.i <= 5:
                    winsound.Beep(350, 2000)
                    time.sleep(2)
                    self.i += 1
                else:
                    break
                # winsound.PlaySound('MB_ICONHAND', winsound.SND_ASYNC)

        schedule.every().second.do(set_second)
        schedule.every().minute.do(set_minute)
        schedule.every().day.at("12:41:00").do(alarm)

        while True:
            schedule.run_pending()




win = ScaleWin()




