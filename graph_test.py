from tkinter import * ##Импорт библиотек для графической оболояки
from tkinter.ttk import *
import matplotlib.pyplot as plt ## Импорт библиотек для построения графиков
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random  ## Импорт библиотеки для генератора ошибок
from modulations.ask import ASK, ASDK ##Импорт самописных модулей для модуляций
from modulations.fsk import FSK
from coders.convolutation_coder import conv_encode ## Импорт самописных модулей для кодирования
from coders.virerby_decoder import viterby_decode
from coders.iter_coder import iter_code, iter_decode
from errors_counter import errors_count

# Создание и конфигурация рабочего окна
window = Tk()
window.rowconfigure([0, 1, 2, 3, 4, 5], minsize=50)
window.columnconfigure([0, 1, 2, 3, 4], minsize=50)

tab_control = Notebook(window)
tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab_control.add(tab1, text='Одиночный запуск')
tab_control.add(tab2, text='Режим исследования')
tab_control.grid()
# Добавление виджетов


# Создание фотообъектов для кнопок главное панели
photo = PhotoImage(file=r"C:\Users\Казбек\PycharmProjects\diplom_tokaev\images\input.png")
photo2 = PhotoImage(file=r"C:\Users\Казбек\PycharmProjects\diplom_tokaev\images\coder.png")
photo3 = PhotoImage(file=r"C:\Users\Казбек\PycharmProjects\diplom_tokaev\images\modulations.png")
photo4 = PhotoImage(file=r"C:\Users\Казбек\PycharmProjects\diplom_tokaev\images\channel.png")

Label(tab1, text='Система передачи информации', font=('Verdana', 15)).grid(row=1, column=2)
Label(tab2, text='Система передачи информации 2', font=('Verdana', 15)).grid(row=1, column=2)
# Описание рабочих кнопок

def button_ask():
    def button5_ask():
        global input_bits
        input_bits = entry.get()
        Label(tab1, text='Входная последовательность: ' + input_bits).grid(row=3, column=1)
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

        Label(tab1, text='Способ кодирования: ' + input_coder).grid(row=3, column=2)
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
        Label(tab1, text='Вид модуляции: ' + modulation_type).grid(row=3, column=3)
        Label(tab1, text='Частота: ' + frequency).grid(row=4, column=3)
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

def button_ask4():
    def button8_ask():
        global bits_error
        bits_error = entry3.get()
        Label(tab1, text='Число битовых ошибок: ' + bits_error).grid(row=3, column=4)
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

    if (modulation_type == 'Амплитудная манипуляция') and (input_coder == 'Сверточный код'):
        bits = input_bits.split(' ')
        bits_encode = ''
        Label(e, text="Исходная последовательность: ").grid(row=1, column=0)
        Label(e, text=bits).grid(row=1, column=1)
        bits_encode = conv_encode(bits)
        Label(e, text="Закодированная последовательность: ").grid(row=2, column=0)
        Label(e, text=bits_encode).grid(row=2, column=1)
        Label(e, text="Результат манипуляции").grid(row=1, column=3)
        Label(e, text="Результат деманипуляции").grid(row=1, column=4)

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

    elif (modulation_type == 'Частотная манипуляция') and (input_coder == 'Сверточный код'):
        bits = input_bits.split(' ')
        bits_encode = ''
        Label(e, text="Исходная последовательность: ").grid(row=1, column=0)
        Label(e, text=bits).grid(row=1, column=1)
        bits_encode = conv_encode(bits)
        Label(e, text="Закодированная последовательность: ").grid(row=2, column=0)
        Label(e, text=bits_encode).grid(row=2, column=1)
        Label(e, text="Результат манипуляции").grid(row=1, column=3)
        Label(e, text="Результат деманипуляции").grid(row=1, column=4)

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

    elif (modulation_type == 'Амплитудная манипуляция') and (input_coder == 'Итеративный код'):
        bits = str(input_bits)
        #print("len" + str(len(bits)))
        #'101',
        # '011',
        # '110'
        #101011111
        bits_n = []
        for i in range(0, len(bits), 3):
            troika = str(bits[i]) + str(bits[i+1]) +  str(bits[i+2])
            bits_n.append(troika)

        bits_encode = ''
        Label(e, text="Исходная последовательность: ").grid(row=1, column=0)
        Label(e, text=bits_n).grid(row=1, column=1)

        #print("in " + str(bits_n))
        bits_encode = iter_code(bits_n)
        bits_for_manipulation = str(bits_encode[0]) + str(bits_encode[1]) +str(bits_encode[2]) +str(bits_encode[3]) +str(bits_encode[4])
        Label(e, text="Закодированная последовательность: ").grid(row=2, column=0)
        Label(e, text=bits_encode).grid(row=2, column=1)
        Label(e, text="Результат манипуляции").grid(row=1, column=3)
        Label(e, text="Результат деманипуляции").grid(row=1, column=4)

        figure1 = plt.Figure(figsize=(5, 4), dpi=100)
        ax1 = figure1.add_subplot(111)
        line1 = FigureCanvasTkAgg(figure1, e)
        line1.get_tk_widget().grid(row=2, column=3)
        modulated_signal = ASK(frequency, bits_for_manipulation)
        ax1.plot(modulated_signal)

        figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, e)
        line2.get_tk_widget().grid(row=2, column=4)
        demodulated_signal = ASDK(frequency, modulated_signal)

        ax2.plot(demodulated_signal)
        Label(e, text="Принятая последовательность: ").grid(row=4, column=0)
        fc = frequency
        N = 10 * fc
        bits_after_demodulation = []
        #print('len_d ' + str(len(str(demodulated_signal))))
        for i in range(0, len(str(demodulated_signal)) // 3, N * 10):
            mid = 0
            if i < 15000:
                for j in range(i, i + N):
                    if j < 15001:
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
            #print(error_in_bit)
            if bits_after_demodulation[error_in_bit] == '1':
                bits_after_demodulation[error_in_bit] = 0
            else:
                bits_after_demodulation[error_in_bit] = 1

        Label(e, text=bits_after_demodulation).grid(row=4, column=1)

        Label(e, text="Декодированая последовательность: ").grid(row=5, column=0)
        bits_for_iter_decode = []
        #print(bits_after_demodulation)
        #print(len(bits_after_demodulation))

        for i in range(0, len(bits_after_demodulation), 3):
            troika = str(bits_after_demodulation[i]) + str(bits_after_demodulation[i+1]) +  str(bits_after_demodulation[i+2])
            bits_for_iter_decode.append(troika)

        result = iter_decode(bits_for_iter_decode)
        Label(e, text=result).grid(row=5, column=1)

    elif (modulation_type == 'Частотная манипуляция') and (input_coder == 'Итеративный код'):
        bits = str(input_bits)
        #print("len" + str(len(bits)))
        bits_n = []
        for i in range(0, len(bits), 3):
            troika = str(bits[i]) + str(bits[i+1]) +  str(bits[i+2])
            bits_n.append(troika)

        bits_encode = ''
        Label(e, text="Исходная последовательность: ").grid(row=1, column=0)
        Label(e, text=bits_n).grid(row=1, column=1)

        #print("in " + str(bits_n))
        bits_encode = iter_code(bits_n)
        bits_for_manipulation = str(bits_encode[0]) + str(bits_encode[1]) +str(bits_encode[2]) +str(bits_encode[3]) +str(bits_encode[4])
        Label(e, text="Закодированная последовательность: ").grid(row=2, column=0)
        Label(e, text=bits_encode).grid(row=2, column=1)
        Label(e, text="Результат манипуляции").grid(row=1, column=3)
        Label(e, text="Результат деманипуляции").grid(row=1, column=4)

        figure1 = plt.Figure(figsize=(5, 4), dpi=100)
        ax1 = figure1.add_subplot(111)
        line1 = FigureCanvasTkAgg(figure1, e)
        line1.get_tk_widget().grid(row=2, column=3)
        modulated_signal = FSK(frequency, bits_for_manipulation)
        ax1.plot(modulated_signal)

        figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, e)
        line2.get_tk_widget().grid(row=2, column=4)
        modulated_signal = ASK(frequency, bits_for_manipulation)
        demodulated_signal = ASDK(frequency, modulated_signal)

        ax2.plot(demodulated_signal)
        Label(e, text="Принятая последовательность: ").grid(row=4, column=0)
        fc = frequency
        N = 10 * fc
        bits_after_demodulation = []
        #print('len_d ' + str(len(str(demodulated_signal))))
        for i in range(0, len(str(demodulated_signal)) // 3, N * 10):
            mid = 0
            if i < 15000:
                for j in range(i, i + N):
                    if j < 15001:
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
        bits_for_iter_decode = []
        #print(bits_after_demodulation)
        #print(len(bits_after_demodulation))

        for i in range(0, len(bits_after_demodulation), 3):
            troika = str(bits_after_demodulation[i]) + str(bits_after_demodulation[i+1]) +  str(bits_after_demodulation[i+2])
            bits_for_iter_decode.append(troika)

        result = iter_decode(bits_for_iter_decode)
        Label(e, text=result).grid(row=5, column=1)



#################################################
#################################################
#################################################
#################################################

def button_ask11():
    def button5_ask():
        global input_bits
        global sequence_count
        sequence_count = 0
        input_bits = entry.get()
        print(input_bits)

        if len(input_bits) % 3 == 1:
            input_bits = input_bits + '00'
        elif len(input_bits) % 3 == 2:
            input_bits = input_bits + '0'
        for i in range(0, len(input_bits),3):
            sequence_count+=1

        print(input_bits)
        print(sequence_count)
        input_bits_for_print = 0
        if len(input_bits) > 10:
            input_bits_for_print = str(input_bits_for_print) + input_bits[0:9] + '...'
        else:
            input_bits_for_print = input_bits
        Label(tab2, text='Входная последовательность: ' + str(input_bits_for_print)).grid(row=3, column=1)
        a.destroy()

    a = Toplevel()
    a.rowconfigure([0, 1, 2, 3, 4], minsize=50)
    a.columnconfigure([0, 1, 2, 3, 4], minsize=50)
    Label(a, text="Введите входную последоватеьность").grid(row=0, column=3)
    entry = Entry(a)
    entry.grid(row=1, column=3)
    button5 = Button(a, text="ОК", command = button5_ask)
    button5.grid(row=2, column=3)

def button_ask12():
    def button17_ask():
        global input_coder
        if var.get() == 0:
            input_coder = 'Сверточный код'
        elif var.get() == 1:
            input_coder = 'Итеративный код'
        b.destroy()

        Label(tab2, text='Способ кодирования: ' + input_coder).grid(row=3, column=2)
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
    button6 = Button(b, text="ОК", command = button17_ask)
    button6.grid(row=3, column=3)

def button_ask13():
    def button18_ask():
        global frequency
        frequency = entry2.get()
        global modulation_type
        if var.get() == 0:
            modulation_type = 'Амплитудная манипуляция'
        elif var.get() == 1:
            modulation_type = 'Частотная манипуляция'
        c.destroy()
        Label(tab2, text='Вид модуляции: ' + modulation_type).grid(row=3, column=3)
        Label(tab2, text='Частота: ' + frequency).grid(row=4, column=3)
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
    button7 = Button(c, text="ОК", command = button18_ask)
    button7.grid(row=3, column=3)

def button_ask14():
    def button19_ask():
        global bits_error
        bits_error = entry3.get()
        Label(tab2, text='Число битовых ошибок: ' + bits_error).grid(row=3, column=4)
        d.destroy()

    d = Toplevel()
    d.rowconfigure([0, 1, 2, 3, 4], minsize=50)
    d.columnconfigure([0, 1, 2, 3, 4], minsize=50)
    Label(d, text="Введите число битовых ошибок").grid(row=0, column=3)
    entry3 = Entry(d)
    entry3.insert(END, 1)
    entry3.grid(row=1, column=3)
    button8 = Button(d, text="ОК", command = button19_ask)
    button8.grid(row=2, column=3)

##
##моделирование
##
def button_ask16():
    print("запускаю моделирование")
    e = Toplevel()
    e.rowconfigure([0, 1, 2, 3, 4, 5], minsize=50)
    e.columnconfigure([0, 1, 2, 3, 4], minsize=50)
    Label(e, text="Результат моделирования").grid(row=0, column=3)

    if (modulation_type == 'Амплитудная манипуляция') and (input_coder == 'Сверточный код'):
        sequences_of_input_bits_for_code = []
        for i in range(0, len(input_bits), 3):
            seq = str(input_bits[i]) + str(input_bits[i+1]) + str(input_bits[i+2])
            sequences_of_input_bits_for_code.append(seq)
        print('seq++ ' + str(sequences_of_input_bits_for_code))
        bits_encode_sequence = []
        for i in sequences_of_input_bits_for_code:
            sequence_of_input_bits = i
            sequence_of_input_bits_for_code = []
            sequence_of_input_bits_for_code.append(str(sequence_of_input_bits[0]))
            sequence_of_input_bits_for_code.append(str(sequence_of_input_bits[1]))
            sequence_of_input_bits_for_code.append(str(sequence_of_input_bits[2]))
            bits = sequence_of_input_bits_for_code
            bits_encode = ''

            bits_encode = conv_encode(bits)
            bits_encode_sequence += bits_encode
        print('enc++' + str(bits_encode_sequence))
        input_bits_for_print = []
        if len(input_bits) > 9:
            input_bits_for_print = str(input_bits[0:9]) + '...'
        else:
            input_bits_for_print = input_bits
        Label(e, text="Исходная последовательность: ").grid(row=1, column=0)
        Label(e, text=input_bits_for_print).grid(row=1, column=1)
        bits_encode_sequence_for_print = []
        if len(bits_encode_sequence) > 9:
            bits_encode_sequence_for_print = str(bits_encode_sequence[0:9]) + '...'
        else:
            bits_encode_sequence_for_print = bits_encode_sequence
        Label(e, text="Закодированная последовательность: ").grid(row=2, column=0)
        Label(e, text=bits_encode_sequence_for_print).grid(row=2, column=1)
        Label(e, text="Результат манипуляции").grid(row=1, column=3)
        Label(e, text="Результат деманипуляции").grid(row=1, column=4)

        figure1 = plt.Figure(figsize=(5,4), dpi=100)
        ax1 = figure1.add_subplot(111)
        line1 = FigureCanvasTkAgg(figure1, e)
        line1.get_tk_widget().grid(row=2, column=3)
        modulated_signal = ASK(frequency, bits_encode_sequence)
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
            if i < 10000*sequence_count:
                for j in range(i, i + N):
                    if j < 10000*sequence_count+1:
                        mid = mid + int(str(demodulated_signal[j]))
                mid = mid / N
                # print(mid)
                if mid > 0.01:
                    bits_after_demodulation.append('1')
                else:
                    bits_after_demodulation.append('0')
        # print((str(bits_after_demodulation)))
        # if bits_error == '1':
        #     error_in_bit = random.randint(0, len(bits_after_demodulation))
        #     print(error_in_bit)
        #     if bits_after_demodulation[error_in_bit] == '1':
        #         bits_after_demodulation[error_in_bit] = 0
        #     else:
        #         bits_after_demodulation[error_in_bit] = 1
        if bits_error != '0':
            for i in range(int(bits_error)):
                error_in_bit = random.randint(0, len(bits_after_demodulation))
                print(error_in_bit)
                if bits_after_demodulation[error_in_bit] == '1':
                    bits_after_demodulation[error_in_bit] = 0
                else:
                    bits_after_demodulation[error_in_bit] = 1

        sequences_of_output_bits_for_decode = []
        print('demod ' + str(bits_after_demodulation))
        print(len(bits_after_demodulation))
        for i in range(0, len(bits_after_demodulation), 10):
            seq = str(bits_after_demodulation[i]) + \
                  str(bits_after_demodulation[i+1]) + \
                  str(bits_after_demodulation[i+2]) + \
                  str(bits_after_demodulation[i+3]) + \
                  str(bits_after_demodulation[i + 4]) + \
                  str(bits_after_demodulation[i + 5]) + \
                  str(bits_after_demodulation[i + 6]) + \
                  str(bits_after_demodulation[i + 7]) + \
                  str(bits_after_demodulation[i + 8]) + \
                  str(bits_after_demodulation[i + 9])
            sequences_of_output_bits_for_decode.append(seq)

        decoded_bits = []
        for j in sequences_of_output_bits_for_decode:
            decoded_bits += str(viterby_decode(j))
        bits_after_demodulation_for_print = []
        if  len(bits_after_demodulation) > 9:
            bits_after_demodulation_for_print += bits_after_demodulation[0:9]
        else:
            bits_after_demodulation_for_print = bits_after_demodulation
        Label(e, text=bits_after_demodulation).grid(row=4, column=1)
        Label(e, text="Декодированая последовательность: ").grid(row=5, column=0)
        #result = viterby_decode(bits_after_demodulation)
        Label(e, text=decoded_bits).grid(row=5, column=1)

        Label(e, text="Количество ошибок: ").grid(row=5, column=2)
        #result = viterby_decode(bits_after_demodulation)
        Label(e, text=errors_count(input_bits ,decoded_bits)).grid(row=5, column=3)

    elif (modulation_type == 'Частотная манипуляция') and (input_coder == 'Сверточный код'):
        bits = input_bits.split(' ')
        bits_encode = ''
        Label(e, text="Исходная последовательность: ").grid(row=1, column=0)
        Label(e, text=bits).grid(row=1, column=1)
        bits_encode = conv_encode(bits)
        Label(e, text="Закодированная последовательность: ").grid(row=2, column=0)
        Label(e, text=bits_encode).grid(row=2, column=1)
        Label(e, text="Результат манипуляции").grid(row=1, column=3)
        Label(e, text="Результат деманипуляции").grid(row=1, column=4)

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

    elif (modulation_type == 'Амплитудная манипуляция') and (input_coder == 'Итеративный код'):
        bits = str(input_bits)
        #print("len" + str(len(bits)))
        #'101',
        # '011',
        # '110'
        #101011111
        bits_n = []
        for i in range(0, len(bits), 3):
            troika = str(bits[i]) + str(bits[i+1]) +  str(bits[i+2])
            bits_n.append(troika)

        bits_encode = ''
        Label(e, text="Исходная последовательность: ").grid(row=1, column=0)
        Label(e, text=bits_n).grid(row=1, column=1)

        #print("in " + str(bits_n))
        bits_encode = iter_code(bits_n)
        bits_for_manipulation = str(bits_encode[0]) + str(bits_encode[1]) +str(bits_encode[2]) +str(bits_encode[3]) +str(bits_encode[4])
        Label(e, text="Закодированная последовательность: ").grid(row=2, column=0)
        Label(e, text=bits_encode).grid(row=2, column=1)
        Label(e, text="Результат манипуляции").grid(row=1, column=3)
        Label(e, text="Результат деманипуляции").grid(row=1, column=4)

        figure1 = plt.Figure(figsize=(5, 4), dpi=100)
        ax1 = figure1.add_subplot(111)
        line1 = FigureCanvasTkAgg(figure1, e)
        line1.get_tk_widget().grid(row=2, column=3)
        modulated_signal = ASK(frequency, bits_for_manipulation)
        ax1.plot(modulated_signal)

        figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, e)
        line2.get_tk_widget().grid(row=2, column=4)
        demodulated_signal = ASDK(frequency, modulated_signal)

        ax2.plot(demodulated_signal)
        Label(e, text="Принятая последовательность: ").grid(row=4, column=0)
        fc = frequency
        N = 10 * fc
        bits_after_demodulation = []
        #print('len_d ' + str(len(str(demodulated_signal))))
        for i in range(0, len(str(demodulated_signal)) // 3, N * 10):
            mid = 0
            if i < 15000:
                for j in range(i, i + N):
                    if j < 15001:
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
            #print(error_in_bit)
            if bits_after_demodulation[error_in_bit] == '1':
                bits_after_demodulation[error_in_bit] = 0
            else:
                bits_after_demodulation[error_in_bit] = 1

        Label(e, text=bits_after_demodulation).grid(row=4, column=1)

        Label(e, text="Декодированая последовательность: ").grid(row=5, column=0)
        bits_for_iter_decode = []
        #print(bits_after_demodulation)
        #print(len(bits_after_demodulation))

        for i in range(0, len(bits_after_demodulation), 3):
            troika = str(bits_after_demodulation[i]) + str(bits_after_demodulation[i+1]) +  str(bits_after_demodulation[i+2])
            bits_for_iter_decode.append(troika)

        result = iter_decode(bits_for_iter_decode)
        Label(e, text=result).grid(row=5, column=1)

    elif (modulation_type == 'Частотная манипуляция') and (input_coder == 'Итеративный код'):
        bits = str(input_bits)
        #print("len" + str(len(bits)))
        bits_n = []
        for i in range(0, len(bits), 3):
            troika = str(bits[i]) + str(bits[i+1]) +  str(bits[i+2])
            bits_n.append(troika)

        bits_encode = ''
        Label(e, text="Исходная последовательность: ").grid(row=1, column=0)
        Label(e, text=bits_n).grid(row=1, column=1)

        #print("in " + str(bits_n))
        bits_encode = iter_code(bits_n)
        bits_for_manipulation = str(bits_encode[0]) + str(bits_encode[1]) +str(bits_encode[2]) +str(bits_encode[3]) +str(bits_encode[4])
        Label(e, text="Закодированная последовательность: ").grid(row=2, column=0)
        Label(e, text=bits_encode).grid(row=2, column=1)
        Label(e, text="Результат манипуляции").grid(row=1, column=3)
        Label(e, text="Результат деманипуляции").grid(row=1, column=4)

        figure1 = plt.Figure(figsize=(5, 4), dpi=100)
        ax1 = figure1.add_subplot(111)
        line1 = FigureCanvasTkAgg(figure1, e)
        line1.get_tk_widget().grid(row=2, column=3)
        modulated_signal = FSK(frequency, bits_for_manipulation)
        ax1.plot(modulated_signal)

        figure2 = plt.Figure(figsize=(5, 4), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, e)
        line2.get_tk_widget().grid(row=2, column=4)
        modulated_signal = ASK(frequency, bits_for_manipulation)
        demodulated_signal = ASDK(frequency, modulated_signal)

        ax2.plot(demodulated_signal)
        Label(e, text="Принятая последовательность: ").grid(row=4, column=0)
        fc = frequency
        N = 10 * fc
        bits_after_demodulation = []
        #print('len_d ' + str(len(str(demodulated_signal))))
        for i in range(0, len(str(demodulated_signal)) // 3, N * 10):
            mid = 0
            if i < 15000:
                for j in range(i, i + N):
                    if j < 15001:
                        mid = mid + int(str(demodulated_signal[j]))
                mid = mid / N
                # print(mid)
                if mid > 0.01:
                    bits_after_demodulation.append('1')
                else:
                    bits_after_demodulation.append('0')
        print((str(bits_after_demodulation)))
        if bits_error == '1':
            error_in_bit = random.randint(0, len(bits_after_demodulation))
            print(error_in_bit)
            if bits_after_demodulation[error_in_bit] == '1':
                bits_after_demodulation[error_in_bit] = 0
            else:
                bits_after_demodulation[error_in_bit] = 1
        # if bits_error != '0':
        #     for i in range(int(bits_error)):
        #         error_in_bit = random.randint(0, len(bits_after_demodulation))
        #         print(error_in_bit)
        #         if bits_after_demodulation[error_in_bit] == '1':
        #             bits_after_demodulation[error_in_bit] = 0
        #         else:
        #             bits_after_demodulation[error_in_bit] = 1

        Label(e, text=bits_after_demodulation).grid(row=4, column=1)

        Label(e, text="Декодированая последовательность: ").grid(row=5, column=0)
        bits_for_iter_decode = []
        #print(bits_after_demodulation)
        #print(len(bits_after_demodulation))

        for i in range(0, len(bits_after_demodulation), 3):
            troika = str(bits_after_demodulation[i]) + str(bits_after_demodulation[i+1]) +  str(bits_after_demodulation[i+2])
            bits_for_iter_decode.append(troika)

        result = iter_decode(bits_for_iter_decode)
        Label(e, text=result).grid(row=5, column=1)


##
##
##
#################################################
#################################################
#################################################
#################################################

def button_ask10():
    window.destroy()

button1 = Button(tab1, text='Click Me !', image=photo, command=button_ask).grid(row=2, column=1)
button2 = Button(tab1, text='Click Me !', image=photo2, command=button_ask2).grid(row=2, column=2)
button3 = Button(tab1, text='Click Me !', image=photo3, command=button_ask3).grid(row=2, column=3)
button4 = Button(tab1, text='Click Me !', image=photo4, command=button_ask4).grid(row=2, column=4)
button9 = Button(tab1, text='Запустить моделирование', command=button_ask9).grid(row=4, column=2)
button10 = Button(tab1, text='Выйти', command=button_ask10).grid(row=4, column=4)

button11 = Button(tab2, text='Click Me !', image=photo, command=button_ask11).grid(row=2, column=1)
button12 = Button(tab2, text='Click Me !', image=photo2, command=button_ask12).grid(row=2, column=2)
button13 = Button(tab2, text='Click Me !', image=photo3, command=button_ask13).grid(row=2, column=3)
button14 = Button(tab2, text='Click Me !', image=photo4, command=button_ask14).grid(row=2, column=4)
button15 = Button(tab2, text='Запустить моделирование', command=button_ask16).grid(row=4, column=2)
button16 = Button(tab2, text='Выйти', command=button_ask10).grid(row=4, column=4)

mainloop()