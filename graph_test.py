from tkinter import *
from tkinter.ttk import *
import matplotlib.pyplot as plt
from modulations.ask import ASK, ASDK
from modulations.fsk import FSK
from coders.convolutation_coder import conv_encode
from coders.virerby_decoder import viterby_decode
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# creating tkinter window
window = Tk()
window.rowconfigure([0, 1, 2, 3, 4], minsize=50)
window.columnconfigure([0, 1, 2, 3, 4], minsize=50)
# Adding widgets to the root window
Label(window, text='Система передачи информации', font=('Verdana', 15)).grid(row=0, column=1)

# Creating a photoimage object to use image
photo = PhotoImage(file=r"C:\Users\Казбек\PycharmProjects\diplom_tokaev\images\input.png")
photo2 = PhotoImage(file=r"C:\Users\Казбек\PycharmProjects\diplom_tokaev\images\coder.png")
photo3 = PhotoImage(file=r"C:\Users\Казбек\PycharmProjects\diplom_tokaev\images\modulations.png")
photo4 = PhotoImage(file=r"C:\Users\Казбек\PycharmProjects\diplom_tokaev\images\channel.png")

# here, image option is used to
# set image on button


def button_ask():
    def button5_ask():
        global input_bits
        input_bits = entry.get()
        Label(window, text='Входная последовательность: ' + input_bits).grid(row=3, column=1)
        a.destroy()

    a = Toplevel()
    a.rowconfigure([0, 1, 2, 3, 4], minsize=50)
    a.columnconfigure([0, 1, 2, 3, 4], minsize=50)
    Label(a, text="Введите входную последоватеьность через пробел").grid(row=0, column=3)
    entry = Entry(a)
    entry.grid(row=1, column=3)
    button5 = Button(a, text="ОК", command = button5_ask)
    button5.grid(row=2, column=3)

def button_ask2():
    def button6_ask():
        global input_coder
        if var.get() == 0:
            input_coder = 'Сверточный код'
        elif var.get() == 1:
            input_coder = 'Итеративный код'
        b.destroy()

        Label(window, text='Способ кодирования: ' + input_coder).grid(row=3, column=2)
    b = Toplevel()
    b.rowconfigure([0, 1, 2, 3, 4], minsize=50)
    b.columnconfigure([0, 1, 2, 3, 4], minsize=50)
    Label(b, text="Выберите способ кодирования").grid(row=0, column=3)
    var = IntVar()
    var.set(0)
    svert = Radiobutton(b, text="Сверточный код",
                      variable=var, value=0)
    iter = Radiobutton(b, text="Итеративный код",
                        variable=var, value=1)
    svert.grid(row=1, column=3)
    iter.grid(row=2, column=3)
    button6 = Button(b, text="ОК", command = button6_ask)
    button6.grid(row=3, column=3)
    #print(input_bits)
    return 2

def button_ask3():
    def button7_ask():
        global frequency
        frequency = entry2.get()
        global modulation_type
        if var.get() == 0:
            modulation_type = 'Амплитудная манипуляция'
        elif var.get() == 1:
            modulation_type = 'Частотная манипуляция'
        c.destroy()
        Label(window, text='Вид модуляции: ' + modulation_type).grid(row=3, column=3)
        Label(window, text='Частота: ' + frequency).grid(row=4, column=3)
        frequency = int(frequency)
    c = Toplevel()
    c.rowconfigure([0, 1, 2, 3, 4], minsize=50)
    c.columnconfigure([0, 1, 2, 3, 4], minsize=50)
    Label(c, text="Выберите тип модуляции").grid(row=0, column=2)
    var = IntVar()
    var.set(0)
    ampl = Radiobutton(c, text="Амплитудная манипуляция",
                      variable=var, value=0)
    freq = Radiobutton(c, text="Частотная манипуляция",
                        variable=var, value=1)
    ampl.grid(row=1, column=2)
    freq.grid(row=2, column=2)
    Label(c, text="Частота: ").grid(row=3, column=1)
    entry2 = Entry(c)
    entry2.insert(END, 10)
    entry2.grid(row=3, column=2)
    button7 = Button(c, text="ОК", command = button7_ask)
    button7.grid(row=3, column=3)

    return 3
def button_ask4():
    def button8_ask():
        global bits_error
        bits_error = entry3.get()
        Label(window, text='Число битовых ошибок: ' + bits_error).grid(row=3, column=4)
        d.destroy()

    d = Toplevel()
    d.rowconfigure([0, 1, 2, 3, 4], minsize=50)
    d.columnconfigure([0, 1, 2, 3, 4], minsize=50)
    Label(d, text="Введите число битовых ошибок").grid(row=0, column=3)
    entry3 = Entry(d)
    entry3.insert(END, 1)
    entry3.grid(row=1, column=3)
    button8 = Button(d, text="ОК", command = button8_ask)
    button8.grid(row=2, column=3)
##
##моделирование
##
def button_ask9():
    print("запускаю моделирование")
    e = Toplevel()
    e.rowconfigure([0, 1, 2, 3, 4, 5], minsize=50)
    e.columnconfigure([0, 1, 2, 3, 4], minsize=50)
    Label(e, text="Результат моделирования").grid(row=0, column=3)
    bits = input_bits.split(' ')
    #bits = conv_encode(bits)
    bits_encode = ''
    Label(e, text="Исходящая последовательность: ").grid(row=1, column=0)
    Label(e, text=bits).grid(row=1, column=1)
    if input_coder == 'Сверточный код':
        bits_encode = conv_encode(bits)
    else:
        print("errror")
    Label(e, text="Закодированная последовательность: ").grid(row=2, column=0)
    Label(e, text=bits_encode).grid(row=2, column=1)
    Label(e, text="Результат манипуляции").grid(row=1, column=3)
    Label(e, text="Результат деманипуляции").grid(row=1, column=4)

    if modulation_type == 'Амплитудная манипуляция':
        figure1 = plt.Figure(figsize=(5,4), dpi=100)
        ax1 = figure1.add_subplot(111)
        line1 = FigureCanvasTkAgg(figure1, e)
        line1.get_tk_widget().grid(row=2, column=3)
        modulated_signal = ASK(frequency, bits_encode)
        ax1.plot(modulated_signal)

        figure2 = plt.Figure(figsize=(5,4), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, e)
        line2.get_tk_widget().grid(row=2, column=4)
        demodulated_signal = ASDK(frequency, modulated_signal)

        ax2.plot(demodulated_signal)
        Label(e, text="Принятая последовательность: ").grid(row=4, column=0)
        fc = frequency
        N = 10 * fc
        bits_after_demodulation = []
        for i in range(0, len(str(demodulated_signal)) // 3, N * 10):
            mid = 0
            if i < 10000:
                for j in range(i, i + N):
                    if j < 10001:
                        mid = mid + int(str(demodulated_signal[j]))
                mid = mid / N
                # print(mid)
                if mid > 0.01:
                    bits_after_demodulation.append('1')
                else:
                    bits_after_demodulation.append('0')
        # print((str(bits_after_demodulation)))
        if bits_error == '1':
            error_in_bit = random.randint(0, len(bits_after_demodulation))
            print(error_in_bit)
            if bits_after_demodulation[error_in_bit] == '1':
                bits_after_demodulation[error_in_bit] = 0
            else:
                bits_after_demodulation[error_in_bit] = 1


        Label(e, text=bits_after_demodulation).grid(row=4, column=1)

        Label(e, text="Декодированая последовательность: ").grid(row=5, column=0)
        result = viterby_decode(bits_after_demodulation)
        Label(e, text=result).grid(row=5, column=1)

    elif modulation_type == 'Частотная манипуляция':
        figure1 = plt.Figure(figsize=(5,4), dpi=100)
        ax1 = figure1.add_subplot(111)
        line1 = FigureCanvasTkAgg(figure1, e)
        line1.get_tk_widget().grid(row=2, column=3)
        modulated_signal = FSK(frequency, bits_encode)
        ax1.plot(modulated_signal)

        figure2 = plt.Figure(figsize=(5,4), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, e)
        line2.get_tk_widget().grid(row=2, column=4)
        modulated_signal = ASK(frequency, bits_encode)
        demodulated_signal = ASDK(frequency, modulated_signal)

        ax2.plot(demodulated_signal)
        Label(e, text="Принятая последовательность: ").grid(row=4, column=0)
        fc = frequency
        N = 10 * fc
        bits_after_demodulation = []
        for i in range(0, len(str(demodulated_signal)) // 3, N * 10):
            mid = 0
            if i < 10000:
                for j in range(i, i + N):
                    if j < 10001:
                        mid = mid + int(str(demodulated_signal[j]))
                mid = mid / N
                # print(mid)
                if mid > 0.01:
                    bits_after_demodulation.append('1')
                else:
                    bits_after_demodulation.append('0')
        # print((str(bits_after_demodulation)))
        if bits_error == '1':
            error_in_bit = random.randint(0, len(bits_after_demodulation))
            print(error_in_bit)
            if bits_after_demodulation[error_in_bit] == '1':
                bits_after_demodulation[error_in_bit] = 0
            else:
                bits_after_demodulation[error_in_bit] = 1


        Label(e, text=bits_after_demodulation).grid(row=4, column=1)

        Label(e, text="Декодированая последовательность: ").grid(row=5, column=0)
        result = viterby_decode(bits_after_demodulation)
        Label(e, text=result).grid(row=5, column=1)


##
##
##

def button_ask10():
    window.destroy()

button1 = Button(window, text='Click Me !', image=photo, command=button_ask).grid(row=2, column=1)
button2 = Button(window, text='Click Me !', image=photo2, command=button_ask2).grid(row=2, column=2)
button3 = Button(window, text='Click Me !', image=photo3, command=button_ask3).grid(row=2, column=3)
button4 = Button(window, text='Click Me !', image=photo4, command=button_ask4).grid(row=2, column=4)


button9 = Button(window, text='Запустить моделирование', command=button_ask9).grid(row=4, column=2)
button10 = Button(window, text='Выйти', command=button_ask10).grid(row=4, column=4)
mainloop()