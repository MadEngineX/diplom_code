import pickle

def hamming_weight(a, b):
    weight = int(a) ^ int(b)
    #print('w in f  ' + str(weight))
    weight = str(weight)
    if weight == '11':
        return 2
    elif (weight == '01') or (weight == '10') or (weight == '1'):
        return 1
    else:
        return 0

def  viterby_decode(message):
    bits = []

    for i in range(0, len(message), 2):
        i = int(i)
        bits.append(str(message[i]) + str(message[i+1]))

    a_file = open("dicr_viterby.pkl", "rb")
    diagram = pickle.load(a_file)
    a_file.close()
    new_dict = {}

    for key in diagram:
        h_weight = 0

        for i in range(0, len(key), 2):
            i = int(i)
            couple_in_key = str(key[i]) + str(key[i + 1])
            h_weight = h_weight + hamming_weight(bits[i//2], couple_in_key)
            new_dict[diagram[key]] = h_weight

    print(new_dict)
    ves = 10
    result = 0
    for i in new_dict:
        if (new_dict[i]) < ves:
            ves = int(new_dict[i])
            result = i
    print('answer = ' + result + ' ves = ' + str(ves))

    return bits, result, ves

message = [1, 1, 1, 0, 0, 0, 1, 0, 1, 1]
print(viterby_decode(message))

print()