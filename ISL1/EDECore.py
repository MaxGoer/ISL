from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from EDEui import Ui_MainWindow as EDEui
import Codec
from random import randint
from pathlib import Path


def show_error(e: str):
    ###
    # Show error message

    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setWindowTitle('Error')
    msg.setText(e)
    msg.exec_()


class EDECore(EDEui):
    key = 0

    def setup_callbacks(self):
        # connect callbacks with buttons

        self.input.textChanged.connect(self.cypher_callback)
        self.decrypt_mode.clicked.connect(self.switch_mode_callback)
        self.encrypt_mode.clicked.connect(self.switch_mode_callback)
        self.enable_encrypting_cb.clicked.connect(self.cypher_callback)

        self.code_rb.clicked.connect(self.cypher_callback)
        self.char_rb.clicked.connect(self.cypher_callback)

        self.rand_b.clicked.connect(self.rand_b_callback)
        self.key_input.textChanged.connect(self.set_key_callback)
        self.key_input.setValidator(QtGui.QIntValidator())

        # Connect with file menu
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)

    def switch_mode_callback(self):
        if self.encrypt_mode.isChecked():
            self.output_box.setTitle('Encrypted')
        elif self.decrypt_mode.isChecked():
            self.output_box.setTitle('Decrypted')

        self.key = 0
        self.key_input.setText(str(self.key))
        self.cypher_callback()

    def cypher_callback(self):
        # cypher here
        if not self.enable_encrypting_cb.isChecked():
            return

        try:
            cypher = self.input.toPlainText()

            if self.encrypt_mode.isChecked():
                cypher = Codec.encrypt(cypher, self.key)
            elif self.decrypt_mode.isChecked():
                cypher = Codec.decrypt(cypher, self.key)
            if self.code_rb.isChecked():
                cypher = Codec.DELIMITER.join(str(ord(ch)) for ch in cypher)

            self.output.setPlainText(cypher)

        except Exception as e:
            show_error(str(e))
            pass

    def set_key_callback(self):
        new_key = self.key_input.text()

        try:
            self.key = int(new_key, base=10) if new_key is not '' else 0
            self.cypher_callback()
        except Exception as e:
            self.key = 0
            #show_error(str(e))

    def rand_b_callback(self):
        # random value in settings

        if self.encrypt_mode.isChecked():
            self.key = randint(0, 4095)
        elif self.decrypt_mode.isChecked():
            self.key = randint(-4096, 0)

        self.key_input.setText(str(self.key))
        self.cypher_callback()

    # Fileo added
    def __check_path(self, path: str):
        return True if path not in ('', None) and Path(path).exists() and Path(path).resolve().suffix == '.txt' else False
    
    def open_file(self):
        path = QFileDialog.getOpenFileName()
        
        if self.__check_path(path[0]):
            try:
                with open(path[0], 'r') as f:
                    self.input.setPlainText(f.read())
            except:
                pass

    def save_file(self):
        path = QFileDialog.getSaveFileName(filter='.txt', initialFilter='.txt')

        print(path)
        
        #if self.__check_path(path[0]):
        if path[0] not in ('', None):
            #if Path(path[0]).resolve().suffix != '.txt':
                #path[0] += '.txt'
                
            with open(path[0] + path[1], 'w') as f:
                ws = self.output.toPlainText()
                try:
                    f.write(ws)
                except Exception as e:
                    print(e)
                
