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
        #self.decrypt_mode.clicked.connect(self.switch_mode_callback)
        self.decrypt_mode.toggled['bool'].connect(self.switch_mode_callback)
        # self.encrypt_mode.clicked.connect(self.switch_mode_callback)
        self.encrypt_mode.toggled['bool'].connect(self.switch_mode_callback)
        self.enable_encrypting_cb.clicked.connect(self.cypher_callback)

        self.code_rb.clicked.connect(self.cypher_callback)
        self.char_rb.clicked.connect(self.cypher_callback)

        self.rand_b.clicked.connect(self.rand_b_callback)
        self.key_input.textChanged.connect(self.set_key_callback)
        self.key_input.setValidator(QtGui.QIntValidator())

        # Connect with file menu
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)

    def switch_mode_callback(self, enabled: bool):

        if not enabled:
            return

        in_ = self.input.toPlainText()
        out_ = self.output.toPlainText()

        self.input.setPlainText(out_)
        self.output.setPlainText(in_)

        if self.encrypt_mode.isChecked():
            self.output_box.setTitle('Encrypted')
        elif self.decrypt_mode.isChecked():
            self.output_box.setTitle('Decrypted')

    def cypher_callback(self):
        # cypher here
        if not self.enable_encrypting_cb.isChecked():
            return

        try:
            str_in = self.input.toPlainText()

            if self.encrypt_mode.isChecked():
                str_in = Codec.encrypt(str_in, self.key)
                str_in = Codec.str_to_codes(str_in)
            elif self.decrypt_mode.isChecked():
                str_in = Codec.codes_to_str(str_in)
                str_in = Codec.decrypt(str_in, self.key)

            self.output.setPlainText(str_in)
        except:
            pass

    def set_key_callback(self):
        new_key = self.key_input.text()

        try:
            self.key = int(new_key, base=10) if new_key is not '' else 0
            self.cypher_callback()
        except Exception as e:
            self.key = 0

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
        return True if path not in ('', None) and \
                       Path(path).exists() and \
                       Path(path).resolve().suffix == '.txt' else False
    
    def open_file(self):
        path = QFileDialog.getOpenFileName()
        
        if self.__check_path(path[0]):
            try:
                with open(path[0], 'rb') as f:
                    txt = f.read()
                    self.input.setPlainText(txt.decode('utf-8', 'ignore'))
            except Exception as e:
                show_error(str(e))

        elif path[0] not in ('', None):
            show_error('Select *.txt file please')

    def save_file(self):
        path = QFileDialog.getSaveFileName(filter='.txt', initialFilter='.txt')

        if path[0] not in ('', None):

            with open(path[0] + path[1], 'wb') as f:
                ws = self.output.toPlainText()
                try:
                    f.write(ws.encode('utf-8', 'ignore'))
                except Exception as e:
                    print(e)
