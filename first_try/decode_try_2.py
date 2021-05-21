import numpy as np
import cv2


def decode(adress, key):
    '''
    декодер ключа
    '''
    decode_key = key
    key_array = decode_key.split(",")
    len_text = 0
    if key_array[1][0] == '1':
        len_text = (int(key_array[0]) - int(key_array[1][1:])) * 4
    elif key_array[1][0] == '0':
        len_text = (int(key_array[0]) + int(key_array[1][1:])) * 4

    text_array = []
    key = int(key_array[0])
    bufer_i = 0

    img = cv2.imread(adress)
    image = np.array(img)
    (height, width, c) = image.shape  # это вроде даже не нужно мне
    bufer = []

    # переписывание в обычный массив виды [пиксель1, пиксель2, пиксель3]
    for row in list(image):
        for elem in row:
            bufer.append(elem)

    # карта посещенных пикселей
    map = ['0' for i in range(len(bufer))]
    '''
    карту скорее всего нужно будет удалить, т.к. она не юзается
    '''

    def recurs_func(bufer_i, len_text):
        while bufer_i < len(bufer):
            while len_text > 0:
                for j in range(0, len(map)):
                    if j == bufer_i:
                        if map[j] == '1':
                            # улавливатель бага(если он будет)
                            print("111111111111111111111111111111--------------------1111111")
                        else:
                            #
                            for number in range(len(bufer[bufer_i])):
                                donwload_info(bufer[bufer_i][number])
                                len_text -= 1
                            map[j] = '1'
                    else:
                        continue
                if bufer_i == len(bufer) - 1:
                    bufer_i = key - 1
                    return recurs_func(bufer_i, len_text)
                elif bufer_i + key > len(bufer):
                    bufer_i = bufer_i + key - len(bufer)
                    return recurs_func(bufer_i, len_text)
                else:
                    bufer_i += key
            else:
                break

    def donwload_info(pixel_i):
        bufer_pixel = bin(pixel_i)[2:]
        bufer_pixel = ('0' * (8 - len(str(bufer_pixel))) + str(bufer_pixel))
        if bufer_pixel[-2:] == '00':
            text_array.append(bufer_pixel[-2:])
        elif bufer_pixel[-2:] == '01':
            text_array.append(bufer_pixel[-2:])
        elif bufer_pixel[-2:] == '10':
            text_array.append(bufer_pixel[-2:])
        elif bufer_pixel[-2:] == '11':
            text_array.append(bufer_pixel[-2:])

    recurs_func(bufer_i, len_text)

    bufer_text_array = []

    i = 0
    c = int(len(text_array)/4)
    while i < c * 4:
        s = ''
        for j in range(0, 4):
            # улавливаем ошибку с выходом за пределы масива в последнем трае
            try:
                # попробовать пофиксить выписывание лишних битов, т.к. они не редактировались
                if i + j > c * 4:
                    break
                else:
                    s = s + text_array[i + j]
            except IndexError:
                break
        bufer_text_array.append(chr(int(s, 2)))
        i += 4
    else:
        pass

    return ''.join(bufer_text_array)

