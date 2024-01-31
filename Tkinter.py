from tkinter import *

# window/icon setting
win = Tk()
win.title("calculator")
#icon = PhotoImage(file="icon1.png")
#win.iconphoto(False, icon)
win.geometry("303x285")
win.config(bg="#ab2200")
win.resizable(width=False, height=False)

# text "calculator"
text = Label(text="calculator premium", bg="#aa6666", padx=80, pady=3).grid(row=1, column=1, columnspan=4)

# entry
calc = Entry(font=("Arial", 15), bg="#a1a1a1", justify=RIGHT)
calc.grid(row=2, column=1, columnspan=3, sticky="ew", padx=5, pady=6, ipady=3)

# adding char to entry
def add_char(char):
    value = calc.get() + str(char)
    calc.delete(0, END)
    calc.insert(0, value)

# calculating entry
def calculate():
    try:
        value2 = calc.get()
        answer = eval(str(value2))
        calc.delete(0, END)
        calc.insert(0, answer)
    except:
        calc.delete(0, END)
        calc.insert(0, "error")

def make_btn(text, row, clmn):
    Button(text=text, padx=4, pady=4, bd=5, command=lambda: add_char(text)).grid(row=row, column=clmn, stick="wens", padx=7, pady=7)

make_btn(1, 3, 1)
make_btn(2, 3, 2)
make_btn(3, 3, 3)

make_btn(4, 4, 1)
make_btn(5, 4, 2)
make_btn(6, 4, 3)

make_btn(7, 5, 1)
make_btn(8, 5, 2)
make_btn(9, 5, 3)

make_btn(0, 6, 2)

Button(text="=", padx=4, pady=4, bd=5, bg="#ffaf00", command=calculate).grid(row=6, column=3,
                                                                              stick="wens",
                                                                              padx=7,
                                                                              pady=7)

Button(text="C", padx=4, pady=4, bd=5, bg="#ffaf00", command=lambda: calc.delete(0, END)).grid(row=6, column=1, stick="wens", padx=7, pady=7)

Button(text="+", padx=4, pady=4, bd=5, bg="#888888", command=lambda: add_char("+")).grid(row=3, column=4, stick="wens", padx=7, pady=7)
Button(text="-", padx=4, pady=4, bd=5, bg="#888888", command=lambda: add_char("-")).grid(row=4, column=4, stick="wens", padx=7, pady=7)
Button(text="/", padx=4, pady=4, bd=5, bg="#888888", command=lambda: add_char("/")).grid(row=5, column=4, stick="wens", padx=7, pady=7)
Button(text="*", padx=4, pady=4, bd=5, bg="#888888", command=lambda: add_char("*")).grid(row=6, column=4, stick="wens", padx=7, pady=7)

Button(text="del", padx=4, pady=4, bd=5, bg="#ffaf00", command=lambda: calc.delete(len(calc.get())-1)).grid(row=2, column=4, stick="wens", padx=7, pady=7)

# moving to center
win.columnconfigure(1, minsize=83)
win.columnconfigure(2, minsize=83)
win.columnconfigure(3, minsize=83)

win.rowconfigure(3, minsize=30)
win.rowconfigure(4, minsize=30)
win.rowconfigure(5, minsize=30)
win.rowconfigure(6, minsize=30)

mainloop()