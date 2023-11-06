import os, fitz, pytesseract
from PIL import Image

os.system('cls')

pdf_file = 'C:/Users/dgabr/Cloud/Python/OCR/kyc2.pdf'
pdf_savein = 'C:/Users/dgabr/Cloud/Python/OCR/'
savin = pdf_file.split('/')
title = savin.pop()
title = title.replace('.pdf','')
savin = '/'.join(savin)

doc = fitz.open(pdf_file)

zoom_x = 4.0
zoom_y = 4.0

pix = doc[0].get_pixmap()
mat = fitz.Matrix(zoom_x, zoom_y)
pix = doc[0].get_pixmap(matrix=mat)
pix.save(f'{savin}/{title}.jpg')

file_name = 'C:/Users/dgabr/Cloud/Python/OCR/kyc2.jpg'

global raw_text, text_to_lines, crafted_text, required_text
raw_text = ''; text_to_lines = ''; crafted_text = ''; required_text = []

def wizzard():
    raw_text = str(((pytesseract.image_to_string(Image.open(file_name)))))
    print(raw_text)
    text_to_lines = raw_text.split('\n')
    crafted_text = []
    for line in text_to_lines:
        if line != '': crafted_text.append(f'{line}')
    fullname = []
    for line in crafted_text:
        _line_ = line.upper()
        if _line_.__contains__('PRODUCTO') and _line_.__contains__('PAGAR'):
            _line_ = line.split(' ')
            _line_ = _line_.pop()
            required_text.append(_line_)
        if _line_.__contains__('FECHA') and _line_.__contains__('VENDEDOR'):
            _line_ = line.split(' ')
            _line_ = _line_[2:4]
            _line_ = ' '.join(_line_)
            required_text.append(_line_)
        if _line_.__contains__('PRIMER') and _line_.__contains__('SEGUNDO'):
            _line_ = line.split(' ')
            fullname = []
            for l in _line_:
                l = l.upper()
                if l != 'PRIMER' and l != 'NOMBRE' and l != 'SEGUNDO' and l != 'APELLIDO': fullname.append(l)
            fullname = ' '.join(fullname)
            required_text.append(fullname)
        if _line_.__contains__('TIPO') and _line_.__contains__('IDENTIDAD'):
            _line_ = line.split(' ')
            _line_ = _line_[3]
            required_text.append(_line_)
    doc.close()
    print(required_text)

    img = Image.open('C:/Users/dgabr/Cloud/Python/OCR/kyc2.jpg')
    img = img.convert('RGB')
    img.close()
    # os.rename(pdf_file, f'C:/Users/dgabr/Cloud/Python/OCR/KYC 2 {required_text[-1]} {required_text[-2]} {required_text[1]}.pdf')
    # os.remove('C:/Users/dgabr/Cloud/Python/OCR/kyc2.jpg')

wizzard()
