
def iter_code(message):
    check_bits1 = []
    for j in range(len(message)):
        check_bit = int(message[0][j]) ^ int(message[1][j]) ^ int(message[2][j])
        check_bits1.append(check_bit)
    check_bits2 = []
    for i in range(len(message)):
        check_bit = int(message[i][0]) ^ int(message[i][1]) ^ int(message[i][2])
        check_bits2.append(check_bit)
    message.append(check_bits1)
    message.append(check_bits2)
    k = [str(x) for x in message[3]]
    t = [str(x) for x in message[4]]
    k = "".join(k)
    k = str(k)
    message[3] = k
    t = "".join(t)
    t = str(t)
    message[4] = t
    #print(message)
    return message

def iter_decode(message):
    check = iter_code(message[:-2])
    print("message " + str(message))
    print("check " + str(check))
    if (message[3] != check[3]) or (message[4] != check[4]):
        print('Есть ошибки')
        x_of_error = 0
        y_of_error = 0
        for i in range(3):
            if (message[4][i] != check[4][i]):
                x_of_error = i
        for j in range(3):
            if (message[3][j] != check[3][j]):
                y_of_error = j

        print("position of error: " + str(x_of_error) + str(y_of_error))
        if message[x_of_error][y_of_error] == str(0):
            message[x_of_error] = message[x_of_error][:y_of_error] + str(1) + message[x_of_error][y_of_error + 1:]
        else:
            message[x_of_error] = message[x_of_error][:y_of_error] + str(0) + message[x_of_error][y_of_error + 1:]
        print("Исправленное сообщение" + str(message))
        return(str(message))
    else:
        print('Ошибок нет')
        return (str(message))
#message_in = ["101",
#              "011",
#              "110"]
message_in = ['101', '011', '110', '000', '000']
iter_decode(message_in)