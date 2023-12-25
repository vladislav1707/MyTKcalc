from tkinter import *

# window/icon setting
win = Tk()
win.title("calculator")
icon = PhotoImage(file="icon1.png")
win.iconphoto(False, icon)
win.geometry("303x285")
win.config(bg="#ab2200")

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
    value2 = calc.get()
    answer = eval(str(value2))
    calc.delete(0, END)
    calc.insert(0, answer)

# buttons
Button(text="1", padx=4, pady=4, bd=5, command=lambda: add_char(1)).grid(row=3, column=1, stick="wens", padx=7, pady=7)
Button(text="2", padx=4, pady=4, bd=5, command=lambda: add_char(2)).grid(row=3, column=2, stick="wens", padx=7, pady=7)
Button(text="3", padx=4, pady=4, bd=5, command=lambda: add_char(3)).grid(row=3, column=3, stick="wens", padx=7, pady=7)
Button(text="4", padx=4, pady=4, bd=5, command=lambda: add_char(4)).grid(row=4, column=1, stick="wens", padx=7, pady=7)
Button(text="5", padx=4, pady=4, bd=5, command=lambda: add_char(5)).grid(row=4, column=2, stick="wens", padx=7, pady=7)
Button(text="6", padx=4, pady=4, bd=5, command=lambda: add_char(6)).grid(row=4, column=3, stick="wens", padx=7, pady=7)
Button(text="7", padx=4, pady=4, bd=5, command=lambda: add_char(7)).grid(row=5, column=1, stick="wens", padx=7, pady=7)
Button(text="8", padx=4, pady=4, bd=5, command=lambda: add_char(8)).grid(row=5, column=2, stick="wens", padx=7, pady=7)
Button(text="9", padx=4, pady=4, bd=5, command=lambda: add_char(9)).grid(row=5, column=3, stick="wens", padx=7, pady=7)
Button(text="0", padx=4, pady=4, bd=5, command=lambda: add_char(0)).grid(row=6, column=2, stick="wens", padx=7, pady=7)

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