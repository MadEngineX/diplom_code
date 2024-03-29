from tkinter import * ##Импорт библиотек для графической оболояки
from tkinter.ttk import *
import matplotlib.pyplot as plt ## Импорт библиотек для построения графиков
import random  ## Импорт библиотеки для генератора ошибок
from coders.convolutation_coder import conv_encode ## Импорт самописных модулей для кодирования
from coders.virerby_decoder import viterby_decode
from coders.iter_coder import iter_code, iter_decode
from errors_counter import errors_count
from approximation import approximate

# Создание и конфигурация рабочего окна
window = Tk()
window.rowconfigure([0, 1, 2, 3, 4, 5], minsize=50)
window.columnconfigure([0, 1, 2, 3, 4], minsize=50)
Label(window, text="Введите входную последоватеьность    ").grid(row=0, column=0)
entry = Entry(window)
entry.insert(END, 1011001100000001110011001000001011100100110110101)
#entry.insert(END, 101100110001100110100111010000100100101001111110001110000010100010000110100001001111110111110101111111110000000111111010100111100100111001001100000100000111001010000010000111011111100100001101011000111010010001110111001011010101000000000111101011110000000110111101001010111111101110101110101001)
entry.grid(row=1, column=0)
#Label(window, text="Выберите способ кодирования"    ).grid(row=0, column=1)
var = IntVar()
var.set(1)
svert = Radiobutton(window, text="Сверточный код",
                    variable=var, value=0)
iter = Radiobutton(window, text="Итеративный код",
                   variable=var, value=1)
#svert.grid(row=1, column=1)
#iter.grid(row=2, column=1)
Label(window, text="Введите число битовых ошибок    ").grid(row=0, column=2)
entry2 = Entry(window)
entry2.insert(END, 100)
entry2.grid(row=1, column=2)
Label(window, text="Введите число экспериментов    ").grid(row=0, column=3)
entry3 = Entry(window)
entry3.insert(END, 10)
entry3.grid(row=1, column=3)
def button_ask1():
    window.destroy()
def button_ask2():
    global input_bits
    global sequence_count
    global input_coder
    global bits_error
    global experiments_count
    experiments_count = entry3.get()
    bits_error = entry2.get()

    bits_error_for_cycle = int(bits_error)
    print(bits_error_for_cycle)
    experiments_count_cycle = int(experiments_count)
    sequence_count = 0
    input_bits = entry.get()
    if var.get() == 0:
        input_coder = 'Сверточный код'
    elif var.get() == 1:
        input_coder = 'Итеративный код'
    if len(input_bits) % 3 == 1:
        input_bits = input_bits + '00'
    elif len(input_bits) % 3 == 2:
        input_bits = input_bits + '0'
    for i in range(0, len(input_bits), 3):
        sequence_count += 1


    x_axes = []
    y_axes = []
    ss = []
    n = 0
    for j in range(bits_error_for_cycle):
        y = 0
        n+=1
        print(j)
        for t in range(experiments_count_cycle):
            print(t)
            try:
                sequences_of_input_bits_for_code = []
                for i in range(0, len(input_bits), 3):
                    seq = str(input_bits[i]) + str(input_bits[i+1]) + str(input_bits[i+2])
                    sequences_of_input_bits_for_code.append(seq)
                #print('seq++ ' + str(sequences_of_input_bits_for_code))
                bits_encode_sequence = []
                for i in sequences_of_input_bits_for_code:
                    #print(i)
                    sequence_of_input_bits = i
                    sequence_of_input_bits_for_code = []
                    sequence_of_input_bits_for_code.append(str(sequence_of_input_bits[0]))
                    sequence_of_input_bits_for_code.append(str(sequence_of_input_bits[1]))
                    sequence_of_input_bits_for_code.append(str(sequence_of_input_bits[2]))
                    bits = sequence_of_input_bits_for_code
                    bits_encode = ''

                    bits_encode = conv_encode(bits)
                    bits_encode_sequence += bits_encode
                    #print(bits_encode)
                #print(bits_encode_sequence)
                if j != '0':
                    for i in range(int(j)):
                        error_in_bit = random.randint(0, len(bits_encode_sequence)-1)
                        #print('j ' + str(j) + ' error_in_bit: ' + str(error_in_bit))
                        #print(error_in_bit)
                        if bits_encode_sequence[error_in_bit] == '1':
                            bits_encode_sequence[error_in_bit] = 0
                        else:
                            bits_encode_sequence[error_in_bit] = 1
                #print(bits_encode_sequence)
                sequences_of_output_bits_of_encode = []
                for i in range(0, len(bits_encode_sequence), 10):
                    seq = str(bits_encode_sequence[i]) + \
                          str(bits_encode_sequence[i + 1]) + \
                          str(bits_encode_sequence[i + 2]) + \
                          str(bits_encode_sequence[i + 3]) + \
                          str(bits_encode_sequence[i + 4]) + \
                          str(bits_encode_sequence[i + 5]) + \
                          str(bits_encode_sequence[i + 6]) + \
                          str(bits_encode_sequence[i + 7]) + \
                          str(bits_encode_sequence[i + 8]) + \
                          str(bits_encode_sequence[i + 9])
                    sequences_of_output_bits_of_encode.append(seq)

                decoded_bits = []
                for seq in sequences_of_output_bits_of_encode:
                    decoded_bits += str(viterby_decode(seq))
                #количество ошибок
                count_of_errors = errors_count(input_bits, decoded_bits)
                #print(count_of_errors)
                y+= (count_of_errors)
            except Exception as e:
                print(e)
                y+=0
        #print(j)
        x_axes.append(n)
        #print(y)
        ss.append(y)
        #y_axes.append(y/experiments_count_cycle/10)
        y_axes.append(y / experiments_count_cycle / len(input_bits))
    # plt.title('Эффективность кодера')
    # plt.plot(x_axes, y_axes, 'ro')
    # plt.show()

    approximate(x_axes, y_axes)
    plt.title('Сравнение эффективности кодеров')
    plt.ylabel('Коэффициент битовых ошибок ( BER )')
    plt.xlabel('Количество ошибок')
    plt.plot(x_axes, y_axes, 'b.')



    x_axes = []
    y_axes = []
    ii = []
    n = 0
    bits_n = []
    sequence_count = 0

    if len(input_bits) % 9 == 0:
        input_bits = input_bits
    elif len(input_bits) % 9 == 8:
        input_bits = input_bits + '0'
    elif len(input_bits) % 9 == 7:
        input_bits = input_bits + '00'
    elif len(input_bits) % 9 == 6:
        input_bits = input_bits + '000'
    elif len(input_bits) % 9 == 5:
        input_bits = input_bits + '0000'
    elif len(input_bits) % 9 == 4:
        input_bits = input_bits + '00000'
    elif len(input_bits) % 9 == 3:
        input_bits = input_bits + '000000'
    elif len(input_bits) % 9 == 2:
        input_bits = input_bits + '0000000'
    elif len(input_bits) % 9 == 1:
        input_bits = input_bits + '00000000'

    for i in range(0, len(input_bits), 9):
        sequence_count += 1

    for i in range(0, len(input_bits), 3):
        troika = str(input_bits[i]) + str(input_bits[i+1]) +  str(input_bits[i+2])
        bits_n.append(troika)

    for j in range(bits_error_for_cycle):
        y = 0
        n+=1
        for t in range(experiments_count_cycle):
            bits_encode = []
            sequence_of_input_bits_for_code = []
            for i in range(0, len(bits_n), 3):
                troika = []
                troika.append(str(bits_n[i]))
                troika.append(str(bits_n[i+1]))
                troika.append(str(bits_n[i+2]))

                bits_encode+=(iter_code(troika))
            #print(bits_encode)
            bits_for_error = []
            for ut in bits_encode:
                bits_for_error+=ut
            #print(bits_for_error)
            #print(len(bits_for_error))
            if j != '0':
                for i in range(int(j)):
                    #print(i)
                    error_in_bit = random.randint(0, len(bits_for_error)-1)
                    #print('error_in_bit: ' + str(error_in_bit))
                    #print('bits_for_error ' + str(bits_for_error))
                    #print('len(bits_for_error) ' + str(len(bits_for_error)))
                    if bits_for_error[error_in_bit] == '1':
                        bits_for_error[error_in_bit] = 0
                    else:
                        bits_for_error[error_in_bit] = 1
            #print(bits_for_error)
            bit_for_decode = []
            for i in range(0, len(bits_for_error), 3):
                troika = str(bits_for_error[i]) + str(bits_for_error[i + 1]) + str(bits_for_error[i + 2])
                bit_for_decode.append(troika)
            #print('bit_for_decode')
            #print(bit_for_decode)

            bits_decode = []
            for i in range(0, len(bit_for_decode), 5):
                five = []
                five.append(str(bit_for_decode[i]))
                five.append(str(bit_for_decode[i+1]))
                five.append(str(bit_for_decode[i+2]))
                five.append(str(bit_for_decode[i + 3]))
                five.append(str(bit_for_decode[i + 4]))

                bits_decode+=(iter_decode(five))
                #print(bits_decode)
            #print(bits_decode)
            words = []
            filtered = [v for v in bits_decode if v.startswith('1') or v.startswith('0')]
            #print(filtered)
            bits_decode_out = []
            for m in range(0, len(filtered), 15):
                bits_decode_out+=str(filtered[m])+str(filtered[m+1])+str(filtered[m+2])+str(filtered[m+3])+str(filtered[m+4])+str(filtered[m+5])+str(filtered[m+6])+str(filtered[m+7])+str(filtered[m+8])
            #print('deca' + str(bits_decode_out))
            bits_decode_for_compare = []
            bits_decode_for_compare = [int("".join(map(str, bits_decode_out)))]

            #print('____')
            #print(bits_decode_for_compare)
            #print(input_bits)
            #print(errors_count(input_bits,str(bits_decode_for_compare[0])))
            y += errors_count(input_bits,str(bits_decode_for_compare[0]))
        # print(j)
        x_axes.append(n)
        #print(y)
        #print(experiments_count_cycle)

        ii.append(y)
        print(ii)
        #y_axes.append(y / experiments_count_cycle/10)
        y_axes.append(y / experiments_count_cycle / len(input_bits))
    for i in range(0,len(y_axes)):
        if (y_axes[i] == 0) and (i<len(y_axes)-1) and (i>5):
            y_axes[i] = (y_axes[i-1] + y_axes[i+1])/2

    print('svert' + str(ss))
    print('iter' + str(ii))
    approximate(x_axes, y_axes)
    #plt.title('Эффективность итеративного кода')
    plt.ylabel('Коэффициент битовых ошибок ( BER )')
    plt.xlabel('Количество ошибок')
    plt.plot(x_axes, y_axes, 'r.')
    plt.show()

    return
button1 = Button(window, text='Выйти', command=button_ask1).grid(row=4, column=4)
button2 = Button(window, text='Запустить моделирование', command=button_ask2).grid(row=4, column=2)

mainloop()
