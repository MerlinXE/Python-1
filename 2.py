import tkinter as tk

root = tk.Tk()

s1 = tk.Scale(root, from_=0, to=42)
s1.pack()

s2 = tk.Scale(root, from_=0, to=200, orient="horizontal")
s2.pack()

def show():
    print(s1.get(), s2.get())

tk.Button(root, text="獲得位置", command=show).pack()

root.mainloop()