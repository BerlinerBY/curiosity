import numpy as np
import cv2
from textwrap import wrap
from PyQt5.QtCore import QThread, pyqtSignal
import RSA_encoder
import pretty_errors


class HideScript(QThread):

    def __init__(self, path, save_path, message):
        super(HideScript, self).__init__()

        self.path = path
        self.save_path = save_path
        self.message = message

    count_percent = pyqtSignal(int)
    global_extraction_key = pyqtSignal(str)
    global_rsa_key = pyqtSignal(str)

    def run(self):
        encrypt_rsa_text, rsa_key = RSA_encoder.RSA(self.message)
        count = 15
        self.count_percent.emit(count)

        extraction_key, count = self.hide('%s' % self.path, '%s' % encrypt_rsa_text, '%s' % self.save_path, count)

        self.global_rsa_key.emit(rsa_key)
        self.global_extraction_key.emit(extraction_key)

        count = count + 5
        self.count_percent.emit(count)

    def hide(self, address, text, save_address, count):
        """
        address - it is path of container for changing bytes
        text - it is message from user. the script will process it and convert it to bit form
        save_address - it is path, name and format of saved image
        """
        text_array = np.array([bin(ord(elem))[2:] for elem in text], dtype=object)

        for i in range(len(text_array)):
            if len(text_array[i]) < 8:
                text_array[i] = (str('0' * (8 - len(text_array[i])))) + str(text_array[i])
            else:
                continue

        redaction_text_array = np.array(['+'], dtype=object)

        for elem in text_array:
            if redaction_text_array[0] == '+':
                redaction_text_array = np.delete(redaction_text_array, 0)
                element = wrap(elem, 2)
                redaction_text_array = np.concatenate((redaction_text_array, element), axis=0)
            else:
                element = wrap(elem, 2)
                redaction_text_array = np.concatenate((redaction_text_array, element), axis=0)

        def Eratosfen(n):
            # Sieve of Eratosthenes
            mass = [2]
            m = int((n - 1) / 2)
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

        count = count + 10
        self.count_percent.emit(count)

        '''open image and manipulation of bytes in pixels'''
        img = cv2.imread(address)
        image = np.array(img)
        height, width, depth = image.shape

        result_mass = Eratosfen(int((height * width * 7) / 20))  # find
        step_key = result_mass[-1]

        variable_for_recursion = 0

        copy_image = np.copy(np.nditer(image))  # make 1D array from 3D

        count = count + 20
        self.count_percent.emit(count)

        def lsb(functions_value, elem):
            value = bin(functions_value)[2:]  # 127 -> 1111 111
            value = ('0' * (8 - len(str(value))) + str(value))  # 1111 111 -> 0111 1111
            if value[-2:] == '01':
                value = bin(int(str(value), 2) - 1)[2:]
            elif value[-2:] == '10':
                value = bin(int(str(value), 2) - 2)[2:]
            elif value[-2:] == '11':
                value = bin(int(str(value), 2) - 3)[2:]  # 111 1100
            else:
                pass
            value = ('0' * (8 - len(str(value))) + str(value))  # 0111 1100 mb i can delete this string
            # (0111 1100) + (elem from stack = 01) = 0111 1101
            return int(bin(int(str(value), 2) + int(str(elem), 2))[2:], 2)

        for elem in redaction_text_array:
            copy_image[variable_for_recursion] = lsb(copy_image[variable_for_recursion], elem)
            if variable_for_recursion + step_key <= len(copy_image):
                variable_for_recursion += step_key
            elif variable_for_recursion + step_key > len(copy_image):
                variable_for_recursion = variable_for_recursion + step_key - len(copy_image)

        count = count + 20
        self.count_percent.emit(count)

        cv2.imwrite(save_address,
                    np.copy(copy_image.reshape(height, width, depth)))  # make 3D array and save modified image

        count = count + 20
        self.count_percent.emit(count)

        def recovery_key():
            # recovery key = "step_key,(0\1)(step_key-len(redaction_text_array)"
            difference = step_key - len(redaction_text_array)
            if difference < 0:
                result_key = ',0'.join([str(step_key), str(abs(difference))])
            else:
                result_key = ',1'.join([str(step_key), str(abs(difference))])
            return result_key

        count = count + 10
        self.count_percent.emit(count)

        return recovery_key(), count
