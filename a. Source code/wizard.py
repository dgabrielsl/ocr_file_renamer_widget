import os
from PyQt6.QtWidgets import QMessageBox, QFileDialog

os.system('cls')

class dir_scanner():
    def __init__(self):
        self.fn_record_output()
        self.fn_record_input()

    def fn_record_output(self, label_files_to_drop_selected_display, button_files_to_scan):
        self.folder_to_save = QFileDialog.getExistingDirectory(self, 'Guardar documentos procesados en')
        if self.folder_to_save != '':
            label_files_to_drop_selected_display.setText(self.folder_to_save)
            button_files_to_scan.setDisabled(False)
        else:
            label_files_to_drop_selected_display.setText('-')
            button_files_to_scan.setDisabled(True)
            QMessageBox.information(self, 'PyTesseract - warning', 'You must tell PyTesseract the folder where to save the processed files in order to continue.', QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)

    def fn_record_input(self, label_files_to_scan_selected_display, button_run_wizzard):
        self.cwd = '-'
        self.folder_to_scan = ''
        button_run_wizzard.setDisabled(True)
        self.folder_to_scan = QFileDialog.getExistingDirectory(self, 'Buscar carpeta con los documentos a procesar')
        if self.folder_to_scan != '':
            self.cwd = self.folder_to_scan
            button_run_wizzard.setDisabled(False)
            self.folder_to_scan = os.listdir(self.folder_to_scan)
        else:
            label_files_to_scan_selected_display.setText(self.cwd)
            QMessageBox.information(self, 'PyTesseract - warning', 'You must tell PyTesseract the folder where the subdirectories or documents to be processed are located.', QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
        label_files_to_scan_selected_display.setText(self.cwd)
