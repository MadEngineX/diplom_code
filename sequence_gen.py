import random  ## Импорт библиотеки для генератора ошибок

def generate_sec(len):
    bits = [random.randint(0, 1) for _ in range(int(len))]
    bits = [int("".join(map(str, bits)))]
    return bits


print(generate_sec(300))