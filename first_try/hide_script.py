import numpy as np
import cv2

"""
Конечено прикол с помещением всего алгоритма в функцию сработал,
но лучше попробовать переписать код 
"""
def encrypt(adress, text, save_adress):
    """
    Участок для работы с введенной фразой
    """
    # перевод в ASCII, затем в бинарку
    text = text
    text_array = [bin(ord(elem))[2:] for elem in text]

    # проверка на четность символов в бинарном варианте/ и подгонка под 8 знаков
    for i in range(len(text_array)):
        if len(text_array[i]) < 8:
            text_array[i] = ('0' * (8 - len(text_array[i]))) + str(text_array[i])
        else:
            continue

    # редактрируем массив фразы из '01001000' в ['01', '00', '10', '00']
    redaction_text_array = []
    for i in range(len(text_array)):
        for j in range(len(text_array[i])):
            if j % 2 == 0:
                redaction_text_array.append(text_array[i][j] + text_array[i][j + 1])
            else:
                continue

    # реверс массива фразы для превращения его в стек
    c = len(redaction_text_array)
    stec_text_array = []
    for i in range(c):
        stec_text_array.append(redaction_text_array.pop())

    """
    Решето Эратосфена
    """
    mass = [2]

    def Eratosfen(n):
        m = (n - 1) // 2  # // - целочисленное деление
        b = [True] * m
        i, p = 0, 3
        while p * p < n:
            if b[i]:
                mass.append(p)
                j = 2 * i * i + 6 * i + 3
                while j < m:
                    b[j] = False
                    j = j + 2 * i + 3
            i += 1
            p += 2
        while i < m:
            if b[i]:
                mass.append(p)
            i += 1
            p += 2
        return mass

    """
    Участок с обработкой изображения
    """

    img = cv2.imread(adress)
    image = np.array(img)
    (height, width, c) = image.shape
    bufer = []

    z = Eratosfen(int((height * width * 7) / 20))

    key = mass[-1]  # ключ_шаг
    bufer_i = 0  # переменная для рекурсии

    # переписывание в обычный массив виды [пиксель1, пиксель2, пиксель3]
    for row in list(image):
        for elem in row:
            bufer.append(elem)

    # карта посещенных пикселей
    map = ['0' for i in range(len(bufer))]
    '''
    карту скорее всего нужно будет удалить, т.к. она не юзается
    '''

    # рекурсивная функция для обхода массива
    def func(bufer_i):
        try:
            while bufer_i < len(bufer):
                for j in range(0, len(map)):
                    if j == bufer_i:
                        if map[j] == '1':
                            # улавливатель бага(если он будет)
                            print("111111111111111111111111111111--------------------1111111")
                        else:
                            # вызов функции с обработкой значений
                            bufer[bufer_i][0] = magic_in_pixel(bufer[bufer_i][0])
                            bufer[bufer_i][1] = magic_in_pixel(bufer[bufer_i][1])
                            bufer[bufer_i][2] = magic_in_pixel(bufer[bufer_i][2])
                            map[j] = '1'
                    else:
                        continue
                if bufer_i == len(bufer) - 1:
                    bufer_i = key - 1
                    return func(bufer_i)
                elif bufer_i + key > len(bufer):
                    bufer_i = bufer_i + key - len(bufer)
                    return func(bufer_i)
                else:
                    bufer_i += key
        except IndexError:
            pass

    # функция для работы с пикселем
    def magic_in_pixel(pixel_i):
        bufer_pixel = bin(pixel_i)[2:]
        if len(bufer_pixel) < 8:
            bufer_pixel = ('0' * (8 - len(str(bufer_pixel))) + str(bufer_pixel))
            if bufer_pixel[-2:] == '00':
                pass
            elif bufer_pixel[-2:] == '01':
                bufer_pixel = bin(int(str(bufer_pixel), 2) - 1)[2:]
            elif bufer_pixel[-2:] == '10':
                bufer_pixel = bin(int(str(bufer_pixel), 2) - 2)[2:]
            elif bufer_pixel[-2:] == '11':
                bufer_pixel = bin(int(str(bufer_pixel), 2) - 3)[2:]
            bufer_pixel = ('0' * (8 - len(str(bufer_pixel))) + str(bufer_pixel))
        else:
            if bufer_pixel[-2:] == '00':
                pass
            elif bufer_pixel[-2:] == '01':
                bufer_pixel = bin(int(str(bufer_pixel), 2) - 1)[2:]
            elif bufer_pixel[-2:] == '10':
                bufer_pixel = bin(int(str(bufer_pixel), 2) - 2)[2:]
            elif bufer_pixel[-2:] == '11':
                bufer_pixel = bin(int(str(bufer_pixel), 2) - 3)[2:]
            bufer_pixel = ('0' * (8 - len(str(bufer_pixel))) + str(bufer_pixel))
        bufer_pixel = int(bin(int(str(bufer_pixel), 2) + int(str(stec_text_array.pop()), 2))[2:], 2)
        return bufer_pixel

    func(bufer_i)

    final_array = []
    k = 0
    while k < len(bufer):
        for i in range(height):
            arr = []
            for j in range(width):
                arr.append(bufer[k])
                k += 1
            final_array.append(arr)

    last = np.array(final_array)

    def key_text():
        raznica = key - len(text_array)
        last_key = ''
        if raznica < 0:
            last_key = ',0'.join([str(key), str(raznica)])
        elif raznica >= 0:
            last_key = ',1'.join([str(key), str(raznica)])
        return last_key

    cv2.imwrite(save_adress, last)  # сохранение картинки

    return key_text()
