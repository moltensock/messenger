import datetime
import sys
import time

import requests
from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('./messenger.ui', self)

        self.pushButton.pressed.connect(self.send_message)

        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_message)
        self.timer.start(1000)

    def get_message(self):
        try:
            response = requests.get(
                'http://127.0.0.1:5000/messages',
                params={'after': self.after}
            )
        except:
            return

        messages = response.json()['messages']
        for message in messages:
            self.print_message(message)
            self.after = message['time']

    def print_message(self, message):
        t = message['time']
        dt = datetime.datetime.fromtimestamp(t)
        dt = dt.strftime('%d.%m.%Y %H:%M:%S')
        self.textBrowser.append(dt + ' ' + message['name'])
        self.textBrowser.append(message['text'])
        self.textBrowser.append('')

    def send_message(self):
        name = self.lineEdit.text()
        text = self.textEdit.toPlainText()

        try:
            response = requests.post(
                'http://127.0.0.1:5000/send',
                json={
                    'name': name,
                    'text': text
                }
            )
        except:
            self.textBrowser.append('Сервер недоступен, попробуйте позднее')
            self.textBrowser.append('')
            return

        if response.status_code != 200:
            self.textBrowser.append('Проверьте корректность имени или текста')
            self.textBrowser.append('')
            return

        self.textEdit.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("plastique")

    window = MainWindow()
    window.show()
    app.exec()