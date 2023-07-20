import cv2 as cv
import re
import os
from pyzbar.pyzbar import decode

folder_path = r"barcodes"

def main():

    files_found = False

    for filename in os.listdir(folder_path):         # Searching a file in root
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            files_found = True                       # The file is real!
            image = cv.imread(filepath)
            detectedBarcodes = decode(image)

            for barcode in detectedBarcodes:
                (x, y, w, h) = barcode.rect

                cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 5)

                data = barcode.data.decode('utf-8')

                clean_data_1 = remover_num(data)  # Saving parts of name
                clean_data_2 = remover_words(data)  # Saving parts of DoB

                print('Your name: ' + clean_data_1)
                print('Your dd/mm/yy: ' + clean_data_2)
                #print(barcode.type)  # CODE128

            cv.imshow("Our Barcode", image)

            cv.waitKey(0)
            cv.destroyAllWindows()

def remover_num(data):
    return re.sub(r'^A-|[\d]+|-Z$', ' ', data)  # Removing every nums

def remover_words(data):
    return re.sub(r'[^\d]', ' ', data)  # Removing every words
