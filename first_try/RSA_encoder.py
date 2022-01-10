import random
import preparation_of_numbers

revers_dict_rus_en = {'!': 100, '"': 101, '#': 102, '$': 103, '%': 104, '&': 105, "'": 106, '(': 107, ')': 108,
                      '*': 109, '+': 110, ',': 111, '-': 112, '.': 113, '/': 114, '0': 115, '1': 116, '2': 117,
                      '3': 118, '4': 119, '5': 120, '6': 121, '7': 122, '8': 123, '9': 124, ':': 125, ';': 126,
                      '<': 127, '=': 128, '>': 129, '?': 130, '@': 131, 'A': 132, 'B': 133, 'C': 134, 'D': 135,
                      'E': 136, 'F': 137, 'G': 138, 'H': 139, 'I': 140, 'J': 141, 'K': 142, 'L': 143, 'M': 144,
                      'N': 145, 'O': 146, 'P': 147, 'Q': 148, 'R': 149, 'S': 150, 'T': 151, 'U': 152, 'V': 153,
                      'W': 154, 'X': 155, 'Y': 156, 'Z': 157, '[': 158, '\\': 159, ']': 160, '^': 161, '_': 162,
                      '`': 163, 'a': 164, 'b': 165, 'c': 166, 'd': 167, 'e': 168, 'f': 169, 'g': 170, 'h': 171,
                      'i': 172, 'j': 173, 'k': 174, 'l': 175, 'm': 176, 'n': 177, 'o': 178, 'p': 179, 'q': 180,
                      'r': 181, 's': 182, 't': 183, 'u': 184, 'v': 185, 'w': 186, 'x': 187, 'y': 188, 'z': 189,
                      '{': 190, '|': 191, '}': 192, 'А': 193, 'Б': 194, 'В': 195, 'Г': 196, 'Д': 197, 'Е': 198,
                      'Ж': 199, 'З': 200, 'И': 201, 'Й': 202, 'К': 203, 'Л': 204, 'М': 205, 'Н': 206, 'О': 207,
                      'П': 208, 'Р': 209, 'С': 210, 'Т': 211, 'У': 212, 'Ф': 213, 'Х': 214, 'Ц': 215, 'Ч': 216,
                      'Ш': 217, 'Щ': 218, 'Ъ': 219, 'Ы': 220, 'Ь': 221, 'Э': 222, 'Ю': 223, 'Я': 224, 'а': 225,
                      'б': 226, 'в': 227, 'г': 228, 'д': 229, 'е': 230, 'ж': 231, 'з': 232, 'и': 233, 'й': 234,
                      'к': 235, 'л': 236, 'м': 237, 'н': 238, 'о': 239, 'п': 240, 'р': 241, 'с': 242, 'т': 243,
                      'у': 244, 'ф': 245, 'х': 246, 'ц': 247, 'ч': 248, 'ш': 249, 'щ': 250, 'ъ': 251, 'ы': 252,
                      'ь': 253, 'э': 254, 'ю': 255, 'я': 256, ' ': 257, '–': 258, '‘': 259, '’': 260, "“": 261,
                      '”': 262}


def word_processing(text):
    text = ''.join([str(revers_dict_rus_en.get(elem)) for elem in text])
    mass_block = []

    start_i = 0
    bol = True
    while bol:
        while start_i <= len(text):
            i = random.randint(3, 10)
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
