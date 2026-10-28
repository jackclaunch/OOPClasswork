import tkinter as tk

def show(x):
    try:
        if x == "=":
            final_answer = eval(T1.get(1.0, "end-1c"))
            T1.insert(tk.INSERT, x)
            T1.insert(tk.END, final_answer)
        else:
            T1.insert(tk.INSERT, x)
    except SyntaxError or NameError or ZeroDivisionError:
        T1.delete(1.0, "end-1c")


top = tk.Tk()
top.geometry("600x500")
top.configure(background="dark green")

B1 = tk.Button(top, text="1", width = 10, height = 5, command = lambda: show(1))
B1.place(x = 50, y = 100)
B2 = tk.Button(top, text="2", width = 10, height = 5, command = lambda: show(2))
B2.place(x = 150, y = 100)
B3 = tk.Button(top, text="3", width = 10, height = 5, command = lambda: show(3))
B3.place(x = 250, y = 100)
B4 = tk.Button(top, text="4", width = 10, height = 5, command = lambda: show(4))
B4.place(x = 350, y = 100)
B5 = tk.Button(top, text="5", width = 10, height = 5, command = lambda: show(5))
B5.place(x = 450, y = 100)
B6 = tk.Button(top, text="6", width = 10, height = 5, command = lambda: show(6))
B6.place(x = 50, y = 200)
B7 = tk.Button(top, text="7", width = 10, height = 5, command = lambda: show(7))
B7.place(x = 150, y = 200)
B8 = tk.Button(top, text="8", width = 10, height = 5, command = lambda: show(8))
B8.place(x = 250, y = 200)
B9 = tk.Button(top, text="9", width = 10, height = 5, command = lambda: show(9))
B9.place(x = 350, y = 200)
B0 = tk.Button(top, text="0", width = 10, height = 5, command = lambda: show(0))
B0.place(x = 450, y = 200)
Badd = tk.Button(top, text="+", width = 10, height = 5, command = lambda: show("+"))
Badd.place(x = 50, y = 300)
Bsub = tk.Button(top, text="-", width = 10, height = 5, command = lambda: show("-"))
Bsub.place(x = 150, y = 300)
Bmult = tk.Button(top, text="*", width = 10, height = 5, command = lambda: show("*"))
Bmult.place(x = 250, y = 300)
Bdiv = tk.Button(top, text="/", width = 10, height = 5, command = lambda: show("/"))
Bdiv.place(x = 350, y = 300)
Bequal = tk.Button(top, text="=", width = 10, height = 5, command = lambda: show("="))
Bequal.place(x = 450, y = 300)
T1 = tk.Text(top, width = 47, height = 2)
T1.place(x = 100, y = 400)
top.mainloop()