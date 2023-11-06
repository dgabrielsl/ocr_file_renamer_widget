import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon, QFont, QCursor
from PyQt6.QtCore import Qt

from wizard import *
from handler import *

class Py_Tesseract(QWidget):
    def __init__(self):
        super().__init__()
        global flag_counter, item_working
        self.flag_counter = 0
        self.item_working = ''
        self.root()
    
    def root(self):
        self.setWindowTitle('Tesseract')
        self.setWindowIcon(QIcon('C:/Users/dgabr/My Drive/Python/a) Laboratorio (ocr)/icon.ico'))
        self.ui()
        self.show()
    
    def ui(self):
        label_files_to_drop = QLabel('Guardar en:')
        label_files_to_drop.setFixedWidth(130)
        button_files_to_drop = QPushButton('Buscar')
        button_files_to_drop.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        button_files_to_drop.clicked.connect(self.dir_to_save_processed_files)
        label_files_to_drop_selected = QLabel('Carpeta seleccionada:')
        label_files_to_drop_selected.setFixedWidth(130)
        self.label_files_to_drop_selected_display = QLabel('-')
        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label_files_to_drop)
        h_layout_1.addWidget(button_files_to_drop)

        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(label_files_to_drop_selected)
        h_layout_2.addWidget(self.label_files_to_drop_selected_display)
        h_layout_2.setContentsMargins(0,0,0,10)

        label_files_to_scan = QLabel('Carpeta a procesar:')
        label_files_to_scan.setFixedWidth(130)
        self.button_files_to_scan = QPushButton('Buscar')
        self.button_files_to_scan.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_files_to_scan.setMinimumWidth(250)
        self.button_files_to_scan.clicked.connect(self.dir_to_get_unprocessed_files)
        self.button_files_to_scan.setDisabled(True)
        label_files_to_scan_selected = QLabel('Carpeta seleccionada:')
        label_files_to_scan_selected.setFixedWidth(130)
        self.label_files_to_scan_selected_display = QLabel('-')
        h_layout_3 = QHBoxLayout()
        h_layout_3.addWidget(label_files_to_scan)
        h_layout_3.addWidget(self.button_files_to_scan)

        h_layout_4 = QHBoxLayout()
        h_layout_4.addWidget(label_files_to_scan_selected)
        h_layout_4.addWidget(self.label_files_to_scan_selected_display)
        h_layout_4.setContentsMargins(0,0,0,20)

        self.button_run_wizzard = QPushButton('Procesar')
        self.button_run_wizzard.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_run_wizzard.clicked.connect(self.run_wizzard)
        self.button_run_wizzard.setDisabled(True)

        display = QVBoxLayout()
        display.setContentsMargins(35,35,35,35)
        display.addLayout(h_layout_1)
        display.addLayout(h_layout_2)
        display.addLayout(h_layout_3)
        display.addLayout(h_layout_4)
        display.addWidget(self.button_run_wizzard)

        self.setLayout(display)

    def dir_to_save_processed_files(self):
        dir_scanner.fn_record_output(self, self.label_files_to_drop_selected_display, self.button_files_to_scan)

    def dir_to_get_unprocessed_files(self):
        dir_scanner.fn_record_input(self, self.label_files_to_scan_selected_display, self.button_run_wizzard)

    def run_wizzard(self):
        # print(f'Guardar en: {self.folder_to_save}')
        # print(f'Ruta para ubicar cada documento: {self.cwd}\n')
        # print(f'Documentos a procesar ({len(self.folder_to_scan)}):')
        # for item in self.folder_to_scan:
        #     print(item)
        HandByItem.fn_next_file(self, self.cwd, self.folder_to_scan, self.folder_to_save)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Py_Tesseract()
    sys.exit(app.exec())