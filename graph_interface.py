import tkinter as tk
import matplotlib.pyplot as plt
from modulations.ask import ASK
from coders.convolutation_coder import conv_encode

def main_pannel():
    ####Объявление кнопки построения графика####
    def button_ask():
        input_str = entry.get()
        bits = input_str.split(' ')
        bits = conv_encode(bits)
        plt.plot(ASK(10, bits))
        plt.show()


    ####Описание графического интерфейса####
    window = tk.Tk()
    #window.geometry('600x700')
    window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], minsize=50)
    window.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], minsize=50)
    label1 = tk.Label(text="Амплитудная манипуляция на Python")
    label1.grid(row=0, column=5)
    #label1.pack()
    label2 = tk.Label(text="______________________________________")
    label2.grid(row=2, column=5)
    #label2.pack()
    label3 = tk.Label(text="Введите битовую последовательность через пробел: ")
    label3.grid(row=3, column=5)
    #label3.pack()
    entry = tk.Entry()
    entry.grid(row=4, column=5)
    #entry.pack()

    button = tk.Button(
        text="Построить график",
        width=25,
        height=5,
        bg="blue",
        fg="yellow",
        command=button_ask
    )
    button.grid(row=6, column=5)
    #button.pack()
    window.mainloop()