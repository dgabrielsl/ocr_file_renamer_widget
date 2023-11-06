import os, fitz, pytesseract
from PIL import Image

class HandByItem():
    def __init__(self):
        self.fn_next_file()

    def fn_next_file(self, cwd, folder_to_scan, folder_to_save):
        zoom_x = 4.0
        zoom_y = 4.0
        self.counter = 1
        self.to_ocr = []

        for item in folder_to_scan:

            title_folder = item.replace('.pdf', '')
            print(f'Creando carpeta... {folder_to_save}/{title_folder}')
            try: os.makedirs(f'{folder_to_save}/{title_folder}')
            except Exception as e: print(e)

            doc = fitz.open(f'{cwd}/{item}')
            for d in doc:
                print(f'\tCreando JPG... {folder_to_save}/{title_folder}/{self.counter}.jpg')
                self.to_ocr.append(f'{folder_to_save}/{title_folder}/{self.counter}.jpg')
                mat = fitz.Matrix(zoom_x, zoom_y)
                pix = d.get_pixmap(matrix=mat)
                new_img = f'{folder_to_save}/{title_folder}/{self.counter}.jpg'
                pix.save(new_img)
                self.counter += 1

            self.counter = 1
            print()

            # print(f'\t\tPyTesseract... {title_folder}/{self.counter}.jpg')
            # raw_text = str(((pytesseract.image_to_string(Image.open(new_img)))))
            # text_to_lines = raw_text.split('\n')
            # print(f'\t\t\t[Texto generado]\n')

        # print(self.to_fitz)
        # print(self.new_folders)
        # print(self.to_ocr)

        print('El programa ha finalizado')


