
def conv_encode(message):
    register = ['0','0','0']
    bits = ['0', '0']
    #message = message.split(' ')
    bits = message + bits
    output1 = 0
    output2 = 0
    output_message = []
    for i in bits:
        register.insert(0, i)
        output1 = int(register[0]) ^ int(register[1]) ^ int(register[2])
        output2 = int(register[0]) ^ int(register[2])
        output_message.append(output1)
        output_message.append(output2)
    print(output_message)
    return(output_message)

#message = '1 1 0'
#print(conv_encode(message))

