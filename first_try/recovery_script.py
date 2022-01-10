import numpy as np
import cv2


def decode(address, key):
    """
    address - it is path of stegocontainer with our information
    key - it is for extracting hidden information from stegocontainer
    """
    decode_key = key
    key_array = decode_key.split(",")
    len_text = 0
    if key_array[1][0] == '1':
        len_text = (int(key_array[0]) - int(key_array[1][1:]))
    elif key_array[1][0] == '0':
        len_text = (int(key_array[0]) + int(key_array[1][1:]))

    img = cv2.imread(address)
    image = np.array(img)

    copy_image = np.copy(np.nditer(image))  # make 1D array from 3D

    text_array = []
    step_key = int(key_array[0])
    variable_for_recursion = 0

    def download_info(value):
        binary_value = ('0' * (8 - len(str(bin(value)[2:]))) + str(bin(value)[2:]))
        if binary_value[-2:] == '00':
            text_array.append(binary_value[-2:])
        elif binary_value[-2:] == '01':
            text_array.append(binary_value[-2:])
        elif binary_value[-2:] == '10':
            text_array.append(binary_value[-2:])
        elif binary_value[-2:] == '11':
            text_array.append(binary_value[-2:])

    run = True
    while run:
        if len(text_array) < len_text:
            download_info(copy_image[variable_for_recursion])
            if variable_for_recursion + step_key <= len(copy_image):
                variable_for_recursion += step_key
            elif variable_for_recursion + step_key > len(copy_image):
                variable_for_recursion += step_key - len(copy_image)
        else:
            run = False

    bufer_text_array = []

    i = 0
    while i < len(text_array):
        string = ""
        for j in range(4):
            string += text_array[i + j]
        bufer_text_array.append(chr(int(string, 2)))
        i += 4

    return ''.join(bufer_text_array)
