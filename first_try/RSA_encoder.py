import random
import preparation_of_numbers


def word_processing(text):
    # заменяем символы согласно словарю на их числовой эквивалент,
    # а затем сливаем все в одну строку
    text = ''.join(['1' + str('0' * (5 - len(str(ord(elem)))) + str(ord(elem))) for elem in text])
    mass_block = []

    start_i = 0
    bol = True
    while bol:
        while start_i <= len(text):
            i = random.randint(3, 10)
            # а затем разбиваем на рандомные кусочки длинной от 3 до 10 и добавляем 1 в качестве примеси
            if start_i == len(text):
                bol = False
                break
            elif start_i + i > len(text):
                mass_block.append('1' + text[start_i:])
                bol = False
                break
            else:
                mass_block.append('1' + text[start_i: start_i + i])
                start_i = start_i + i
        else:
            bol = False

    return mass_block


def encode(text_mass, e, n):
    array = []
    for elem in text_mass:
        array.append(str(pow(int(elem), e, n)))

    return array


def rsa_key(mass):
    raznica = mass[-1] - mass[1]
    last_key = ''
    if raznica < 0:
        last_key = ',0'.join([str(mass[-1]), str(raznica)])
    elif raznica >= 0:
        last_key = ',1'.join([str(mass[-1]), str(raznica)])
    return last_key


def RSA(text):
    text_mass = word_processing(text)
    mass_edn = preparation_of_numbers.main_func()

    encode_text = encode(text_mass, mass_edn[0], mass_edn[2])

    encode_key = rsa_key(mass_edn)

    return ' '.join(encode_text), encode_key
